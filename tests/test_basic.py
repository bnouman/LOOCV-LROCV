from loocv_lrocv.metrics import cindex


def test_sanity():
    assert 1 + 1 == 2


def test_cindex_runs():
    y_true = [1, 2, 3]
    y_pred = [1, 2, 3]
    value = cindex(y_true, y_pred)
    assert 0.0 <= value <= 1.0
