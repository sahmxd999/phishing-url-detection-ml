
from pathlib import Path
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)

from src.feature_extraction import extract_placeholder_features

SEED = 42
DATASET = Path("data/processed/phishing_binary.csv")
RESULTS = Path("results")
MODELS = Path("models")

RESULTS.mkdir(exist_ok=True)
MODELS.mkdir(exist_ok=True)

# Reconstruct the original balanced experiment.
df = pd.read_csv(DATASET)

sampled = pd.concat([
    group.sample(n=min(10000, len(group)), random_state=SEED)
    for _, group in df.groupby("label")
]).sample(frac=1, random_state=SEED)

X = pd.DataFrame([
    extract_placeholder_features(url)
    for url in sampled["url"]
])

y = (sampled["label"] == "phishing").astype(int)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, stratify=y, random_state=SEED
)


# Load the original tracked Random Forest baseline.
baseline = joblib.load(
    MODELS / "random_forest.joblib"
)


# Experimental model: increase the weight of legitimate URLs.
improved = RandomForestClassifier(
    n_estimators=100,
    max_depth=12,
    random_state=SEED,
    n_jobs=-1,
    class_weight={0: 3, 1: 1},
)

improved.fit(X_train, y_train)

def evaluate(name, model):
    predictions = model.predict(X_test)
    tn, fp, fn, tp = confusion_matrix(
        y_test, predictions, labels=[0, 1]
    ).ravel()

    return {
        "model": name,
        "accuracy": accuracy_score(y_test, predictions),
        "precision": precision_score(
            y_test, predictions, zero_division=0
        ),
        "recall": recall_score(
            y_test, predictions, zero_division=0
        ),
        "f1": f1_score(
            y_test, predictions, zero_division=0
        ),
        "false_positive_rate": fp / (fp + tn),
        "false_positive": int(fp),
        "false_negative": int(fn),
    }

results = pd.DataFrame([
    evaluate("Baseline Random Forest", baseline),
    evaluate("Weighted Random Forest", improved),
])

print("\nMODEL COMPARISON")
print(results.to_string(index=False))

results.to_csv(
    RESULTS / "hs5_experiment_comparison.csv",
    index=False
)

# Test both models on independently selected homepage examples.
urls = [
    "https://www.google.com",
    "https://www.microsoft.com",
    "https://www.amazon.com",
    "https://www.wikipedia.org",
    "https://www.github.com",
]

checks = []

for url in urls:
    features = pd.DataFrame(
        [extract_placeholder_features(url)]
    )[list(X.columns)]

    checks.append({
        "url": url,
        "baseline_prediction": int(baseline.predict(features)[0]),
        "weighted_prediction": int(improved.predict(features)[0]),
    })

homepage_results = pd.DataFrame(checks)

print("\nHOMEPAGE TESTS")
print(homepage_results.to_string(index=False))

homepage_results.to_csv(
    RESULTS / "hs5_homepage_tests.csv",
    index=False
)

# Save separately; do not overwrite the working Streamlit model.
joblib.dump(
    improved,
    MODELS / "random_forest_hs5_weighted.joblib"
)

# Evaluate performance specifically on empty-path URLs.
empty_path_mask = X_test["path_length"] == 0

print("\nEMPTY-PATH TEST SET ANALYSIS")

for name, model in [
    ("Baseline", baseline),
    ("Weighted", improved),
]:
    
    X_empty = X_test.loc[empty_path_mask]
    y_empty = y_test.iloc[empty_path_mask.to_numpy()]


    predictions = model.predict(X_empty)

    tn, fp, fn, tp = confusion_matrix(
        y_empty, predictions, labels=[0, 1]
    ).ravel()

    print(f"\n{name}")
    print(f"Total empty-path test URLs: {len(y_empty)}")
    print(f"Legitimate URLs: {(y_empty == 0).sum()}")
    print(f"Phishing URLs: {(y_empty == 1).sum()}")
    print(f"False positives: {fp}")
    print(f"False negatives: {fn}")
    print(f"True positives: {tp}")
    print(f"True negatives: {tn}")

print("\nExperiment completed. Results and model saved.")
