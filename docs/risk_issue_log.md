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
