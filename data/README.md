
# Dataset Documentation — Hard Stop 5

## Dataset Source

Dataset: Malicious URLs Dataset

Source:
https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset

The dataset contains URLs categorized as benign,
defacement, phishing, and malware.

This project uses only benign and phishing URLs
for binary machine learning classification.

## Dataset Setup

1. Download the dataset from the Kaggle link.
2. Extract the downloaded archive.
3. Locate malicious_phish.csv.
4. Place that CSV file in:

   data/raw/malicious_phish.csv

## Dataset Preprocessing

From the project root, run:

    python -m src.prepare_dataset

The preprocessing script:

- Removes URLs with conflicting labels.
- Retains benign and phishing categories.
- Removes duplicate URLs.
- Converts benign labels to legitimate.
- Saves the processed binary dataset.

Expected output:

    data/processed/phishing_binary.csv

## Expected Processed Dataset

The previously recorded output contains:

- Total URLs: 522,160
- Legitimate URLs: 428,074
- Phishing URLs: 94,086

These counts are reference results. Reproduction
should verify them against the downloaded dataset.

## Model Training

Run:

    python -m src.model_training

The training script samples 10,000 URLs per
class using random seed 42.

It uses an 80/20 stratified train/test split
and trains three classifiers:

- Logistic Regression
- Decision Tree
- Random Forest

## Hard Stop 5 Experiment

After preparing the dataset, run:

    python -m src.hs5_experiment

This compares the original Random Forest
model against a class-weighted experiment.

The experiment generates:

- results/hs5_experiment_comparison.csv
- results/hs5_homepage_tests.csv
- models/random_forest_hs5_weighted.joblib

The original Random Forest model is retained
as the baseline.

## Limitations

The classifier uses seven lexical URL features.

Testing identified false-positive predictions
for several legitimate website homepages.

The dataset contains a strong label imbalance
among URLs with empty paths.

The weighted model reduces overall false
positives but also reduces phishing recall.

Neither model should be treated as a definitive
website safety assessment.

## Data Availability

The full original and processed datasets are
not included in this GitHub repository.

Users must download the source dataset and
run the preprocessing script to reproduce
the training experiments.

Dataset licensing and redistribution conditions
should be verified with the original provider.
