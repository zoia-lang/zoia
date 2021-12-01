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
"""Implements the AST node for lines."""
from dataclasses import dataclass
from typing import Optional

from ast_nodes.base import ASTNode
from ast_nodes.line_elements import LineElementsNode

@dataclass(slots=True)
class LineNode(ASTNode):
    """AST node for lines."""
    elements: Optional[LineElementsNode]

    def canonical(self) -> str:
        elements_canon = self.elements.canonical() if self.elements else ''
        return elements_canon + '\n'
