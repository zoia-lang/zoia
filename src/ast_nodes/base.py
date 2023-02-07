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
"""Implements the base class for all Zoia AST nodes."""
from dataclasses import dataclass, field
from io import StringIO

from exception import AbstractError
from src_pos import SourcePos

@dataclass(slots=True)
class AASTNode:
    """Base class for all Zoia AST nodes."""
    src_pos: SourcePos = field(kw_only=True, repr=False)

    def accept(self, visitor):
        """Called by a visitor when it's about to visit this node. It should
        call a specific method on the visitor that will then visit this
        node."""
        raise AbstractError()

    def canonical(self) -> str:
        """Returns a canonical string representation of this node."""
        raise AbstractError()

def _write_arguments(s: StringIO, arguments: list[AASTNode]) -> None:
    """Helper method for writing out a list of nodes as arguments to a
    command, including the brackets used to open and close the command (or a
    vertical bar as a terminator, if the command does not have any
    arguments)."""
    if arguments:
        s.write('[')
        if len(arguments) == 1:
            s.write(arguments[0].canonical())
        else:
            s.write('\n')
            for a in arguments:
                s.write('    ')
                s.write(a.canonical())
                s.write(';\n')
        s.write(']')
    else:
        s.write('|')
