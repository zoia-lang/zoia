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
from dataclasses import dataclass
import importlib
import pkgutil
import sys

from exception import ValidationError

def get_command_type(node):
    try:
        return _cmd_map[node.cmd_name]
    except TypeError: # _cmd_map is None
        _init_commands()
        return get_command_type(node)
    except KeyError: # node.cmd_name not in _cmd_map
        raise ValidationError(
            node.src_pos,
            f"Unknown command '\\{node.cmd_name}'")

def new_state_container():
    try:
        return _state_class()
    except TypeError:
        _init_commands()
        return _state_class()

_cmd_map: dict | None = None
_state_class: type | None = None

def _init_commands():
    global _cmd_map, _state_class
    _cmd_map = {}
    state_exts = []
    commands_name = __name__
    commands_path = sys.modules[commands_name].__path__
    for _imp, mod_name, _is_pkg in pkgutil.iter_modules(commands_path):
        # Internal module, does not define a command
        if mod_name.startswith('_'):
            continue
        module = importlib.import_module(f'{commands_name}.{mod_name}')
        cmd_type = getattr(module, 'CMD_TYPE')
        _cmd_map[cmd_type.cmd_name] = cmd_type
        cmd_ext = cmd_type.state_ext
        if cmd_ext:
            state_exts.append(cmd_ext)
    @dataclass(slots=True)
    class _StateClass(*state_exts):
        pass
    _state_class = _StateClass
