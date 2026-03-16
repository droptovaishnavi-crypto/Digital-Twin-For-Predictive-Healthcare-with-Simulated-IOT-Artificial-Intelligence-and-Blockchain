import random

def generate_heart_data():
    """Generate simulated patient vitals for digital twin prediction."""
    return {
        "patient_id": 1,
        "age": random.randint(20, 80),
        "glucose": random.randint(70, 180),
        "blood_pressure": random.randint(90, 140),
        "cholesterol": random.randint(150, 300),
        "bmi": round(random.uniform(18.5, 35.0), 1),
        "heart_rate": random.randint(60, 100),
        "blood_pressure_systolic": random.randint(110, 140),
        "blood_pressure_diastolic": random.randint(70, 90),
        "body_temperature": round(random.uniform(97.0, 99.5), 1),
        "respiratory_rate": random.randint(12, 20)
    }

if __name__ == "__main__":
    import time
    while True:
        print("❤️ Heart Sensor Data:", generate_heart_data())
        time.sleep(3)
