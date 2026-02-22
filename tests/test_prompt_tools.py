import pathlib
from src.prompt_tools.token_estimator import rough_token_estimate
from src.prompt_tools.prompt_metrics import stats


def test_token_estimate_simple():
    assert rough_token_estimate("hello world") >= 2


def test_stats_keys():
    s = stats("Hallo AI Welt")
    assert set(s.keys()) == {"chars", "words", "avg_word_len", "rough_tokens"}


def test_stats_values_types():
    s = stats("eins zwei drei vier")
    assert isinstance(s["chars"], int)
    assert isinstance(s["words"], int)
    assert isinstance(s["avg_word_len"], float)
    assert isinstance(s["rough_tokens"], int)
