from datetime import date
from decimal import Decimal
from pathlib import Path

import pytest

from app.core.types.bitcoin import CandleType
from app.etl.loaders import (
    CsvIngestionError,
    load_bitcoin_csv_strict,
    load_bitcoin_csv_tolerant,
)
from app.etl.transformers import normalize_row


def test_load_bitcoin_csv_strict_success(tmp_path: Path) -> None:
    csv_path = tmp_path / "btc.csv"
    csv_path.write_text(
        "date,open,high,low,close,volume\n"
        "2024-01-01,42000,43000,41000,42500,123.45\n",
        encoding="utf-8",
    )

    rows = load_bitcoin_csv_strict(csv_path)
    assert len(rows) == 1
    assert str(rows[0].date) == "2024-01-01"


def test_load_bitcoin_csv_strict_success_and_type(tmp_path: Path) -> None:
    csv_path = tmp_path / "btc.csv"
    csv_path.write_text(
        "date,open,high,low,close,volume,type\n"
        "2024-01-01,42000,43000,41000,42500,123.45,spot\n",
        encoding="utf-8",
    )

    rows = load_bitcoin_csv_strict(csv_path)
    assert len(rows) == 1
    assert str(rows[0].date) == "2024-01-01"
    assert rows[0].type == CandleType.SPOT


def test_load_bitcoin_csv_tolerant_collects_errors(tmp_path: Path) -> None:
    csv_path = tmp_path / "btc.csv"
    csv_path.write_text(
        "date,open,high,low,close,volume\n"
        "2024-01-01,42000,43000,41000,42500,123.45\n"
        "2024-01-02,-1,44000,42000,43800,150\n",
        encoding="utf-8",
    )

    rows, errors = load_bitcoin_csv_tolerant(csv_path)
    assert len(rows) == 1
    assert len(errors) == 1
    assert errors[0].row_number == 3  # header=1, first data=2, second data=3


def test_load_bitcoin_csv_strict_raises_on_errors(tmp_path: Path) -> None:
    csv_path = tmp_path / "btc.csv"
    csv_path.write_text(
        "date,open,high,low,close,volume\n" "2024-01-01,-1,43000,41000,42500,123.45\n",
        encoding="utf-8",
    )

    with pytest.raises(CsvIngestionError) as exc:
        load_bitcoin_csv_strict(csv_path)

    assert exc.value.errors[0].row_number == 2


def test_load_bitcoin_csv_and_convert_to_candle(tmp_path: Path) -> None:
    csv_path = tmp_path / "btc.csv"
    csv_path.write_text(
        "date,open,high,low,close,volume\n"
        "2024-01-01,42000,43000,41000,42500,123.45\n",
        encoding="utf-8",
    )

    rows = load_bitcoin_csv_strict(csv_path)
    assert len(rows) == 1

    row = rows[0]
    candle = normalize_row(row)

    assert candle.date == date(2024, 1, 1)
    assert candle.close == Decimal("42500")
    assert candle.open == Decimal("42000")
