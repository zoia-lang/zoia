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
"""Implements the base class for all Zoia AST nodes."""
from dataclasses import dataclass, field

from exception import AbstractError
from src_pos import SourcePos

@dataclass(slots=True)
class ASTNode:
    """Base class for all Zoia AST nodes."""
    src_pos: SourcePos = field(kw_only=True)

    def canonical(self) -> str:
        """Returns a canonical string representation of this node."""
        raise AbstractError(self.canonical)
