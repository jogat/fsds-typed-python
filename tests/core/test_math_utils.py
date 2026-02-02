import pytest

from app.core.math_utils import add, average, clamp, safe_divide, to_percentage


def test_add() -> None:
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_average() -> None:
    assert average([1.0, 2.0, 3.0]) == 2.0


def test_average_empty_raises() -> None:
    with pytest.raises(ValueError):
        average([])


def test_safe_divide() -> None:
    assert safe_divide(10.0, 2.0) == 5.0


def test_safe_divide_by_zero_raises() -> None:
    with pytest.raises(ZeroDivisionError):
        safe_divide(10.0, 0.0)


def test_to_percentage() -> None:
    assert to_percentage(50.0, 200.0) == 25.0


def test_to_percentage_negative_total_raises() -> None:
    with pytest.raises(ValueError):
        to_percentage(50.0, -100.0)


def test_clamp_in_range() -> None:
    assert clamp(5.0, 1.0, 10.0) == 5.0


def test_clamp_low() -> None:
    assert clamp(-1.0, 0.0, 10.0) == 0.0


def test_clamp_high() -> None:
    assert clamp(15.0, 0.0, 10.0) == 10.0


def test_clamp_invalid_range_raises() -> None:
    with pytest.raises(ValueError):
        clamp(5.0, 10.0, 1.0)
