import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import os

# Load dataset
df = pd.read_csv("../data/diabetes.csv")

# Features and target
X = df.drop("Outcome", axis=1)
y = df["Outcome"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Diabetes Model Accuracy:", accuracy_score(y_test, y_pred))

# Save model safely
save_dir = os.path.join(os.path.dirname(__file__), "saved_models")
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

joblib.dump(model, os.path.join(save_dir, "diabetes_model.pkl"))
print(f"Model saved to {os.path.join(save_dir, 'diabetes_model.pkl')}")
