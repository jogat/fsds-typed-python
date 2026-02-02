def add(a: int, b: int) -> int:
    """Returns the sum of two integers."""
    return a + b


def average(values: list[float]) -> float:
    """
    Return the arithmetc mean of values.

    Raises:
        ValueError: If values is empty.
    """
    if not values:
        raise ValueError("Cannot compute the average of an empty list.")
    return sum(values) / len(values)


def safe_divide(numerator: float, denominator: float) -> float:
    """
    Divides numerator by denominator safely.

    Raises:
        ZeroDivisionError: If denominator 0.0.
    """
    if denominator == 0.0:
        raise ZeroDivisionError("Denominator cannot be zero.")
    return numerator / denominator


def to_percentage(value: float, total: float) -> float:
    """
    Converts value/total to a percentage (0..100+ depending on the inputs)

    Raises:
        ValueError: If total < 0.
    """
    if total <= 0.0:
        raise ValueError("Total must be > 0")
    return (value / total) * 100.0


def clamp(value: float, min_value: float, max_value: float) -> float:
    """
    Clamps the value into inclusive the range [min_value, max_value].

    Raises:
        ValueError: If min_value > max_value.
    """
    if min_value > max_value:
        raise ValueError("min_value must be <= max_value.")
    if value < min_value:
        return min_value
    if value > max_value:
        return max_value
    return value
