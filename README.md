
# Machine Learning-Based Phishing URL Detection System

## Project Status
**Course:** CISC 699 Applied Project  
**Milestone:** Hard Stop 5 — Artifact Hardening and Reproducibility Check  
**Student:** Salman Ahmed  
**Institution:** Harrisburg University of Science and Technology

This is a local Python and Streamlit research prototype that uses machine learning to classify URLs as potentially phishing or legitimate.

The project is experimental and is not intended to provide definitive website safety decisions.

## System Overview

The project includes:

- A public labeled URL dataset
- Dataset preparation and cleaning
- Seven lexical URL features
- Logistic Regression, Decision Tree, and Random Forest classifiers
- Model evaluation and comparison
- A saved Random Forest model
- A Streamlit interface for URL classification
- Automated tests and reproducibility documentation

## Prerequisites

- Windows computer
- Python 3.11.9
- Internet access for installing Python packages
- Sufficient disk space for the dataset and dependencies
- No GPU required for the demonstrated baseline

## Environment Versions

The following versions were verified on November 8, 2026:

| Component | Version |
|---|---|
| Python | 3.11.9 |
| Streamlit | 1.65.0 |
| Scikit-learn | 1.9.1 |
| Pandas | 3.0.6 |
| NumPy | 2.4.6 |
| Joblib | 1.6.0 |
| Pytest | 9.1.1 |

Additional dependencies are listed in `requirements.txt`.

## Installation

Open PowerShell in the project's root directory.

Create a virtual environment:

```powershell
py -3.11 -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

## Dataset

Dataset: Kaggle Malicious URLs Dataset  
Source: https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset

The original dataset contains 651,191 records across benign, defacement, phishing, and malware categories.

For this binary classification study, only benign and phishing records are retained.

The preprocessing script removes conflicting URL labels and duplicate URLs.

The resulting binary dataset contains 522,160 unique records:

- Legitimate: 428,074
- Phishing: 94,086

The expected original dataset path is:

`data/raw/malicious_phish.csv`

Dataset licensing and redistribution permissions should be checked against the original source before distributing the raw file.

## Dataset Preparation

From the project root, run:

```powershell
python -m src.prepare_dataset
```

Expected processed dataset:

`data/processed/phishing_binary.csv`

## Feature Extraction

Seven lexical features are used:

1. URL length
2. Hostname length
3. Path length
4. Dot count
5. Hyphen count
6. Digit count
7. Explicit HTTPS indicator

The current research parser supports analysis of URLs without an explicit scheme. However, the Streamlit input validator still requires `http://` or `https://`.

This inconsistency is a known limitation.

## Model Training

Run:

```powershell
python -m src.model_training
```

The script trains:

- Logistic Regression
- Decision Tree
- Random Forest

The demonstrated balanced experiment uses 20,000 URLs, including 10,000 legitimate and 10,000 phishing records.

The experiment uses random seed 42 and an 80/20 train/test split.

### Observed Results

| Model | Accuracy | Precision | Recall | F1 |
|---|---|---|---|---|
| Logistic Regression | 72.80% | 69.44% | 81.45% | 74.97% |
| Decision Tree | 82.73% | 84.39% | 80.30% | 82.30% |
| Random Forest | 84.70% | 84.80% | 84.55% | 84.68% |

These are experimental results, not claims of production performance.

The Random Forest model is saved to:

`models/random_forest.joblib`

The comparison results are saved to:

`results/hs4_model_comparison.csv`

## Running the Streamlit Application

From the project root, run:

```powershell
python -m streamlit run app/main.py
```

Open:

http://localhost:8501

Enter a URL beginning with `http://` or `https://` and select **Analyze URL**.

The application extracts lexical features, loads the saved Random Forest classifier, and displays a classification.

## Expected Outputs

Successful execution produces:

- Dataset preparation results
- Model comparison metrics
- A saved Random Forest classifier
- Automated test results
- Streamlit phishing/legitimate classifications

The application does not visit submitted URLs or execute website content.

## Automated Tests

Run:

```powershell
python -m pytest -q
```

During Hard Stop 5 verification, the existing test suite returned:

`2 passed`

This confirms the executed tests passed, but does not establish exhaustive input coverage or classifier reliability.

## Clean-Environment Reproducibility

A second Python virtual environment named `venv_clean` was created on November 8, 2026.

Dependencies were installed using:

```powershell
.\venv_clean\Scripts\python.exe -m pip install -r requirements.txt
```

The test suite was executed using:

```powershell
.\venv_clean\Scripts\python.exe -m pytest -q
```

Two tests passed in the clean environment.

The saved Random Forest model also loaded successfully and reported seven input features.

This verifies dependency installation, test execution, and model loading in a fresh environment within the existing project folder. A completely independent repository checkout remains a separate verification task.

## Known Limitations

- The model uses only seven lexical features.
- The balanced experiment does not represent real-world phishing prevalence.
- A source-like distribution experiment produced 55.34% phishing recall.
- Exact-hostname overlap was investigated, but registered-domain separation remains pending.
- The application requires explicit HTTP/HTTPS schemes, while experimental preprocessing accepts some scheme-less URLs.
- The model classified `https://example.com` as phishing during the demonstrated application test.
- Only two automated tests passed in the current suite.
- Independent final model acceptance and supervisor approval have not been established.
- No production deployment, live URL crawling, or external threat-intelligence API is included.

## Troubleshooting

**ModuleNotFoundError**

Confirm the correct virtual environment is active and install the dependencies using `requirements.txt`.

**Saved model not found**

Run:

```powershell
python -m src.model_training
```

Then confirm that `models/random_forest.joblib` exists.

**Streamlit does not open**

Run the application from the root directory and check the terminal for the local URL and any error messages.

**URL rejected**

Enter a complete URL beginning with `http://` or `https://`.

**Unexpected classification**

The model can produce false positives and false negatives. Predictions should be treated as experimental outputs, not security guarantees.

## Reproducibility and Academic Integrity

The project uses public labeled data and local Python execution.

ChatGPT assisted with project planning, code refinement, debugging, documentation, and interpretation. Development actions, terminal execution, validation, and reported observations remain the student's responsibility.

See `AI_USAGE_LOG.md` for the detailed AI assistance record.

## Security and Scope

The project does not perform live crawling, execute malicious URLs, or use commercial threat-intelligence APIs.

It is intended for academic research and controlled evaluation only.
