import pytest

from app.core.domain import Score


def test_score_valid() -> None:
    score = Score(value=85)
    assert score.value == 85


def test_score_invalid_low() -> None:
    with pytest.raises(ValueError):
        Score(value=-1.0)


def test_score_invalid_high() -> None:
    with pytest.raises(ValueError):
        Score(value=101.0)
