from datetime import date
from decimal import Decimal

import pytest

from app.analytics.reports import (
    build_price_summary,
    build_return_summary,
    build_volume_summary,
)
from app.core.types.bitcoin import BitcoinDailyCandle


def _candle(
    d: date, close: Decimal, volume: Decimal = Decimal("1")
) -> BitcoinDailyCandle:
    return BitcoinDailyCandle(
        date=d, open=close, high=close, low=close, close=close, volume=volume
    )


def test_build_price_summary() -> None:
    candles = [
        _candle(date(2024, 1, 1), Decimal("100")),
        _candle(date(2024, 1, 2), Decimal("110")),
        _candle(date(2024, 1, 3), Decimal("121")),
    ]

    summary = build_price_summary(candles)

    assert float(summary.average_close) == pytest.approx(110.3333333333)
    assert summary.min_close == Decimal("100")
    assert summary.max_close == Decimal("121")


def test_build_volume_summary() -> None:
    candles = [
        _candle(date(2024, 1, 1), Decimal("100"), volume=Decimal("10")),
        _candle(date(2024, 1, 2), Decimal("110"), volume=Decimal("5")),
    ]

    summary = build_volume_summary(candles)

    assert summary.total_volume == Decimal("15")
    assert summary.average_volume == Decimal("7.5")


def test_build_return_summary() -> None:
    candles = [
        _candle(date(2024, 1, 1), Decimal("100")),
        _candle(date(2024, 1, 2), Decimal("110")),
        _candle(date(2024, 1, 3), Decimal("121")),
    ]

    summary = build_return_summary(candles)

    assert summary.observation_count == 2
    assert summary.mean_daily_return == pytest.approx(0.10)
    assert summary.volatility == pytest.approx(0.0)


def test_build_return_summary_one_candle() -> None:
    candles = [_candle(date(2024, 1, 1), Decimal("100"))]

    summary = build_return_summary(candles)

    assert summary.observation_count == 0
    assert summary.mean_daily_return == 0.0
    assert summary.volatility == 0.0
