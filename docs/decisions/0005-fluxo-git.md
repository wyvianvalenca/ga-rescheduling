# ADR 0005 — Fluxo de trabalho com git (equipe de 1 pessoa)

- **Status:** aceita
- **Data:** 2026-11-08
- **Decisão:**
  - Trabalho direto na `main`, com commits pequenos (um passo explicável por commit); sem pull requests nem proteção de branch.
  - Branches curtas só para variações experimentais que podem ser descartadas (ex.: `ga-v2-crossover`).
  - Tags nos marcos (ex.: `v0.1-reuniao-2026-11-10`, `v1.0-resultados-artigo`) para congelar o código que gerou cada resultado.
  - Mensagens em português com prefixo: `feat:`, `exp:`, `docs:`, `fix:`, `decisão:`.
  - Cada entrada em `docs/experiments.md` referencia o commit que a produziu. `TASKS.md` é atualizado no mesmo commit que conclui a tarefa.
- **Por quê:** PRs e revisão não agregam com uma pessoa; o histórico serve de diário técnico e de rastreabilidade para o artigo (reprodutibilidade).
