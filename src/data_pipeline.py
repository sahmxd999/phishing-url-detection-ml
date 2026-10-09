from urllib.parse import urlparse


def validate_url(url: str) -> bool:
    """Perform minimal validation for the implementation baseline."""
    if not isinstance(url, str) or not url.strip():
        return False

    parsed = urlparse(url.strip())
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def load_dataset(file_path: str):
    """Load a labeled phishing URL dataset from a CSV file."""
    import pandas as pd

    df = pd.read_csv(file_path)

    required_columns = {"url", "label"}
    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Dataset is missing required columns: {sorted(missing_columns)}"
        )

    df = df.dropna(subset=["url", "label"]).copy()
    df["url"] = df["url"].astype(str).str.strip()
    df = df[df["url"].apply(validate_url)]

    if df.empty:
        raise ValueError("No valid labeled URLs found in dataset.")

    return df

