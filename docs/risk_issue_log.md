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


## Hard Stop 4 — Technical Evidence Review
Date: October 26, 2026
Project: Machine Learning-Based Phishing URL Detection System

### Evidence Collected

- Original dataset: 651,191 URL records.
- Cleaned binary dataset: 522,160 unique URLs.
- Legitimate URLs: 428,074.
- Phishing URLs: 94,086.
- Duplicate URLs remaining: 0.
- Conflicting URL labels detected in original data: 6 URLs.
- URL parsing failures: 17, all phishing-labeled.
- Automated regression tests: 2 passed in 1.08 seconds.

### Model Benchmark Results

Balanced dataset experiment:
- 20,000 URLs; 16,000 training and 4,000 testing.
- Logistic Regression accuracy: 72.80%.
- Decision Tree accuracy: 82.73%.
- Random Forest accuracy: 84.70%.
- Random Forest F1-score: 84.68%.
- Random Forest false-positive rate: 15.15%.

Natural-distribution experiment:
- Random Forest accuracy: 89.93%.
- Precision: 83.13%.
- Phishing recall: 55.34%.
- F1-score: 66.45%.
- False-positive rate: 2.47%.
- False negatives: 322 out of 721 phishing test URLs.

### Updated Issues and Risks

I-01 — Model Training
Status: Partially resolved.
Three baseline classifiers were trained and compared successfully.
Remaining: Independent evaluation, model versioning, and final validation.

I-02 — Prediction Integration
Status: Open.
The Streamlit application still uses a placeholder prediction stage.
Action: Integrate a validated, saved classifier.

R-01 — Dataset Quality
Status: Partially mitigated.
Duplicates and conflicting labels were addressed during preprocessing.
Remaining: URL-format validation, dataset provenance, and leakage analysis.

R-02 — Class Imbalance
Status: Open — High priority.
Natural-distribution evaluation produced 55.34% phishing recall.
Action: Evaluate class weighting and alternative decision thresholds.

R-03 — False Positives and False Negatives
Status: Open — High priority.
The natural-distribution test produced 81 false positives and
322 false negatives.
Action: Analyze misclassified URLs and improve phishing recall.

R-04 — Environment Compatibility
Status: Monitoring.
Python 3.11.9 and scikit-learn 1.9.1 were used successfully.
Existing automated tests passed.

R-05 — Overfitting and Data Leakage
Status: Open — High priority.
Current experiments use random URL-level splitting.
Action: Evaluate domain overlap and implement domain-aware separation.

R-06 — Malformed URL Parsing
Status: Open.
Seventeen records caused parsing failures.
The current fallback prevents crashes but returns empty parsed components.
Action: Record rejected cases and improve parsing validation.

### Priority Decisions

P0: Investigate low phishing recall and domain leakage.
P0: Perform independent held-out evaluation.
P1: Document malformed-URL handling and negative-case tests.
P1: Save and version the selected trained model.
P1: Integrate actual model inference into Streamlit.
P2: Improve optional user-interface appearance.

### Review and Exit Criteria

Owner: Student developer — Salman Ahmed.
Reviewer: Dr. Shaalan (review pending).

- Dataset-quality report saved and reproducible.
- Evaluation methods and model parameters documented.
- False positives and false negatives analyzed.
- Domain-aware evaluation completed or explicitly documented as pending.
- Selected model saved and independently loadable.
- Streamlit prediction integration verified with automated tests.

Supervisor review decision: Pending.
Final model acceptance: Not yet earned.
Production readiness: Not claimed.


### Hard Stop 4 — Hostname-Separated Evaluation Update
Date: October 26, 2026

Evidence:
- Original random-split hostname overlap: 37.7% of test URLs.
- Shared hostnames in random split: 721.
- Hostname-separated training records: 15,634.
- Hostname-separated testing records: 4,366.
- Shared exact hostnames after grouping: 0.

Random Forest performance:
- Accuracy: 85.39%.
- Precision: 85.51%.
- Phishing recall: 85.59%.
- F1-score: 85.55%.
- False-positive rate: 14.82%.
- False positives: 320.
- False negatives: 318.

Decision:
Exact-hostname overlap was eliminated in this experiment.
This reduces one potential source of evaluation leakage.

Remaining limitations:
- Registered-domain overlap has not been checked.
- GroupShuffleSplit does not guarantee stratified labels.
- Natural-distribution phishing recall remains low.
- Independent final model acceptance remains pending.

Owner: Student developer.
Supervisor review: Pending.

Next exit test:
Evaluate using registered-domain grouping and representative
class proportions, with recorded confusion matrices.


