from UMAPplot import UMAPplot
import pandas as pd
import matplotlib.pyplot as plt


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
    # print(df.columns)
    df.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis=1, inplace=True)
    target = 'discretized FADY'
    
    for fet in [(fet2, 2), (fet3, 3),(fet4, 4), (fet9, 9), (fet14, 14), (fet17, 17), (fet20,20), (fet21, 21), (fet22, 22), (fet25, 25), (fet26, 26), (fet28, 28)]:
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
        ump.plot()
        plt.show()
    
