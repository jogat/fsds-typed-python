from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True, slots=True)
class PriceSummary:
    average_close: Decimal
    min_close: Decimal
    max_close: Decimal


@dataclass(frozen=True)
class VolumeSummary:
    total_volume: Decimal
    average_volume: Decimal


@dataclass(frozen=True)
class ReturnSummary:
    mean_daily_return: float
    volatility: float
    observation_count: int
