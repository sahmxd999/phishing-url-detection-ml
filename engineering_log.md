# Engineering Log

## 2026-10-05 — Pre-Hard Stop 3 Baseline

### Work Completed
- Established repository and folder structure.
- Created Streamlit application entry point.
- Added URL validation.
- Added a basic feature-extraction stub.
- Added placeholder prediction stage.
- Added automated smoke test.
- Added baseline engineering documentation.
- Created risk and issue tracking documentation.

### Engineering Decisions
- Kept the first release intentionally small and runnable.
- Avoided claiming trained-model functionality before implementation.
- Maintained separation between UI, data handling, feature extraction, model training,
  and prediction modules so later sprints can extend the system without major restructuring.

### Current Blockers
- Dataset has not yet been integrated into the runtime pipeline.
- Final URL feature set is not yet implemented.
- Machine-learning models have not yet been trained or evaluated.

### Next Sprint
- Load and validate the approved public phishing URL dataset.
- Perform initial cleaning and class-distribution checks.
- Implement the approved lexical feature set.
- Create a reproducible train/test split.
- Begin Logistic Regression baseline training.



## 2026-10-09 – Hard Stop 3 Early Implementation Validation

### Implementation Activities

- Created a separate Git branch named `hard-stop-3`.
- Extended `src/data_pipeline.py` with a CSV dataset loader.
- Added checks for required dataset columns and missing values.
- Created `data/sample_urls.csv` containing six synthetic URLs.
- Validated URL feature extraction using seven lexical features.
- Created `tests/test_pipeline_integration.py`.
- Tested the combined data loading and feature extraction workflow.
- Executed the complete baseline workflow through the placeholder prediction stage.

### Validation Results

- Streamlit application launched successfully.
- CSV loading test processed six sample records.
- Feature extraction returned seven features per URL.
- Pipeline integration test passed.
- Full baseline workflow processed six URLs.
- All six URLs reached the placeholder prediction stage.
- Full automated test suite: 2 passed in 11.70 seconds.
- Python version: 3.11.9.
- Dependency check: No broken requirements found.

### Engineering Decisions

- Retained the modular project architecture.
- Kept machine learning training separate from early pipeline validation.
- Used synthetic data only to validate execution and integration.
- Preserved the placeholder prediction stage to avoid presenting untrained output as a classification.
- Documented limitations instead of claiming unsupported model performance.

### Documentation Updates

- Updated the project README for Hard Stop 3.
- Updated `docs/risk_issue_log.md`.
- Created `docs/HS3_Technical_Validation_Memo.md`.
- Captured an environment snapshot in
  `docs/HS3_environment_snapshot.txt`.

### Current Blockers

- Real labeled phishing dataset not integrated.
- Model training and evaluation not implemented.
- Prediction output remains a placeholder.
- Negative-input and edge-case test coverage is incomplete.
- Supervisor review outcome is pending.

### Next Steps

1. Integrate and profile a public labeled URL dataset.
2. Expand automated validation tests.
3. Train initial machine learning models.
4. Evaluate classification performance.
5. Integrate trained predictions into Streamlit.
6. Obtain and document supervisor feedback.
7. Prepare the midpoint demonstration.