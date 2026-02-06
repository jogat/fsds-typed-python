from __future__ import annotations

import pytest
from alembic.config import Config
from sqlalchemy import Engine

from alembic import command
from app.db.engine import create_db_engine
from app.db.session import SessionFactory, create_session_factory
from app.settings.db import DatabaseSettings


def _run_migrations(db_url: str) -> None:
    alembic_cfg = Config("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", db_url)
    command.upgrade(alembic_cfg, "head")


@pytest.fixture()
def engine(tmp_path) -> Engine:
    db_file = tmp_path / "test.db"
    db_url = f"sqlite+pysqlite:///{db_file}"

    settings = DatabaseSettings(url=db_url, echo=False)
    eng = create_db_engine(settings)

    _run_migrations(db_url)
    return eng


@pytest.fixture()
def session_factory(engine: Engine) -> SessionFactory:
    return create_session_factory(engine)
