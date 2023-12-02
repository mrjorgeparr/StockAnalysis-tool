import pandas as pd
import os


if __name__ == "__main__":
    base = './meaningfulSetse'
    files = os.listdir(os.path.join(base))

    for f in files:
        df = pd.read_csv(os.path.join(base, f))
        df.drop('Unnamed: 0.1', axis=1, inplace=True)
        df.to_csv(os.path.join(base, f))