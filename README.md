# Machine Learning-Based Phishing URL Detection System

## Project Status
**Version:** Pre-Hard Stop 3 Baseline  
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
