import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import statistics

df = pd.read_csv('../Dataset/pred.csv')
print(df.dtypes)
fig, axes = plt.subplots(2, 4, figsize=(20, 15), sharex=True, sharey=False)
axes = axes.flatten()

#plt.xticks(rotation = 45)
companies = ['GOOGL','AMZN','AMD','EBAY','META','NFLX','NVDA','PYPL']

df['Date'] = df['Date'].str[-2:]
print(df)

fig.suptitle("November closing price prediction", fontsize=30)

perc_error = []
for idx, company in enumerate(companies):
    pred = df[(df['Ticker'] == company) & (df['Type'] == 'prediction')]
    real = df[(df['Ticker'] == company) & (df['Type'] == 'real')]
    for _, p in pred.iterrows():
        day = p['Date']
        pval = p['Close']
        rval = real[real['Date']==day]
        rval = rval.iloc[0]['Close']
        perc_error.append((pval-rval)/rval * 1000)        #pe = p[]


    axes[idx].set_title(company)#+ ' prediction error:'+str(  round(statistics.mean(perc_error),2)) + '%')
    sns.lineplot(data=df[df['Ticker'] == company], x="Date", y="Close", hue="Type",ax = axes[idx])
fig.tight_layout()
fig.subplots_adjust(top=0.88)
plt.show()
