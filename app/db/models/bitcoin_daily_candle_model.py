from __future__ import annotations

from datetime import date
from decimal import Decimal

from sqlalchemy import Date, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class BitcoinDailyCandleModel(Base):
    __tablename__ = "bitcoin_daily_candles"

    date: Mapped[date] = mapped_column(Date, primary_key=True)

    open: Mapped[Decimal] = mapped_column(Numeric(20, 8), nullable=False)

    high: Mapped[Decimal] = mapped_column(Numeric(20, 8), nullable=False)

    low: Mapped[Decimal] = mapped_column(Numeric(20, 8), nullable=False)

    close: Mapped[Decimal] = mapped_column(Numeric(20, 8), nullable=False)

    volume: Mapped[Decimal] = mapped_column(Numeric(28, 8), nullable=False)