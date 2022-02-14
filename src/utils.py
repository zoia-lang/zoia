# -*- coding: utf-8 -*-
#
# GPL License and Copyright Notice ============================================
#
#   This file is part of Zoia, a language for writing fiction.
#   Copyright (C) 2021-2022 Infernio
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
from os import PathLike
from pathlib import Path

import log
from exception import ProjectStructureError

def is_contiguous(l: list[int]) -> bool:
    """Returns True if the specified list of integers is contiguous. In other
    words, if the element at index n has value v, then the element at index
    n + 1 must have value v + 1."""
    return len(list(groupby(enumerate(l), key=lambda x: x[0] - x[1]))) == 1

def ps_error(msg: str, relevant_path: PathLike, raise_errors: bool, *,
             orig_error: Exception = None):
    """Prints or raises a project structure error, depending on whether
    raise_errors is True or not."""
    if raise_errors:
        raise ProjectStructureError(relevant_path, msg) from orig_error
    else:
        log.error(f'Invalid project structure at $fWl${relevant_path}$fT$: '
                  f'$fRl${msg}$fT$')
        return None

def dir_case_is_valid(dir_path: Path, rel_dir_path: Path,
                      raise_errors: bool) -> bool:
    """Checks that the contents of the specified directory are all entirely in
    lowercase and return True. If not, calls ps_error (see above) with an error
    message and returns False."""
    case_valid = True
    for f in dir_path.iterdir():
        if f.name != f.name.lower():
            ps_error(f"'{f.name}' is not lowercased", rel_dir_path,
                     raise_errors)
            case_valid = False
    return case_valid
