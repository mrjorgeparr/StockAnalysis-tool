#!apt update
#!apt install chromium-chromedriver
#!pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import pandas as pd


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
        
        metrics.append(child_elements[1].text)
        
        # TODO!
        #if get_key_from_metric_label(child_elements[0].text) != metric_label:
        #    print("Caution: modified metric-name from website " + get_key_from_metric_label(child_elements[0].text) + " differs from the used column-key: "+ metric_label )
        
        
        #metrics[get_key_from_metric_label(child_elements[0].text)] = child_elements[1].text
        #metrics.append((child_elements[0].text, child_elements[1].text))  # TODO return metric_label value (but be aware of the contains-search!)

    return metrics
    
	
# -----------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------ MAIN -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------

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
    
    required_metrics = Metrics().from_slides()
    
    df_metrics = pd.DataFrame(columns=[get_key_from_metric_label(label) for label in required_metrics])
    
    # call metric-webpage for each ticker and scrape values
    for ticker in tickers:
        #if not ticker.name == "ES=F":
        #    continue
            
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

finally:
    # Close the WebDriver
    driver.quit()
    
print()
print("finished scraping")
print(df_metrics)


import os

base = '/'.join(os.getcwd().split('/')[:-1])
datasetpath = os.path.join(base, 'Dataset')
df_metrics.to_csv(os.path.join(datasetpath, 'data.csv'))