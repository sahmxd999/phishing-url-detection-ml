from urllib.parse import urlparse


def extract_placeholder_features(url: str) -> dict:
    """Return basic lexical features to prove the pipeline is executable."""
    parsed = urlparse(url)

    return {
        "url_length": len(url),
        "hostname_length": len(parsed.netloc),
        "path_length": len(parsed.path),
        "dot_count": url.count("."),
        "hyphen_count": url.count("-"),
        "digit_count": sum(ch.isdigit() for ch in url),
        "uses_https": int(parsed.scheme == "https"),
    }
