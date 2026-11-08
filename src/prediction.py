
from pathlib import Path

import joblib
import pandas as pd

MODEL_PATH = Path(__file__).resolve().parents[1] / "models" / "random_forest.joblib"

FEATURE_NAMES = [
    "url_length",
    "hostname_length",
    "path_length",
    "dot_count",
    "hyphen_count",
    "digit_count",
    "uses_https",
]


def predict_url(features: dict) -> str:
    """Predict whether a URL is phishing or legitimate."""
    if not isinstance(features, dict):
        raise ValueError("Features must be a dictionary.")

    missing = [name for name in FEATURE_NAMES if name not in features]
    if missing:
        raise ValueError(f"Missing URL features: {missing}")

    if not MODEL_PATH.is_file():
        raise FileNotFoundError("Trained model not found. Run model training first.")

    model = joblib.load(MODEL_PATH)

    X = pd.DataFrame(
        [[features[name] for name in FEATURE_NAMES]],
        columns=FEATURE_NAMES,
    )

    prediction = int(model.predict(X)[0])

    if prediction == 1:
        return "PHISHING - This URL was classified as potentially malicious."

    return "LEGITIMATE - This URL was classified as legitimate."
