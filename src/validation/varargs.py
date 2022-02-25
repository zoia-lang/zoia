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
"""This module provides support for specifying vararg parameters."""
from dataclasses import dataclass
from enum import Enum

from validation.base import _ACmdValidator
from validation.default import Default
from validation.tys import ATy

from ast_nodes import LineElementsNode

class _VarArgsKind(Enum):
    """The three kinds of varargs. Use the constants defined in this module
    directly instead of accessing this enum."""
    VA_STD = 0
    VA_EITHER_OR = 1
    VA_KWD = 2

    def __repr__(self):
        return self.name

VARARGS_STD = _VarArgsKind.VA_STD
VARARGS_EITHER_OR = _VarArgsKind.VA_EITHER_OR
VARARGS_KWD = _VarArgsKind.VA_KWD

@dataclass(slots=True)
class Varargs(_ACmdValidator):
    """A validator that accepts zero or more arguments of a certain type. You
    must also provide the kind of varargs this is - std-only, either-or or
    kwd-only."""
    va_kind: _VarArgsKind
    ty: ATy

    def __post_init__(self):
        # This is nonsense type-wise, but Python does not have static typing,
        # so we'll have to do it manually...
        if isinstance(self.ty, Default):
            raise SyntaxError('Varargs may not have Default values')

    def validate_arg(self, cmd_arg: LineElementsNode):
        return self.ty.validate_arg(cmd_arg)

    def compact(self) -> str:
        if self.va_kind is VARARGS_STD:
            return f'~ {self.ty.compact()}*'
        elif self.va_kind is VARARGS_EITHER_OR:
            return f'{self.ty.compact()}*'
        elif self.va_kind is VARARGS_KWD:
            return f'$ {self.ty.compact()}*'
        raise NotImplementedError(f'compact() not implemented for unknown '
                                  f'kind of varargs {self.va_kind}')
