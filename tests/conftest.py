from __future__ import annotations

from pathlib import Path

import pytest
from alembic.config import Config
from sqlalchemy import Engine

import app.db.models  # noqa: F401
from alembic import command
from app.db.base import Base
from app.db.engine import create_db_engine

# from app.db.models.bitcoin_daily_candle_model import (
#     BitcoinDailyCandleModel,
# )
from app.db.session import SessionFactory, create_session_factory
from app.settings.db import DatabaseSettings


def _run_migrations(engine: Engine) -> None:
    ini_path = Path(__file__).resolve().parents[1] / "alembic.ini"  # repo root
    alembic_cfg = Config(str(ini_path))
    alembic_cfg.set_main_option("script_location", "alembic")

    with engine.begin() as connection:
        alembic_cfg.attributes["connection"] = connection
        command.upgrade(alembic_cfg, "head")


@pytest.fixture()
def engine(tmp_path: Path) -> Engine:
    db_file = tmp_path / "test.db"
    db_url = f"sqlite+pysqlite:///{db_file}"

    eng = create_db_engine(DatabaseSettings(url=db_url, echo=False))

    Base.metadata.create_all(eng)

    return eng


@pytest.fixture()
def session_factory(engine: Engine) -> SessionFactory:
    return create_session_factory(engine)
