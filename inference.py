import joblib
import numpy as np
from sklearn.datasets import load_iris


def load_model(filename="model.joblib"):
    return joblib.load(filename)


def predict(model, data: dict):
    iris = load_iris()
    target_names = iris.target_names

    features = np.array(
        [
            [
                data["sepal_length"],
                data["sepal_width"],
                data["petal_length"],
                data["petal_width"],
            ]
        ]
    )

    prediction_class = model.predict(features)[0]
    return target_names[prediction_class]
