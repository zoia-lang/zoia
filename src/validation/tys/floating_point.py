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
import re

from validation.tys.word import WordTy

from ast_nodes import LineElementsNode
from exception import ValidationError, InternalError

# This defines the valid types of floats. This does not match Python's float
# syntax exactly, e.g. '1.' and '.0' are removed
_STD_FLOAT = re.compile(r'-?[0-9](?:_?[0-9])*\.[0-9](?:_?[0-9])*')
_EXP_FLOAT = re.compile(r'-?[0-9](?:_?[0-9])*(?:\.[0-9](?:_?[0-9])*)?e[+-]?'
                        r'[0-9](?:_?[0-9])*', re.I)
_FLT_CONST = re.compile('-?(?:nan|inf)', re.I)

class FloatTy(WordTy):
    """A parameter of type Float will accept any valid float (see regexes
    above). Subtype of Word."""
    _ty_name = 'Float'
    __slots__ = ()

    def validate_arg(self, cmd_arg: LineElementsNode):
        txt_str = super().validate_arg(cmd_arg)
        invalid_float_msg = (f"Parameters of type {self._ty_name} only accept "
                             f"valid floats, which {txt_str} is not")
        # Validate the string against our regexes, then let Python parse it
        if (not _STD_FLOAT.fullmatch(txt_str) and
                not _EXP_FLOAT.fullmatch(txt_str) and
                not _FLT_CONST.fullmatch(txt_str)):
            raise ValidationError(cmd_arg.src_pos, invalid_float_msg)
        try:
            return float(txt_str)
        except ValueError as e:
            # If we got here, then Python doesn't accept an int that we do
            # accept - so raise an internal error
            raise InternalError(invalid_float_msg) from e
