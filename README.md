# Rescheduling Project Schedules with Genetic Algorithms

> 🇧🇷 Resumo em português: [README.pt-BR.md](README.pt-BR.md)

Academic research project (paper in progress): reactive **rescheduling of project schedules** using genetic algorithms (GA), written in Python.

## Two research fronts
- **A — Reactive RCPSP:** a GA builds a baseline schedule for [PSPLIB](https://www.om-db.wi.tum.de/psplib/) instances (Resource-Constrained Project Scheduling Problem); an activity is delayed (disruption); rescheduling strategies are compared (right-shift, priority rule, GA).
- **B — Domain transfer:** reuse a university course timetabling GA (teacher–course–room–slot) for team member–task assignment in projects (multi-skill RCPSP, [iMOPSE](https://annals-csis.org/proceedings/2015/drp/273.html) benchmark).

## Status
Early stage: repository setup and groundwork. See [`TASKS.md`](TASKS.md).

## Setup
Python 3.12 managed with [uv](https://docs.astral.sh/uv/):

```bash
uv sync          # creates .venv and installs dependencies
uv run pytest    # tests
```

## Documentation (in Portuguese)
- [`TASKS.md`](TASKS.md) — backlog and progress
- [`docs/decisions/`](docs/decisions/) — decision records (ADRs)
- [`docs/references.md`](docs/references.md) — references
- [`docs/literature/`](docs/literature/) — reading notes
- [`docs/experiments.md`](docs/experiments.md) — experiment log
