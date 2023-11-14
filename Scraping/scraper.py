import requests
from bs4 import BeautifulSoup

base = 'https://finance.yahoo.com'
trending = '/trending-tickers'
response = requests.get(base+trending)

assert(response.status_code == 200)

soup = BeautifulSoup(response.text, 'html.parser')
tab = soup.find('tbody')
tickers = {}
assert(tab)
elements = tab.find_all('tr')
links = [e.find('a') for e in elements]
for l in links:
    tickers[l.text] = l.get('href')
print(tickers)

# For each ticker find corresponding features
# for t in tickers:
#     url = base + tickers[t]
#     response = requests.get(url)
#     if response.status_code != 200:
#         print('error retrieving data for ', t)
#         continue
#     print(response.text)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     tickers['previous close'] = soup.find('PREV_CLOSE-value').text
#     print(tickers['previous close'])
