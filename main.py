from fastapi import FastAPI
from schema import FairInput
from predict import predict_fare

app = FastAPI(title="Taxi Fare Prediction API")

@app.get("/")
def health():
    return {"status": "ok", "service": "taxi-fare-api"}

@app.post("/predeict")
def predict(data: FairInput):
    fare = predict_fare(
        distance_km=data.distance_km,
        passenger_count=data.passenger_count,
        hour=data.hour,
        weekday=data.weekday,
        month=data.month,
        year=data.year,
    )
    return {"predicted_fare": fare}