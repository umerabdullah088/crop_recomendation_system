from pathlib import Path

import joblib
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

MODEL_PATH = (
    PROJECT_ROOT
    / "ml"
    / "fertilizer"
    / "fertilizer_model.pkl"
)

fertilizer_model = joblib.load(MODEL_PATH)


def predict_fertilizer(
    temperature,
    moisture,
    rainfall,
    ph,
    nitrogen,
    phosphorous,
    potassium,
    carbon,
    soil,
    crop,
):
    input_data = pd.DataFrame([{
        "Temperature": temperature,
        "Moisture": moisture,
        "Rainfall": rainfall,
        "PH": ph,
        "Nitrogen": nitrogen,
        "Phosphorous": phosphorous,
        "Potassium": potassium,
        "Carbon": carbon,
        "Soil": soil,
        "Crop": crop,
    }])

    prediction = fertilizer_model.predict(input_data)

    return prediction[0]