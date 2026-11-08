# Reprogramação de cronogramas de projetos com Algoritmos Genéticos

Trabalho acadêmico (artigo científico) sobre reprogramação (*rescheduling*) de cronogramas de projetos com AG, em Python.

## Frentes
- **A — RCPSP reativo:** AG gera o cronograma base a partir da PSPLIB; uma atividade atrasa (perturbação); estratégias de reprogramação são comparadas (right-shift, regra de prioridade, AG).
- **B — Transferência de domínio:** reaproveitar um AG de timetabling universitário (professor–disciplina–sala–horário) para alocação membro–tarefa em projetos (MS-RCPSP, benchmark iMOPSE).

## Documentação
- [`TASKS.md`](TASKS.md) — backlog e andamento
- [`docs/decisions/`](docs/decisions/) — decisões (ADRs)
- [`docs/references.md`](docs/references.md) — referências
- [`docs/literature/`](docs/literature/) — fichamentos
- [`docs/experiments.md`](docs/experiments.md) — diário de experimentos

## Ambiente
Python 3.12 gerenciado com [uv](https://docs.astral.sh/uv/) (ver ADR 0001):

```bash
uv sync          # cria .venv e instala dependências
uv run pytest    # testes
```

Instruções de execução dos experimentos serão adicionadas conforme o código surgir.
