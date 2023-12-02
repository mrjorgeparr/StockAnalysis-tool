# mypackage/knnc.py
import numpy as np
from sklearn.neighbors import NearestNeighbors, KNeighborsClassifier
from sklearn.metrics import accuracy_score, roc_auc_score
from scipy.spatial import cKDTree

class kNNc:
    def __init__(self, c, k):
        self.c = c
        self.k = k
        self.subset = None
        self.knn_classifier = KNeighborsClassifier(n_neighbors=self.k)

    def fit(self, X_train, y_train, subset):
        self.x = X_train
        self.y = y_train
        self.subset = subset
        cols = list(self.subset.columns)
        # fitting nearest neighbors
        self.knn_subset = cKDTree(subset[cols[:-1]])
        #NearestNeighbors(n_neighbors=self.c).fit(self.subset)
        print('K-nearest neighbor classifier fits')

        

    def get_c_classes(self, X):
        # X is a row, a single point

        # getting indices of nearest neighbors
        _, cindices = self.knn_subset.query(X, k=self.c)
        # getting classes of neighbors on subset
        classes = self.subset.loc[cindices, 'discretized FADY'].tolist()
        # print(classes)
        return classes

    def predict(self, X_test):

        #X_test = X_test[self.subset.columns]
        labels = []
        for index, row in X_test.iterrows():

            cl = self.get_c_classes(row.values)
            # fit classifier only using training examples within
            # cl
            self.knn_classifier.fit(self.x[np.isin(self.y, cl)], self.y[np.isin(self.y, cl)])

            labels.append(self.knn_classifier.predict(np.array(row).reshape(1,-1)))

        # refit KNN only using samples who are instances of the c_classes
        return labels
    
    def compute_accuracy(self, y_pred, y_true):
        # Ensure that the features during prediction match those during fitting 
        return accuracy_score(y_pred, y_true)



if __name__ == "__main__":
    
    """
    # Example usage
    from sklearn.datasets import load_iris
    iris = load_iris()
    X, y = iris.data, iris.target
    subset = X[:-50]  # Replace this with your actual subset
    knnc = kNNc(c=3, k=5)
    knnc.fit(X, y, subset)
    y_pred = knnc.predict(X)
    print(f"Predicted labels for X: {y_pred}")
    """
    
