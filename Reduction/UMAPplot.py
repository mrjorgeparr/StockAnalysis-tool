import umap 
import matplotlib.pyplot as plt
import numpy as np


class UMAPplot:
    """
    Preliminary design of a UMAPplot class to quickly
    assess how good our data separation is
    """
    def __init__(self, features, labels, n_comp):
        self.data = features
        self.labels = labels
        assert n_comp in [2,3], "invalid number of components"
        self.umodel = umap.UMAP(n_components=n_comp)
        self.umres = self.umodel.fit_transform(self.data)

    def plot(self):
        if self.umres.shape[1] == 2:
            plt.scatter(self.umres[:, 0], self.umres[:, 1], c=self.labels, cmap='viridis')
            plt.title('UMAP Projection (2D)')
            plt.xlabel('UMAP Component 1')
            plt.ylabel('UMAP Component 2')
            plt.colorbar()
            plt.show()
        elif self.umres.shape[1] == 3:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            sc = ax.scatter(self.umres[:, 0], self.umres[:, 1], self.umres[:, 2], c=self.labels, cmap='viridis')
            plt.title('UMAP Projection (3D)')
            ax.set_xlabel('UMAP Component 1')
            ax.set_ylabel('UMAP Component 2')
            ax.set_zlabel('UMAP Component 3')
            plt.colorbar(sc)
            plt.show()
        else:
            raise ValueError("Invalid number of components for plotting")

