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
"""Implements .zoia files."""
from dataclasses import dataclass
from enum import Enum
from functools import total_ordering

from paths import ZPath

# FIXME finish
class FileType(Enum):
    ALIASES = 0


@dataclass(slots=True)
@total_ordering
class ZoiaFile:
    """A Zoia file is a file with the .zoia extension, following the layout
    specified by the Zoia grammar."""
    file_path: ZPath

    def is_main_file(self) -> bool:
        """Checks if this is a main.zoia file."""
        return self.file_path.cname == 'main.zoia'

    def __lt__(self, other) -> bool:
        if not isinstance(other, ZoiaFile):
            return NotImplemented
        return self.file_path < other.file_path

    # FIXME parse_zoia_file method
