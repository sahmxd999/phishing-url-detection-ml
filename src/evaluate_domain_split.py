
from pathlib import Path
import json

import pandas as pd
from sklearn.model_selection import GroupShuffleSplit
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)

from src.feature_extraction import (
    extract_placeholder_features,
    parse_url,
)

SEED = 42

df = pd.read_csv("data/processed/phishing_binary.csv")

# Reproduce the balanced 20,000-URL experiment.
sample = pd.concat([
    group.sample(n=10000, random_state=SEED)
    for _, group in df.groupby("label")
]).sample(frac=1, random_state=SEED).reset_index(drop=True)


def hostname(url):
    try:
        return (parse_url(url).hostname or "").lower().rstrip(".")
    except ValueError:
        return ""


sample["hostname"] = sample["url"].apply(hostname)

# Use unique groups for empty hostnames so malformed
# records do not all become one artificial website.
groups = [
    host if host else f"unknown-host-{i}"
    for i, host in enumerate(sample["hostname"])
]

splitter = GroupShuffleSplit(
    n_splits=1,
    test_size=0.20,
    random_state=SEED,
)

train_idx, test_idx = next(
    splitter.split(sample, sample["label"], groups)
)

train = sample.iloc[train_idx]
test = sample.iloc[test_idx]

train_hosts = set(train["hostname"]) - {""}
test_hosts = set(test["hostname"]) - {""}

assert not (train_hosts & test_hosts), "Hostname overlap detected"

X_train = pd.DataFrame([
    extract_placeholder_features(u) for u in train["url"]
])
X_test = pd.DataFrame([
    extract_placeholder_features(u) for u in test["url"]
])

y_train = (train["label"] == "phishing").astype(int)
y_test = (test["label"] == "phishing").astype(int)

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
    "training_rows": len(train),
    "testing_rows": len(test),
    "training_phishing": int(y_train.sum()),
    "testing_phishing": int(y_test.sum()),
    "shared_hostnames": len(train_hosts & test_hosts),
    "random_seed": SEED,
    "split_method": "GroupShuffleSplit by parsed hostname",
}

Path("results").mkdir(exist_ok=True)
Path("results/hs4_domain_split.json").write_text(
    json.dumps(results, indent=2)
)

print("HOSTNAME-SEPARATED EVALUATION")
for key, value in results.items():
    print(f"{key}: {value}")
