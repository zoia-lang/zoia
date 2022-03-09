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
"""Implements the AST node for commands."""
from dataclasses import dataclass
from io import StringIO

from ast_nodes.argument import AArgumentNode
from ast_nodes.base import _write_arguments
from ast_nodes.line_element import ALineElementNode

@dataclass
class CommandNode(ALineElementNode):
    """AST node for commands."""
    arguments: list[AArgumentNode]
    cmd_name: str
    __slots__ = ('arguments', 'cmd_name', 'proc_cmd')

    # TODO I want this gone
    def accept_command(self, proc_cmd):
        """Called during validation - stores the processed version of this
        command in the node."""
        # pylint: disable=attribute-defined-outside-init
        self.proc_cmd = proc_cmd

    def accept(self, visitor):
        return visitor.visit_command(self)

    def canonical(self) -> str:
        s = StringIO()
        s.write('\\')
        s.write(self.cmd_name)
        _write_arguments(s, self.arguments)
        return s.getvalue()
