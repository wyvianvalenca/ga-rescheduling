"""Representação de um cronograma (solução de uma instância RCPSP)."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Schedule:
    """Instante de início de cada job.

    Attributes:
        start_times: ``start_times[j]`` é o início do job ``j`` (índices de 0 a n-1).
    """

    start_times: tuple[int, ...]

    @property
    def makespan(self) -> int:
        """Duração total do projeto: início do job fictício final (último índice, duração 0)."""
        return self.start_times[-1]
