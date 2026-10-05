import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import streamlit as st

from src.data_pipeline import validate_url
from src.feature_extraction import extract_placeholder_features
from src.prediction import placeholder_predict

st.set_page_config(
    page_title="Phishing URL Detection System",
    page_icon="🔐",
    layout="centered",
)

st.title("Machine Learning-Based Phishing URL Detection System")
st.caption("Pre-Hard Stop 3 implementation baseline")

st.write(
    "This baseline demonstrates the initial runnable application shell. "
    "The final machine-learning models will be integrated in later sprints."
)

url = st.text_input("Enter a URL", placeholder="https://example.com")

if st.button("Analyze URL"):
    if not validate_url(url):
        st.error("Please enter a valid URL beginning with http:// or https://")
    else:
        features = extract_placeholder_features(url)
        result = placeholder_predict(features)
        st.success(result)
        st.info("Baseline pipeline executed successfully.")
