
from pathlib import Path
import json
import platform
import time
import joblib
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)

from src.feature_extraction import extract_placeholder_features

RANDOM_SEED = 42
DATASET = Path("data/processed/phishing_binary.csv")
RESULTS = Path("results")


def main():
    RESULTS.mkdir(exist_ok=True)

    df = pd.read_csv(DATASET)
    assert df["url"].is_unique, "Duplicate URLs found"
    assert set(df["label"]) == {"legitimate", "phishing"}

    # Controlled initial experiment: 10,000 samples from each class.
    sampled = pd.concat([
        group.sample(
            n=min(10000, len(group)),
            random_state=RANDOM_SEED
        )
        for _, group in df.groupby("label")
    ]).sample(frac=1, random_state=RANDOM_SEED)

    print("Rows used:", len(sampled))
    print("Label distribution:")
    print(sampled["label"].value_counts())

    print("Extracting URL features...")
    X = pd.DataFrame([
        extract_placeholder_features(url)
        for url in sampled["url"]
    ])
    y = (sampled["label"] == "phishing").astype(int)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.20,
        stratify=y,
        random_state=RANDOM_SEED,
    )

    models = {
        "Logistic Regression": make_pipeline(
            StandardScaler(),
            LogisticRegression(max_iter=1000, random_state=RANDOM_SEED)
        ),
        "Decision Tree": DecisionTreeClassifier(
            max_depth=12, random_state=RANDOM_SEED
        ),
        "Random Forest": RandomForestClassifier(
            n_estimators=100,
            max_depth=12,
            random_state=RANDOM_SEED,
            n_jobs=-1,
        ),
    }

    rows = []

    for name, model in models.items():
        print(f"\nTraining {name}...")
        start = time.perf_counter()
        model.fit(X_train, y_train)
        if name == "Random Forest":
            Path("models").mkdir(exist_ok=True)
            joblib.dump(model, "models/random_forest.joblib")
            print("Random Forest model saved successfully.")
        training_seconds = time.perf_counter() - start

        predictions = model.predict(X_test)
        tn, fp, fn, tp = confusion_matrix(
            y_test, predictions, labels=[0, 1]
        ).ravel()

        result = {
            "model": name,
            "accuracy": accuracy_score(y_test, predictions),
            "precision": precision_score(y_test, predictions),
            "recall": recall_score(y_test, predictions),
            "f1": f1_score(y_test, predictions),
            "false_positive_rate": fp / (fp + tn),
            "true_negative": int(tn),
            "false_positive": int(fp),
            "false_negative": int(fn),
            "true_positive": int(tp),
            "training_seconds": round(training_seconds, 3),
        }
        rows.append(result)

        print(result)

    output = RESULTS / "hs4_model_comparison.csv"
    pd.DataFrame(rows).to_csv(output, index=False)

    metadata = {
        "python_version": platform.python_version(),
        "sklearn_version": sklearn.__version__,
        "random_seed": RANDOM_SEED,
        "sample_size": len(sampled),
        "training_rows": len(X_train),
        "testing_rows": len(X_test),
        "features": list(X.columns),
        "dataset": str(DATASET),
        "experiment": "Balanced 20,000-row exploratory comparison",
    }

    (RESULTS / "hs4_run_metadata.json").write_text(
        json.dumps(metadata, indent=2)
    )

    print("\nExperiment complete.")
    print("Saved:", output)


if __name__ == "__main__":
    main()
