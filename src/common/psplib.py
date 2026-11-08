"""Leitor de instâncias PSPLIB no formato ``.sm`` (single-mode RCPSP).

O arquivo é lido apenas como texto; nada dele é executado.
"""

from __future__ import annotations

import re
from pathlib import Path

from common.instance import Instance

_JOBS_RE = re.compile(r"jobs \(incl\. supersource/sink \)\s*:\s*(\d+)")
_RENEWABLE_RE = re.compile(r"-\s*renewable\s*:\s*(\d+)")
_NONRENEWABLE_RE = re.compile(r"-\s*nonrenewable\s*:\s*(\d+)")
_DOUBLY_RE = re.compile(r"-\s*doubly constrained\s*:\s*(\d+)")


class ParseError(ValueError):
    """Arquivo ``.sm`` malformado ou fora do escopo suportado."""


def _find_int(pattern: re.Pattern[str], text: str, what: str) -> int:
    match = pattern.search(text)
    if match is None:
        raise ParseError(f"campo não encontrado: {what}")
    return int(match.group(1))


def _find_section(lines: list[str], title: str) -> int:
    for i, line in enumerate(lines):
        if line.strip().startswith(title):
            return i
    raise ParseError(f"seção não encontrada: {title}")


def _ints(line: str, where: str) -> list[int]:
    try:
        return [int(tok) for tok in line.split()]
    except ValueError as exc:
        raise ParseError(f"linha com valor não inteiro em {where}: {line!r}") from exc


def parse_sm(text: str, name: str) -> Instance:
    """Converte o conteúdo de um arquivo ``.sm`` em uma :class:`Instance`.

    Args:
        text: Conteúdo do arquivo.
        name: Nome a atribuir à instância.

    Raises:
        ParseError: Se o formato for inválido ou houver mais de um modo,
            recursos não renováveis ou duplamente restritos.
    """
    lines = text.splitlines()
    n_jobs = _find_int(_JOBS_RE, text, "jobs")
    n_res = _find_int(_RENEWABLE_RE, text, "recursos renováveis")
    if _find_int(_NONRENEWABLE_RE, text, "recursos não renováveis") != 0:
        raise ParseError("recursos não renováveis não são suportados")
    if _find_int(_DOUBLY_RE, text, "recursos duplamente restritos") != 0:
        raise ParseError("recursos duplamente restritos não são suportados")

    # Precedências: pula o título e a linha de cabeçalho.
    start = _find_section(lines, "PRECEDENCE RELATIONS") + 2
    successors: list[tuple[int, ...]] = []
    for i in range(n_jobs):
        row = _ints(lines[start + i], "PRECEDENCE RELATIONS")
        if len(row) < 3 or row[0] != i + 1:
            raise ParseError(f"job fora de ordem em PRECEDENCE RELATIONS: {lines[start + i]!r}")
        if row[1] != 1:
            raise ParseError(f"job {row[0]} tem {row[1]} modos; só single-mode é suportado")
        succ = row[3:]
        if len(succ) != row[2] or any(not 1 <= s <= n_jobs for s in succ):
            raise ParseError(f"sucessores inválidos para o job {row[0]}")
        successors.append(tuple(s - 1 for s in succ))

    # Durações e demandas: pula o título, o cabeçalho e a linha de traços.
    start = _find_section(lines, "REQUESTS/DURATIONS") + 3
    durations: list[int] = []
    demands: list[tuple[int, ...]] = []
    for i in range(n_jobs):
        row = _ints(lines[start + i], "REQUESTS/DURATIONS")
        if len(row) != 3 + n_res or row[0] != i + 1:
            raise ParseError(f"linha inválida em REQUESTS/DURATIONS: {lines[start + i]!r}")
        if row[2] < 0 or any(d < 0 for d in row[3:]):
            raise ParseError(f"valor negativo para o job {row[0]}")
        durations.append(row[2])
        demands.append(tuple(row[3:]))

    # Capacidades: pula o título e a linha com os nomes dos recursos.
    start = _find_section(lines, "RESOURCEAVAILABILITIES") + 2
    capacities = _ints(lines[start], "RESOURCEAVAILABILITIES")
    if len(capacities) != n_res or any(c < 0 for c in capacities):
        raise ParseError(f"capacidades inválidas: {lines[start]!r}")

    predecessors: list[list[int]] = [[] for _ in range(n_jobs)]
    for job, succ_list in enumerate(successors):
        for s in succ_list:
            predecessors[s].append(job)

    return Instance(
        name=name,
        durations=tuple(durations),
        demands=tuple(demands),
        capacities=tuple(capacities),
        successors=tuple(successors),
        predecessors=tuple(tuple(p) for p in predecessors),
    )


def load_sm(path: Path) -> Instance:
    """Lê um arquivo ``.sm`` do disco; o nome da instância é o nome do arquivo sem extensão."""
    return parse_sm(path.read_text(encoding="utf-8"), name=path.stem)
