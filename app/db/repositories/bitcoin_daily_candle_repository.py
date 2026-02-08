from __future__ import annotations

from datetime import date

from sqlalchemy import select
from sqlalchemy.dialects.sqlite import insert as sqlite_insert
from sqlalchemy.orm import Session

from app.core.types.bitcoin import BitcoinDailyCandle, CandleType
from app.db.models.bitcoin_daily_candle_model import BitcoinDailyCandleModel


def _model_to_domain(model: BitcoinDailyCandleModel) -> BitcoinDailyCandle:
    return BitcoinDailyCandle(
        date=model.date,
        open=model.open,
        high=model.high,
        low=model.low,
        close=model.close,
        volume=model.volume,
        type=CandleType(model.type) if model.type is not None else None,
    )


def _domain_to_model(domain: BitcoinDailyCandle) -> BitcoinDailyCandleModel:
    return BitcoinDailyCandleModel(
        date=domain.date,
        open=domain.open,
        high=domain.high,
        low=domain.low,
        close=domain.close,
        volume=domain.volume,
        type=domain.type.value if domain.type is not None else None,
    )


class BitcoinDailyCandleRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def add(self, candle: BitcoinDailyCandle) -> None:
        self._session.add(_domain_to_model(candle))

    def get_by_date(
        self,
        candle_date: date,
        candle_type: CandleType | None = None,
    ) -> BitcoinDailyCandle | None:
        stmt = select(BitcoinDailyCandleModel).where(
            BitcoinDailyCandleModel.date == candle_date,
        )

        if candle_type is None:
            stmt = stmt.where(BitcoinDailyCandleModel.type.is_(None))
        else:
            stmt = stmt.where(BitcoinDailyCandleModel.type == candle_type.value)

        result = self._session.execute(stmt).scalar_one_or_none()
        return None if result is None else _model_to_domain(result)

    def list_range(
        self,
        start_date: date,
        end_date: date,
    ) -> list[BitcoinDailyCandle]:
        stmt = (
            select(BitcoinDailyCandleModel)
            .where(BitcoinDailyCandleModel.date >= start_date)
            .where(BitcoinDailyCandleModel.date <= end_date)
            .order_by(BitcoinDailyCandleModel.date)
        )

        results = self._session.execute(stmt).scalars().all()
        return [_model_to_domain(row) for row in results]

    def add_or_ignore(self, candle: BitcoinDailyCandle) -> None:
        stmt = (
            sqlite_insert(BitcoinDailyCandleModel)
            .values(
                date=candle.date,
                open=candle.open,
                high=candle.high,
                low=candle.low,
                close=candle.close,
                volume=candle.volume,
                type=candle.type.value if candle.type else None,
            )
            .on_conflict_do_nothing(index_elements=["date"])
        )

        self._session.execute(stmt)
