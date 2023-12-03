import pandas as pd
from knnc import kNNc
import os
from sklearn.model_selection import train_test_split
import warnings
from sklearn.preprocessing import StandardScaler


# Set the warning filter to "ignore" to suppress all warnings
warnings.filterwarnings("ignore")

# for betweenness : best accuracy .75, (k,c) = 6,4, uv26.csv
# for degree: best accuracy: .8125 (k,c) = 3,2 uv9.csv
# for closeness: best accuracy: .8125 for (k,c) = 3,2 uv9.csv
# eigenvector: 0.75, (k,c) = 6,4, best feature set is uv26.csv
# for page rank: 0.75 (k, c) = 6,4 uv26.csv


if __name__ == "__main__":
    ROOT = './../../Dataset'
    subst = os.path.join(ROOT, 'meaningfulSetsp')
    full = os.path.join(ROOT, 'umap reduced')

    dsNames= [f for f in os.listdir(full)]
    # redNames = [f for f in os.listdir(subst)]
    # print(f"Dataset names: {dsNames}")
    # print(f"Reduced subset names: {redNames}")
    target = 'discretized FADY'
    maxacc = 0
    bestparams = ''
    bestfet = ''
    for n in dsNames:
        sbst = pd.read_csv(os.path.join(subst, 'r' + n))
        zet = pd.read_csv(os.path.join(full, n))
        features = ['Umap 1', 'Umap 2', 'discretized FADY']
        print(f"File name: {n}")
        zet = zet[features]
        sbst = sbst[features]
        scaler = StandardScaler()
        # following the same train test split as for constructing the subsets
        traindf = zet.iloc[:66,:]
        testdf = zet.iloc[67:,:]
        y_train = traindf[target]
        X_train = traindf.drop(target, axis=1)
        y_test = testdf[target]
        X_test = testdf.drop(target, axis=1)
        X_trains = scaler.fit_transform(X_train)
        X_tests = scaler.fit_transform(X_test)
        X_train = pd.DataFrame(X_trains, columns = X_train.columns)
        X_test = pd.DataFrame(X_tests, columns = X_train.columns)

        # print(zet.head())
        # print(sbst.head())
        # y = zet[target]
        # X = zet.drop(target, axis=1)
        #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)
        # print(X_train)

        cvals = range(2,5)
        for c in cvals:
            for k in range(c+1,c+4):
                params = f"Parameters (k,c): {k}, {c}"
                print(params)
                knnc = kNNc(c=c, k=k)
                #print(X_train)
                #print(sbst.head())
                # print(sbst.columns)
                knnc.fit(X_train, y_train, sbst)
                #print(X_train)
                # print('\n')
                y_pred = knnc.predict(X_test)
                acc = knnc.compute_accuracy(y_pred, y_test)
                if acc >= maxacc:
                    # print('in')
                    maxacc = acc
                    bestparams = params
                    bestfet=n
                print(f"Accuracy: {acc}")
                # print(f"AUC: {knnc.compute_auc(X_test, y_test)}")

    print('\nBest accuracy and parameters found\n')
    print(f"{maxacc}")
    print(bestparams)
    print(bestfet)

            