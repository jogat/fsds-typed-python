from app.core.domain import Score
from app.core.reporting import format_score, is_honors_student


def test_format_score_none() -> None:
    assert format_score(None) == "N/A"


def test_format_score_value() -> None:
    assert format_score(Score(value=85)) == "Score: 85"


def test_is_honors_student_true() -> None:
    scores = [Score(value=95), Score(value=92), Score(value=90)]
    assert is_honors_student(scores) is True


def test_is_honors_student_false() -> None:
    scores = [Score(value=50.0), Score(value=70.0), Score(value=80.0)]
    assert is_honors_student(scores) is False
