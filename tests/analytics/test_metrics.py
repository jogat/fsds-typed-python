from datetime import date
from decimal import Decimal

import pytest

from app.analytics.metrics import (
    average_close,
    daily_returns,
    max_close,
    min_close,
    total_volume,
    volatility,
)
from app.core.types.bitcoin import BitcoinDailyCandle


def _candle(
    d: date,
    close: Decimal,
    volume: Decimal = Decimal("1"),
) -> BitcoinDailyCandle:
    return BitcoinDailyCandle(
        date=d,
        open=close,
        high=close,
        low=close,
        close=close,
        volume=volume,
        type=None,
    )


def test_average_max_min_close() -> None:
    candles = [
        _candle(date(2024, 1, 1), Decimal("100")),
        _candle(date(2024, 1, 2), Decimal("200")),
        _candle(date(2024, 1, 3), Decimal("300")),
    ]

    assert average_close(candles) == Decimal("200")
    assert min_close(candles) == Decimal("100")
    assert max_close(candles) == Decimal("300")


def test_total_volume() -> None:
    candles = [
        _candle(date(2024, 1, 1), Decimal("100"), volume=Decimal("10")),
        _candle(date(2024, 1, 2), Decimal("200"), volume=Decimal("20")),
    ]

    assert total_volume(candles) == Decimal("30")


def test_daily_returns_sorted_and_computed() -> None:
    candles = [
        _candle(date(2024, 1, 2), Decimal("100")),
        _candle(date(2024, 1, 3), Decimal("110")),
        _candle(date(2024, 1, 1), Decimal("121")),
    ]

    returns = daily_returns(candles)

    # After sorting by date: 121 -> 100 -> 110
    expected = [
        float((Decimal("100") - Decimal("121")) / Decimal("121")),
        float((Decimal("110") - Decimal("100")) / Decimal("100")),
    ]

    assert returns == pytest.approx(expected)


def test_daily_returns_sorted_and_computed_from_input() -> None:
    candles = [
        _candle(date(2024, 1, 2), Decimal("100")),
        _candle(date(2024, 1, 3), Decimal("110")),
        _candle(date(2024, 1, 1), Decimal("121")),
    ]

    ordered = sorted(candles, key=lambda c: c.date)

    expected = [
        float((ordered[1].close - ordered[0].close) / ordered[0].close),
        float((ordered[2].close - ordered[1].close) / ordered[1].close),
    ]

    assert daily_returns(candles) == pytest.approx(expected)


def test_volatility_single_day_is_zero() -> None:
    candles = [_candle(date(2024, 1, 1), 100)]
    assert volatility(candles) == 0.0


def test_empty_input_raises() -> None:
    with pytest.raises(ValueError):
        average_close([])
