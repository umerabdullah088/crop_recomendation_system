import joblib
import pandas as pd

# Load trained model
model = joblib.load("crop_model.pkl")

# Example input
sample = pd.DataFrame([{
    "N": 10,
    "P": 42,
    "K": 43,
    "temperature": 20.8,
    "humidity": 82,
    "ph": 6.5,
    "rainfall": 22
}])

# Predict crop
prediction = model.predict(sample)

print("Recommended Crop:", prediction[0])