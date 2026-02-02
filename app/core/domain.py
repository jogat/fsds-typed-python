from dataclasses import dataclass

from app.core.types import MAX_PERCENTAGE, Percentage


@dataclass(frozen=True)
class Score:
    value: Percentage

    def __post_init__(self) -> None:
        if not (0.0 <= self.value <= MAX_PERCENTAGE):
            raise ValueError(f"must be between 0 - {MAX_PERCENTAGE}, got {self.value}")

    def is_passing(self, threshold: Percentage = 60.0) -> bool:
        return self.value >= threshold


@dataclass(frozen=True)
class GradeSummary:
    scores: list[Score]

    def __post_init__(self) -> None:
        if not self.scores:
            raise ValueError("GradeSummary requires at least one score")

    def average(self) -> Percentage:
        total = sum(score.value for score in self.scores)
        return total / len(self.scores)

    def passing_count(self, threshold: Percentage = 60.0) -> int:
        return sum(1 for score in self.scores if score.is_passing(threshold))
