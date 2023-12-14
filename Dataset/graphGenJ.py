

import pandas as pd
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_decision_regions
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

if __name__ == "__main__":
    ns = [18,29]

    for n in ns:
        df = pd.read_csv('umap reduced/Uv'+str(n)+'.csv')
        y = df['discretized FADY']
        df = df[['UMAP 1', 'UMAP 2']]
        knn = KNeighborsClassifier(n_neighbors=1)
        knn.fit(df, y)
        plt.scatter(np.array(df)[:, 0], np.array(df)[:, 1], c=y, cmap='viridis')
        plt.title('UMAP Projection (2D)')
        plt.xlabel('UMAP Component 1')
        plt.ylabel('UMAP Component 2')
        plt.show()
        plot_decision_regions(np.array(df), np.array(y), clf=knn, legend=2)
        plt.show()