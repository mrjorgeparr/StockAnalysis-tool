import umap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.decomposition import KernelPCA

class UMAPplot:
    def __init__(self, features, labels, n_comp, applyKernel=True):
        self.data = features
        self.labels = labels
        self.n_comp = n_comp
        self.selected_features = None  # Store selected features for printing
        assert n_comp in [2, 3], "invalid number of components"
        self.umodel = umap.UMAP(n_components=n_comp, random_state=42, n_jobs=1)
        self.umres = self.umodel.fit_transform(self.data)
        
        if applyKernel:
            self.kernel = KernelPCA(n_components=n_comp, kernel='rbf', gamma=.3)
            self.umres = self.kernel.fit_transform(self.umres)

    def plot(self, ax=None):
        if self.umres.shape[1] == 2:
            if ax is None:
                plt.scatter(self.umres[:, 0], self.umres[:, 1], c=self.labels, cmap='viridis')
                plt.title('UMAP Projection (2D)')
                plt.xlabel('UMAP Component 1')
                plt.ylabel('UMAP Component 2')
            else:
                ax.scatter(self.umres[:, 0], self.umres[:, 1], c=self.labels, cmap='viridis')
                ax.set_title('UMAP Projection (2D)')
                ax.set_xlabel('UMAP Component 1')
                ax.set_ylabel('UMAP Component 2')

        elif self.umres.shape[1] == 3:
            raise ValueError("3D plotting not supported for this example")
        else:
            raise ValueError("Invalid number of components for plotting")

if __name__ == "__main__":
    
    df = pd.read_csv('./../Dataset/scaledData.csv')
    """

    df.drop(['Unnamed: 0'], axis=1, inplace=True)
    target = 'discretized FADY'
    target = df.columns.tolist()[-1]
    y = df[target]
    X = df.drop(columns=[target, 'Ticker'], axis=1)
    
    from sklearn.impute import SimpleImputer
    imputer = SimpleImputer(strategy='mean')
    X_imputed = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)
    

    # Test the UMAPplot class
    umap_plotter = UMAPplot(features=X_imputed, labels=df[target], n_comp=2, applyKernel=True)
    umap_plotter.plot()
    plt.show()
    
    ################################# TO STUDY FEATURE SUBSETS WITH BETTER SEPARATION ##################################################
    """
    
    
    df.drop(['Unnamed: 0'], axis=1, inplace=True)
    target = 'discretized FADY'
    target = df.columns.tolist()[-1]
    y = df[target]
    X = df.drop(columns=[target, 'Ticker'], axis=1)
    
    from sklearn.impute import SimpleImputer
    imputer = SimpleImputer(strategy='mean')
    X_imputed = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)

    # Create a 6x5 grid plot for 30 random selections of 5 features
    fig, axs = plt.subplots(6, 5, figsize=(20, 20))

    for i in range(6):
        for j in range(5):
            # Select 5 random features
            selected_feature_names = np.random.choice(X.columns, size=5, replace=False)
            X_selected = X_imputed[selected_feature_names]

            # Print selected feature names to the terminal
            print(f"Selected Features for Plot {i*5 + j + 1}: {', '.join(selected_feature_names)}")

            # Initialize UMAPplot for the selected features
            umpPlotter = UMAPplot(X_selected, y, 2, applyKernel=False)
            
            # Plot the UMAP projection without kernel
            umpPlotter.plot(ax=axs[i, j])

    plt.tight_layout()
    plt.show()
    
    # umpPlotter.plot()
   
    
    """
    print(df.head())
    ############### SCALING DATA  AND DISCRETIZING ############
    df2 = df.copy()
    df2['Ticker'] = df['Ticker']
    target = 'Forward_Annual_Dividend_Yield'
    n_bins=5
    df2[target] = pd.to_numeric(df2[target], errors='coerce')
    df2[target].fillna(0, inplace=True)  # You can replace 0 with another appropriate value

    df2['discretized FADY'] = pd.cut(df2[target], bins=n_bins, labels=False)
    df2.drop(target, axis=1, inplace=True)
    df2.to_csv('./../Dataset/scaledData.csv')
    """
    


