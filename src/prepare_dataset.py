
from pathlib import Path
import pandas as pd

# Load original dataset
source = Path("data/raw/malicious_phish.csv")
output = Path("data/processed/phishing_binary.csv")

df = pd.read_csv(source)

# Identify URLs with conflicting labels across all categories
conflicts = df.groupby("url")["type"].nunique()
conflicting_urls = set(conflicts[conflicts > 1].index)

# Remove conflicting URLs
df = df[~df["url"].isin(conflicting_urls)].copy()

# Retain the two categories required for this project
df = df[df["type"].isin(["benign", "phishing"])].copy()

# Remove duplicate URLs
df = df.drop_duplicates(subset=["url"])

# Convert labels to the project's format
df["label"] = df["type"].map({
    "benign": "legitimate",
    "phishing": "phishing"
})

df = df[["url", "label"]]

# Save processed dataset
output.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output, index=False)

print("DATASET PREPARATION COMPLETE")
print("TOTAL CLEANED URLS:", len(df))
print("LABEL DISTRIBUTION:")
print(df["label"].value_counts())
print("DUPLICATES REMAINING:", df["url"].duplicated().sum())
print("OUTPUT FILE:", output)
