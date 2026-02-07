from __future__ import annotations

from datetime import date

from sqlalchemy import select
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
        self, candle_date: date, candle_type: CandleType
    ) -> BitcoinDailyCandle | None:
        statement = select(BitcoinDailyCandleModel).where(
            BitcoinDailyCandleModel.date == candle_date,
            BitcoinDailyCandleModel.type == candle_type.value,
        )

        result = self._session.execute(statement).scalar_one_or_none()
        return None if result is None else _model_to_domain(result)
