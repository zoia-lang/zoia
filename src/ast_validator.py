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
"""Performs validation on a parsed Zoia AST. High-level interface to the
validation package."""
from ast_nodes import HeaderNode, CommandNode
from ast_visitor import ACommandVisitor
from commands import get_command_type

class ASTValidator(ACommandVisitor):
    """Performs validation on a Zoia AST, detecting and reporting errors that
    cannot be detected during parsing."""
    __slots__ = ()

    def visit_header(self, node: HeaderNode):
        node.accept_command(get_command_type(node)(node))
        super().visit_header(node)

    def visit_command(self, node: CommandNode):
        node.accept_command(get_command_type(node)(node))
        super().visit_command(node)
