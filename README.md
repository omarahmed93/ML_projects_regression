# ML_projects_regression

🚖 Taxi Fare Prediction API

Production-ready Machine Learning regression service built with FastAPI and Docker.

📌 Overview

This project implements an end-to-end machine learning pipeline to predict taxi fare amounts based on trip metadata (distance, passenger count, datetime features).

The trained regression model is exposed through a REST API using FastAPI and containerized using Docker for reproducible deployment.


🚀 Features

End-to-End ML pipeline (preprocessing + model)

Feature engineering from datetime

Regression model for fare prediction

Input validation using Pydantic

REST API with FastAPI

Dockerized for consistent deployment

Interactive API docs (/docs)

🧠 Model Details

Target: fare_amount

Features:

distance_km

passenger_count

hour

weekday

month

year

Preprocessing:

Datetime feature extraction

Scaling (if applied)

Feature selection

Model Type:
(e.g. Random Forest Regressor / Linear Regression / Gradient Boosting)

Evaluation Metrics:

MAE: X.XX

RMSE: X.XX

R²: 0.82 

