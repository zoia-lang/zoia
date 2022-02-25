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
from collections import defaultdict

from validation.tys.word import WordTy

from ast_nodes import LineElementsNode
from exception import ValidationError

# The valid base prefixes that Zoia integers may have
_base_prefix = defaultdict(lambda: 10, {
    '0b': 2,
    '0o': 8,
    '0x': 16,
})

class IntTy(WordTy):
    """A parameter of type Int will accept any valid integer, which is defined
    by the following ANTLR-like grammar:

        int: '-'? (binInt | octInt | hexInt | decInt);
        binInt: '0' [bB] ('_'? [01])+;
        octInt: '0' [oO] ('_'? [0-7])+;
        hexInt: '0' [xX] ('_'? [0-9a-fA-F])+;
        decInt: [0-9] ('_'? [0-9])*;

    Specialization of Word."""
    _ty_name = 'Int'
    __slots__ = ()

    def validate_arg(self, cmd_arg: LineElementsNode):
        txt_str = super().validate_arg(cmd_arg)
        is_negative = txt_str.startswith('-')
        if is_negative:
            txt_str = txt_str[1:]
        int_base = _base_prefix[txt_str[:2].lower()]
        try:
            parsed_int = int(txt_str, base=int_base)
        except ValueError as e:
            raise ValidationError(
                cmd_arg.src_pos,
                f"Parameters of type {self._ty_name} only accept valid "
                f"integers, which {txt_str} is not") from e
        return -parsed_int if is_negative else parsed_int
