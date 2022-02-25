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
"""This module implements the Float type."""
from validation.tys.word import WordTy

from ast_nodes import LineElementsNode
from exception import ValidationError

class FloatTy(WordTy):
    """A parameter of type Float will accept any valid float, which is defined
    by the following ANTLR-like grammar:

        float: '-'? (stdFloat | expFloat | floatConst);
        stdFloat: digits '.' digits;
        expFloat: (digits | stdFloat) [eE] [+-]? digits;
        digits: [0-9] ('_'? [0-9])*;
        floatConst: ([nN] [aA] [nN]) | ([iI] [nN] [fF]);

    Specialization of Word."""
    _ty_name = 'Float'
    __slots__ = ()

    def validate_arg(self, cmd_arg: LineElementsNode):
        txt_str = super().validate_arg(cmd_arg)
        try:
            return float(txt_str)
        except ValueError as e:
            raise ValidationError(
                cmd_arg.src_pos,
                f"Parameters of type {self._ty_name} only accept valid "
                f"floats, which {txt_str} is not") from e
