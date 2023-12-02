# mypackage/knnc.py
import numpy as np
from sklearn.neighbors import NearestNeighbors, KNeighborsClassifier
from sklearn.metrics import accuracy_score, roc_auc_score


class kNNc:
    def __init__(self, c, k):
        self.c = c
        self.k = k
        self.subset = None
        self.knn_classifier = KNeighborsClassifier(n_neighbors=self.k)

    def fit(self, X, y, subset):
        self.subset = subset
        # fitting nearest neighbors
        self.knn_subset = NearestNeighbors(n_neighbors=self.c).fit(self.subset)
        cs = self.get_c_classes(X)
        self.knn_classifier.fit(X[np.isin(y, cs)], y)

    def get_c_classes(self, X):
        distances, indices = self.knn_subset.kneighbors(X)
        return np.unique(indices)

    def predict(self, X):
        c_classes = self.get_c_classes(X)
        return self.knn_classifier.predict(X[c_classes])
    
    def compute_accuracy(self, X, y_true):
        y_pred = self.predict(X)
        return accuracy_score(y_true, y_pred)

    def compute_auc(self, X, y_true):
        y_scores = self.knn_classifier.predict_proba(X)[:, 1]  # Assuming binary classification
        return roc_auc_score(y_true, y_scores)


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
    
