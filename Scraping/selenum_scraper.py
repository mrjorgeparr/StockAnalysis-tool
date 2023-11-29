#!apt update
#!apt install chromium-chromedriver
#!pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait




# supporting class with constants from the website (keys etc.)
class Metrics(object):
    
    # Valuation Measures
    MARKET_CAP = 'Market Cap'
    ENTERPRISE_VALUE = 'Enterprise Value'
    
    
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
    # TODO Dividend Date ...
    
    
    def basics(self):
        return [self.MARKET_CAP, self.ENTERPRISE_VALUE]
    
    def diviends(self):
        return [self.FADR, self.FADY, self.TADR, self.TADY, self.Y5ADY, self.PR]
    
    def dividends_slides(self):
        return [self.FADY, self.TADY, self.Y5ADY, self.PR, self.PM, self.ROE, self.TC]
    
    def stability_slides(self):
        return [self.TDE, self.OCF, self.LFCF]
    
    def from_slides(self):
        return self.dividends_slides() + self.stability_slides()


def get_metrics_from_site(driver, metrics_by_label):
    metrics = []
    
    metrics_body = driver.find_element(By.ID, 'Col1-0-KeyStatistics-Proxy')
    #print(metrics_body.text)
    
    
    for metric_label in metrics_by_label:
        market_cap_element = metrics_body.find_element(By.XPATH, "//tr[contains(., '"+metric_label+"')]")
        child_elements = market_cap_element.find_elements(By.XPATH, "./*")

        assert(len(child_elements) == 2)
        metrics.append((child_elements[0].text, child_elements[1].text))  # TODO return metric_label value (but be aware of the contains-search!)

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


url = "https://finance.yahoo.com/quote/GME/key-statistics?p=GME"
driver.get(url)

print("build of driver finished")

metrics = []
try:
    # Accept cookies by clicking the button with the specified ID
    iframe = driver.find_element(By.CLASS_NAME, 'con-wizard')
    accept_cookies_button = iframe.find_element(By.CLASS_NAME, 'accept-all')
    accept_cookies_button.click()

    
    # get metric values from website
    print("start scraping metrics for ticker")
    metrics = get_metrics_from_site(driver, Metrics().from_slides())
    
    print(metrics)

finally:
    # Close the WebDriver
    driver.quit()