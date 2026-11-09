# ADR 0009 — Codificação do AG: lista de atividades

- **Status:** aceita (provisória; revisar após a leitura de Hartmann (1998) e a busca 2021–2026)
- **Data:** 2026-11-09
- **Decisão:** o cromossomo é a **lista de atividades** (permutação dos jobs respeitando as precedências). O `Schedule` é o **fenótipo**: o cronograma obtido ao decodificar a lista com o SGS serial. O fitness é medido no `Schedule`.
- **Por quê:** qualquer lista viável quanto à precedência produz um cronograma viável pelo SGS, sem reparo nem penalização. Evoluir os inícios diretamente exigiria tratar cruzamentos e mutações que geram cronogramas inviáveis.
- **Consequência:** os operadores de cruzamento e mutação precisam preservar a viabilidade de precedência da lista (ou o resultado deve ser corrigido).
- **A confirmar na literatura:** Hartmann (1998) como referência da codificação por lista de atividades (ainda não lido; ver `docs/references.md`).
