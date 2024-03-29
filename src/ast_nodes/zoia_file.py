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
"""Implements the root AST node for entire Zoia files."""
from dataclasses import dataclass
from io import StringIO

from ast_nodes.base import AASTNode
from ast_nodes.header import HeaderNode
from ast_nodes.line import LineNode

@dataclass(slots=True)
class ZoiaFileNode(AASTNode):
    """AST node for Zoia files."""
    header: HeaderNode
    lines: list[LineNode]

    def accept(self, visitor):
        return visitor.visit_zoia_file(self)

    def canonical(self) -> str:
        s = StringIO()
        s.write(self.header.canonical())
        s.write('\n')
        for l in self.lines:
            s.write(l.canonical())
        return s.getvalue()
