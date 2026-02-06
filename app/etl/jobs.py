from pathlib import Path

from app.core.types.bitcoin import BitcoinDailyCandle
from app.etl.loaders import load_bitcoin_csv_strict
from app.etl.pipeline import run_pipeline


def ingest_csv_to_candles(path: Path) -> list[BitcoinDailyCandle]:
    rows = load_bitcoin_csv_strict(path)
    return run_pipeline(rows)
