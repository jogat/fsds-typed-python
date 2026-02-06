from __future__ import annotations

from sqlalchemy import text

from app.db.session import session_scope


def test_db_smoke(session_factory) -> None:
    with session_scope(session_factory) as session:
        result = session.execute(text("SELECT 1")).scalar_one()
        assert result == 1
