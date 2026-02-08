from datetime import date
from decimal import Decimal

from app.core.types.bitcoin import BitcoinDailyCandle, CandleType
from app.db.repositories.bitcoin_daily_candle_repository import (
    BitcoinDailyCandleRepository,
)
from app.db.session import session_scope


def test_add_or_ignore_is_idempotent(session_factory) -> None:
    candle = BitcoinDailyCandle(
        date=date(2024, 1, 1),
        open=Decimal("40000"),
        high=Decimal("41000"),
        low=Decimal("39500"),
        close=Decimal("40500"),
        volume=Decimal("123.45"),
        type=None,
    )

    with session_scope(session_factory) as session:
        repo = BitcoinDailyCandleRepository(session)
        repo.add_or_ignore(candle)
        repo.add_or_ignore(candle)

    with session_scope(session_factory) as session:
        repo = BitcoinDailyCandleRepository(session)
        fetched = repo.get_by_date(date(2024, 1, 1))


    assert fetched == candle

def test_add_or_ignore_is_idempotent_with_type(session_factory) -> None:
    candle = BitcoinDailyCandle(
        date=date(2024, 1, 1),
        open=Decimal("40000"),
        high=Decimal("41000"),
        low=Decimal("39500"),
        close=Decimal("40500"),
        volume=Decimal("123.45"),
        type=CandleType.SPOT,
    )

    with session_scope(session_factory) as session:
        repo = BitcoinDailyCandleRepository(session)
        repo.add_or_ignore(candle)
        repo.add_or_ignore(candle)

    with session_scope(session_factory) as session:
        repo = BitcoinDailyCandleRepository(session)
        fetched = repo.get_by_date(date(2024, 1, 1), CandleType.SPOT)


    assert fetched == candle
