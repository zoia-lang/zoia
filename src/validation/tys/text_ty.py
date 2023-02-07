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
"""This module implements the Text type."""
from dataclasses import dataclass

from validation.tys.content_ty import ContentTy

from ast_nodes import LineElementsNode, CommandNode, TextFragmentNode
from ast_visitor import ACommandVisitor
from commands import get_command_type
from exception import ValidationError

@dataclass(slots=True)
class _TextValidator(ACommandVisitor):
    """Command visitor that ensures every command in the value has a PureText
    or Text return type."""
    parent_ty_name: str

    def visit_command(self, node: CommandNode):
        cmd_ret_ty = get_command_type(node).signature.ret_ty
        if not isinstance(cmd_ret_ty, TextTy):
            raise ValidationError(
                node.src_pos,
                f'Parameters of type {self.parent_ty_name} only accept '
                f'Text and its subtypes, but \\{node.cmd_name} returns '
                f'{cmd_ret_ty.compact()}')
        super().visit_command(node)

class TextTy(ContentTy):
    """A parameter of type Text will accept any value that will eventually
    result in PureText after evaluating it (in other words, its return type
    must be Text or a subtype of Text)."""
    _ty_name = 'Text'
    __slots__ = ()

    def validate_arg(self, cmd_arg: LineElementsNode):
        for arg_element in cmd_arg.elements:
            if not isinstance(arg_element, (TextFragmentNode, CommandNode)):
                raise ValidationError(
                    arg_element.src_pos,
                    f'Parameters of type {self._ty_name} only accept text '
                    f'fragments and commands with a return type of Text (or '
                    f'one of its subtypes)')
        _TextValidator(self._ty_name).visit(cmd_arg)
        return super().validate_arg(cmd_arg)
