"""Operações sobre o grafo de precedência de uma instância."""

from __future__ import annotations

from collections import deque
from collections.abc import Sequence

from common.instance import Instance


def topological_order(instance: Instance) -> list[int]:
    """Uma ordem topológica dos jobs (algoritmo de Kahn).

    Raises:
        ValueError: Se o grafo de precedência tiver ciclo.
    """
    pending = [len(p) for p in instance.predecessors]
    queue = deque(j for j, n in enumerate(pending) if n == 0)
    order: list[int] = []
    while queue:
        job = queue.popleft()
        order.append(job)
        for s in instance.successors[job]:
            pending[s] -= 1
            if pending[s] == 0:
                queue.append(s)
    if len(order) != instance.n_jobs:
        raise ValueError("o grafo de precedência tem ciclo")
    return order


def is_precedence_feasible(instance: Instance, activity_list: Sequence[int]) -> bool:
    """Indica se a lista é uma permutação de todos os jobs com cada job após seus predecessores."""
    if sorted(activity_list) != list(range(instance.n_jobs)):
        return False
    position = {job: i for i, job in enumerate(activity_list)}
    return all(
        position[p] < position[job]
        for job in range(instance.n_jobs)
        for p in instance.predecessors[job]
    )
