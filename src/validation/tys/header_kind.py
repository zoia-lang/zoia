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
"""This module implements the HeaderKind type."""
from enum import Enum

from validation.tys.word import WordTy

from ast_nodes import LineElementsNode
from exception import ValidationError
from utils import format_word_list

class HeaderKind(Enum):
    """The possible header kinds"""
    ALIASES = 'aliases'
    CHAPTER = 'chapter'
    DICTIONARY = 'dictionary'
    FRAGMENT = 'fragment'

_str_to_hk = {h.value: h for h in HeaderKind.__members__.values()}

class HeaderKindTy(WordTy):
    """A parameter of type HeaderKind will accept any header kind (see
    HeaderKind enum). Subtype of Word."""
    _ty_name = 'HeaderKind'
    __slots__ = ()

    def validate_arg(self, cmd_arg: LineElementsNode):
        txt_str = super().validate_arg(cmd_arg)
        try:
            return _str_to_hk[txt_str]
        except KeyError as e:
            fmt_header_kinds = format_word_list(list(_str_to_hk))
            raise ValidationError(
                cmd_arg.src_pos,
                f'Parameters of type {self._ty_name} only accept valid header '
                f'kinds ({fmt_header_kinds})') from e
