def test_model_accuracy():
    assert r2_score(y_true, y_pred) > 0.8