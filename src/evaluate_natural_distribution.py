
from pathlib import Path
import json

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)
from sklearn.model_selection import train_test_split

from src.feature_extraction import extract_placeholder_features

SEED = 42
df = pd.read_csv("data/processed/phishing_binary.csv")

# Reproduce the natural class proportions using a 20,000-URL sample.
sample = df.groupby("label", group_keys=False).sample(
    frac=20000 / len(df),
    random_state=SEED
)

# Keep unique URLs separated between training and testing.
X = pd.DataFrame(
    [extract_placeholder_features(u) for u in sample["url"]]
)
y = (sample["label"] == "phishing").astype(int)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, stratify=y, random_state=SEED
)

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=12,
    random_state=SEED,
    n_jobs=-1,
)
model.fit(X_train, y_train)
pred = model.predict(X_test)

tn, fp, fn, tp = confusion_matrix(
    y_test, pred, labels=[0, 1]
).ravel()

results = {
    "accuracy": accuracy_score(y_test, pred),
    "precision": precision_score(y_test, pred, zero_division=0),
    "recall": recall_score(y_test, pred, zero_division=0),
    "f1": f1_score(y_test, pred, zero_division=0),
    "false_positive_rate": float(fp / (fp + tn)),
    "true_negative": int(tn),
    "false_positive": int(fp),
    "false_negative": int(fn),
    "true_positive": int(tp),
    "training_rows": len(X_train),
    "testing_rows": len(X_test),
    "random_seed": SEED,
}

Path("results").mkdir(exist_ok=True)
Path("results/hs4_natural_distribution.json").write_text(
    json.dumps(results, indent=2)
)

print("CLASS DISTRIBUTION:")
print(sample["label"].value_counts())
print("\nNATURAL DISTRIBUTION EVALUATION:")
for key, value in results.items():
    print(f"{key}: {value}")
