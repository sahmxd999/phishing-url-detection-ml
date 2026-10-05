def placeholder_predict(features: dict) -> str:
    """Temporary baseline output. This is not a trained phishing classifier."""
    if not isinstance(features, dict) or not features:
        return "Baseline pipeline could not process the input."

    return (
        "Baseline system operational — URL accepted, basic features extracted, "
        "and the prediction stage was reached. Trained ML prediction will be "
        "integrated in the next sprint."
    )
