# ADR 0007 — Estrutura de dados e tipagem

- **Status:** aceita (provisória quanto a tuplas × numpy; reavaliar se o desempenho pedir)
- **Data:** 2026-11-08
- **Decisões:**
  - **Dados** em `dataclass(frozen=True)` (biblioteca padrão): `Instance` (problema) e, na próxima etapa, `Schedule` (solução). **Algoritmos** (SGS, validador, operadores do AG) como funções puras; classes só onde há estado/configuração (ex.: o AG com seus parâmetros e gerador aleatório).
  - **Tuplas** (imutáveis) em vez de arrays numpy nos dados da instância: mais legíveis e seguras para instâncias de 30–120 jobs.
  - **Índices internos começam em 0**; o parser converte os números de job do arquivo (1..n). Job 0 = início fictício, job n-1 = fim fictício.
  - **Tipagem estática** com type hints em todo o código, verificada com `mypy --strict`.
  - **Sem pydantic**: o parser já valida o que lê, e `dataclass` evita uma dependência a mais.
  - **Documentação:** docstrings (estilo Google); site gerado (mkdocs/sphinx) fica para depois dos resultados.
- **Por quê:** objetos imutáveis para dados evitam alterações acidentais; funções puras são fáceis de testar e de trocar na comparação com/sem AG; a Frente B reaproveita o que não depende do problema.
- **Instância de teste:** `tests/fixtures/j301_1.sm` (primeira instância do conjunto j30 da PSPLIB). Os experimentos usarão os conjuntos completos, não esta instância.
