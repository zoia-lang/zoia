# -*- coding: utf-8 -*-
#
# GPL License and Copyright Notice ============================================
#
#   This file is part of Zoia, a language for writing fiction.
#   Copyright (C) 2021 Infernio
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
"""This module contains all custom exceptions for Zoia."""
from pathlib import Path

# NO LOCAL IMPORTS! This has to be importable from any module/package.

class AbstractError(Exception):
    """Abstract section of code called."""
    def __init__(self, abs_method: callable) -> None:
        super().__init__(f"Abstract method '{abs_method.__qualname__}' was "
                         f"called")

class ASTConversionError(Exception):
    """An error that occurred during AST conversion."""

class ProjectStructureError(Exception):
    """The project structure is invalid."""
    def __init__(self, offending_folder: Path, msg: str) -> None:
        super().__init__(f"Invalid project structure at '{offending_folder}': "
                         f"{msg}")
