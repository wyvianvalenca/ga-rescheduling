# ADR 0001 — Linguagem: Python 3.12

- **Status:** aceita
- **Data:** 2026-11-08
- **Decisão:** Python 3.12 (fixado em `pyproject.toml`; ambiente via `uv`).
- **Por quê:** escolha do usuário; 3.12 é mais estável para bibliotecas científicas que a 3.14 instalada no sistema. Ecossistema (numpy, pandas, matplotlib, scipy.stats) cobre experimentos, estatística e gráficos.
- **Consequência:** desempenho inferior a Java/C++ (iMOPSE original é Java); aceitável para j30–j120. Reavaliar (numba/numpy) se a avaliação de fitness virar gargalo.
