# Hard Stop 3 – Early Implementation Validation Memo

**Course:** CISC 699 – Applied Project  
**Project:** Machine Learning-Based Phishing URL Detection System  
**Student:** Salman Ahmed  
**Date:** October 9, 2026  
**Implementation Stage:** Hard Stop 3 – Early Implementation Validation

## 1. Purpose

The purpose of this technical memo is to document the early implementation and validation results of the Machine Learning-Based Phishing URL Detection System. This validation focuses on verifying that the development environment, data ingestion, URL feature extraction, and baseline execution workflow function correctly and can support further implementation.

The objective is to demonstrate technical feasibility and identify remaining implementation risks rather than claim final classification performance.

## 2. Implementation Environment

The prototype is developed locally using the following technologies:

- **Operating system:** Windows
- **Python:** 3.11.9
- **Development environment:** Visual Studio Code
- **Application framework:** Streamlit
- **Data processing:** pandas
- **Testing framework:** pytest 9.1.1
- **Version control:** Git and GitHub
- **Environment management:** Python virtual environment (`venv`)

The Streamlit application was successfully launched locally at `http://localhost:8501`.

## 3. Implemented Components

### 3.1 Data Ingestion and Validation

The `src/data_pipeline.py` module provides basic HTTP/HTTPS URL syntax validation and CSV dataset loading.

The loader checks for the required `url` and `label` columns, removes rows with missing values, strips surrounding whitespace from URLs, and filters records that fail the current URL validation function.

The loader was executed successfully using `data/sample_urls.csv`, which contains six synthetic test records.

### 3.2 URL Feature Extraction

The `src/feature_extraction.py` module extracts seven numerical features:

1. URL length
2. Hostname/network-location length
3. Path length
4. Number of dots
5. Number of hyphens
6. Number of digits
7. HTTPS usage indicator

The function successfully extracted the expected features from `https://www.google.com`.

### 3.3 Prediction Stage

The `src/prediction.py` module currently uses a placeholder prediction function. It confirms that feature extraction has completed and that execution has reached the prediction stage.

This function is not a trained classifier and does not return actual phishing or legitimate predictions.

### 3.4 User Interface

The existing Streamlit application starts successfully and supports the baseline URL-processing interface.

## 4. Early Validation Results

| Validation Activity | Observed Result | Status |
|---|---|---|
| Streamlit application startup | Local application started | Passed |
| Sample CSV ingestion | Six records loaded | Passed |
| Feature extraction | Seven features extracted from sample URL | Passed |
| Pipeline integration test | One pytest test passed in 1.15 seconds | Passed |
| Full baseline workflow | Six URLs processed | Passed |
| Placeholder prediction integration | Six records reached the prediction stage | Passed |
| Model training | Not implemented | Pending |
| Classification performance evaluation | Not performed | Pending |

The integration test was run with:

`python -m pytest tests/test_pipeline_integration.py -v -s`

The test confirmed that six records could be loaded and that each record produced seven feature values.

The baseline workflow also demonstrated that all six sample records reached the placeholder prediction stage.

## 5. Evidence Interpretation

The successful tests provide initial evidence that the Python environment and implemented modules can operate together.

They establish that CSV loading, basic URL parsing, feature extraction, and placeholder prediction-stage execution function on the supplied synthetic examples.

However, the tests do not establish that the system can accurately distinguish phishing URLs from legitimate URLs.

The current dataset is synthetic and too small for meaningful machine learning model training or performance evaluation. In addition, negative-input cases and real-world dataset quality have not yet been fully tested.

The results should therefore be interpreted as **early technical validation rather than final model validation**.

## 6. Known Issues and Technical Risks

The following limitations remain:

- A real, public labeled phishing URL dataset has not yet been integrated.
- Logistic Regression, Decision Tree, and Random Forest training remains incomplete.
- The prediction component still returns a placeholder message.
- Classification performance metrics are unavailable.
- Automated negative-input and edge-case testing remains incomplete.
- Class imbalance, potential false positives, and model overfitting remain important evaluation risks.

These risks are tracked in `docs/risk_issue_log.md`.

The most important risk before the midpoint demonstration is the absence of a validated real-world dataset and trained classification model.

## 7. Reproducibility

The baseline project uses a local Python virtual environment with dependencies documented in `requirements.txt`.

The integration test can be rerun from the project root using:

`python -m pytest tests/test_pipeline_integration.py -v -s`

The Streamlit application can be started with:

`python -m streamlit run app/main.py`

The observed test run completed successfully. A separate clean-environment restart and dependency reinstall validation has not yet been documented and remains a follow-up activity.

## 8. Next Implementation Priorities

The next implementation sprint will prioritize:

1. Obtaining and profiling a public labeled URL dataset.
2. Verifying label meanings, missing values, duplicates, and class distributions.
3. Extending automated tests for invalid and incomplete inputs.
4. Implementing Logistic Regression, Decision Tree, and Random Forest training.
5. Evaluating models using held-out data and appropriate classification metrics.
6. Replacing the placeholder prediction function with tested model inference.
7. Integrating trained predictions into the Streamlit interface.

## 9. Supervisor Review Status

Supervisor consultation is required to confirm whether the proposed implementation sequence remains appropriate for the midpoint demonstration.

The review should focus on dataset integration, model training readiness, and the risk of entering the midpoint demonstration without a trained classifier.

**Status:** Supervisor review outcome not yet documented. This section must be updated following the actual consultation.

## 10. Conclusion

Hard Stop 3 validation demonstrates that the project's basic software components are technically operational. The Python environment supports data loading, basic lexical feature extraction, automated integration testing, and execution of the placeholder prediction workflow.

The successful results reduce uncertainty regarding initial environment and component integration. However, they do not validate the effectiveness of a phishing URL detection model.

The project is ready to continue into dataset integration and model development, subject to the remaining technical risks and supervisor feedback.