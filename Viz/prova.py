import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

df = pd.read_csv('/Users/filipponardi/Documents/GitHub/StockAnalysis-tool/Dataset/data_historic_stock.csv')
df = df[df['Ticker'] == 'GOOGL']
df['Date'] = pd.to_datetime(df['Date'], format="%Y-%m-%d")
print(df.dtypes)

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])

fig.show()