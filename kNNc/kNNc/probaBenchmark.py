import pandas as pd
import os
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

if __name__ == "__main__":
    ROOT = './../../Dataset'
    subst = os.path.join(ROOT, 'meaningfulSetsd')
    full = os.path.join(ROOT, 'umap reduced')
    dsNames= [f for f in os.listdir(full)]
    # redNames = [f for f in os.listdir(subst)]
    # print(f"Dataset names: {dsNames}")
    # print(f"Reduced subset names: {redNames}")
    target = 'discretized FADY'

    ###### TO OBSERVE THE ZERO-R benchmark
    for n in dsNames:
        zet = pd.read_csv(os.path.join(full, n))
        X = zet.drop(target, axis=1)
        y = zet[target]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train a RandomForestClassifier as a benchmark
        rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
        rf_classifier.fit(X_train, y_train)
        class_probabilities = rf_classifier.predict_proba(X_train)

        # Use DummyClassifier 
        #print(f"Value counts: {zet['discretized FADY'].value_counts(normalize=True)}")
        dummy_classifier = DummyClassifier(strategy='stratified')
        dummy_classifier.fit(class_probabilities, y_train)
        dummy_predictions = dummy_classifier.predict(rf_classifier.predict_proba(X_test))

        # Evaluate the accuracy of the dummy classifier
        accuracy = accuracy_score(y_test, dummy_predictions)
        print(f"Accuracy of the dummy classifier: {accuracy:.2f}")

    