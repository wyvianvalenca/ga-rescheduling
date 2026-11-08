# Reprogramação de cronogramas de projetos com Algoritmos Genéticos

> 🇬🇧 English version: [README.md](README.md)

Trabalho acadêmico (artigo em andamento) sobre **reprogramação reativa de cronogramas de projetos** com algoritmos genéticos (AG), em Python.

## Duas frentes
- **A — RCPSP reativo:** um AG gera o cronograma base a partir de instâncias da [PSPLIB](https://www.om-db.wi.tum.de/psplib/); uma atividade atrasa (perturbação); estratégias de reprogramação são comparadas (right-shift, regra de prioridade, AG).
- **B — Transferência de domínio:** reaproveitar um AG de timetabling universitário (professor–disciplina–sala–horário) para alocação membro–tarefa em projetos (MS-RCPSP, benchmark [iMOPSE](https://annals-csis.org/proceedings/2015/drp/273.html)).

## Estado
Fase inicial: estrutura do repositório e base. Veja [`TASKS.md`](TASKS.md).

## Ambiente
Python 3.12 com [uv](https://docs.astral.sh/uv/): `uv sync` instala as dependências e `uv run pytest` roda os testes.

## Documentação
[`TASKS.md`](TASKS.md) · [`docs/decisions/`](docs/decisions/) · [`docs/references.md`](docs/references.md) · [`docs/literature/`](docs/literature/) · [`docs/experiments.md`](docs/experiments.md)
