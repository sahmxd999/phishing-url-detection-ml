# Architecture Notes

## Project
Machine Learning-Based Phishing URL Detection System

## Baseline Architecture

1. **Streamlit User Interface**
   - Accepts a URL from the user.
   - Displays validation and pipeline status.

2. **URL Validation**
   - Confirms that the input is non-empty.
   - Confirms use of the HTTP or HTTPS scheme.
   - Confirms that a network location is present.

3. **Feature Extraction**
   - The baseline extracts simple lexical URL characteristics.
   - Future sprints will finalize the feature set based on the approved design.

4. **Model Layer**
   - Current version contains a placeholder prediction stage.
   - Future versions will compare:
     - Logistic Regression
     - Decision Tree
     - Random Forest

5. **Evaluation Layer**
   - Planned metrics:
     - Accuracy
     - Precision
     - Recall
     - F1-score
     - False-positive rate
     - Confusion matrices

## Architecture-to-Code Mapping

| Architecture Element | Current Location |
|---|---|
| User Interface | `app/main.py` |
| URL Validation / Data Pipeline | `src/data_pipeline.py` |
| Feature Extraction | `src/feature_extraction.py` |
| Model Training | `src/model_training.py` |
| Prediction | `src/prediction.py` |
| Smoke Test | `tests/test_smoke.py` |

## Scope Boundary

The project is designed as a local academic prototype. It does not perform malware
execution, unrestricted live crawling, production deployment, or commercial threat
intelligence integration.
