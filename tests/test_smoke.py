from src.data_pipeline import validate_url
from src.feature_extraction import extract_placeholder_features
from src.prediction import predict_url


def test_baseline_pipeline_runs():
    url = "https://example.com/login"

    assert validate_url(url) is True

    features = extract_placeholder_features(url)
    assert isinstance(features, dict)
    assert features["url_length"] > 0

    result = predict_url(features)
    assert isinstance(result, str)
    assert result.startswith(("PHISHING -", "LEGITIMATE -"))
