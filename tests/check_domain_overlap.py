
import pandas as pd
from sklearn.model_selection import train_test_split
from src.feature_extraction import parse_url

SEED = 42

df = pd.read_csv("data/processed/phishing_binary.csv")

# Reproduce the original balanced experiment
sample = pd.concat([
    group.sample(n=10000, random_state=SEED)
    for _, group in df.groupby("label")
]).sample(frac=1, random_state=SEED).reset_index(drop=True)

# Extract hostnames using the updated parser
def get_hostname(url):
    try:
        return (parse_url(url).hostname or "").lower().rstrip(".")
    except ValueError:
        return ""

sample["hostname"] = sample["url"].apply(get_hostname)

# Reproduce the training/test split
train, test = train_test_split(
    sample,
    test_size=0.20,
    stratify=sample["label"],
    random_state=SEED
)

train_hosts = set(train["hostname"]) - {""}
test_hosts = set(test["hostname"]) - {""}

shared_hosts = train_hosts & test_hosts

test_overlap = test["hostname"].isin(shared_hosts)

print("DOMAIN OVERLAP ANALYSIS")
print("TRAINING ROWS:", len(train))
print("TESTING ROWS:", len(test))
print("UNIQUE TRAINING HOSTNAMES:", len(train_hosts))
print("UNIQUE TEST HOSTNAMES:", len(test_hosts))
print("SHARED HOSTNAMES:", len(shared_hosts))
print("TEST ROWS WITH TRAINING HOSTNAME:", test_overlap.sum())
print("OVERLAP PERCENTAGE:", round(test_overlap.mean() * 100, 2))
print("EMPTY HOSTNAMES:", (sample["hostname"] == "").sum())
