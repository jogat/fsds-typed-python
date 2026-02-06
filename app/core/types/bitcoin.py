from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from enum import Enum


class RowType(str, Enum):
    A = "A"
    B = "B"
    C = "C"


@dataclass(frozen=True)
class BitcoinDailyCandle:
    date: date
    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal
    volume: Decimal
    type: RowType | None
