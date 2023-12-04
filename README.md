# Stock Data Analysis and Clustering

## Overview

This project is a web analytics tool for scraping data from Yahoo Finance to obtain key financial features of stocks. The objective is to provide insights into stock clustering based on these features and the discretized dividend rate.


## Features

- **Web Scraping**: We utilize web scraping techniques to collect financial data from Yahoo Finance, providing detailed information on a variety of stocks.

- **Interactive Tool**: We've built an interactive tool that allows users to explore and analyze stock data, evaluate feature importance, and discover relationships between stocks.


- **Dimensionality Reduction**: We employ techniques such as t-SNE (t-Distributed Stochastic Neighbor Embedding) and Autoencoders (AE) to reduce the dimensionality of the data, aiding in visualization, we stuck with UMAP, for its topology preserving design.

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




## Folder structure


#### Dataset

Contains the different versions of csvs that are generated throughout the completion of the project. It contains:
   1. data.csv: the raw scraped data file
   2. scaledData.csv: scaled data. The following csvs are built selecting features from this scaled version.
   3. v2.csv: feature subset that contains 5_Year_Average_Dividend_Yield,Payout_Ratio,Total_Debt/Equity_(mrq),Return_on_Equity,Trailing_Annual_Dividend_Yield
   4. v3.csv: feature subset that contains Return_on_Equity,Total_Debt/Equity_(mrq),Payout_Ratio,Trailing_Annual_Dividend_Yield,Total_Cash_(mrq)
   5. v4.csv: feature subset containing Trailing_Annual_Dividend_Yield,Return_on_Equity,Total_Debt/Equity_(mrq),Payout_Ratio and Profit_Margin.
   6. v9.csv: contains Return_on_Equity, Total_Cash_(mrq),  Trailing_Annual_Dividend_Yield, 5_Year_Average_Dividend_Yield and Profit_Margin.
   7. v14.csv: Total_Cash_(mrq), 5_Year_Average_Dividend_Yield, Trailing_Annual_Dividend_Yield, Operating_Cash_Flow, Payout_Ratio
   8. v17.csv: Levered_Free_Cash_Flow, Total_Cash_(mrq),Payout_Ratio, Trailing_Annual_Dividend_Yield and Operating_Cash_Flow
   9. v20.csv: Return_on_Equity, Total_Debt/Equity_(mrq),Total_Cash_(mrq), Levered_Free_Cash_Flow and '5_Year_Average_Dividend_Yield'
   10. v21.csv: Levered_Free_Cash_Flow, Profit_Margin, Total_Cash_(mrq), Payout_Ratio and 5_Year_Average_Dividend_Yield
   11. v22.csv: Levered_Free_Cash_Flow, Total_Cash_(mrq), Payout_Ratio, Trailing_Annual_Dividend_Yield and Operating_Cash_Flow
   12. v25.csv: Trailing_Annual_Dividend_Yield,5_Year_Average_Dividend_Yield, Return_on_Equity, Levered_Free_Cash_Flow and Total_Cash_(mrq)
   13. v26.csv: Return_on_Equity, Trailing_Annual_Dividend_Yield, Total_Debt/Equity_(mrq), Total_Cash_(mrq) and 5_Year_Average_Dividend_Yield
   14. v28.csv: Trailing_Annual_Dividend_Yield, 5_Year_Average_Dividend_Yield, Total_Debt/Equity_(mrq), Return_on_Equity and Operating_Cash_Flow

 Now on top of these files we have the following 6 subfolders

   1. umap reduced: stores the 2-d versions computed via UMAP of all the feature subsets explained above
   2. meaningfulSetsb: stores, for all feature subsets, the reduced subsets of nodes found using the betweenness centrality as analysis metric
   3. meaningfulSetsc: the same as above but for closeness centrality.
   4. meaningfulSetsd: the same but for degree centrality
   5. meaningfulSetsp: the same but for page rank.

#### Reduction

This folder contains three different scripts

   1. UMAPPlot.py: class for quickly plotting the 2d (or 3d, however this case is never used) distribution of the output of UMAP, so that we are able to assess rapidly the suitability of the features for our graph-based method.

   2. reducer.py: script responsible for actually building and storing the 2-d subsets found through UMAP corresponding to each of the feature subsets explained above.

   3. fetselection.py: for the different feature sets, it saves and plots two different visualizations of the data distribution, a regular scatter plot, and one where the Voronoi regions are also displayed.

 #### kNNc

 This folder contains two subfolders, buildGraph, and kNNc
    1. BuildGraph: in an incremental, OOP approach we developed a class that encompasses the graph-building procedure and the filtering methods that were proposed, i.e., from the data it creates a graph by       joining those samples whose pairwise distance is below the average and then filters out the bottom 80% in terms of some centrality measure in a class-wise manner.

  2. kNNc: this subfolder contains 4 different files
         + knnc.py: the class implementation for the kNNc algorithm itself
     
         + main.py: where the class is tested fort he different centrality measures and feature subsets, with the hyperparameters tuned and the results found.
     
         + probaBenchmark.py: benchmarking our classifier's performance against a dummy classifier that is based on guessing, this test is passed easily.
     
         + ZeroR.py: different benchmark which is also passed by 13-19% accuracy


#### Scraping

In an incremental approach we scraped the necessary features from yahoo finance employing selenium, the whole procedure is in selenum_scraper.py, and equivalent jupyter notebook is also included.
