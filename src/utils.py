# -*- coding: utf-8 -*-
#
# GPL License and Copyright Notice ============================================
#
#   This file is part of Zoia, a language for writing fiction.
#   Copyright (C) 2021-2023 Infernio
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

def valid_src_path(src_path: str):
    """Returns True if the specified string path is valid as a src-relative
    path."""
    return src_path.lower() == src_path

def valid_zoia_path(zoia_path: str):
    """Returns True if the specified string path is valid as a src-relative
    path to a Zoia file."""
    return valid_src_path(zoia_path) and zoia_path.endswith('.zoia')

def format_word_list(word_list: list[str]) -> str:
    """Creates a human-readable version of the specified list of words."""
    quoted_words = [f"'{w}'" for w in word_list]
    if len(word_list) < 2:
        return ''.join(quoted_words)
    # Put an 'and' between the last two words
    last_two = ' and '.join(quoted_words[-2:])
    if len(word_list) == 2:
        return last_two
    # We have more than two words, so put commas between all the others
    first_few = ', '.join(quoted_words[:-2])
    return f'{first_few}, {last_two}'
