# src/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Cargar modelo y scaler
model = joblib.load("../models/rf_model.joblib")
scaler = joblib.load("../models/scaler.joblib")

# Definir los campos que espera la API (24 features)
class CreditInput(BaseModel):
    LIMIT_BAL: float
    SEX: int
    EDUCATION: int
    MARRIAGE: int
    AGE: int
    PAY_0: int
    PAY_2: int
    PAY_3: int
    PAY_4: int
    PAY_5: int
    PAY_6: int
    BILL_AMT1: float
    BILL_AMT2: float
    BILL_AMT3: float
    BILL_AMT4: float
    BILL_AMT5: float
    BILL_AMT6: float
    PAY_AMT1: float
    PAY_AMT2: float
    PAY_AMT3: float
    PAY_AMT4: float
    PAY_AMT5: float
    PAY_AMT6: float

@app.post("/predict")
def predict_credit_default(data: CreditInput):
    input_data = np.array([[getattr(data, field) for field in data.__fields__]])
    scaled_data = scaler.transform(input_data)
    prediction = model.predict(scaled_data)
    return {"default_prediction": int(prediction[0])}

