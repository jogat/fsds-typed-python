from app.core.types import BitcoinDailyCandle
from app.etl.schemas import RawBitcoinRow


def normalize_row(row: RawBitcoinRow) -> BitcoinDailyCandle:
    """
    Convert a validated raw Bitcoin row into a cannonical domain candle.
    No validation. No IO. No side effects
    """

    return BitcoinDailyCandle(
        date=row.date,
        open=row.open,
        high=row.high,
        low=row.low,
        close=row.close,
        volume=row.volume,
    )
