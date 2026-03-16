import random
import time

def generate_glucose_data():
    return {
        "Pregnancies": random.randint(0, 10),
        "Glucose": random.randint(80, 200),
        "BloodPressure": random.randint(60, 120),
        "SkinThickness": random.randint(10, 50),
        "Insulin": random.randint(15, 200),
        "BMI": round(random.uniform(18, 40), 1),
        "DiabetesPedigreeFunction": round(random.uniform(0.1, 2.5), 2),
        "Age": random.randint(20, 70),
    }

if __name__ == "__main__":
    while True:
        print("📊 Glucose Sensor Data:", generate_glucose_data())
        time.sleep(3)



