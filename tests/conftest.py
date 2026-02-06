from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

import pytest
from sqlalchemy import Engine

from app.db.engine import create_db_engine
from app.db.init_db import init_db
from app.db.session import SessionFactory, create_session_factory
from app.settings.db import DatabaseSettings


@pytest.fixture()
def engine(tmp_path) -> Engine:
    db_file = tmp_path / "test.db"
    settings = DatabaseSettings(url=f"sqlite+pysqlite:///{db_file}", echo=False)
    eng = create_db_engine(settings)
    init_db(eng)
    return eng


@pytest.fixture()
def session_factory(engine: Engine) -> SessionFactory:
    return create_session_factory(engine)
