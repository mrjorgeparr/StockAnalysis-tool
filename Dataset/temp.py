import pandas as pd

if __name__ == "__main__":
    raw = pd.read_csv('data.csv')
    v2 = pd.read_csv('v2.csv')

    # Merge DataFrames based on index
    merged_df = pd.concat([raw['Ticker'], v2['discretized FADY']], axis=1)

    # Rename columns
    merged_df.columns = ['Ticker', 'discretized FADY']

    # Save the resulting DataFrame to a new CSV file
    merged_df.to_csv('dFadydis.csv', index=False)
