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
"""This module houses SourcePos, a class for storing source code positions."""
from dataclasses import dataclass

@dataclass(slots=True)
class SourcePos:
    """Stores a position in source code somewhere, consisting of the source
    file, line number and character offset within that line."""
    src_file: str
    src_line: int
    src_char: int

    def __repr__(self) -> str:
        return (f"File '{self.src_file}', on line "
                f"{self.src_line} at offset {self.src_char + 1}")
