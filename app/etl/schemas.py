from datetime import date
from decimal import Decimal

from pydantic import BaseModel, Field, field_validator

from app.core.types.bitcoin import RowType


class RawBitcoinRow(BaseModel):
    date: date
    open: Decimal = Field(gt=0)
    high: Decimal = Field(gt=0)
    low: Decimal = Field(gt=0)
    close: Decimal = Field(gt=0)
    volume: Decimal = Field(ge=0)

    type: RowType = RowType.A

    @field_validator("type", mode="before")
    @classmethod
    def normalize_type(cls, v: object) -> object:
        if v is None:
            return RowType.A
        if not isinstance(v, str):
            return v

        s = v.strip()
        if s == "":
            return RowType.A

        return s.upper()
