import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression


def load_data():
    iris = load_iris()
    return iris.data, iris.target, iris.target_names


def train_model(X, y):
    model = LogisticRegression(max_iter=200)
    model.fit(X, y)
    return model


def save_model(model, filename="model.joblib"):
    joblib.dump(model, filename)


if __name__ == "__main__":
    X, y, names = load_data()
    model = train_model(X, y)
    save_model(model)
