from datetime import date
from decimal import Decimal

from pydantic import BaseModel, Field


class RawBitcoinRow(BaseModel):
    date: date
    open: Decimal = Field(gt=0)
    high: Decimal = Field(gt=0)
    low: Decimal = Field(gt=0)
    close: Decimal = Field(gt=0)
    volume: Decimal = Field(gt=0)
