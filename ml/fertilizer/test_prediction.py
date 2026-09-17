import joblib
import pandas as pd

# Load trained model
model = joblib.load("fertilizer_model.pkl")


# Sample farmer data
input_data = pd.DataFrame([{
    "Temperature": 25,
    "Moisture": 45,
    "Rainfall": 100,
    "PH": 6.5,
    "Nitrogen": 80,
    "Phosphorous": 40,
    "Potassium": 40,
    "Carbon": 1.5,
    "Soil": "Loamy",
    "Crop": "Rice"
}])


# Make prediction
prediction = model.predict(input_data)


print("=" * 50)
print("FERTILIZER RECOMMENDATION")
print("=" * 50)

print("\nInput Data:")
print(input_data.to_string(index=False))

print("\nRecommended Fertilizer:", prediction[0])

print("=" * 50)