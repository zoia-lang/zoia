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

def is_contiguous(l: list[int]) -> bool:
    """Returns True if the specified list of integers is contiguous. In other
    words, if the element at index n has value v, then the element at index
    n + 1 must have value v + 1."""
    return len(list(groupby(enumerate(l), key=lambda x: x[0] - x[1]))) == 1