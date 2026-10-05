from src.data_pipeline import validate_url
from src.feature_extraction import extract_placeholder_features
from src.prediction import placeholder_predict


def test_baseline_pipeline_runs():
    url = "https://example.com/login"

    assert validate_url(url) is True

    features = extract_placeholder_features(url)
    assert isinstance(features, dict)
    assert features["url_length"] > 0

    result = placeholder_predict(features)
    assert "Baseline system operational" in result
