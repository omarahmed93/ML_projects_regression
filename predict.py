# predict.py

import os
import joblib
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "taxi_fare_model.pkl")

_model = None

def get_model():
    global _model
    if _model is None:
        _model = joblib.load(MODEL_PATH)
    return _model

def predict_fare(distance_km, passenger_count, hour, weekday, month, year):
    model = get_model()
    X = np.array([[distance_km, passenger_count, hour, weekday, month, year]], dtype=float)
    y_pred = model.predict(X)
    return float(y_pred[0])