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
"""This module implements the Any type."""
from validation.tys.ty import ATy

from ast_nodes import LineElementsNode

class AnyTy(ATy):
    """A parameter of type Any accepts absolutely any value. In type theory
    terms, Any = Content + None."""
    _ty_name = 'Any'
    __slots__ = ()

    def validate_arg(self, cmd_arg: LineElementsNode):
        return cmd_arg
