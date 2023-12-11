import pandas as pd
import numpy as np
from hmmlearn.hmm import GaussianHMM
import itertools
import seaborn as sns
import matplotlib.pyplot as plt
import random

class StockPricePredictor(object):
    def __init__(self, company, train_data, n_components=2, n_days = 30):
        self.company = company
        self.data = train_data[['Date','Open','High','Low','Close']]
        self.n_days = n_days
        self.hmm = GaussianHMM(n_components=n_components)
        
        self._compute_all_possible_outcomes(20,10,10)
        print(self._possible_outcomes)

    def fit(self):
        ## start by transforming absolute values into relative
        rel_close = np.array((self.data['Close'] - self.data['Open']) / self.data['Open'])
        rel_close = np.round(rel_close, decimals=2)
        rel_high = np.array((self.data['High']-self.data['Open'])/self.data['Open'])
        rel_high = np.round(rel_high, decimals=2)
        rel_low = np.array((self.data['Low']-self.data['Open'])/self.data['Open'])
        rel_low = np.round(rel_low, decimals=2)
        feature_vector = np.column_stack((rel_close, rel_high, rel_low))
        feature_vector = feature_vector[::-1]
        print(feature_vector)
        self.hmm.fit(feature_vector)
        return

    def _compute_all_possible_outcomes(self, n_steps_frac_change, n_steps_frac_high, n_steps_frac_low):
        #frac_change_range = [-0.1,-0.09,-0.08,-0.07,-0.06,-0.05,-0.04,-0.03,-0.02,-0.01,0.,0.01,]
        frac_change_range = np.linspace(-0.10, 0.10, n_steps_frac_change+1)
        frac_high_range = np.linspace(0, 0.10, n_steps_frac_high + 1)
        frac_low_range = np.linspace(0, 0.10, n_steps_frac_low + 1)
 
        self._possible_outcomes = np.array(list(itertools.product(
            frac_change_range, frac_high_range, frac_low_range)))

    def predict(self, previous_data, open_price):
        rel_close = np.array((previous_data['Close'] - previous_data['Open']) / previous_data['Open'])
        rel_close = np.round(rel_close, decimals=2)
            
        rel_high = np.array((previous_data['High']-previous_data['Open'])/previous_data['Open'])
        rel_high = np.round(rel_high, decimals=2)

        rel_low = np.array((previous_data['Low']- previous_data['Open'])/previous_data['Open'])
        rel_low = np.round(rel_low, decimals=2)
        
        feature_vector = np.column_stack((rel_close,rel_high,rel_low))
        #feature_vector = feature_vector[::-1]

        outcome_score = []
        for possible_outcome in self._possible_outcomes:
            total_data = np.row_stack((feature_vector, possible_outcome))
            total_data = total_data[::-1]
            prob, _ = self.hmm.decode(total_data)
            score = self.hmm.score(total_data)
            #print('predict:', self.hmm.predict(total_data))
            outcome_score.append(score)
        
        # TO GET ONLY THE MAXIMUM VALUE
        #most_probable_outcome = self._possible_outcomes[np.argmax(outcome_score)]

        # TO GET THE TOP N VALUES AND EXTRACT RANDOMLY
        n = 4
        best_pred = np.argpartition(outcome_score, -n)[-n:]
        most_probable_outcome = self._possible_outcomes[random.choice(best_pred)]

        
        prev_high = open_price * (1 + most_probable_outcome[1])
        prev_low = open_price * (1 - most_probable_outcome[2])
        prev_close = open_price * (1 + most_probable_outcome[0])
        return open_price, prev_high, prev_low, prev_close 


data = pd.read_csv('../Dataset/data_historic_stock.csv')
data['Date'] = pd.to_datetime(data['Date'], format="%Y-%m-%d")

companies = ['GOOGL','AMZN','AMD','CSCO','EBAY','EA','META','NFLX','NVDA','PYPL']
#company = 'ABNB'
#print(data[data['Date'] == sel_date])
#x = data[data['Date'] == sel_date]
#print(x['Open'].iloc[0])
#ret = predictor.predict(test_data, x['Open'].values[0])
#print(ret)
df_tot = pd.DataFrame(columns=["Ticker","Date", "Open", "High", "Low", "Close", "Type"])

fig, axes = plt.subplots(2, 5, figsize=(20, 15), sharex=True, sharey=False)
axes = axes.flatten()

for idx, company in enumerate(companies):
    data_c = data[data['Ticker'] == company]
    train_data = data_c[data_c['Date'] < pd.to_datetime(['2023-11-01'])[0]]
    test_data = data_c[data_c['Date'] >= pd.to_datetime(['2023-11-01'])[0]]
    predictor = StockPricePredictor(company, test_data)
    predictor.fit()

    prev_df = pd.DataFrame(columns=["Ticker","Date", "Open", "High", "Low", "Close", "Type"])
    sel_date = pd.to_datetime(['2023-12-01'])[0]
    test_data = test_data[test_data['Date'] < sel_date]

    for i in range(1,31):
        date = '2023-11-' + str(i)
        date = pd.to_datetime([date])[0]
        x = data_c[data_c['Date']==date]
        if len(x) == 0:
            continue
        print('##############',date,'###############')
        print(x)
        df = test_data[test_data['Date'] < date]
        #if len(x) == 0:
        #    x = df.iloc[len(df)-1]
        #print(df)

        ret = predictor.predict(df, x['Open'].iloc[0])
        prev_df.loc[-1] = [company, date,ret[0],ret[1],ret[2],ret[3],'prediction']
        prev_df.index = prev_df.index + 1 
        print('ret:', ret)
        print('#####################################')
#print(prev_df)
    date = '2023-11-30'
    date = pd.to_datetime([date])[0]
    #x = data[data['Date']==date]
    actual_df = test_data[test_data['Date'] <= date]
    actual_df['Type'] = ['real'] * len(actual_df.index)
    df_comp = pd.concat([prev_df,actual_df])
    df_tot = pd.concat([df_comp, df_tot])
#print(df_tot)
    #sns.lineplot(data=df_comp, x="Date", y="Close", hue="Type",ax = axes[idx])
#sns.catplot(data=df_tot, x="Date", y="Close", hue="Type", col="Ticker", kind="lineplot", col_wrap=5)
df_tot.to_csv('../Dataset/pred.csv',index=False)
plt.show()

