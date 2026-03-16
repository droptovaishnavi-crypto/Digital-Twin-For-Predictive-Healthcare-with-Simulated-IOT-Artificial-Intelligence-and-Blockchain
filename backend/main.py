from fastapi import FastAPI
from pydantic import BaseModel
from blockchain.blockchain import Blockchain  # import correctly

app = FastAPI(title="Digital Twin Healthcare with Python Blockchain")
blockchain = Blockchain()

# ---------------- HEART MODEL ----------------
class PatientVitals(BaseModel):
    name: str
    heart_rate: float
    blood_pressure_systolic: float
    blood_pressure_diastolic: float
    body_temperature: float
    respiratory_rate: float


def simulate_health_risk(vitals: PatientVitals) -> dict:
    risk_score = (
        0.4 * (vitals.heart_rate / 100) +
        0.3 * (vitals.blood_pressure_systolic / 120) +
        0.2 * (vitals.body_temperature / 37) +
        0.1 * (vitals.respiratory_rate / 20)
    )
    risk_score = min(max(risk_score, 0.0), 1.0)
    return {
        "risk_score": round(risk_score, 2),
        "status": "high risk" if risk_score > 0.75 else "moderate risk" if risk_score > 0.5 else "low risk",
    }

# ---------------- DIABETES MODEL ----------------
class DiabetesData(BaseModel):
    name: str
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int


def simulate_diabetes_risk(data: DiabetesData) -> dict:
    score = (
        0.3 * (data.Glucose / 200) +
        0.2 * (data.BMI / 40) +
        0.2 * (data.Age / 70) +
        0.1 * (data.BloodPressure / 120) +
        0.2 * (data.Pregnancies / 10)
    )
    score = min(max(score, 0.0), 1.0)
    return {
        "risk_score": round(score, 2),
        "status": "high risk" if score > 0.75 else "moderate risk" if score > 0.5 else "low risk",
    }

# ---------------- ROUTES ----------------
@app.get("/")
def home():
    return {"message": "Digital Twin Healthcare API is running! Visit /docs for Swagger UI."}


@app.post("/predict")
def predict(vitals: PatientVitals):
    result = simulate_health_risk(vitals)
    block = blockchain.create_block(data={"patient_name": vitals.name, "type": "heart", "risk": result})
    result["block_index"] = block["index"]
    result["block_hash"] = block["hash"]
    return {"input": vitals, "prediction": result}


@app.post("/predict_diabetes")
def predict_diabetes(data: DiabetesData):
    result = simulate_diabetes_risk(data)
    block = blockchain.create_block(data={"patient_name": data.name, "type": "diabetes", "risk": result})
    result["block_index"] = block["index"]
    result["block_hash"] = block["hash"]
    return {"input": data, "prediction": result}


@app.get("/chain")
def get_chain():
    return {"chain": blockchain.get_chain(), "length": len(blockchain.get_chain())}

