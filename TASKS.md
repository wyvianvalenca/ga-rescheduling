# TASKS

Legenda: `[ ]` a fazer · `[~]` em andamento · `[x]` feito

## Sprint até a reunião de 10/11/2026
### Sábado — base
- [x] Fase 0: repo git, estrutura, docs iniciais
  - [x] git init + estrutura de pastas + .gitignore + README
  - [x] TASKS.md, ADRs 0001–0004, references.md
  - [x] pyproject.toml / venv (uv, Python 3.12)
  - [x] Repositório público `ga-rescheduling` no GitHub + primeiro push
- [ ] Parser PSPLIB `.sm` + download do j30 (+ ótimos conhecidos)
- [ ] Modelo de dados, SGS serial, validador de viabilidade
- [ ] Baseline sem AG: regra de prioridade + SGS; Gantt em PNG

### Domingo — AG da Frente A
- [ ] AG do zero (activity list, crossover de Hartmann, mutação swap, torneio, elitismo)
- [ ] Experimento em ~10 instâncias j30: gap vs. ótimo, AG vs. regra

### Segunda — reprogramação + Frente B mínima
- [ ] Perturbação + R0 (right-shift), R1 (regra+SGS), R3 (AG reativo semeado)
- [ ] Comparação R0 × R1 × R3
- [ ] Frente B mínima: mapeamento timetabling → MS-RCPSP + parser iMOPSE pequeno
- [ ] `docs/reuniao-2026-11-10.md`

## Leituras (avaliar tamanho/densidade antes: completa, focada ou adiar)
- [ ] Hartmann (1998) — AG com activity list `[fundamento]`
- [ ] Definição de custo de estabilidade (proativo/reativo) `[fundamento]`
- [ ] Kolisch & Sprecher (1997) — PSPLIB `[fundamento]`
- [ ] Myszkowski et al. — iMOPSE `[fundamento]`

## Depois da reunião
- [ ] Busca estruturada 2021–2026 (Frentes A e B) — protocolo em `docs/literature/search-protocol.md`
- [ ] R2 (AG do zero no restante), NSGA-II opcional, j60/j120
- [ ] Estatística (≥30 execuções, Wilcoxon/Friedman)
- [ ] Escolha do AG de timetabling a reaproveitar
- [ ] Escrita do artigo
