
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

## Hard Stop 5 — Independent GitHub Checkout Verification

Verification date: November 10, 2026

Repository:
https://github.com/sahmxd999/phishing-url-detection-ml

Branch: hard-stop-5

### Verification Environment

- Operating system: Windows
- Python version: 3.11.9
- Fresh GitHub clone: Successful
- Separate Python virtual environment: Created
- Dependency installation: Completed

### Automated Testing

Command:
.\venv\Scripts\python.exe -m pytest -q

Observed result:
2 passed in 54.23 seconds

### Saved Model Verification

The tracked Random Forest model loaded successfully.

- Model: RandomForestClassifier
- Expected input features: 7

### Streamlit Verification

Command:
.\venv\Scripts\python.exe -m streamlit run app/main.py

The application launched from the cloned repository.

Test URL:
https://www.google.com

Observed prediction:
PHISHING

This is a known false positive, not a correct
classification.

### Verification Scope

The independent checkout confirmed:

- Repository accessibility
- Python environment setup
- Automated test execution
- Saved model loading
- Streamlit application execution

Full preprocessing and model-training reproduction
from the external Kaggle dataset has not yet been
verified in this checkout.

## Hard Stop 5 — Full Workflow Reproduction

Verification date: November 10, 2026

Environment:
Independent clone of the hard-stop-5 GitHub branch.
Windows, Python 3.11.9.

### Dataset Preparation

Command:
python -m src.prepare_dataset

Result:
- Total processed URLs: 522,160
- Legitimate URLs: 428,074
- Phishing URLs: 94,086
- Remaining duplicate URLs: 0

Status: Passed

### Model Training

Command:
python -m src.model_training

The following models trained successfully:

- Logistic Regression: 72.80% accuracy
- Decision Tree: 82.73% accuracy
- Random Forest: 84.70% accuracy

Training used 20,000 balanced examples and
random seed 42.

Status: Passed

### Hard Stop 5 Experimental Reproduction

Command:
python -m src.hs5_experiment

Baseline Random Forest:
- Accuracy: 84.70%
- Recall: 84.55%
- False-positive rate: 15.15%

Weighted Random Forest:
- Accuracy: 80.95%
- Recall: 65.95%
- False-positive rate: 4.05%

The weighted model reduced false positives,
but also reduced phishing recall.

Both models incorrectly classified five
legitimate homepage URLs as phishing.

The empty-path evaluation contained 481 URLs,
of which 479 were labeled phishing and two
were labeled legitimate.

Both legitimate empty-path examples were
incorrectly classified as phishing.

Status: Passed — Results reproduced.

### Final Verification Summary

The following were independently reproduced:

- Dataset preprocessing
- Model training
- Model evaluation
- Hard Stop 5 experimental comparison

The external Kaggle dataset was supplied
separately and was not downloaded automatically
by the repository.

The system remains a research prototype with
known false-positive and generalization
limitations.
