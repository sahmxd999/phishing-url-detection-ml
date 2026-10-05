# Sprint Reflection — Pre-Hard Stop 3

## Completed
This sprint converted the approved system design into a concrete implementation baseline.
The project now has a structured repository, isolated application and source modules,
environment/setup documentation, a Streamlit application shell, an executable baseline
pipeline, an automated smoke test, and supporting engineering documentation.

## Blockers
The public phishing URL dataset has not yet been integrated into the runtime path, and the
three approved machine-learning models have not yet been trained. The current prediction
stage is therefore intentionally a placeholder rather than a simulated final classifier.

## Lessons Learned
Establishing a small, reproducible execution path before adding model complexity creates a
clear reference point for later development. Separating the user interface, data pipeline,
feature extraction, training, and prediction logic also reduces future integration risk.

## Risk Implications
Dataset quality, class imbalance, false positives, overfitting, and environment
reproducibility remain the main technical risks. These items are tracked in the project risk
and issue log and will be revisited as implementation progresses.

## Next Sprint Target
The next sprint will integrate the approved public dataset, validate and clean the data,
review class distribution, implement the initial lexical feature set, establish a reproducible
training/test split, and begin the Logistic Regression baseline before comparing Decision
Tree and Random Forest.
