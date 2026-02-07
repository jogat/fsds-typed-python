from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from enum import Enum


class CandleType(str, Enum):
    SPOT = "spot"
    FEATURES = "features"


@dataclass(frozen=True)
class BitcoinDailyCandle:
    date: date
    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal
    volume: Decimal
    type: CandleType | None
