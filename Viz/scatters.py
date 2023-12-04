import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":
    ROOT = './../Dataset/umap reduced'
    files = [f for f in os.listdir(ROOT)]
    for f in files:
        df = pd.read_csv(os.path.join(ROOT,f))
        res = np.array(df)
        plt.scatter(res[:, 0], res[:, 1],c= res[:,2], cmap='viridis')
        plt.title('UMAP Projection (2D)')
        plt.xlabel('UMAP Component 1')
        plt.ylabel('UMAP Component 2')
        plt.show()