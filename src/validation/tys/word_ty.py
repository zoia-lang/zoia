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
"""This module implements the Word type."""
from validation.tys.pure_text_ty import PureTextTy

from ast_nodes import LineElementsNode
from exception import ValidationError
from utils import format_word_list

# TextTy that is restricted to only one word
class WordTy(PureTextTy):
    """A parameter of type Word will accept any PureText that consists of only
    one word (with whitespace trimmed). Subtype of PureText."""
    _ty_name = 'Word'
    __slots__ = ()

    def validate_arg(self, cmd_arg: LineElementsNode):
        text_str = super().validate_arg(cmd_arg)
        split_text = text_str.split()
        if len(split_text) > 1:
            fmt_extra = format_word_list(split_text[1:])
            if len(split_text) == 2:
                # Fix the grammar for a single extraneous word
                raise ValidationError(
                    cmd_arg.src_pos,
                    f'Parameters of type {self._ty_name} only accept single '
                    f'words - {fmt_extra} is extraneous')
            raise ValidationError(
                cmd_arg.src_pos,
                f'Parameters of type {self._ty_name} only accept single '
                f'words - {fmt_extra} are extraneous')
        return text_str
