from sqlalchemy import Engine

from app.db.engine import create_db_engine
from app.db.session import SessionFactory, create_session_factory
from app.settings.db import DatabaseSettings


def build_engine(settings: DatabaseSettings | None = None) -> Engine:
    return create_db_engine(settings or DatabaseSettings())


def build_session_factory(settings: DatabaseSettings | None = None) -> SessionFactory:
    engine = build_engine(settings=settings)
    return create_session_factory(engine)
