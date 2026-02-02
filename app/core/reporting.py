from app.core.domain import Score


def format_score(score: Score | None) -> str:
    if score is None:
        return "N/A"
    return f"Score: {score.value}"


def is_honors_student(
    scores: list[Score],
    minimum_average: float = 90.0,
) -> bool:
    if not scores:  # No scores means not an honors student
        return False
    total = sum(score.value for score in scores)
    average = total / len(scores)
    return average >= minimum_average
