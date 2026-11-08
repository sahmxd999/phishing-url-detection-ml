
# Hard Stop 5 — Reproducibility Log

**Project:** Machine Learning-Based Phishing URL Detection System  
**Student:** Salman Ahmed  
**Course:** CISC 699 Applied Project  
**Date:** November 8, 2026

## Environment

- Operating system: Windows
- Python: 3.11.9
- Streamlit: 1.65.0
- Scikit-learn: 1.9.1
- Pandas: 3.0.6
- NumPy: 2.4.6
- Joblib: 1.6.0
- Pytest: 9.1.1

## Reproducibility Steps and Results

| Step | Action | Observed Result |
|---|---|---|
| 1 | Created `venv_clean` | Environment created |
| 2 | Installed dependencies from `requirements.txt` | Installation completed |
| 3 | Ran pytest using `venv_clean` | 2 tests passed |
| 4 | Repeated pytest execution | 2 tests passed |
| 5 | Loaded saved Random Forest model | Successful |
| 6 | Inspected model feature count | 7 features |
| 7 | Tested Streamlit prediction in the original environment | Prediction displayed |
| 8 | Submitted invalid URL `hello123` | Validation error displayed |

## Model Integration

The Random Forest model was saved as:

`models/random_forest.joblib`

The application loads this model using Joblib and performs inference using seven lexical URL features.

## Observed Limitations

- The model classified `https://example.com` as phishing.
- The Streamlit validator requires URLs beginning with HTTP or HTTPS.
- The experimental feature parser handles some scheme-less URLs.
- Only two automated tests were executed.
- A completely independent repository checkout was not tested.

## Conclusion

A fresh Python virtual environment successfully installed the recorded dependencies, ran the existing tests, and loaded the trained Random Forest model.

This demonstrates partial reproducibility within the existing project directory. Independent repository-level reproduction remains to be verified.
