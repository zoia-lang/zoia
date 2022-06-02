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
"""This module implements the PureText type."""
from io import StringIO

from validation.tys.text_ty import TextTy

from ast_nodes import LineElementsNode, TextFragmentNode
from exception import ValidationError

class PureTextTy(TextTy):
    """A parameter of type PureText will accept any Content that consists
    purely of text fragments. Subtype of Text."""
    _ty_name = 'PureText'
    __slots__ = ()

    def validate_arg(self, cmd_arg: LineElementsNode):
        super().validate_arg(cmd_arg)
        s = StringIO()
        for arg_element in cmd_arg.elements:
            if not isinstance(arg_element, TextFragmentNode):
                raise ValidationError(
                    arg_element.src_pos,
                    f'Parameters of type {self._ty_name} only accept text '
                    f'fragments')
            s.write(arg_element.text_val)
        return s.getvalue().strip()
