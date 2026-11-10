
from urllib.parse import urlparse



def parse_url(url: str):
    """Safely parse URL components without assuming HTTPS."""
    url = url.strip()

    try:
        if url.lower().startswith(("http://", "https://")):
            return urlparse(url)

        return urlparse("//" + url)

    except ValueError:
        # Return an empty parsed result for malformed URLs.
        # Keep the existing lexical features measurable.
        return urlparse("")



def extract_placeholder_features(url: str) -> dict:
    """Extract seven lexical URL features."""
    parsed = parse_url(url)

    return {
        "url_length": len(url),
        "hostname_length": len(parsed.netloc),
        "path_length": len(parsed.path),
        "dot_count": url.count("."),
        "hyphen_count": url.count("-"),
        "digit_count": sum(ch.isdigit() for ch in url),
        "uses_https": int(parsed.scheme.lower() == "https"),
    }
