import pandas as pd
from UMAPplot import UMAPplot
from fancyimpute import KNN
import numpy as np
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_decision_regions
from sklearn.neighbors import KNeighborsClassifier

if __name__ == "__main__":
    df = pd.read_csv('./../Dataset/scaledData.csv')
    # feature subsets
    fet1 = ['Total_Debt/Equity_(mrq)', 'Levered_Free_Cash_Flow', 'Trailing_Annual_Dividend_Yield', 'Operating_Cash_Flow', 'Total_Cash_(mrq)']
    fet2 = ['Payout_Ratio', 'Profit_Margin', 'Operating_Cash_Flow', 'Total_Debt/Equity_(mrq)', 'Trailing_Annual_Dividend_Yield']
    fet3 = ['Levered_Free_Cash_Flow', 'Trailing_Annual_Dividend_Yield', 'Profit_Margin', 'Total_Debt/Equity_(mrq)', 'Payout_Ratio']
    fet4 = ['Total_Debt/Equity_(mrq)', 'Return_on_Equity', 'Levered_Free_Cash_Flow', '5_Year_Average_Dividend_Yield', 'Payout_Ratio']
    fet5 = ['5_Year_Average_Dividend_Yield', 'Total_Cash_(mrq)', 'Levered_Free_Cash_Flow', 'Trailing_Annual_Dividend_Yield', 'Payout_Ratio']
    fet6 = ['Payout_Ratio', 'Levered_Free_Cash_Flow', 'Trailing_Annual_Dividend_Yield', 'Profit_Margin', 'Return_on_Equity']
    fet7 = ['Levered_Free_Cash_Flow', 'Return_on_Equity', 'Total_Debt/Equity_(mrq)', 'Total_Cash_(mrq)', 'Profit_Margin']
    fet8 = ['Return_on_Equity', 'Payout_Ratio', 'Total_Cash_(mrq)', 'Profit_Margin', 'Trailing_Annual_Dividend_Yield']
    fet9 = ['Payout_Ratio', '5_Year_Average_Dividend_Yield', 'Return_on_Equity', 'Levered_Free_Cash_Flow', 'Trailing_Annual_Dividend_Yield']
    fet10 = ['Return_on_Equity', 'Payout_Ratio', '5_Year_Average_Dividend_Yield', 'Total_Debt/Equity_(mrq)', 'Levered_Free_Cash_Flow']
    fet11 = ['Return_on_Equity', 'Payout_Ratio', 'Operating_Cash_Flow', 'Total_Debt/Equity_(mrq)', 'Total_Cash_(mrq)']
    fet12 = ['Profit_Margin', 'Trailing_Annual_Dividend_Yield', 'Payout_Ratio', 'Operating_Cash_Flow', 'Total_Debt/Equity_(mrq)']
    fet13 = ['Trailing_Annual_Dividend_Yield', '5_Year_Average_Dividend_Yield', 'Levered_Free_Cash_Flow', 'Profit_Margin', 'Payout_Ratio']
    fet14 = ['Operating_Cash_Flow', 'Levered_Free_Cash_Flow', '5_Year_Average_Dividend_Yield', 'Payout_Ratio', 'Trailing_Annual_Dividend_Yield']
    fet15 = ['Payout_Ratio', 'Levered_Free_Cash_Flow', 'Profit_Margin', 'Total_Cash_(mrq)', 'Operating_Cash_Flow']
    fet16 = ['Total_Cash_(mrq)', 'Total_Debt/Equity_(mrq)', 'Operating_Cash_Flow', '5_Year_Average_Dividend_Yield', 'Trailing_Annual_Dividend_Yield']
    fet17 = ['Levered_Free_Cash_Flow', 'Trailing_Annual_Dividend_Yield', 'Profit_Margin', 'Return_on_Equity', '5_Year_Average_Dividend_Yield']
    fet18 = ['Return_on_Equity', 'Trailing_Annual_Dividend_Yield', 'Total_Cash_(mrq)', 'Profit_Margin', 'Levered_Free_Cash_Flow']
    fet19 = ['Return_on_Equity', 'Total_Cash_(mrq)', 'Payout_Ratio', 'Total_Debt/Equity_(mrq)', 'Operating_Cash_Flow']
    fet20 = ['Profit_Margin', 'Levered_Free_Cash_Flow', 'Operating_Cash_Flow', '5_Year_Average_Dividend_Yield', 'Total_Debt/Equity_(mrq)']
    fet21 = ['Levered_Free_Cash_Flow', 'Total_Debt/Equity_(mrq)', 'Trailing_Annual_Dividend_Yield', 'Payout_Ratio', 'Return_on_Equity']
    fet22 = ['5_Year_Average_Dividend_Yield', 'Levered_Free_Cash_Flow', 'Return_on_Equity', 'Payout_Ratio', 'Total_Debt/Equity_(mrq)']
    fet23 = ['Total_Cash_(mrq)', 'Profit_Margin', 'Payout_Ratio', 'Total_Debt/Equity_(mrq)', 'Trailing_Annual_Dividend_Yield']
    fet24 = ['Total_Debt/Equity_(mrq)', 'Trailing_Annual_Dividend_Yield', 'Return_on_Equity', '5_Year_Average_Dividend_Yield', 'Operating_Cash_Flow']
    fet25 = ['Levered_Free_Cash_Flow', 'Operating_Cash_Flow', '5_Year_Average_Dividend_Yield', 'Profit_Margin', 'Return_on_Equity']
    fet26 = ['Payout_Ratio', 'Levered_Free_Cash_Flow', 'Return_on_Equity', 'Profit_Margin', '5_Year_Average_Dividend_Yield']
    fet27 = ['Profit_Margin', 'Return_on_Equity', 'Total_Debt/Equity_(mrq)', 'Total_Cash_(mrq)', 'Operating_Cash_Flow']
    fet28 = ['Operating_Cash_Flow', 'Total_Cash_(mrq)', 'Return_on_Equity', 'Trailing_Annual_Dividend_Yield', 'Total_Debt/Equity_(mrq)']
    fet29 = ['5_Year_Average_Dividend_Yield', 'Operating_Cash_Flow', 'Trailing_Annual_Dividend_Yield', 'Profit_Margin', 'Payout_Ratio']
    fet30 = ['Total_Debt/Equity_(mrq)', 'Return_on_Equity', 'Profit_Margin', 'Payout_Ratio', 'Levered_Free_Cash_Flow']

    l = [(fet1, 1), (fet2, 2), (fet3, 3),(fet4, 4), (fet5, 5), (fet6, 6), (fet7, 7), (fet8,8), (fet9, 9), (fet10, 10), (fet11, 11), (fet12,12),
          (fet13, 13), (fet14, 14), (fet15, 15), (fet16, 16), (fet17, 17), (fet18, 18), (fet19, 19),
          (fet20,20), (fet21, 21), (fet22, 22), (fet23, 23), (fet24, 24), (fet25, 25), (fet26, 26), (fet27, 27), (fet28, 28), (fet29, 29), (fet30, 30)]

    imputer = KNN()
    target = 'discretized FADY'
    df.drop('Ticker', axis=1, inplace=True)
    y = df[target]
    X = df.drop(target,axis=1)
    X_imputed = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)

    for fet in l:
        a,b = fet
        dfs = X_imputed[a]
        ump = UMAPplot(np.array(dfs.values), y,2, applyKernel=False)
        # save feature subset
        dfs[target] = y
        dfs.to_csv('./../Dataset/v'+str(b)+'.csv')
        df2 = pd.DataFrame(ump.umres, columns=['UMAP 1', 'UMAP 2'])
        df2[target] = y
        df2.to_csv('./../Dataset/umap reduced/Uv'+str(b)+'.csv')
        #ump.plot()
        #plt.show()

        """
        knn = KNeighborsClassifier(n_neighbors=1)
        knn.fit(ump.umres, y)
        plot_decision_regions(np.array(ump.umres), np.array(y), clf=knn, legend=2)
        plt.show()
        """