from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import Final

# ----------------------------
# Cross-cutting primitives
# ----------------------------
UserId = int
Email = str
Percentage = float

MAX_PERCENTAGE: Final[Percentage] = 100.0


# ----------------------------
# Bitcoin domain contracts
# ----------------------------
@dataclass(frozen=True)
class BitcoinDailyCandle:
    date: date
    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal
    volume: Decimal
