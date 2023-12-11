import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../Dataset/pred.csv')
print(df.dtypes)
fig, axes = plt.subplots(2, 4, figsize=(20, 15), sharex=True, sharey=False)
axes = axes.flatten()

#plt.xticks(rotation = 45)
companies = ['GOOGL','AMZN','AMD','EBAY','META','NFLX','NVDA','PYPL']

df['Date'] = df['Date'].str[-2:]
print(df)

fig.suptitle("November closing price prediction", fontsize=30)

for idx, company in enumerate(companies):
    axes[idx].set_title(company)
    sns.lineplot(data=df[df['Ticker'] == company], x="Date", y="Close", hue="Type",ax = axes[idx])
fig.tight_layout()
fig.subplots_adjust(top=0.88)
plt.show()
