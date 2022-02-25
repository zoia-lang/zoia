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
"""This module provides an abstract base class for every kind of validator."""
from typing import Any

from ast_nodes import LineElementsNode
from exception import AbstractError

# NO IMPORTS FROM CMD_VALIDATION! This has to be importable in the entire
# package, including cmd_validation.tys

class _ACmdValidator:
    """Abstract base class for validators."""
    __slots__ = ()

    def validate_arg(self, cmd_arg: LineElementsNode) -> Any:
        """Validates the specified argument (a LineElementsNode) and transforms
        it into a more convenient internal representation, if possible."""
        raise AbstractError()

    def compact(self) -> str:
        """Returns the compact signature representation of this validator as a
        string."""
        raise AbstractError()

    def __repr__(self):
        return self.compact()
