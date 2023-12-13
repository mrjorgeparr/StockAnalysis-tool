import pandas as pd
from sklearn.preprocessing import StandardScaler


if __name__ == "__main__":

    ########### SCALING DATA #######################
    
    raw = pd.read_csv('data.csv')
    # v2 = pd.read_csv('v2.csv')
    tickers= raw.iloc[:, :1]
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(raw.iloc[:, 2:])

    # Concatenate the first column with the scaled data
    scaled_df = pd.concat([tickers, pd.DataFrame(scaled_data, columns=raw.columns[2:])], axis=1)

    scaled_df.to_csv('scaledData.csv', index=False)
    """
    # Merge DataFrames based on index
    merged_df = pd.concat([raw['Ticker'], v2['discretized FADY']], axis=1)

    # Rename columns
    merged_df.columns = ['Ticker', 'discretized FADY']

    # Save the resulting DataFrame to a new CSV file
    merged_df.to_csv('dFadydis.csv', index=False)
    """
