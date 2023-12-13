from UMAPplot import UMAPplot
import pandas as pd
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_decision_regions
from sklearn.neighbors import KNeighborsClassifier
import numpy as np


if __name__ == "__main__":
    df = pd.read_csv('./../Dataset/scaledData.csv')
    features = ['Operating_Cash_Flow', 'Return_on_Equity', 'Total_Cash_(mrq)', 'Total_Debt/Equity_(mrq)', '5_Year_Average_Dividend_Yield']
    fet2 = ['5_Year_Average_Dividend_Yield', 'Payout_Ratio', 'Total_Debt/Equity_(mrq)', 'Return_on_Equity', 'Trailing_Annual_Dividend_Yield']

    # this one looks good
    fet3 = ['Return_on_Equity', 'Total_Debt/Equity_(mrq)', 'Payout_Ratio', 'Trailing_Annual_Dividend_Yield', 'Total_Cash_(mrq)']
    fet4 = ['Trailing_Annual_Dividend_Yield', 'Return_on_Equity', 'Total_Debt/Equity_(mrq)', 'Payout_Ratio', 'Profit_Margin']
    fet9 = ['Return_on_Equity', 'Total_Cash_(mrq)', 'Trailing_Annual_Dividend_Yield', '5_Year_Average_Dividend_Yield', 'Profit_Margin']
    fet14 = ['Total_Cash_(mrq)', '5_Year_Average_Dividend_Yield', 'Trailing_Annual_Dividend_Yield', 'Operating_Cash_Flow', 'Payout_Ratio']
    fet17 = ['Levered_Free_Cash_Flow', 'Total_Cash_(mrq)', 'Payout_Ratio', 'Trailing_Annual_Dividend_Yield', 'Operating_Cash_Flow']
    fet20 = ['Return_on_Equity', 'Total_Debt/Equity_(mrq)', 'Total_Cash_(mrq)', 'Levered_Free_Cash_Flow', '5_Year_Average_Dividend_Yield']
    fet21 = ['Levered_Free_Cash_Flow', 'Profit_Margin', 'Total_Cash_(mrq)', 'Payout_Ratio', '5_Year_Average_Dividend_Yield']
    fet22 = ['Levered_Free_Cash_Flow', 'Total_Cash_(mrq)', 'Payout_Ratio', 'Trailing_Annual_Dividend_Yield', 'Operating_Cash_Flow']
    fet25 = ['Trailing_Annual_Dividend_Yield', '5_Year_Average_Dividend_Yield', 'Return_on_Equity', 'Levered_Free_Cash_Flow', 'Total_Cash_(mrq)']
    fet26 = ['Return_on_Equity', 'Trailing_Annual_Dividend_Yield', 'Total_Debt/Equity_(mrq)', 'Total_Cash_(mrq)', '5_Year_Average_Dividend_Yield']
    fet28 = ['Trailing_Annual_Dividend_Yield', '5_Year_Average_Dividend_Yield', 'Total_Debt/Equity_(mrq)', 'Return_on_Equity', 'Operating_Cash_Flow']

    fet1 = ['Profit_Margin', 'Return_on_Equity', 'Trailing_Annual_Dividend_Yield', 'Operating_Cash_Flow', 'Total_Cash_(mrq)']
    fet2 = ['Return_on_Equity', 'Total_Cash_(mrq)', '5_Year_Average_Dividend_Yield', 'Levered_Free_Cash_Flow', 'Trailing_Annual_Dividend_Yield']
    fet3 = ['Profit_Margin', 'Operating_Cash_Flow', 'Total_Debt/Equity_(mrq)', 'Levered_Free_Cash_Flow', '5_Year_Average_Dividend_Yield']
    fet4 = ['Return_on_Equity', '5_Year_Average_Dividend_Yield', 'Profit_Margin', 'Total_Cash_(mrq)', 'Operating_Cash_Flow']
    fet5 = ['Total_Cash_(mrq)', 'Trailing_Annual_Dividend_Yield', 'Levered_Free_Cash_Flow', 'Operating_Cash_Flow', '5_Year_Average_Dividend_Yield']
    fet6 = ['5_Year_Average_Dividend_Yield', 'Levered_Free_Cash_Flow', 'Return_on_Equity', 'Profit_Margin', 'Operating_Cash_Flow']
    fet7 = ['Profit_Margin', 'Trailing_Annual_Dividend_Yield', 'Payout_Ratio', 'Total_Cash_(mrq)', 'Return_on_Equity']
    fet8 = ['Return_on_Equity', 'Total_Debt/Equity_(mrq)', 'Operating_Cash_Flow', '5_Year_Average_Dividend_Yield', 'Levered_Free_Cash_Flow']
    fet9 = ['Total_Debt/Equity_(mrq)', 'Operating_Cash_Flow', 'Return_on_Equity', 'Levered_Free_Cash_Flow', 'Trailing_Annual_Dividend_Yield']
    fet10 = ['5_Year_Average_Dividend_Yield', 'Payout_Ratio', 'Operating_Cash_Flow', 'Profit_Margin', 'Trailing_Annual_Dividend_Yield']
    fet11 = ['Trailing_Annual_Dividend_Yield', 'Payout_Ratio', 'Total_Debt/Equity_(mrq)', '5_Year_Average_Dividend_Yield', 'Levered_Free_Cash_Flow']
    fet12 = ['Return_on_Equity', '5_Year_Average_Dividend_Yield', 'Levered_Free_Cash_Flow', 'Payout_Ratio', 'Trailing_Annual_Dividend_Yield']
    fet13 = ['Total_Cash_(mrq)', 'Operating_Cash_Flow', '5_Year_Average_Dividend_Yield', 'Levered_Free_Cash_Flow', 'Trailing_Annual_Dividend_Yield']
    fet14 = ['Operating_Cash_Flow', 'Trailing_Annual_Dividend_Yield', '5_Year_Average_Dividend_Yield', 'Profit_Margin', 'Return_on_Equity']
    fet15 = ['Profit_Margin', 'Total_Cash_(mrq)', 'Trailing_Annual_Dividend_Yield', 'Return_on_Equity', 'Levered_Free_Cash_Flow']
    fet16 = ['5_Year_Average_Dividend_Yield', 'Levered_Free_Cash_Flow', 'Total_Cash_(mrq)', 'Return_on_Equity', 'Trailing_Annual_Dividend_Yield']
    fet17 = ['5_Year_Average_Dividend_Yield', 'Levered_Free_Cash_Flow', 'Total_Cash_(mrq)', 'Trailing_Annual_Dividend_Yield', 'Return_on_Equity']
    fet18 = ['Total_Debt/Equity_(mrq)', 'Levered_Free_Cash_Flow', 'Total_Cash_(mrq)', '5_Year_Average_Dividend_Yield', 'Return_on_Equity']
    fet19 = ['Total_Debt/Equity_(mrq)', 'Payout_Ratio', 'Profit_Margin', 'Levered_Free_Cash_Flow', '5_Year_Average_Dividend_Yield']
    fet20 = ['Total_Debt/Equity_(mrq)', 'Levered_Free_Cash_Flow', 'Operating_Cash_Flow', 'Profit_Margin', '5_Year_Average_Dividend_Yield']
    fet21 = ['Levered_Free_Cash_Flow', 'Trailing_Annual_Dividend_Yield', '5_Year_Average_Dividend_Yield', 'Operating_Cash_Flow', 'Profit_Margin']
    fet22 = ['Total_Cash_(mrq)', 'Total_Debt/Equity_(mrq)', 'Trailing_Annual_Dividend_Yield', 'Levered_Free_Cash_Flow', 'Operating_Cash_Flow']
    fet23 = ['Total_Cash_(mrq)', 'Return_on_Equity', 'Operating_Cash_Flow', 'Trailing_Annual_Dividend_Yield', 'Payout_Ratio']
    fet24 = ['Total_Cash_(mrq)', 'Payout_Ratio', 'Total_Debt/Equity_(mrq)', 'Profit_Margin', 'Trailing_Annual_Dividend_Yield']
    fet25 = ['Return_on_Equity', '5_Year_Average_Dividend_Yield', 'Total_Cash_(mrq)', 'Operating_Cash_Flow', 'Profit_Margin']
    fet26 = ['Return_on_Equity', 'Total_Cash_(mrq)', '5_Year_Average_Dividend_Yield', 'Payout_Ratio', 'Trailing_Annual_Dividend_Yield']
    fet27 = ['Operating_Cash_Flow', 'Total_Cash_(mrq)', 'Levered_Free_Cash_Flow', 'Total_Debt/Equity_(mrq)', 'Trailing_Annual_Dividend_Yield']
    fet28 = ['Trailing_Annual_Dividend_Yield', 'Total_Cash_(mrq)', 'Profit_Margin', 'Levered_Free_Cash_Flow', 'Operating_Cash_Flow']
    fet29 = ['Trailing_Annual_Dividend_Yield', 'Total_Cash_(mrq)', 'Profit_Margin', 'Levered_Free_Cash_Flow', 'Return_on_Equity']
    fet30 = ['Levered_Free_Cash_Flow', '5_Year_Average_Dividend_Yield', 'Total_Cash_(mrq)', 'Trailing_Annual_Dividend_Yield', 'Operating_Cash_Flow']

    # print(df.columns)
    #df.drop(['Ticker'], axis=1, inplace=True)
    target = 'discretized FADY'
    
    indices = range(1,31)
    ts = [(globals()[f'fet{i}'], i) for i in indices]
    #for fet in [(fet2, 2), (fet3, 3),(fet4, 4), (fet9, 9), (fet14, 14), (fet17, 17), (fet20,20), (fet21, 21), (fet22, 22), (fet25, 25), (fet26, 26), (fet28, 28)]:
    for fet in ts:
        features, idx = fet
        features.append(target)
        dfs = df[features]
        dfs.to_csv('./../Dataset/v'+str(idx)+'.csv')
        y = df[target]                                        
        X = df.drop([target, 'Ticker'], axis=1)
        from sklearn.impute import SimpleImputer
        imputer = SimpleImputer(strategy='mean')
        X_imputed = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)
    
        ump = UMAPplot(X_imputed, y,2, applyKernel=False)
        #ump.plot()
        #plt.show()
        
        # to get the visualizations of the Voronoi regions as well
        """
        knn = KNeighborsClassifier(n_neighbors=1)
        knn.fit(ump.umres, y)
        plot_decision_regions(np.array(ump.umres), np.array(y), clf=knn, legend=2)
        plt.show()
        """
    
