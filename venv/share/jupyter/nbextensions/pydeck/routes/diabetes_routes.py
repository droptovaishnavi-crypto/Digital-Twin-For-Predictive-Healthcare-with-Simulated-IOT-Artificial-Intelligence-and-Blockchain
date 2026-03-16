# backend/routes/diabetes_routes.py
from fastapi import APIRouter
import pickle
import pandas as pd
from utils.shap_utils import generate_shap_values

router = APIRouter()

# Load model & SHAP explainer
model = pickle.load(open("../models/diabetes_model.pkl", "rb"))
explainer = pickle.load(open("../models/diabetes_explainer.pkl", "rb"))

@router.post("/")
def predict_diabetes(data: dict):
    df = pd.DataFrame([data])
    # Predict probability
    risk = model.predict_proba(df)[0][1]
    # Get SHAP values
    shap_vals = generate_shap_values(explainer, df)
    return {"risk": float(risk), "shap_values": shap_vals}
