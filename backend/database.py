import sqlite3

DB_NAME = "health.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        age INTEGER,
        glucose REAL,
        blood_pressure REAL,
        cholesterol REAL,
        bmi REAL,
        heart_prediction INTEGER,
        diabetes_prediction INTEGER,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()
