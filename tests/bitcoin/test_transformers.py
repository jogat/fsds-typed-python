from datetime import date
from decimal import Decimal

from app.etl.schemas import RawBitcoinRow
from app.etl.transformers import normalize_row


def test_normalize_row() -> None:

    raw = RawBitcoinRow(
        date=date(2024, 1, 1),
        open=Decimal("42000"),
        high=Decimal("43000"),
        low=Decimal("41000"),
        close=Decimal("42500"),
        volume=Decimal("123.45"),
    )

    candle = normalize_row(raw)
    assert candle.close == Decimal("42500")
    assert candle.date == date(2024, 1, 1)
