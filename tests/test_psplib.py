import re
from pathlib import Path

import pytest

from common.instance import Instance
from common.psplib import ParseError, load_sm, parse_sm

FIXTURE = Path(__file__).parent / "fixtures" / "j301_1.sm"


@pytest.fixture(scope="module")
def inst() -> Instance:
    return load_sm(FIXTURE)


def test_basic_dimensions(inst: Instance) -> None:
    assert inst.name == "j301_1"
    assert inst.n_jobs == 32
    assert inst.n_resources == 4
    assert (inst.source, inst.sink) == (0, 31)


def test_capacities(inst: Instance) -> None:
    assert inst.capacities == (12, 13, 4, 12)


def test_durations_and_demands(inst: Instance) -> None:
    # job 2 do arquivo (índice 1): duração 8, usa 4 unidades de R1
    assert inst.durations[1] == 8
    assert inst.demands[1] == (4, 0, 0, 0)
    # jobs fictícios
    assert inst.durations[0] == inst.durations[31] == 0
    assert inst.demands[0] == inst.demands[31] == (0, 0, 0, 0)


def test_successors_zero_indexed(inst: Instance) -> None:
    assert inst.successors[0] == (1, 2, 3)  # job 1 -> 2, 3, 4 no arquivo
    assert inst.successors[31] == ()


def test_predecessors_consistent_with_successors(inst: Instance) -> None:
    for job, succ in enumerate(inst.successors):
        for s in succ:
            assert job in inst.predecessors[s]
    assert sum(map(len, inst.successors)) == sum(map(len, inst.predecessors))
    assert set(inst.predecessors[31]) == {28, 29, 30}  # jobs 29, 30, 31 do arquivo
    assert inst.predecessors[0] == ()


def test_multimode_is_rejected() -> None:
    text = FIXTURE.read_text(encoding="utf-8").replace("   2        1          3", "   2        2          3", 1)
    with pytest.raises(ParseError, match="modos"):
        parse_sm(text, "x")


def test_missing_section_is_rejected() -> None:
    text = FIXTURE.read_text(encoding="utf-8").replace("RESOURCEAVAILABILITIES", "OUTRA COISA")
    with pytest.raises(ParseError, match="RESOURCEAVAILABILITIES"):
        parse_sm(text, "x")


def test_nonrenewable_is_rejected() -> None:
    original = FIXTURE.read_text(encoding="utf-8")
    text = re.sub(r"(nonrenewable\s*:\s*)0", r"\g<1>1", original, count=1)
    assert text != original  # garante que a alteração de fato ocorreu
    with pytest.raises(ParseError, match="não renováveis"):
        parse_sm(text, "x")
