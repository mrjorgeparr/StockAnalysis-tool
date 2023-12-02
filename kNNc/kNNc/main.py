import pandas as pd
from knnc import kNNc
import os
from sklearn.model_selection import train_test_split

if __name__ == "__main__":
    ROOT = './../../Dataset'
    subst = os.path.join(ROOT, 'meaningfulSetse')
    full = os.path.join(ROOT, 'umap reduced')

    dsNames= [f for f in os.listdir(full)]
    # redNames = [f for f in os.listdir(subst)]
    # print(f"Dataset names: {dsNames}")
    # print(f"Reduced subset names: {redNames}")
    target = 'discretized FADY'
    for n in dsNames:
        knnc = kNNc(c=3, k=5)
        sbst = pd.read_csv(os.path.join(subst, 'r' + n))
        zet = pd.read_csv(os.path.join(full, n))
        features = ['Umap 1', 'Umap 2', 'discretized FADY']
        print(f"File name: {n}")
        #zet.drop('Unnamed: 0', axis=1, inplace=True)
        # sbst.drop(['Unnamed: 0.1, Unnamed: 0'], axis=1, inplace=True)
        
        zet = zet[features]
        sbst = sbst[features]
        print(zet.head())
        print(sbst.head())
        y = zet[target]
        X = zet.drop(target, axis=1)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        #print(X_train)
        #print(sbst.head())
        # Check if the number of features in X_train and sbst is the same
        # assert X_train.shape[1] == sbst.shape[1], "Number of features in X_train and sbst must be the same"
        
        knnc.fit(X_train.values, y_train.values, sbst.values)
        print(f"Accuracy: {knnc.compute_accuracy(X_test, y_test)}")
        print(f"AUC: {knnc.compute_auc(X_test, y_test)}")

    