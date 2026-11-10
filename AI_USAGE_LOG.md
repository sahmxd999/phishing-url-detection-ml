# AI Usage Log

This log records AI-supported work used during the project in accordance with academic
integrity requirements.

| Date | Tool | Purpose | AI-Supported Output | Student Review / Action |
|---|---|---|---|---|
| 2026-10-05 | ChatGPT | Pre-Hard Stop 3 implementation planning | Suggested repository structure, starter-code organization, documentation categories, smoke-test approach, and risk-log format. | Reviewed the suggestions, retained only items consistent with the approved Hard Stop 2 design, and will test all code locally before submission. |
| 2026-10-05 | ChatGPT | Baseline starter-code assistance | Generated an initial Streamlit shell, URL validation logic, placeholder feature extraction, and smoke-test template. | Student is responsible for running, understanding, modifying as needed, and verifying the code before committing it to the course repository. |

## Academic Integrity Note

AI output is treated as assisted drafting and technical support rather than as independently
verified work. All generated material must be reviewed, tested, and understood before it is
submitted or incorporated into the project.


## Hard Stop 5 — Artifact Hardening and Reproducibility
**Date:** November 8, 2026  
**Tool:** ChatGPT

### AI Assistance
ChatGPT provided technical guidance on model serialization, integration of trained Random Forest predictions into Streamlit, resolving Python import and indentation errors, improving test assertions, and organizing reproducibility documentation.

AI assistance also included suggested terminal commands, README revisions, and recommendations for documenting model limitations and environment dependencies.

### Student Implementation and Verification
I personally performed the following activities in Visual Studio Code:

1. Modified the model-training script to save the trained Random Forest classifier using Joblib.
2. Executed the model-training pipeline and reviewed the evaluation metrics for Logistic Regression, Decision Tree, and Random Forest.
3. Verified that the trained Random Forest model was saved successfully and could be reloaded with seven input features.
4. Updated the prediction module and Streamlit application to replace the original placeholder prediction with trained-model inference, using AI-assisted code suggestions.
5. Identified and corrected code indentation issues and outdated test references.
6. Executed the automated test suite and verified that two tests passed.
7. Launched the Streamlit application locally and tested the classification interface.
8. Tested URL validation using an invalid input and confirmed that the application displayed an appropriate error.
9. Generated an updated dependency file and verified the installed Python library versions.
10. Created a separate virtual environment, installed project dependencies, and successfully executed the automated tests within it.
11. Verified that the saved Random Forest model could be loaded in the clean environment.
12. Reviewed and updated project documentation to record the implementation progress, reproducibility results, and known limitations.

### Results and Critical Review
The Random Forest achieved 84.70% accuracy in the balanced experimental evaluation.

The application successfully generated classifications using the saved model. However, testing with a legitimate demonstration URL showed a potential false-positive result.

The clean-environment test confirmed dependency installation, model loading, and two passing automated tests. Complete reproduction from an independent repository checkout remains unverified.

### Academic Integrity Declaration
ChatGPT was used as a technical support and drafting tool, not as an independent evaluator of experimental results.

I executed the commands, modified and saved the local project files, inspected the outputs, and captured the supporting evidence. I remain responsible for reviewing AI-assisted code and documentation, interpreting the results, acknowledging limitations, and ensuring the submitted work accurately represents the experiments performed.

## Hard Stop 5 — November 10, 2026

**Tool:** ChatGPT

### AI Assistance

ChatGPT assisted with:

- Diagnosing false-positive URL predictions.
- Investigating lexical feature importance.
- Analyzing empty-path URL label imbalance.
- Designing a controlled class-weight experiment.
- Debugging a Pandas index-alignment error.
- Preparing Git commands and repository updates.
- Writing dataset reproduction instructions.
- Organizing the reproducibility verification.
- Drafting documentation and evidence descriptions.

### Student Execution and Verification

I personally executed the suggested commands
in Visual Studio Code and reviewed the results.

I verified:

- Independent GitHub repository cloning.
- Python environment and dependency installation.
- Two passing automated tests.
- Saved Random Forest model loading.
- Streamlit application execution.
- Dataset preprocessing of 522,160 URLs.
- Training of three classifiers.
- Baseline and weighted-model evaluation.

### Experimental Results

Baseline Random Forest:
- Accuracy: 84.70%
- Recall: 84.55%
- False-positive rate: 15.15%

Weighted Random Forest:
- Accuracy: 80.95%
- Recall: 65.95%
- False-positive rate: 4.05%

The weighted model reduced false positives
but also reduced phishing recall.

Both models incorrectly classified five
legitimate website homepages as phishing.

### Academic Integrity

ChatGPT provided suggestions, explanations,
code assistance, and documentation drafts.

I executed and verified the experiments locally,
reviewed the outputs, and retained evidence.

AI assistance is distinguished from my actual
execution and verification of the project.
