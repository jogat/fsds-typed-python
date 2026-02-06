from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DatabaseSettings:
    # SQLite file for local-first development
    url: str = "sqlite+pysqlite:///./app.db"
    echo: bool = False
