from collections.abc import Iterable

from app.core.types import BitcoinDailyCandle
from app.etl.schemas import RawBitcoinRow
from app.etl.transformers import normalize_row


def run_pipeline(rows: Iterable[RawBitcoinRow]) -> list[BitcoinDailyCandle]:
    """
    Orchestrate the ETL transform layer:
    validated rows -> canonical domain candles

    Strict by default: if validation already happened, this should not fail
    """
    return [normalize_row(row) for row in rows]


def run_pipeline_tolerant(
    rows: Iterable[RawBitcoinRow],
) -> tuple[list[BitcoinDailyCandle], list[RawBitcoinRow]]:
    """
    Tolerant mode: returns (good_candles, rejected_rows)

    Note: this assumes rows are already parsed as RawBitcoinRow
    """

    candles: list[BitcoinDailyCandle] = []
    rejected: list[RawBitcoinRow] = []

    for row in rows:
        try:
            candles.append(normalize_row(row))
        except Exception:
            rejected.append(row)
    return candles, rejected