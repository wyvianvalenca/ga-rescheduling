import random
from dataclasses import replace
from pathlib import Path

import pytest

from common.metrics import cpm_lower_bound
from common.precedence import is_precedence_feasible, topological_order
from common.psplib import load_sm
from common.schedule import Schedule
from common.sgs import serial_sgs
from common.validate import validate
from tests.helpers import random_feasible_list, tiny_instance

FIXTURE = Path(__file__).parent / "fixtures" / "j301_1.sm"
J301_1_OPTIMUM = 43  # PSPLIB, j30: parâmetro 1, instância 1 (arquivo de soluções ótimas)
J301_1_CPM = 38  # "MPM-Time" no cabeçalho do próprio arquivo .sm


def test_sgs_hand_example_a_first() -> None:
    schedule = serial_sgs(tiny_instance(), [0, 1, 2, 3, 4])
    assert schedule.start_times == (0, 0, 3, 0, 5)
    assert schedule.makespan == 5


def test_sgs_hand_example_b_first() -> None:
    schedule = serial_sgs(tiny_instance(), [0, 2, 1, 3, 4])
    assert schedule.start_times == (0, 2, 0, 0, 5)


@pytest.mark.parametrize("bad_list", [[4, 0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 1, 3, 4]])
def test_sgs_rejects_infeasible_lists(bad_list: list[int]) -> None:
    with pytest.raises(ValueError, match="permutação"):
        serial_sgs(tiny_instance(), bad_list)


def test_sgs_rejects_demand_above_capacity() -> None:
    inst = replace(tiny_instance(), capacities=(2,))
    with pytest.raises(ValueError, match="capacidade"):
        serial_sgs(inst, [0, 1, 2, 3, 4])


def test_cpm_hand_example() -> None:
    assert cpm_lower_bound(tiny_instance()) == 3  # caminho mais longo: A (3)


def test_topological_order_is_feasible_list() -> None:
    inst = load_sm(FIXTURE)
    assert is_precedence_feasible(inst, topological_order(inst))


def test_cpm_matches_file_header() -> None:
    assert cpm_lower_bound(load_sm(FIXTURE)) == J301_1_CPM


def test_sgs_on_psplib_instance_is_valid_and_bounded() -> None:
    inst = load_sm(FIXTURE)
    rng = random.Random(42)
    for _ in range(100):
        schedule = serial_sgs(inst, random_feasible_list(inst, rng))
        assert validate(inst, schedule) == []
        assert schedule.makespan >= J301_1_OPTIMUM >= J301_1_CPM


def test_validator_catches_precedence_violation() -> None:
    inst = tiny_instance()
    bad = Schedule((0, 0, 3, 0, 2))  # fim fictício em 2, antes de A terminar (em 3)
    assert any("precedência" in v for v in validate(inst, bad))


def test_validator_catches_resource_violation() -> None:
    inst = tiny_instance()
    bad = Schedule((0, 0, 0, 0, 3))  # A (3) + B (3) = 6 > 4 no instante 0
    assert any("recurso" in v for v in validate(inst, bad))


def test_validator_catches_source_not_at_zero_and_wrong_length() -> None:
    inst = tiny_instance()
    assert any("fictício inicial" in v for v in validate(inst, Schedule((1, 1, 4, 1, 6))))
    assert validate(inst, Schedule((0, 0))) != []


def test_validator_accepts_valid_schedule() -> None:
    assert validate(tiny_instance(), Schedule((0, 0, 3, 0, 5))) == []
