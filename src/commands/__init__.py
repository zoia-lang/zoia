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
"""This package implements the various commands that Zoia supports.

All imports should come directly from here - *never* import from the actual
files that define the classes. That way they can be moved around easily."""
from dataclasses import dataclass
import importlib
import pkgutil
import sys

from exception import ValidationError

# Disable some pylint warnings for this file only:
#  - global-statement: This is a lazily loaded framework for creating commands,
#    so needs to use globals to make that happen.
#  - invalid-name: Those aren't constants, they're global variables. Yeah,
#    spooky.
# pylint: disable=global-statement,invalid-name

def get_command_type(node):
    """Returns the command class matching the command describes by the
    specified CommandNode. Raises a ValidationError if it could not be found
    (indicating an unknown command)."""
    try:
        return _cmd_map[node.cmd_name]
    except TypeError: # _cmd_map is None
        _init_commands()
        return get_command_type(node)
    except KeyError as e: # node.cmd_name not in _cmd_map
        raise ValidationError(
            node.src_pos,
            f"Unknown command '\\{node.cmd_name}'") from e

def new_state_container():
    """Returns a new instance of the state container class."""
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
    # First collect all modules in this package that define a command
    for _imp, mod_name, _is_pkg in pkgutil.iter_modules(commands_path):
        # Internal module, does not define a command
        if mod_name.startswith('_'):
            continue
        module = importlib.import_module(f'{commands_name}.{mod_name}')
        cmd_type = getattr(module, 'CMD_TYPE')
        _cmd_map[cmd_type.cmd_name] = cmd_type
        # If the command defines a state extension, we need to include it in
        # the base classes for the state class later
        cmd_ext = cmd_type.state_ext
        if cmd_ext:
            state_exts.append(cmd_ext)
    # All modules have been imported and all signatures created, so we can now
    # finalize the commands we've collected and create the state class
    for cmd_type in _cmd_map.values():
        cmd_type.finalize_command()
    @dataclass(slots=True)
    class _StateClass(*state_exts):
        pass
    _state_class = _StateClass
