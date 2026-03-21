# 🚖 Taxi Fare Prediction API

A production-ready machine learning regression service for predicting taxi fare amounts from trip metadata using **FastAPI**, **Scikit-learn**, and **Docker**.

## 📌 Project Overview

This project delivers an end-to-end machine learning workflow for **taxi fare prediction**, transforming raw trip-related inputs into real-time fare estimates through a REST API.

The solution covers:
- feature engineering from trip datetime data
- regression model training and evaluation
- API deployment with FastAPI
- containerized execution with Docker for reproducibility

This project demonstrates how machine learning can be operationalized into a deployable service rather than remaining only in a notebook environment.

---

## 🎯 Business Problem

Accurate fare estimation is important for ride-hailing and transport platforms because it helps:

- provide transparent upfront pricing to users
- improve customer trust and experience
- support pricing consistency across trips
- enable integration into booking or dispatch systems

This API simulates a real-world ML service that predicts fares instantly based on trip characteristics.

---

## 🛠️ Tech Stack

- **Python**
- **Pandas / NumPy**
- **Scikit-learn**
- **FastAPI**
- **Pydantic**
- **Docker**
- **Uvicorn**

---

## 📂 Input Features

The model predicts `fare_amount` using the following features:

- `distance_km`
- `passenger_count`
- `hour`
- `weekday`
- `month`
- `year`

---

## ⚙️ Machine Learning Pipeline

The project includes an end-to-end regression workflow with:

1. data preprocessing  
2. datetime-based feature engineering  
3. feature selection  
4. model training  
5. model evaluation  
6. REST API inference

### Preprocessing and Feature Engineering
- extracted time-based features from trip datetime
- prepared structured numeric inputs for prediction
- applied scaling where needed
- selected relevant trip-level features

---

## 🧠 Model Information

- **Task:** Regression
- **Target Variable:** `fare_amount`
- **Model Type:** `Random Forest Regressor`  
  \_replace this with the exact model you actually used if different

### Evaluation Metrics
- **MAE:** 2.004
- **RMSE:** 3.8101
- **R² Score:** 0.82

These results indicate that the model explains a strong proportion of fare variance while maintaining relatively low prediction error.

---

## 📊 Model Performance Interpretation

- **R² = 0.82** means the model explains 82% of the variation in taxi fare amounts.
- **MAE = 2.004** means predictions are off by about 2 fare units on average.
- **RMSE = 3.8101** indicates some larger errors exist, which is expected in fare prediction due to trip variability and potential outliers.

---

## 🌐 API Features

- FastAPI-based REST service
- input validation with Pydantic
- interactive API documentation with Swagger UI
- containerized deployment with Docker
- clean and reusable inference workflow

---

## 📥 Example Request

### Endpoint
```http
POST /predict
---

---

## 📥 Example Request

### Endpoint
```http
POST /predict
```

### Sample Input
```json
{
  "distance_km": 5.2,
  "passenger_count": 2,
  "hour": 14,
  "weekday": 3,
  "month": 6,
  "year": 2024
}
```

### Sample Response
```json
{
  "predicted_fare": 12.45
}
```

---

## 🚀 Running the Project Locally

### 1. Clone the repository
```bash
git clone https://github.com/omarahmed93/ML_projects_regression.git
cd ML_projects_regression
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the FastAPI application
```bash
uvicorn main:app --reload
```

### 4. Open the interactive docs
```bash
http://127.0.0.1:8000/docs
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the FastAPI application
```bash
uvicorn main:app --reload
```

### 4. Open the interactive docs
```bash
http://127.0.0.1:8000/docs
```

---

## 🐳 Run with Docker

### Build Docker image
```bash
docker build -t taxi-fare-api .
```

### Run container
```bash
docker run -p 8000:8000 taxi-fare-api
```

### Open the API docs
```bash
http://127.0.0.1:8000/docs
```

## 📁 Project Structure

```bash
ML_projects_regression/
│
├── main.py
├── predict.py
├── schema.py
├── model.pkl
├── requirements.txt
├── Dockerfile
└── README.md
