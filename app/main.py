import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import streamlit as st

from src.data_pipeline import validate_url
from src.feature_extraction import extract_placeholder_features
from src.prediction import predict_url

st.set_page_config(
    page_title="Phishing URL Detection System",
    page_icon="🔐",
    layout="centered",
)


st.title("Machine Learning-Based Phishing URL Detection System")

st.caption("Hard Stop 5 - Trained Random Forest Prototype")

st.write(
    "This application uses a trained Random Forest classifier "
    "to analyze seven lexical URL features and classify URLs "
    "as potentially phishing or legitimate."
)

st.warning(
    "Research prototype only. Predictions may contain false "
    "positives or false negatives and should not be used "
    "as a definitive website safety assessment."
)


url = st.text_input("Enter a URL", placeholder="https://example.com")

if st.button("Analyze URL"):
    if not validate_url(url):
        st.error("Please enter a valid URL beginning with http:// or https://")
    else:
        features = extract_placeholder_features(url)
        result = predict_url(features)
        st.success(result)
        st.info("Random Forest model inference completed.")
