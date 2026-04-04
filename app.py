from fastapi import FastAPI
from api.models.iris import PredictRequest, PredictResponse
import joblib
import numpy as np


app = FastAPI()
model = joblib.load("model.joblib")


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict")
def predict_iris(request: PredictRequest) -> PredictResponse:

    data = np.array(
        [
            [
                request.sepal_length,
                request.sepal_width,
                request.petal_length,
                request.petal_width,
            ]
        ]
    )

    prediction_class = model.predict(data)[0]
    target_names = ["setosa", "versicolor", "virginica"]
    result = target_names[prediction_class]

    return PredictResponse(prediction=result)
