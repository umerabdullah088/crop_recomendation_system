from pathlib import Path

import joblib
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

MODEL_PATH = PROJECT_ROOT / "ml" / "crop" / "crop_model.pkl"

crop_model = joblib.load(MODEL_PATH)


def predict_crop(
    nitrogen,
    phosphorus,
    potassium,
    temperature,
    humidity,
    ph,
    rainfall,
):
    input_data = pd.DataFrame([{
        "N": nitrogen,
        "P": phosphorus,
        "K": potassium,
        "temperature": temperature,
        "humidity": humidity,
        "ph": ph,
        "rainfall": rainfall,
    }])

    prediction = crop_model.predict(input_data)

    return prediction[0]