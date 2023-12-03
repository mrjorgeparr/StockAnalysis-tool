import seaborn as sns
import pandas as pd
import os
from sklearn.metrics import silhouette_score
from sklearn.mixture import GaussianMixture as GMM
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_decision_regions
import re

def optimalGMM(data, ks):
    """
    Fitting GMM for optimal BIC
    """
    bics = []
    for ns in ks:
        gmm = GMM(n_components = ns, random_state=42)
        gmm.fit(data)
        bics.append(gmm.bic(data))
    opt = ks[bics.index(min(bics))]
    gmm = GMM(n_components = opt, random_state=42)
    gmm.fit(data)
    return gmm


if __name__=="__main__":
    ROOT = './../Dataset/umap reduced'
    TOSAVE = 'plots_nobounds'
    if not os.path.exists(TOSAVE):
        os.makedirs(TOSAVE)

    files = [f for f in os.listdir(ROOT)]
    features = ['Umap 1', 'Umap 2', 'discretized FADY']
    for f in files:
        df = pd.read_csv(os.path.join(ROOT, f))
        df = df[features]
        gmm = optimalGMM(df.iloc[:,:-1], range(1,10))
        print(df.head())
        # plot_decision_regions(df.iloc[:,:-1].values, df['discretized FADY'].values, clf=gmm, legend=2)
        plt.scatter(df['Umap 1'], df['Umap 2'], c=df['discretized FADY'].values, cmap='viridis', alpha=0.8)

        matx = re.search(r'Uv(\d+).csv', f)
        n =  int(matx.group(1))
        plt.title(f"GMM clustering for features subset: {n}")
        output_file = os.path.join(TOSAVE, f'plot_{n}.png')
        plt.savefig(output_file)

        # Clear the plot for the next iteration
        plt.clf()
