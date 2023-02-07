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
"""This module provides the ability to specify optional parameters by provding
default values for validators."""
from dataclasses import dataclass, field
from typing import Any

from validation.base import _ACmdValidator
from validation.tys import ATy

from ast_nodes import LineElementsNode
from exception import ValidationError
from zoia_processor import process_zoia_arg

@dataclass(slots=True)
class Default(_ACmdValidator):
    """A validator that provides a default value for a validator, thereby
    making a parameter optional. Optional values are specified as a Zoia
    string, which is then parsed as if it were a lineElementsArg. See
    zoia_processor.process_zoia_arg."""
    ty: ATy
    _default_str: str = field(repr=False)
    default: Any = field(init=False)

    def init_default_value(self):
        """Parses and validates this Default's argument string into an actual
        default value. Called once all signatures are defined to avoid
        situations where validation of a value may end up needing to validate
        itself, which would cause a stack overflow."""
        try:
            self.default = self.validate_arg(process_zoia_arg(
                self._default_str, '<Signature default>'))
        except ValidationError as e:
            raise SyntaxError('Failed to validate a Signature default '
                              'value') from e

    def validate_arg(self, cmd_arg: LineElementsNode):
        return self.ty.validate_arg(cmd_arg)

    def compact(self) -> str:
        return f'{self.ty.compact()} = {self._default_str}'
