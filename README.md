# Stock Data Analysis and Clustering

## Overview

This project is a web analytics tool for scraping data from Yahoo Finance to obtain key financial features of stocks. The objective is to provide insights into stock clustering based on these features and the discretized dividend rate.

## Features

- **Web Scraping**: Utilizing web scraping techniques to collect financial data from Yahoo Finance, providing detailed information on a variety of stocks.

- **Interactive Tool**: Building an interactive tool that allows users to explore and analyze stock data, evaluate feature importance, and discover relationships between stocks.

- **Dimensionality Reduction**: Employing techniques such as t-SNE (t-Distributed Stochastic Neighbor Embedding) and Autoencoders (AE) to reduce the dimensionality of the data, aiding in visualization. We stuck with UMAP for its topology-preserving design.

- **Graph Theory and Bayesian Analysis**: Applying graph theory and Bayesian graph analysis to construct a reduced subset of data for K-Nearest Neighbors (KNN) classification. This optimization enhances the speed and accuracy of predictions, based on the approach proposed in [Improving kNN multi-label classification in Prototype Selection scenarios using class proposals](https://www.sciencedirect.com/science/article/pii/S0031320314004853).

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

## Folder Structure

### Dataset

Contains different versions of CSVs generated throughout the project:

1. **data.csv**: Raw scraped data file.
2. **scaledData.csv**: Scaled data. The following CSVs are built by selecting features from this scaled version.
3. **v2.csv to v28.csv**: Feature subsets with varying combinations (the exact features selected can be seen in fetselection.py).

  
Subfolders:
- **umap reduced**: Stores 2D versions computed via UMAP of all feature subsets.
- **meaningfulSetsb, meaningfulSetsc, meaningfulSetsd, meaningfulSetsp**: Store reduced subsets of nodes found using different centrality metrics.

### Reduction

Contains three scripts:

1. **UMAPPlot.py**: Class for quickly plotting the 2D distribution of UMAP output.
2. **reducer.py**: Script responsible for building and storing 2D subsets found through UMAP for each feature subset.
3. **fetselection.py**: Saves and plots two visualizations of the data distribution for different feature sets.

### kNNc

Subfolders:

1. **BuildGraph**: Class for graph-building and filtering methods, creating a graph by joining samples with pairwise distances below the average and filtering out the bottom 80% based on centrality measures.
2. **kNNc**: Contains files for the kNNc algorithm, testing, benchmarking, and comparing against dummy classifiers.

### Scraping

Incremental scraping of necessary features from Yahoo Finance using Selenium. The whole procedure is in `selenium_scraper.py`, and an equivalent Jupyter notebook is also included.
