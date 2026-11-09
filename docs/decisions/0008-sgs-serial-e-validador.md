# ADR 0008 — SGS serial como decodificador e validador independente

- **Status:** aceita (provisória; revisar após a leitura dos fundamentos e da busca 2021–2026)
- **Data:** 2026-11-08
- **Decisões:**
  - O decodificador é o **SGS serial**: para cada job na ordem da lista, menor início que respeita precedência e capacidade em toda a duração. O SGS paralelo fica para depois.
  - O perfil de recursos é uma lista por instante, com horizonte igual à soma das durações (limite seguro). Python puro; otimizar só após medir.
  - O **validador é independente do SGS**: confere precedência e, por eventos (instantes de início), a capacidade dos recursos. Um erro do SGS não passa despercebido porque os dois não compartilham lógica.
  - `Schedule` guarda só os inícios; o makespan é o início do job fictício final.
  - Referência fraca: limite inferior do **caminho crítico (CPM)**, que ignora recursos.
- **Verificações cruzadas nos testes (instância `j301_1`):** CPM = 38 (igual ao "MPM-Time" do cabeçalho do arquivo); ótimo conhecido = 43 (arquivo de soluções ótimas da PSPLIB); 100 listas aleatórias viáveis geram cronogramas válidos com makespan ≥ 43.
- **A confirmar na literatura:** que o SGS serial alcança um cronograma ótimo para qualquer instância (propriedade que o SGS paralelo não garante). Vem da memória de quem escreveu; entra como `[fundamento]` quando for lido.
