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
"""This module implements the Text type."""
from io import StringIO

from validation.tys.content import ContentTy

from ast_nodes import LineElementsNode, TextFragmentNode
from exception import ValidationError

# TODO We will probably want at least one more type between Text and Content -
#  ToText? Would accept commands that have Text or ToText as return type.
#  Basically anything that will *become* pure text during evaluation, no
#  backend-specific nodes?
class TextTy(ContentTy):
    """A parameter of type Text will accept any Content that consists purely
    of text fragments. Specialization of Content."""
    _ty_name = 'Text'
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
