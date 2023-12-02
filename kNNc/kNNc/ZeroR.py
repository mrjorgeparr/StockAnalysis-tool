import pandas as pd
import os

if __name__ == "__main__":
    ROOT = './../../Dataset'
    subst = os.path.join(ROOT, 'meaningfulSetsd')
    full = os.path.join(ROOT, 'umap reduced')
    dsNames= [f for f in os.listdir(full)]
    # redNames = [f for f in os.listdir(subst)]
    # print(f"Dataset names: {dsNames}")
    # print(f"Reduced subset names: {redNames}")
    target = 'discretized FADY'
    for n in dsNames:
        zet = pd.read_csv(os.path.join(full, n))
        print(f"Value counts: {zet['discretized FADY'].value_counts(normalize=True)}")
    