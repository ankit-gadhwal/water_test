import numpy as np
import pandas as pd
import pickle
from fastapi import FastAPI
from data_model import Water
app = FastAPI(
    title = "Water Potability Prediction",
    description = "Predicting Water Potability"
)

with open(r"model.pkl","rb") as f:
    model = pickle.load(f)

@app.get("/")
def index():
    return "Welcome to Water Potability Prediction FastAPI"

@app.post("/predict")
def model_predict(water: Water):
    sample = pd.DataFrame({
    'ph' : [water.ph],
    'hardness' : [water.hardness] ,
    'tds' : [water.tds], 
    'chlorine' : [water.chlorine], 
    'sulfate' : [water.sulfate], 
    'conductivity' : [water.conductivity], 
    'organic_carbon' : [water.organic_carbon], 
    'trihalomethanes' : [water.trihalomethanes], 
    'turbidity': [water.turbidity] 
    })

    predicted_value = model.predict(sample)
    
    if predicted_value == 1:
        return "Water is Consumable"
    else:
        return "Water is not Consumable"
