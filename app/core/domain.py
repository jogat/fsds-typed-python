from dataclasses import dataclass

from app.core.types import MAX_PERCENTAGE, Percentage


@dataclass(frozen=True)
class Score:
    value: Percentage

    def __post_init__(self) -> None:
        if not (0.0 <= self.value <= MAX_PERCENTAGE):
            raise ValueError(f"must be between 0 - {MAX_PERCENTAGE}, got {self.value}")