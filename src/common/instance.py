"""Modelo de dados de uma instância RCPSP (single-mode, recursos renováveis).

Convenção: índices internos começam em 0. O job 0 é o início fictício e o
job ``n_jobs - 1`` é o fim fictício (duração 0, demanda 0).
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Instance:
    """Um problema RCPSP: atividades, precedências, demandas e capacidades.

    Attributes:
        name: Identificador da instância (ex.: ``"j301_1"``).
        durations: ``durations[j]`` é a duração do job ``j``.
        demands: ``demands[j][r]`` é o consumo do recurso ``r`` pelo job ``j``.
        capacities: ``capacities[r]`` é a capacidade (constante) do recurso ``r``.
        successors: ``successors[j]`` são os jobs que só podem começar após ``j``.
        predecessors: ``predecessors[j]`` são os jobs que precisam terminar antes de ``j``.
    """

    name: str
    durations: tuple[int, ...]
    demands: tuple[tuple[int, ...], ...]
    capacities: tuple[int, ...]
    successors: tuple[tuple[int, ...], ...]
    predecessors: tuple[tuple[int, ...], ...]

    @property
    def n_jobs(self) -> int:
        """Número de jobs, incluindo os dois fictícios."""
        return len(self.durations)

    @property
    def n_resources(self) -> int:
        """Número de recursos renováveis."""
        return len(self.capacities)

    @property
    def source(self) -> int:
        """Índice do job fictício de início."""
        return 0

    @property
    def sink(self) -> int:
        """Índice do job fictício de fim."""
        return self.n_jobs - 1
