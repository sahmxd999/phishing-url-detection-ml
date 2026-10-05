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
