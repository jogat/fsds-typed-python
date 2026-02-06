from datetime import date
from decimal import Decimal

from app.etl.pipeline import run_pipeline, run_pipeline_tolerant
from app.etl.schemas import RawBitcoinRow


def test_run_pipeline_returns_candles() -> None:
    rows = [
        RawBitcoinRow(
            date=date(2024, 1, 1),
            open=Decimal("42000"),
            high=Decimal("43000"),
            low=Decimal("41000"),
            close=Decimal("42500"),
            volume=Decimal("123.45"),
        ),
        RawBitcoinRow(
            date=date(2024, 1, 2),
            open=Decimal("42500"),
            high=Decimal("44000"),
            low=Decimal("42000"),
            close=Decimal("43800"),
            volume=Decimal("150.00"),
        ),
    ]

    candles = run_pipeline(rows)
    assert len(candles) == 2
    assert candles[0].date == date(2024, 1, 1)
    assert candles[1].date == date(2024, 1, 2)


def test_run_pipeline_tolerant_returns_tuple() -> None:
    rows = [
        RawBitcoinRow(
            date=date(2024, 1, 1),
            open=Decimal("42000"),
            high=Decimal("43000"),
            low=Decimal("41000"),
            close=Decimal("42500"),
            volume=Decimal("123.45"),
        )
    ]

    candles, rejected = run_pipeline_tolerant(rows)

    assert len(candles) == 1
    assert rejected == []
