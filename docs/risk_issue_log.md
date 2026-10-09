# Risk and Issue Log

| ID | Type | Description | Severity | Mitigation / Action | Owner | Status |
|---|---|---|---|---|---|---|
| R-01 | Risk | Public dataset may contain missing, duplicated, or inconsistent records. | Medium | Validate, clean, deduplicate, and document preprocessing decisions before model training. | Salman Ahmed | Open |
| R-02 | Risk | Class imbalance may bias phishing-versus-legitimate predictions. | High | Inspect class distribution and use a stratified data split; report class-specific metrics. | Salman Ahmed | Open |
| R-03 | Risk | Lexical features may generate false positives for unusual legitimate URLs. | High | Track false-positive rate and conduct error analysis on misclassified URLs. | Salman Ahmed | Open |
| R-04 | Risk | Package or Python-version incompatibility may reduce reproducibility. | Medium | Use a virtual environment, maintain `requirements.txt`, and record the tested Python version. | Salman Ahmed | Monitoring |
| R-05 | Risk | One model may overfit the training dataset. | High | Compare train/test performance and evaluate Logistic Regression, Decision Tree, and Random Forest under the same procedure. | Salman Ahmed | Open |
| I-01 | Issue | Final machine-learning model is not integrated in the baseline release. | Low | Implement model training and validation in the next development sprint. | Salman Ahmed | Planned |
| I-02 | Issue | Current prediction output is intentionally a placeholder. | Low | Replace placeholder prediction after the approved model pipeline is implemented and tested. | Salman Ahmed | Planned |

## Review Practice

This log should be reviewed at least once per sprint. Status values should be updated
when risks are mitigated, accepted, closed, or converted into active issues.



## Hard Stop 3 - Early Implementation Validation Update

**Review Date:** October 9, 2026

### Validation Summary

The initial implementation was tested using six synthetic
URL records.

Completed validation activities:

- Streamlit application started successfully.
- CSV dataset ingestion completed successfully.
- Six sample records were loaded.
- Seven lexical features were extracted per URL.
- Pytest integration test passed (1 passed in 1.15s).
- All six records reached the placeholder prediction stage.

These tests demonstrate baseline technical functionality.
They do not establish phishing detection accuracy.

### New and Outstanding Issues

#### I-03: Real Labeled Dataset Not Integrated
- Type: Issue
- Severity: High
- Status: Open
- Description: The current validation uses six synthetic URL
  records rather than a public labeled phishing dataset.
- Impact: Real-world data quality and model performance
  cannot yet be evaluated.
- Action: Acquire a public labeled dataset, profile its
  columns, validate labels, and document preprocessing.

#### I-04: Automated Negative-Input Testing Incomplete
- Type: Issue
- Severity: Medium
- Status: Open
- Description: The current integration test confirms
  successful processing of six valid sample URLs.
  Invalid URLs, missing columns, and empty datasets
  have not yet been covered by automated tests.
- Impact: Error-handling behavior is insufficiently tested.
- Action: Add negative-input tests for dataset loading
  and URL validation.

#### I-05: Model Performance Evidence Unavailable
- Type: Issue
- Severity: High
- Status: Open
- Description: Logistic Regression, Decision Tree,
  and Random Forest models have not yet been trained.
- Impact: Accuracy, precision, recall, F1-score,
  and false-positive rate cannot be reported.
- Action: Implement training and held-out evaluation
  after acquiring and validating real labeled data.

### Existing Issues Reviewed

- I-01: Model training remains planned and incomplete.
- I-02: Prediction output remains a placeholder.
- R-01: Dataset quality risk remains open.
- R-02: Class imbalance risk remains open.
- R-03: False-positive risk remains open.
- R-04: Environment compatibility remains under monitoring.
- R-05: Model overfitting risk remains open.

### Midpoint Review Priority

The highest-priority technical risk is the lack of a
validated real-world labeled dataset and trained
classification model.

The next sprint should prioritize dataset integration,
label validation, basic model training, and reproducible
evaluation before the midpoint demonstration.

### Current Workaround

Until trained models are available, the application
uses a clearly labeled placeholder prediction stage.

The placeholder confirms that the core execution path
was reached, but must not be presented as an actual
phishing classification.
