"""Métricas e limites de referência."""

from __future__ import annotations

from common.instance import Instance
from common.precedence import topological_order


def cpm_lower_bound(instance: Instance) -> int:
    """Caminho crítico: menor makespan possível ignorando os recursos (limite inferior fraco)."""
    earliest = [0] * instance.n_jobs
    for job in topological_order(instance):
        for s in instance.successors[job]:
            earliest[s] = max(earliest[s], earliest[job] + instance.durations[job])
    return earliest[instance.sink]
