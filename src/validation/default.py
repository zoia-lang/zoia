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
from dataclasses import dataclass, field

from validation.base import CmdValidator
from validation.tys import Ty

from ast_nodes import LineElementsNode
from exception import ValidationError
from zoia_processor import process_zoia_arg

@dataclass(slots=True)
class Default(CmdValidator):
    ty: Ty
    _default_str: str = field(repr=False)
    default: LineElementsNode = field(init=False)

    def __post_init__(self):
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
