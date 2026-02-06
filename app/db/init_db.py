from __future__ import annotations

from sqlalchemy import Engine

from app.db.base import Base


def init_db(engine: Engine) -> None:
    """
    Create tables from ORM models.

    Temporary for Day 2 / tests.
    Day 3 will introduce Alembic migrations for real schema management.
    """
    Base.metadata.create_all(bind=engine)
