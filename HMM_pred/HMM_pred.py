import pandas as pd
import numpy as np
from hmmlearn.hmm import GaussianHMM
import itertools

class StockPricePredictor(object):
    def __init__(self, company, train_data, n_components=4, n_days = 30):
        self.company = company
        self.data = train_data[['Date','Open','High','Low','Close']]
        self.n_days = n_days
        self.hmm = GaussianHMM(n_components=n_components)
        
        self._compute_all_possible_outcomes(60,30,30)

    def fit(self):
        ## start by transforming absolute values into relative
        rel_close = np.array((self.data['Close'] - self.data['Open']) / self.data['Open'])
        rel_high = np.array((self.data['High']-self.data['Open'])/self.data['Open'])
        rel_low = np.array((self.data['Low']-self.data['Open'])/self.data['Open'])
        feature_vector = np.column_stack((rel_close, rel_high, rel_low))
        self.hmm.fit(feature_vector)
        return

    def _compute_all_possible_outcomes(self, n_steps_frac_change, n_steps_frac_high, n_steps_frac_low):
        frac_change_range = np.linspace(-0.15, 0.15, n_steps_frac_change)
        frac_high_range = np.linspace(-0.15, 0.15, n_steps_frac_high)
        frac_low_range = np.linspace(-0.15, 0.15, n_steps_frac_low)
 
        self._possible_outcomes = np.array(list(itertools.product(
            frac_change_range, frac_high_range, frac_low_range)))

    def predict(self, previous_data, open_price):
        rel_close = np.array((previous_data['Close'].values - previous_data['Open'].values) / previous_data['Open'].values)
        rel_high = np.array((previous_data['High']-previous_data['Open'])/previous_data['Open'])
        rel_low = np.array((previous_data['Low']- previous_data['Open'])/previous_data['Open'])
        feature_vector = np.column_stack((rel_close,rel_high,rel_low))

        outcome_score = []
        for possible_outcome in self._possible_outcomes:
            total_data = np.row_stack((feature_vector, possible_outcome))
            outcome_score.append(self.hmm.score(total_data))
        most_probable_outcome = self._possible_outcomes[np.argmax(outcome_score)]
        #prevision = previous_data.iloc[len(previous_data)-1] #TODO change this for non-ordered data
        print('----------------------')
        print(most_probable_outcome[0])
        print(most_probable_outcome[1])
        print(most_probable_outcome[2])
        prev_high = open_price * (1 + most_probable_outcome[1])
        prev_low = open_price * (1 + most_probable_outcome[2])
        prev_close = open_price * (1 + most_probable_outcome[0])
        return open_price, prev_high, prev_low, prev_close 


data = pd.read_csv('../Dataset/data_historic_stock.csv')
data['Date'] = pd.to_datetime(data['Date'], format="%Y-%m-%d")
company = 'ABNB'
data = data[data['Ticker'] == company]
train_data = data[data['Date'] < pd.to_datetime(['2023-11-01'])[0]]
test_data = data[data['Date'] >= pd.to_datetime(['2023-11-01'])[0]]
predictor = StockPricePredictor(company, test_data)
predictor.fit()

sel_date = pd.to_datetime(['2023-12-01'])[0]
test_data = test_data[test_data['Date'] < sel_date]
print(data[data['Date'] == sel_date])
x = data[data['Date'] == sel_date]
ret = predictor.predict(test_data, x['Open'].values[0])
print(ret)
prev_df = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close"])
#prev_df.append(pd.DataFrame({"Date": [ret[0]], "Open": [ret[1]], "High": [ret[2]], "Low": [ret[3]], "Close": [ret[4]] }))
#print(prev_df)
#x = np.array(ret)
#x.concatenate(x)
#df2 = pd.DataFrame(x, columns=["Date", "Open", "High", "Low", "Close"])

for i in range(1,31):
    date = '2023-11-' + str(i)
    date = pd.to_datetime([date])[0]
    df = test_data[test_data['Date'] < date]
    x = data[data['Date']==date]
    predictor.predict(df, x['Open'].values[0])
    prev_df.loc[-1] = [date,ret[0],ret[1],ret[2],ret[3]]
    prev_df.index = prev_df.index + 1 

print(prev_df)
