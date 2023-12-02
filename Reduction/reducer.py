from umap import UMAP
import pandas as pd
import os
import copy
############################# this file processed all feature subsets, computes the UMAP 2-D representation and stores them
if __name__ == "__main__":
    # df = pd.read_csv('./../Dataset/scaledData.csv')
    base = './../Dataset/umap reduced'
    files = [f for f in os.listdir(base) if f[0] == 'v']
    for f in files:
        df = pd.read_csv(os.path.join(base, f))
        ump = UMAP(n_components=2, random_state=42, n_jobs=1)
        df2 = df.copy()
        df2.drop('discretized FADY', axis=1)
        from sklearn.impute import SimpleImputer
        imputer = SimpleImputer(strategy='mean')
        X_imputed = pd.DataFrame(imputer.fit_transform(df2), columns=df2.columns)

        embedded = pd.DataFrame(ump.fit_transform(X_imputed), columns = ['Umap 1', 'Umap 2'])
        embedded['discretized FADY'] = df['discretized FADY']
        embedded.to_csv(os.path.join(base, 'U' + f))
        