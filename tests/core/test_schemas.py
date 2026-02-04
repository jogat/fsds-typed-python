from datetime import date
from decimal import Decimal

import pytest
from pydantic import ValidationError

from app.etl.schemas import RawBitcoinRow


def test_valid_bitcoin_row() -> None:
    close = "42000"

    row = RawBitcoinRow(
        date=date(2025, 1, 1),
        open=Decimal("42000"),
        high=Decimal("43000"),
        low=Decimal("41000"),
        close=Decimal(close),
        volume=Decimal("123.45"),
    )

    assert row.close == Decimal(close)


def test_invalid_price_rejected() -> None:
    with pytest.raises(ValidationError):
        RawBitcoinRow(
            date=date(2025, 1, 1),
            open=Decimal("-1"),
            high=Decimal("43000"),
            low=Decimal("41000"),
            close=Decimal("42000"),
            volume=Decimal("123.45"),
        )
