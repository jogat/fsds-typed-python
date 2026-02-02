from app.core.types import Email, UserId


def find_user_email(user_id: UserId) -> Email | None:
    if user_id == 0:
        return None
    return "test@example.com"