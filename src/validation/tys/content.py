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
from dataclasses import dataclass

from validation.tys.any_ty import AnyTy
from validation.tys.none_ty import NoneTy

from ast_nodes import LineElementsNode, CommandNode
from ast_visitor import ACommandVisitor
from commands import get_command_type
from exception import ValidationError

@dataclass(slots=True)
class _ContentValidator(ACommandVisitor):
    parent_ty_name: str

    def visit_command(self, node: CommandNode):
        if isinstance(get_command_type(node).signature.ret_ty, NoneTy):
            raise ValidationError(
                node.src_pos,
                f'Parameters of type {self.parent_ty_name} only accept '
                f'document content, but \\{node.cmd_name} returns '
                f'{get_command_type(node).signature.ret_ty.compact()}')
        super().visit_command(node)

# Any type that will result in something visible in the output
class ContentTy(AnyTy):
    _ty_name = 'Content'
    __slots__ = ()

    def validate_arg(self, cmd_arg: LineElementsNode):
        _ContentValidator(self._ty_name).visit(cmd_arg)
        return super().validate_arg(cmd_arg)