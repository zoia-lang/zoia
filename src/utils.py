# -*- coding: utf-8 -*-
#
# GPL License and Copyright Notice ============================================
#
#   This file is part of Zoia, a language for writing fiction.
#   Copyright (C) 2021 Infernio
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# =============================================================================
"""Random utility functions and classes that didn't fit anywhere else."""
from itertools import groupby
from pathlib import Path
from shutil import rmtree

import log
from exception import ProjectStructureError

def arrow(n: int, s: str) -> str:
    """Formats a message with a colorized, leading arrow with n """
    return f'$B${"=" * n}>$R$ {s}'

def is_contiguous(l: list[int]) -> bool:
    """Returns True if the specified list of integers is contiguous. In other
    words, if the element at index n has value v, then the element at index
    n + 1 must have value v + 1."""
    return len(list(groupby(enumerate(l), key=lambda x: x[0] - x[1]))) == 1

def is_fs_case_sensitive(test_path: Path) -> bool:
    """Returns True if the file system used at the specified path is
    case-sensitive."""
    temp_path = test_path / 'temp'
    temp_path.mkdir()
    try:
        (temp_path / 'foo.txt').touch()
        (temp_path / 'Foo.txt').touch()
        return len(list(temp_path.iterdir())) != 1
    finally:
        rmtree(temp_path)

def ps_error(msg: str, relevant_path: Path, raise_errors: bool):
    if raise_errors:
        raise ProjectStructureError(relevant_path, msg)
    else:
        log.error(f'Invalid project structure at $fWl${relevant_path}$fT$: '
                  f'$fRl${msg}$fT$')
        return None
