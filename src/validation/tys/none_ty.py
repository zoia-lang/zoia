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
"""This module implements the None type."""
from validation.tys.any_ty import AnyTy

from ast_nodes import LineElementsNode
from exception import ValidationError

class NoneTy(AnyTy):
    """There are no parameters of type None. It is a special type, only to be
    used as a return type for commands. Commands that return None cannot be
    used in a value of type Content."""
    _ty_name = 'None'
    __slots__ = ()

    def validate_arg(self, cmd_arg: LineElementsNode):
        # TODO Maybe add some detection to log to make it recognize internal
        #  errors and crash everything?
        raise ValidationError(
            cmd_arg.src_pos,
            f'[INTERNAL ERROR]: {self._ty_name} does not accept any kinds of '
            f'values. It should only be specified as a return type')
