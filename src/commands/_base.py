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
"""Provides base classes for implementing commands."""
from dataclasses import dataclass
from typing import Any

from ast_nodes import CommandNode
from exception import AbstractError
from src_pos import SourcePos
from validation import Signature

@dataclass(slots=True)
class _AStateExt:
    pass

class _ACommand:
    state_ext: _AStateExt = None
    cmd_name: str
    signature: Signature
    cmd_args: dict[str, Any]
    cmd_args_pos: dict[str, SourcePos]
    cmd_varargs: list[Any]
    cmd_varargs_pos: list[SourcePos]
    __slots__ = ('cmd_args', 'cmd_args_pos', 'cmd_varargs', 'cmd_varargs_pos')

    def __init__(self, node: CommandNode) -> None:
        c_a, c_ap, c_v, c_vp = self.signature.validate_args(node)
        self.cmd_args = c_a
        self.cmd_args_pos = c_ap
        self.cmd_varargs = c_v
        self.cmd_varargs_pos = c_vp

    @classmethod
    def finalize_command(cls) -> None:
        """Called once all command modules have been imported and all command
        signatures have been created. Finalizes this command class."""
        cls.signature.init_default_values()

    @classmethod
    def compact(cls) -> str:
        """Returns the compact signature representation of this command as a
        string."""
        return f'\\{cls.cmd_name}{cls.signature.compact()}'

    def eval_command(self, state: _AStateExt):
        """Evaluates this command with the specified state."""
        raise AbstractError()

    def __repr__(self) -> str:
        return self.compact()
