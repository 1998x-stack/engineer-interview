from ts_interview.validation import expanding_window_splits

def test_split_is_chronological():
    folds=list(expanding_window_splits(30,10,5,5))
    assert folds
    for tr,va in folds:
        assert tr.max() < va.min()
