from baseBuilder import baseBuilder
from GPclass import GPclass
import pandas as pd
import os
from sklearn.model_selection import train_test_split


if __name__ == "__main__":
    base = './../../Dataset'
    tosave = os.path.join(base, 'meaningfulSetsd')
    os.makedirs(tosave)
    target = 'discretized FADY'
    files = [f for f in os.listdir(os.path.join(base, 'umap reduced'))]
    print(files)
    
    for f in files:
        df = pd.read_csv(os.path.join(base, 'umap reduced', f))
        # splitting because the reduced subset should only be composed out of the training
        bf = GPclass()
        y = df[target]
        X = df.drop(target, axis=1)
        # this is the equivalent of a test train split, because we know there are 83 samples in our dataset
        df = df.iloc[:66,:]
        bf.ccrm("degree", df.values, VERBOSE=False)
        nodes = list(bf.graph.nodes)
        msbs = df.iloc[nodes, :]
        msbs.to_csv(os.path.join(tosave, 'r'+f))


        