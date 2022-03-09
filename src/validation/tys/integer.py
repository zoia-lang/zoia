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
"""This module implements the Int type."""
import re

from validation.tys.word import WordTy

from ast_nodes import LineElementsNode
from exception import ValidationError, InternalError

# This defines the valid types of integers. They must be regex-fullmatched one
# at a time to avoid overlaps (e.g. 0b12423 producing two matches, one for
# _BIN_INT -> 0b1 and one for _DEC_INT -> 2423)
_DEC_INT = re.compile('-?[0-9](?:_?[0-9])*')
_HEX_INT = re.compile('-?0x(?:_?[0-9A-F])+', re.I)
_OCT_INT = re.compile('-?0o(?:_?[0-7])+', re.I)
_BIN_INT = re.compile('-?0b(?:_?[01])+', re.I)

class IntTy(WordTy):
    """A parameter of type Int will accept any valid integer (see regexes
    above). Subtype of Word."""
    _ty_name = 'Int'
    __slots__ = ()

    def validate_arg(self, cmd_arg: LineElementsNode):
        txt_str = super().validate_arg(cmd_arg)
        invalid_int_msg = (f"Parameters of type {self._ty_name} only accept "
                           f"valid integers, which {txt_str} is not")
        # Check that this is a valid integer and determine its base while we're
        # at it (so that Python can handle leading zeroes for decimal ints)
        if _DEC_INT.fullmatch(txt_str):
            int_base = 10
        elif _HEX_INT.fullmatch(txt_str):
            int_base = 16
        elif _OCT_INT.fullmatch(txt_str):
            int_base = 8
        elif _BIN_INT.fullmatch(txt_str):
            int_base = 2
        else:
            raise ValidationError(cmd_arg.src_pos, invalid_int_msg)
        # The integer is valid, so we can let Python handle it from here
        try:
            return int(txt_str, base=int_base)
        except ValueError as e:
            # If we got here, then Python doesn't accept an int that we do
            # accept - so raise an internal error
            raise InternalError(invalid_int_msg) from e
