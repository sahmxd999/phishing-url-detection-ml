# Engineering Log

## September 1, 2026 – Project Workspace Initialization

### Work Completed
- Created the GitHub repository for the CISC 699 applied project.
- Established the initial project folder structure.
- Confirmed the PhiUSIIL Phishing URL dataset as the proposed dataset.
- Confirmed Logistic Regression, Decision Tree, and Random Forest as the initial classifiers.
- Defined accuracy, precision, recall, F1-score, false-positive rate, and confusion matrices as evaluation metrics.
- Reviewed supervisor feedback concerning feature availability for user-entered URLs.

### Technical Decision
The application will avoid live website crawling. The project will identify features that can be derived directly from a raw URL and train the deployable model using the same available feature set. This will maintain consistency between model training and the Streamlit prediction workflow.

### Current Risks / Questions
- Determine which PhiUSIIL features can be calculated directly from a raw URL.
- Check for possible data leakage before model training.
- Evaluate whether the selected feature subset provides sufficient phishing recall and an acceptable false-positive rate.

### Next Steps
1. Download and inspect the PhiUSIIL dataset.
2. Identify raw-URL-compatible features.
3. Perform exploratory data analysis.
4. Create the initial preprocessing pipeline.
5. Begin baseline model training.
