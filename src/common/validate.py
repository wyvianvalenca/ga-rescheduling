"""Validador de cronogramas, independente do SGS.

A checagem de recursos é feita por eventos: o consumo só aumenta no início de
algum job, então basta conferir cada instante de início. Isso evita reaproveitar
a lógica de perfil de recursos do SGS (um erro lá não passaria despercebido aqui).
"""

from __future__ import annotations

from common.instance import Instance
from common.schedule import Schedule


def validate(instance: Instance, schedule: Schedule) -> list[str]:
    """Lista as violações de um cronograma (vazia se for viável)."""
    starts = schedule.start_times
    if len(starts) != instance.n_jobs:
        return [f"número de inícios ({len(starts)}) diferente do número de jobs ({instance.n_jobs})"]

    violations: list[str] = []
    if any(s < 0 for s in starts):
        violations.append("há início negativo")
    if starts[instance.source] != 0:
        violations.append(f"o job fictício inicial começa em {starts[instance.source]}, não em 0")

    for job in range(instance.n_jobs):
        for pred in instance.predecessors[job]:
            if starts[job] < starts[pred] + instance.durations[pred]:
                violations.append(
                    f"precedência violada: job {job} começa em {starts[job]}, "
                    f"antes do fim do job {pred} ({starts[pred] + instance.durations[pred]})"
                )

    for t in sorted(set(starts)):
        active = [
            j for j in range(instance.n_jobs)
            if instance.durations[j] > 0 and starts[j] <= t < starts[j] + instance.durations[j]
        ]
        for r, capacity in enumerate(instance.capacities):
            total = sum(instance.demands[j][r] for j in active)
            if total > capacity:
                violations.append(f"recurso {r} excede a capacidade no instante {t}: {total} > {capacity}")
    return violations
