import pytest

from app.core.domain import GradeSummary, Score


def test_score_valid() -> None:
    score = Score(value=85)
    assert score.value == 85


def test_score_invalid_low() -> None:
    with pytest.raises(ValueError):
        Score(value=-1.0)


def test_score_invalid_high() -> None:
    with pytest.raises(ValueError):
        Score(value=101.0)


def test_score_is_passing() -> None:
    assert Score(value=75).is_passing() is True
    assert Score(value=55).is_passing() is False


def test_grade_summary_average() -> None:
    summary = GradeSummary(scores=[Score(value=80), Score(value=90), Score(value=70)])

    assert summary.average() == 80.0


def test_grade_summary_passing_count() -> None:
    summary = GradeSummary(
        scores=[
            Score(value=80),
            Score(value=50),
            Score(value=70),
            Score(value=40),
        ]
    )

    assert summary.passing_count() == 2


def test_grade_summary_requires_scores() -> None:
    with pytest.raises(ValueError):
        GradeSummary(scores=[])
