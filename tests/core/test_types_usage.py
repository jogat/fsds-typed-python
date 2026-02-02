from app.core.email_lookup import find_user_email


def test_find_user_email_none() -> None:
    assert find_user_email(0) is None

def test_find_user_email_value() -> None:
    assert find_user_email(1) == "test@example.com"

def test_email_uppercase_when_present() -> None:
    email = find_user_email(1)
    assert email is not None
    assert email.upper() == "TEST@EXAMPLE.COM"