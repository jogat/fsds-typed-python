from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool

import app.db.models  # noqa: F401

# IMPORTANT: import models so Base.metadata is populated
from alembic import context
from app.db.base import Base

assert Base.metadata.tables

# from app.db.models.bitcoin_daily_candle_model import (
#     BitcoinDailyCandleModel,
# )
# IMPORTANT: import models so Base.metadata is populated
from app.settings.db import DatabaseSettings

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def get_url() -> str:
    # Respect sqlalchemy.url passed in via alembic Config (tests/CI)
    url = config.get_main_option("sqlalchemy.url")
    if url:
        return url

    # Fallback for local runs if sqlalchemy.url is missing
    return DatabaseSettings().url


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    # ✅ If tests inject a connection, we MUST use it.
    connection = config.attributes.get("connection")

    print("ALEMBIC injected connection?", connection is not None)

    if connection is not None:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )
        with context.begin_transaction():
            context.run_migrations()
        return

    # Normal path (CLI usage)
    configuration = config.get_section(config.config_ini_section) or {}
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection2:
        context.configure(
            connection=connection2,
            target_metadata=target_metadata,
            compare_type=True,
        )
        with context.begin_transaction():
            context.run_migrations()
