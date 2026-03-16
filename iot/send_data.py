import requests
import time
from heart_sensor import generate_heart_data

API_URL = "http://127.0.0.1:8000/predict/"

while True:
    data = generate_heart_data()
    try:
        response = requests.post(API_URL, json=data)
        print(f"Sent: {data}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"❌ Error sending data: {e}")
    time.sleep(5)
