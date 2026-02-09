from collections.abc import Sequence
from decimal import Decimal
from itertools import pairwise
from statistics import mean, stdev

from app.core.types.bitcoin import BitcoinDailyCandle


def _require_non_empty(candles: Sequence[BitcoinDailyCandle]) -> None:
    if not candles:
        raise ValueError("At least one candle is required")


def average_close(candles: Sequence[BitcoinDailyCandle]) -> Decimal:
    _require_non_empty(candles)
    return mean(c.close for c in candles)


def min_close(candles: Sequence[BitcoinDailyCandle]) -> Decimal:
    _require_non_empty(candles)
    return min(c.close for c in candles)


def max_close(candles: Sequence[BitcoinDailyCandle]) -> Decimal:
    _require_non_empty(candles)
    return max(c.close for c in candles)


def total_volume(candles: Sequence[BitcoinDailyCandle]) -> Decimal:
    _require_non_empty(candles)
    return sum((c.volume for c in candles), start=Decimal("0"))


def daily_returns(candles: Sequence[BitcoinDailyCandle]) -> list[float]:
    _require_non_empty(candles)

    if len(candles) < 2:
        return []

    ordered = sorted(candles, key=lambda c: c.date)
    returns: list[float] = []

    for prev, curr in pairwise(ordered):
        ratio: Decimal = (curr.close - prev.close) / prev.close
        returns.append(float(ratio))

    return returns


def volatility(candles: Sequence[BitcoinDailyCandle]) -> float:
    returns = daily_returns(candles)
    if len(returns) < 2:
        return 0.0

    return stdev(returns)
