# Stock Data Analysis and Clustering

## Overview

This project is a web analytics tool for scraping data from Yahoo Finance to obtain key financial features of stocks, including Price/Earnings (P/E) ratio, EBITDA, profit margins, Market Capitalization, yearly percentage change in stock price, and dividend rate. The goal of this project is to provide insights into stock clustering based on these features and the discretized dividend rate.

## Features

- **Web Scraping**: We utilize web scraping techniques to collect financial data from Yahoo Finance, providing detailed information on a variety of stocks.

- **Interactive Tool**: We've built an interactive tool that allows users to explore and analyze stock data, evaluate feature importance, and discover relationships between stocks.

- **Stock Clustering**: The primary objective is to cluster stocks based on their financial features. These clusters are determined with the discretized dividend rate as the target variable.

- **Dimensionality Reduction**: We employ techniques such as t-SNE (t-Distributed Stochastic Neighbor Embedding) and Autoencoders (AE) to reduce the dimensionality of the data, aiding in visualization and clustering.

- **Graph Theory and Bayesian Analysis**: We apply graph theory and Bayesian graph analysis to construct a reduced subset of data for K-Nearest Neighbors (KNN) classification, optimizing the speed and accuracy of predictions.

## Financial Features

1. **Price/Earnings (P/E) Ratio**: A valuation ratio of a company's current share price compared to its earnings per share (EPS). It indicates how much investors are willing to pay for each dollar of earnings.

2. **EBITDA (Earnings Before Interest, Taxes, Depreciation, and Amortization)**: A measure of a company's operating performance that excludes interest, taxes, and non-cash expenses. It provides a clearer picture of a company's profitability.

3. **Profit Margins**: A measure of a company's profitability, often expressed as a percentage. It shows how much profit a company makes for every dollar in sales.

4. **Market Capitalization (Market Cap)**: The total value of a company's outstanding shares of stock. It is calculated by multiplying the share price by the number of outstanding shares.

5. **Yearly Percentage Change in Stock Price**: A measure of how a stock's price has changed over the past year, expressed as a percentage.

6. **Dividend Rate**: The percentage of a stock's price that is paid to shareholders as dividends. It provides an indication of the return on investment from dividends.

## Installation

1. Clone this repository to your local machine.
   
   ```bash
   git clone https://github.com/your-username/stock-analysis.git
