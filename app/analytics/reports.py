from __future__ import annotations

from collections.abc import Sequence
from decimal import Decimal
from statistics import mean

from app.analytics.metrics import (
    average_close,
    daily_returns,
    max_close,
    min_close,
    total_volume,
    volatility,
)
from app.analytics.schemas import (
    BitcoinAnalyticsReport,
    PriceSummary,
    ReturnSummary,
    VolumeSummary,
)
from app.core.types.bitcoin import BitcoinDailyCandle


def build_price_summary(candles: Sequence[BitcoinDailyCandle]) -> PriceSummary:
    return PriceSummary(
        average_close=average_close(candles),
        min_close=min_close(candles),
        max_close=max_close(candles),
    )


def build_volume_summary(candles: Sequence[BitcoinDailyCandle]) -> VolumeSummary:
    total = total_volume(candles)
    avg = total / Decimal(len(candles))

    return VolumeSummary(total_volume=total, average_volume=avg)


def build_return_summary(candles: Sequence[BitcoinDailyCandle]) -> ReturnSummary:
    returns = daily_returns(candles)

    if not returns:
        return ReturnSummary(mean_daily_return=0.0, volatility=0.0, observation_count=0)

    mean_returns = mean(returns)
    vol = volatility(candles)

    return ReturnSummary(
        mean_daily_return=mean_returns,
        volatility=vol,
        observation_count=len(returns),
    )


def build_bitcoin_analytics_report(
    candles: Sequence[BitcoinDailyCandle],
) -> BitcoinAnalyticsReport:
    if not candles:
        raise ValueError("At least one candle is required")

    ordered = sorted(candles, key=lambda c: c.date)

    return BitcoinAnalyticsReport(
        start_date=ordered[0].date,
        end_date=ordered[-1].date,
        price=build_price_summary(ordered),
        volume=build_volume_summary(ordered),
        returns=build_return_summary(ordered),
    )
