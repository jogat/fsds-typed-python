import csv
from dataclasses import dataclass
from pathlib import Path

from pydantic import ValidationError

from app.etl.schemas import RawBitcoinRow


@dataclass(frozen=True)
class RowError:
    row_number: int
    raw: dict[str, str]
    errors: list[str]


class CsvIngestionError(Exception):
    def __init__(self, message: str, errors: list[RowError]):
        super().__init__(message)
        self.errors = errors


def load_bitcoin_csv_strict(path: Path) -> list[RawBitcoinRow]:
    """
    Strict mode: raises CsvIngestionError on any error (or collects and raises)
    """
    rows, errors = load_bitcoin_csv_tolerant(path)
    if errors:
        raise CsvIngestionError(
            f"Invalid rows found in CSV: {path}",
            errors,
        )
    return rows


def load_bitcoin_csv_tolerant(path: Path) -> tuple[list[RawBitcoinRow], list[RowError]]:
    """
    Tolerant mode: returns (valid_rows, row_errors).
    Never raises due to row validation.
    """
    valid: list[RawBitcoinRow] = []
    errors: list[RowError] = []

    with path.open("r", newline="", encoding="utf-8", errors="strict") as f:
        reader = csv.DictReader(f)
        # DictReader yields dict[str, str | None], but in practice values are str/None.
        for index, raw_row in enumerate(reader, start=2):
            cleaned: dict[str, str] = {k: (v or "").strip() for k, v in raw_row.items()}

            try:
                valid.append(RawBitcoinRow.model_validate(cleaned))
            except ValidationError as e:
                errors.append(
                    RowError(
                        row_number=index,
                        raw=cleaned,
                        errors=[err["msg"] for err in e.errors()],
                    )
                )

    return valid, errors
