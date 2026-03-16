import streamlit as st
import requests

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Digital Twin Healthcare", layout="centered")

st.title("🏥 Digital Twin Predictive Healthcare")
st.write("AI + IoT + Blockchain powered predictive system")

# Tabs for Heart & Diabetes
tab1, tab2, tab3 = st.tabs(["❤️ Heart Risk", "🩸 Diabetes Risk", "⛓ Blockchain"])

# ---------------- HEART MODEL ----------------
with tab1:
    st.header("Heart Risk Prediction")

    name = st.text_input("Patient Name (Heart)", key="heart_name")
    heart_rate = st.number_input("Heart Rate (bpm)", min_value=40, max_value=200, value=80)
    systolic = st.number_input("Systolic BP (mmHg)", min_value=80, max_value=200, value=120)
    diastolic = st.number_input("Diastolic BP (mmHg)", min_value=50, max_value=120, value=80)
    temperature = st.number_input("Body Temperature (°C)", min_value=35.0, max_value=42.0, value=37.0)
    respiratory_rate = st.number_input("Respiratory Rate", min_value=10, max_value=40, value=20)

    if st.button("Predict Heart Risk"):
        payload = {
            "name": name,
            "heart_rate": heart_rate,
            "blood_pressure_systolic": systolic,
            "blood_pressure_diastolic": diastolic,
            "body_temperature": temperature,
            "respiratory_rate": respiratory_rate
        }
        response = requests.post(f"{API_URL}/predict", json=payload)
        if response.status_code == 200:
            st.success(response.json())

# ---------------- DIABETES MODEL ----------------
with tab2:
    st.header("Diabetes Risk Prediction")

    name = st.text_input("Patient Name (Diabetes)", key="diabetes_name")
    pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=1)
    glucose = st.number_input("Glucose", min_value=0, max_value=300, value=120)
    blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=200, value=70)
    skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
    insulin = st.number_input("Insulin", min_value=0, max_value=900, value=80)
    bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)
    dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.5)
    age = st.number_input("Age", min_value=1, max_value=120, value=30)

    if st.button("Predict Diabetes Risk"):
        payload = {
            "name": name,
            "Pregnancies": pregnancies,
            "Glucose": glucose,
            "BloodPressure": blood_pressure,
            "SkinThickness": skin_thickness,
            "Insulin": insulin,
            "BMI": bmi,
            "DiabetesPedigreeFunction": dpf,
            "Age": age
        }
        response = requests.post(f"{API_URL}/predict_diabetes", json=payload)
        if response.status_code == 200:
            st.success(response.json())

# ---------------- BLOCKCHAIN ----------------
with tab3:
    st.header("Blockchain Records")
    if st.button("View Blockchain"):
        response = requests.get(f"{API_URL}/chain")
        if response.status_code == 200:
            chain = response.json()
            st.json(chain)

