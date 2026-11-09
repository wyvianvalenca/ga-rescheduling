"""Serial SGS (Schedule Generation Scheme): decodifica uma lista de atividades em cronograma."""

from __future__ import annotations

from collections.abc import Sequence

from common.instance import Instance
from common.precedence import is_precedence_feasible
from common.schedule import Schedule


def serial_sgs(instance: Instance, activity_list: Sequence[int]) -> Schedule:
    """Gera um cronograma viável a partir de uma lista de atividades.

    Cada job, na ordem da lista, recebe o menor início que respeita as
    precedências e mantém o consumo de todos os recursos dentro da capacidade
    durante toda a sua duração.

    Args:
        instance: A instância do problema.
        activity_list: Permutação dos jobs em que cada job aparece após seus predecessores.

    Raises:
        ValueError: Se a lista não for uma permutação viável quanto à precedência,
            ou se algum job demandar mais que a capacidade de um recurso.
    """
    if not is_precedence_feasible(instance, activity_list):
        raise ValueError("a lista de atividades não é uma permutação viável quanto à precedência")
    for job in range(instance.n_jobs):
        if any(d > c for d, c in zip(instance.demands[job], instance.capacities, strict=True)):
            raise ValueError(f"o job {job} demanda mais que a capacidade de algum recurso")

    # Limite seguro: nenhum job precisa começar depois da soma das durações.
    horizon = sum(instance.durations)
    usage = [[0] * horizon for _ in range(instance.n_resources)]
    start = [0] * instance.n_jobs
    finish = [0] * instance.n_jobs

    for job in activity_list:
        duration = instance.durations[job]
        demand = instance.demands[job]
        t = max((finish[p] for p in instance.predecessors[job]), default=0)
        if duration > 0:
            used = [r for r, d in enumerate(demand) if d > 0]
            while not all(
                usage[r][tau] + demand[r] <= instance.capacities[r]
                for r in used
                for tau in range(t, t + duration)
            ):
                t += 1
            for r in used:
                for tau in range(t, t + duration):
                    usage[r][tau] += demand[r]
        start[job] = t
        finish[job] = t + duration

    return Schedule(tuple(start))
