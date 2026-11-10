
import pandas as pd
from urllib.parse import urlparse

df = pd.read_csv("data/processed/phishing_binary.csv")

failures = 0
counts = {}
examples = []

for url, label in zip(df["url"], df["label"]):
    try:
        if url.lower().startswith(("http://", "https://")):
            urlparse(url)
        else:
            urlparse("//" + url)
    except ValueError:
        failures += 1
        counts[label] = counts.get(label, 0) + 1

        if len(examples) < 5:
            examples.append(repr(url)[:120])

print("TOTAL URLS:", len(df))
print("PARSING FAILURES:", failures)
print("FAILURES BY LABEL:", counts)
print("EXAMPLES:")
for example in examples:
    print(example)
