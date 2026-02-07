from datetime import date
from decimal import Decimal

from pydantic import BaseModel, Field, field_validator

from app.core.types.bitcoin import CandleType


class RawBitcoinRow(BaseModel):
    date: date
    open: Decimal = Field(gt=0)
    high: Decimal = Field(gt=0)
    low: Decimal = Field(gt=0)
    close: Decimal = Field(gt=0)
    volume: Decimal = Field(ge=0)

    type: CandleType | None = None

    @field_validator("type", mode="before")
    @classmethod
    def normalize_type(cls, v: object) -> object:
        if v is None:
            return None

        if isinstance(v, str):
            s = v.strip().lower()
            if s == "":
                return None
            return s

        return v
