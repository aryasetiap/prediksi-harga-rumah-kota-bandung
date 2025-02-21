import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

# Load model yang telah disimpan
model = joblib.load("models/xgboost_house_price_model.pkl")

# Definisi request model
class HouseFeatures(BaseModel):
    installment: float
    bedroom_count: int
    bathroom_count: int
    carport_count: int
    land_area: float
    building_area: float
    location_encoded: int

@app.post("/predict")
def predict_price(features: HouseFeatures):
    data = np.array([[features.installment, features.bedroom_count, features.bathroom_count,
                      features.carport_count, features.land_area, features.building_area,
                      features.location_encoded]])
    
    prediction = model.predict(data)[0]
    
    return {"predicted_price": float(prediction)}
