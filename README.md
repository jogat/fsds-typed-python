# fsds-typed-python

A **production-grade, strictly typed Python backend** designed to support a full **ETL → ML → API → Integration** workflow.

This repository is the result of a deliberate transition from a **Senior Laravel / ETL Engineer** mindset to a **Full-Stack Data Scientist / ML Engineer** hybrid role.

The goal is not notebooks or demos — the goal is **real systems**, built with:
- strong typing
- clear architecture
- CI discipline
- long-term maintainability

---

## Core Principles

- **Strict typing is non-negotiable**
  - `mypy --strict`
  - no implicit `Any`
- **Local == CI**
- **Notebooks are for exploration only**
- **Pure functions where possible**
- **Explicit over implicit**
- **Service-oriented architecture**
- **One long-lived repository**

---

## Tech Stack

| Layer | Tooling |
|-----|--------|
| Language | Python 3.11 |
| Dependency Management | Poetry |
| Typing | mypy (`--strict`) |
| Linting | Ruff |
| Formatting | Black |
| Testing | pytest |
| API | FastAPI (later phases) |
| Jobs | RQ (later phases) |
| DB | Postgres / SQLite |
| CI | GitHub Actions |
| Editor | VS Code |

---

## Repository Scope

This repository is **not** a Week-0 sandbox.

It will contain the **entire 4-month project**, evolving week by week:

- Week 0: Environment, tooling, CI
- Weeks 1–4: Typed Python, ETL, persistence
- Weeks 5–8: Stats, experiments, ML
- Weeks 9–12: Serving, integration
- Weeks 13–16: Docker, jobs, polish

---

## Project Structure

```text
fsds-typed-python/
├── app/
│   ├── api/          # FastAPI routes & schemas
│   ├── core/         # Domain logic (pure, typed)
│   ├── db/           # SQLAlchemy models & repositories
│   ├── etl/          # Ingest / clean / transform pipelines
│   ├── features/     # Feature engineering
│   ├── jobs/         # Background jobs (RQ)
│   ├── ml/           # Training, evaluation, model registry
│   └── settings/     # Configuration & environment loading
│
├── notebooks/        # Exploration only (NO production logic)
├── tests/            # Unit tests
│   ├── conftest.py   # Test configuration
│   └── test_*.py
│
├── scripts/          # Utility / CLI scripts
├── .github/
│   └── workflows/
│       └── ci.yml    # GitHub Actions CI
│
├── pyproject.toml
├── README.md
└── .venv/            # Project-local virtual environment
