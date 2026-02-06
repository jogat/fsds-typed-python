from __future__ import annotations

from sqlalchemy import Engine, create_engine

from app.settings.db import DatabaseSettings


def create_db_engine(settings: DatabaseSettings) -> Engine:
    """
    Create the SQLAlchemy Engine.

    Keep engine creation centralized so we don't accidentally create multiple engines
    across the app (hard to debug, messy in tests).
    """
    return create_engine(
        settings.url,
        echo=settings.echo,
        future=True,
    )
