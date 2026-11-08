# ADR 0002 — AG implementado do zero (sem DEAP/pymoo)

- **Status:** aceita
- **Data:** 2026-11-07
- **Decisão:** implementar população, seleção, cruzamento, mutação e elitismo manualmente.
- **Por quê:** objetivo de aprendizado; o decodificador (SGS) e os operadores com precedência são específicos do problema de qualquer forma; controle total para registrar o número de avaliações (comparação justa com a literatura).
- **Alternativas descartadas:** DEAP (acelera o loop, mas pouco ganho aqui); pymoo (útil se a reprogramação virar multiobjetivo — reavaliar nesse caso).
