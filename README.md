# Machine Learning-Based Phishing URL Detection System

## Project Status
**Version:** Hard Stop 3 Early Implementation Validation  
**Purpose:** Establish a reproducible and runnable implementation baseline for CISC 699.

This repository contains the initial engineering skeleton for a local phishing URL
classification prototype built with Python and Streamlit.

## Current Baseline Capabilities

- Runs as a local Streamlit application.
- Accepts a URL through a simple user interface.
- Performs minimal URL validation.
- Extracts basic lexical placeholder features.
- Executes the full baseline path from input to placeholder prediction.
- Includes an automated smoke test.
- Includes architecture, risk, issue, engineering, and AI-use documentation.

> The baseline does **not** claim to perform trained phishing classification yet.

## Planned Machine-Learning Models

- Logistic Regression
- Decision Tree
- Random Forest

## Planned Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-score
- False-positive rate
- Confusion matrix

## Repository Structure

```text
phishing-url-detection/
├── app/
│   ├── __init__.py
│   └── main.py
├── src/
│   ├── __init__.py
│   ├── data_pipeline.py
│   ├── feature_extraction.py
│   ├── model_training.py
│   └── prediction.py
├── data/
│   ├── raw/
│   └── processed/
├── models/
├── tests/
│   └── test_smoke.py
├── docs/
│   ├── architecture.md
│   ├── known_issues.md
│   └── risk_issue_log.md
├── screenshots/
├── AI_USAGE_LOG.md
├── CHANGELOG.md
├── engineering_log.md
├── README.md
├── requirements.txt
└── .gitignore
```

## Environment

Recommended:

- Python 3.11+
- Git
- Visual Studio Code or another Python IDE
- Internet connection for initial package installation

## Setup Instructions

### 1. Clone the repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd phishing-url-detection
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the baseline application

```bash
streamlit run app/main.py
```

### 5. Run the smoke test

```bash
pytest -q
```

Expected result:

```text
1 passed
```

## Minimal Baseline Execution Path

```text
URL Input
   ↓
URL Validation
   ↓
Basic Lexical Feature Extraction
   ↓
Placeholder Prediction Layer
   ↓
Streamlit Output
```

## Branch Strategy

- `main` — stable, reviewable baseline
- `develop` — integration branch for active sprint work
- `feature/*` — isolated implementation work
- `docs/*` — larger documentation changes

## Naming Conventions

- Python files and functions: `snake_case`
- Classes: `PascalCase`
- Git branches: lowercase with hyphens or slashes
- Documentation files: descriptive lowercase names where practical
- Model artifacts: versioned names such as `random_forest_v1.joblib`

## Artifact Storage Conventions

- Raw source data: `data/raw/`
- Processed data: `data/processed/`
- Trained models: `models/`
- Submission screenshots: `screenshots/`
- Technical notes and logs: `docs/` plus root engineering logs

Large datasets and generated model artifacts should not be committed unless required.

## Baseline Release

Recommended tag:

```bash
git tag -a v0.1.0-baseline -m "Pre-Hard Stop 3 implementation baseline"
git push origin v0.1.0-baseline
```

## Scope Boundary

This academic prototype excludes:

- Malware execution
- Unrestricted live web crawling
- Commercial threat-intelligence integration
- Production deployment

## Academic Integrity

AI-supported assistance is documented in `AI_USAGE_LOG.md`.



## Hard Stop 3 - Early Implementation Validation

**Date:** October 9, 2026

### Implementation Status

The project has progressed beyond the initial
implementation skeleton. The current Python
pipeline supports CSV dataset loading, URL
validation, basic lexical feature extraction,
and execution of the placeholder prediction stage.

### Validated Components

- Streamlit application starts successfully.
- CSV loader reads six synthetic sample URLs.
- URL validation filters malformed inputs.
- Feature extraction produces seven numerical features.
- Integration test passes using pytest.
- Full baseline workflow processes six sample URLs.
- All six records reach the placeholder prediction stage.

### Validation Results

- Sample dataset: data/sample_urls.csv
- Records processed: 6
- Features extracted per URL: 7
- Integration test result: 1 passed
- Full baseline workflow: Completed

These results demonstrate basic technical
functionality, not phishing detection accuracy.

### Reproduce the Validation

From the project root, activate the virtual
environment and install the dependencies:

    python -m venv venv
    .\venv\Scripts\Activate.ps1
    python -m pip install -r requirements.txt

Run the Streamlit application:

    python -m streamlit run app/main.py

Run the integration test:

    python -m pytest tests/test_pipeline_integration.py -v -s

### Current Limitations

- The sample dataset contains synthetic records.
- Model training is not implemented.
- Logistic Regression, Decision Tree, and
  Random Forest models are pending.
- The prediction module currently returns
  an operational status message.
- Classification accuracy, precision, recall,
  F1-score, and false-positive rate have
  not yet been measured.
- Dataset labels and preprocessing require
  further validation using real labeled data.

### Next Implementation Priorities

1. Acquire and profile a public labeled URL dataset.
2. Validate label encoding and dataset quality.
3. Implement the model training workflow.
4. Evaluate trained models using held-out data.
5. Connect model predictions to the Streamlit UI.
6. Expand automated tests and performance reporting.

### Validation Evidence

Evidence screenshots are stored in
the screenshots/ folder:

- HS3_Data_Loading_Success.png
- HS3_Feature_Extraction_Success.png
- HS3_Pipeline_Integration_Passed.png
- HS3_Full_Baseline_Workflow.png

These filenames refer to evidence that must be
saved in the repository before final submission.
