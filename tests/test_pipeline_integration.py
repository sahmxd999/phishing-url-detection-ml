from src.data_pipeline import load_dataset
from src.feature_extraction import extract_placeholder_features


def test_pipeline_integration():
    df = load_dataset("data/sample_urls.csv")

    assert len(df) == 6, "Expected six sample records"

    feature_rows = [
        extract_placeholder_features(url)
        for url in df["url"]
    ]

    assert len(feature_rows) == 6
    assert all(len(features) == 7 for features in feature_rows)

    print("\nCombined pipeline test PASSED")
    print("URLs processed:", len(feature_rows))
    print("Features per URL:", len(feature_rows[0]))
    print("Sample features:", feature_rows[0])