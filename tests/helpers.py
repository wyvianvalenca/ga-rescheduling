"""Auxiliares só para testes."""

from __future__ import annotations

import random

from common.instance import Instance


def tiny_instance() -> Instance:
    """Exemplo à mão: capacidade 4; A(d=3, r=3), B(d=2, r=3), C(d=2, r=1).

    Jobs: 0 = início fictício, 1 = A, 2 = B, 3 = C, 4 = fim fictício.
    """
    return Instance(
        name="tiny",
        durations=(0, 3, 2, 2, 0),
        demands=((0,), (3,), (3,), (1,), (0,)),
        capacities=(4,),
        successors=((1, 2, 3), (4,), (4,), (4,), ()),
        predecessors=((), (0,), (0,), (0,), (1, 2, 3)),
    )


def random_feasible_list(instance: Instance, rng: random.Random) -> list[int]:
    """Lista de atividades viável: a cada passo escolhe ao acaso entre os jobs elegíveis."""
    done: set[int] = set()
    order: list[int] = []
    while len(order) < instance.n_jobs:
        eligible = [
            j for j in range(instance.n_jobs)
            if j not in done and all(p in done for p in instance.predecessors[j])
        ]
        job = rng.choice(eligible)
        done.add(job)
        order.append(job)
    return order
