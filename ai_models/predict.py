import joblib
import os

heart_model = joblib.load(os.path.join("ai_models/saved_models", "heart_model.pkl"))
diabetes_model = joblib.load(os.path.join("ai_models/saved_models", "diabetes_model.pkl"))

def predict_risk(age, glucose, blood_pressure, cholesterol, bmi):
    # Heart model needs cholesterol too
    heart_features = [[age, blood_pressure, cholesterol, bmi, glucose]]
    heart_pred = heart_model.predict(heart_features)[0]

    # Diabetes model
    diabetes_features = [[glucose, blood_pressure, bmi, age]]
    diabetes_pred = diabetes_model.predict(diabetes_features)[0]

    return int(heart_pred), int(diabetes_pred)
