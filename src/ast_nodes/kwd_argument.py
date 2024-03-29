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
"""Implements the AST node for keyword arguments."""
from dataclasses import dataclass

from ast_nodes.argument import AArgumentNode

@dataclass(slots=True)
class KwdArgumentNode(AArgumentNode):
    """AST node for keyword arguments."""
    kwd_name: str

    def accept(self, visitor):
        return visitor.visit_kwd_argument(self)

    def canonical(self) -> str:
        # @dataclass with slots=True breaks argument-less super
        # pylint: disable=super-with-arguments
        args_canonical = super(KwdArgumentNode, self).canonical()
        return f'{self.kwd_name} = {args_canonical}'
