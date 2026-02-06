from __future__ import annotations

from collections.abc import Callable, Iterator
from contextlib import contextmanager

from sqlalchemy import Engine
from sqlalchemy.orm import Session, sessionmaker

SessionFactory = Callable[[], Session]


def create_session_factory(engine: Engine) -> SessionFactory:
    """
    Create the SQLAlchemy SessionFactory.

    Keep session factory creation centralized so we don't accidentally create multiple
    factories across the app (hard to debug, messy in tests).
    """
    maker = sessionmaker(bind=engine, autoflush=False, future=True, autocommit=False)
    return maker


@contextmanager
def session_scope(session_factory: SessionFactory) -> Iterator[Session]:
    session = session_factory()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
