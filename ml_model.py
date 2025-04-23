# ml_model.py
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

def train_model():

    iris = load_iris()
    X = iris.data
    y = iris.target


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)


    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)


    print(f"Model Accuracy: {accuracy * 100:.2f}%")


    joblib.dump(clf, 'iris_classifier.pkl')

if __name__ == "__main__":
    train_model()
