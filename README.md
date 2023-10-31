# Stock Data Analysis and Clustering

## Overview

This project is a web analytics tool for scraping data from Yahoo Finance to obtain key financial features of stocks, including Price/Earnings (P/E) ratio, EBITDA, profit margins, Market Capitalization, yearly percentage change in stock price, and dividend rate. The goal of this project is to provide insights into stock clustering based on these features and the discretized dividend rate.

## Features

- **Web Scraping**: We utilize web scraping techniques to collect financial data from Yahoo Finance, providing detailed information on a variety of stocks.

- **Interactive Tool**: We've built an interactive tool that allows users to explore and analyze stock data, evaluate feature importance, and discover relationships between stocks.

- **Stock Clustering**: The primary objective is to cluster stocks based on their financial features. These clusters are determined with the discretized dividend rate as the target variable.

- **Dimensionality Reduction**: We employ techniques such as t-SNE (t-Distributed Stochastic Neighbor Embedding) and Autoencoders (AE) to reduce the dimensionality of the data, aiding in visualization and clustering.

- **Graph Theory and Bayesian Analysis**: We apply graph theory and Bayesian graph analysis to construct a reduced subset of data for K-Nearest Neighbors (KNN) classification, optimizing the speed and accuracy of predictions, based on the approach proposed in ***Improving kNN multi-label classification in Prototype Selection scenarios using class proposals***, reference:

                                  https://www.sciencedirect.com/science/article/pii/S0031320314004853
## Financial Features

1. **Forward Annual Dividend Yield**: Anticipates future dividend payments.

2. **Trailing Annual Dividend Yield**: Reflects the past year's performance.

3. **5-Year Average Dividend Yield**: Evaluates long-term dividend consistency.

4. **Payout Ratio**: Indicates dividend sustainability.

5. **Profit Margin**: Measures the ability to fund dividends with higher profits.

6. **Return on Equity (ROE)**: Evaluates efficiency in generating returns.

7. **Total Cash (mrq)**: Ensures dividend obligations can be met.

8. **Total Debt/Equity (mrq)**: Assesses financial conservatism.

9. **Operating Cash Flow (ttm)**: Vital for sustaining dividend payments.

10. **Levered Free Cash Flow (ttm)**: Manages debt for dividend distribution.

11. **Focus on Debt-to-Equity Ratio, Cash Flow, and Leverage**: These metrics are essential for maintaining a healthy financial structure.


## Installation

1. Clone this repository to your local machine.
   
   ```bash
   git clone https://github.com/your-username/stock-analysis.git
