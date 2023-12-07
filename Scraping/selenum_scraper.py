#!apt update
#!apt install chromium-chromedriver
#!pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import pandas as pd
import time 
from datetime import datetime


# supporting class with constants from the website (keys etc.)
class Metrics(object):
    
    # Valuation Measures
    MARKET_CAP = 'Market Cap'
    MARKET_CAP_KEY = 'Market_Cap'
    ENTERPRISE_VALUE = 'Enterprise Value'
    ENTERPRISE_VALUE_KEY = 'Enterprise_Value'
    
    
    # Profitability
    PM = "Profit Margin"
    OM = "Operating Margin"
    
    # Management Effectiveness
    ROA = "Return on Assets"
    ROE = "Return on Equity"
    
    # Balance Sheet
    TC = "Total Cash (mrq)"  # CAUTION! search only by contains, not equals!
    TCPS = "Total Cash Per Share (mrq)"
    TD = "Total Debt (mrq)"  # CAUTION! search only by contains, not equals!
    TDE = "Total Debt/Equity (mrq)"
    # ...
    
    # Cash Flow Statement
    OCF = "Operating Cash Flow"
    LFCF = "Levered Free Cash Flow"
    
    # Dividiens & Splits
    FADR = "Forward Annual Dividend Rate"
    FADY = "Forward Annual Dividend Yield"
    TADR = "Trailing Annual Dividend Rate"
    TADY = "Trailing Annual Dividend Yield"
    Y5ADY = "5 Year Average Dividend Yield"
    PR = "Payout Ratio"
    # ...
    
    base = []
    TICKER = "Ticker"
    
    
    def __init__(self):
        self.base = [self.TICKER]
    
    def basics(self, addBase=False):
        if addBase:
            return self.base + [self.MARKET_CAP, self.ENTERPRISE_VALUE]
        else:
            return [self.MARKET_CAP, self.ENTERPRISE_VALUE]
    
    def diviends(self, addBase=False):
        if addBase:
            return self.base + [self.FADR, self.FADY, self.TADR, self.TADY, self.Y5ADY, self.PR]
        else:
            return [self.FADR, self.FADY, self.TADR, self.TADY, self.Y5ADY, self.PR]
        
    
    def dividends_slides(self, addBase=False):
        if addBase:
            return self.base + [self.FADY, self.TADY, self.Y5ADY, self.PR, self.PM, self.ROE, self.TC]
        else:
            return [self.FADY, self.TADY, self.Y5ADY, self.PR, self.PM, self.ROE, self.TC]
    
    def stability_slides(self, addBase=False):
        if addBase:
            return self.base + [self.TDE, self.OCF, self.LFCF]
        else:
            return [self.TDE, self.OCF, self.LFCF]
    
    def from_slides(self):
        return self.dividends_slides(addBase=True) + self.stability_slides()
    
    

class Tickerinfo(object):  # for additional type security
    
    def __init__(self, name, url):
        self.name = name
        self.url = url
        


def get_key_from_metric_label(label):
    return label.replace(" ", "_")

def extract_value_from_format(input):
    value = None    # TODO: maybe use NaN instead!?

    input = input.replace(",","") # erase every ",", they just show the thousends: 1,234. To spilt decimals, the "." is used
    if "%" in input:
        value = float(input.replace("%", ""))
    elif "M" in input:
        value = float(input.replace("M", "")) * 1000 * 1000
    elif "B" in input:
        value = float(input.replace("B", "")) * 1000 * 1000 * 1000
    elif input.replace('.','',1).isdigit():
        value = float(input)
    elif "N/A" in input:
        pass  # value = None
    else:
        print("input not preprocessed: ", input)

    return value

def add_metrics_from_site(driver, metrics, metrics_by_label):
    
    if len(driver.find_elements(By.ID, 'Col1-0-KeyStatistics-Proxy')) == 0:
        print("ERROR: no key-statistics page found! Returns empty metrics")
        return metrics + [None] * (len(metrics_by_label) - 1) # return placeholders
    
    
    metrics_body = driver.find_element(By.ID, 'Col1-0-KeyStatistics-Proxy')
    
    for metric_label in metrics_by_label:
        if metric_label == Metrics.TICKER: # tickername only for dataframe-label reasons. Maybe change logic to more sothisticated list 
            continue
            
        market_cap_element = metrics_body.find_element(By.XPATH, "//tr[contains(., '"+metric_label+"')]")
        child_elements = market_cap_element.find_elements(By.XPATH, "./*")

        assert(len(child_elements) == 2)
        
        # extract values from format
        value = extract_value_from_format(child_elements[1].text) 
        metrics.append(value)
        
        # TODO!
        #if get_key_from_metric_label(child_elements[0].text) != metric_label:
        #    print("Caution: modified metric-name from website " + get_key_from_metric_label(child_elements[0].text) + " differs from the used column-key: "+ metric_label )
        
        
        #metrics[get_key_from_metric_label(child_elements[0].text)] = child_elements[1].text
        #metrics.append((child_elements[0].text, child_elements[1].text))  # TODO return metric_label value (but be aware of the contains-search!)

    return metrics

def add_dividends_from_site(driver, df_dividends, tickername):
    
    body_id = 'Col1-1-HistoricalDataTable-Proxy'

    if len(driver.find_elements(By.ID, body_id)) == 0:
        print("ERROR: no HistoricalDataTable page found! Returns no dividends")
        return df_dividends #data + [None] * (len(labels_to_add) - 1) # return placeholders
    
    
    #df_dividends = pd.DataFrame(columns=["Ticker", "Date", "Dividend"])

    body = driver.find_element(By.ID, body_id).find_element(By.TAG_NAME, "tbody")
    
    rows = body.find_elements(By.TAG_NAME, "tr")
    if len(rows) == 0:
        print("no historic dividends found")
        return df_dividends
    
    for row in rows:

        row_data = [tickername]
        child_elements = row.find_elements(By.TAG_NAME, "td")
        
        if len(child_elements) == 1 and "No Dividends" in child_elements[0].text:
            # example: https://finance.yahoo.com/quote/CPRT/history?period1=1543708800&period2=1701475200&interval=capitalGain%7Cdiv%7Csplit&filter=div&frequency=1d&includeAdjustedClose=true
            print("no historic dividends found")
            return df_dividends
            
        assert(len(child_elements) == 2)

        date = datetime.strptime(child_elements[0].text, '%b %d, %Y').date()
        value = extract_value_from_format(child_elements[1].text.split(" ")[0])

        row_data.append(date)
        row_data.append(value)
        # add metrics as new last row to df
        df_dividends.loc[len(df_dividends)] = row_data

    return df_dividends
    

def get_trending_tickers_yahoo(driver):
    print("call trending tickers")
    # call url with tickers:
    driver.get("https://finance.yahoo.com/trending-tickers")
    
    tab = driver.find_element(By.TAG_NAME, 'tbody')
    tickers = []
    assert(tab)
    elements = tab.find_elements(By.TAG_NAME, 'tr')
    
    print("amount of tickers: ", len(elements))
    #elements = elements[:5]  # TODO, take all tickers (only for testing)
    
    
    links = [e.find_element(By.TAG_NAME, 'a') for e in elements]

    for l in links:
        tickers.append(Tickerinfo(l.text, l.get_attribute("href")))
    
    print("getting tickers finished")
    return tickers

def get_nasdaq_100_tickers():
    # get nasdaq-100 tickers from
    # https://www.nasdaq.com/market-activity/quotes/nasdaq-ndx-index

    print("set up driver for nasdaq website")
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    options = webdriver.ChromeOptions()
    #options.add_argument('--headless') # for not displaying the graphical environment, shows virtualized browser without GUI
    options.add_argument('--no-sandbox') # so that it can access machine resources, blocking sandbox processes it can access whatever
    options.add_argument('--disable-dev-shm-usage')  # colab does not have enough memory
    # open it, go to a website, and get results
    nasdaq_driver = webdriver.Chrome(options=options)


    try:
        url = "https://www.nasdaq.com/market-activity/quotes/nasdaq-ndx-index"
        nasdaq_driver.get(url)

        time.sleep(5)
        # Accept cookies by clicking the button with the specified ID
        #iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'onetrust-banner-sdk')))

        print("accept cookies")
        #print(driver.page_source)
        iframe = nasdaq_driver.find_element(By.ID, 'onetrust-banner-sdk')
        accept_cookies_button = iframe.find_element(By.ID, 'onetrust-accept-btn-handler')
        accept_cookies_button.click()

        print("get nasdaq-100 tickers")
        tab = nasdaq_driver.find_element(By.TAG_NAME, 'tbody')
        tickers = []
        assert(tab)
        elements = tab.find_elements(By.TAG_NAME, 'tr')

        print("amount of tickers: ", len(elements))
        #elements = elements[:5]  # TODO, take all tickers (only for testing)

        links = [e.find_element(By.TAG_NAME, 'a') for e in elements]

        for l in links:
            tickers.append(Tickerinfo(l.text, l.get_attribute("href")))

        print("getting tickers finished")
    finally:
        # Close the WebDriver
        nasdaq_driver.quit()

    print()
    print("finished scraping nasdaq website")
    
    return tickers
	

def get_metrics(driver, tickers):
    print("get metrics for "+str(len(tickers))+" tickers")
    required_metrics = Metrics().from_slides()
    
    df_metrics = pd.DataFrame(columns=[get_key_from_metric_label(label) for label in required_metrics])
    
    # call metric-webpage for each ticker and scrape values
    for ticker in tickers:
            
        tickername = ticker.name
        print()
        print("ticker: ", tickername)
        url = "https://finance.yahoo.com/quote/"+tickername+"/key-statistics?p="+tickername
        driver.get(url)

        metrics = [tickername]
         # get metric values from website
        print("start scraping metrics for ticker from: ", driver.current_url)
        metrics = add_metrics_from_site(driver, metrics, required_metrics)

         # add metrics as new last row to df
        df_metrics.loc[len(df_metrics)] = metrics

    #print(df_metrics)
    return df_metrics

def get_dividends(driver, tickers):
    
    df_dividends = pd.DataFrame(columns=["Ticker", "Date", "Dividend"])
    
    # call metric-webpage for each ticker and scrape values
    for ticker in tickers:
            
        tickername = ticker.name
        print()
        print("ticker: ", tickername)
        history_url = "https://finance.yahoo.com/quote/"+tickername+"/history?period1=1543708800&period2=1701475200&interval=capitalGain%7Cdiv%7Csplit&filter=div&frequency=1d&includeAdjustedClose=true"
        driver.get(history_url)

         # get dividend values from website
        print("start dividend values for ticker from: ", driver.current_url)
        df_dividends = add_dividends_from_site(driver, df_dividends, tickername)

    return df_dividends



# -----------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------ MAIN -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------
print("set up driver for yahoo finance website")

options = webdriver.ChromeOptions()
options.add_argument('--headless') # for not displaying the graphical environment, shows virtualized browser without GUI
options.add_argument('--no-sandbox') # so that it can access machine resources, blocking sandbox processes it can access whatever
options.add_argument('--disable-dev-shm-usage')  # colab does not have enough memory
# open it, go to a website, and get results
driver = webdriver.Chrome(options=options)

url = "https://finance.yahoo.com/"
driver.get(url)

try:
    # Accept cookies by clicking the button with the specified ID
    print("accept cookies")
    iframe = driver.find_element(By.CLASS_NAME, 'con-wizard')
    accept_cookies_button = iframe.find_element(By.CLASS_NAME, 'accept-all')
    accept_cookies_button.click()



    #tickers = get_trending_tickers_yahoo(driver)
    tickers = get_nasdaq_100_tickers()
    
    
    df_dividends = get_dividends(driver, tickers)
    
    print()
    print("--- results ---")
    print(df_dividends)
    
    #df_metrics = get_metrics(driver, tickers)


finally:
    # Close the WebDriver
    driver.quit()
    
print()
print("finished scraping")

#print(df_metrics)


print("save data in csv")
# save to project/Dataset/data.csv
df_dividends.to_csv('./../Dataset/data_dividends.csv')



