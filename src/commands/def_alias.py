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
r"""This module implements the \\def_alias command."""
from dataclasses import dataclass, field
from typing import Any

from exception import EvalError
from validation import Signature, WordTy, ContentTy

from commands._base import _ACommand, _AStateExt

@dataclass(slots=True)
class _StateExtDA(_AStateExt):
    seen_alias_keys: set[str] = field(default_factory=set)
    alias_dict: dict[str, Any] = field(default_factory=dict)

class DefAliasCmd(_ACommand):
    r"""The \\def_alias command. Creates a new alias. May only occur in Zoia
    files with header kind 'aliases'."""
    state_ext = _StateExtDA
    cmd_name = 'def_alias'
    signature = Signature(
        std_only={
            'key': WordTy(),
            'val': ContentTy(),
        },
    )
    __slots__ = ()

    def eval_command(self, state: _StateExtDA):
        alias_key = self.cmd_args['key']
        seen_alias_keys = state.seen_alias_keys
        if alias_key in seen_alias_keys:
            raise EvalError(self.cmd_args_pos['key'],
                            f"Duplicate alias key '{alias_key}'")
        seen_alias_keys.add(alias_key)
        state.alias_dict[alias_key] = self.cmd_args['val']

CMD_TYPE = DefAliasCmd
