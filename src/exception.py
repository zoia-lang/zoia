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
"""This module contains all custom exceptions for Zoia."""
from os import PathLike

from src_pos import SourcePos
# NO OTHER LOCAL IMPORTS! This has to be importable from any module/package.

# FIXME docstrings
class AbstractError(Exception):
    """Abstract section of code called."""
    def __init__(self, abs_method: callable) -> None:
        super().__init__(f"Abstract method '{abs_method.__qualname__}' was "
                         f"called")

class _SrcPosError(Exception):
    """Base class for errors that carry information about where in a source
    file they occurred."""
    def __init__(self, pos: SourcePos, msg: str) -> None:
        super().__init__(msg)
        self.src_pos = pos

class ASTConversionError(_SrcPosError):
    """An error that occurred during AST conversion."""
    def __init__(self, pos: SourcePos, msg: str) -> None:
        super().__init__(pos, f'Failed to AST-convert {pos.src_file} at line '
                              f'{pos.src_line}, column {pos.src_char}: {msg}')
        self.orig_msg = msg

class ParsingError(_SrcPosError):
    """An error that occurred during parsing of a Zoia file."""
    def __init__(self, pos: SourcePos, msg: str) -> None:
        super().__init__(pos, f'Failed to parse {pos.src_file} at line '
                              f'{pos.src_line}, column {pos.src_char}: {msg}')
        self.orig_msg = msg

class ProjectStructureError(Exception):
    """The project structure is invalid."""
    def __init__(self, relevant_path: PathLike, msg: str) -> None:
        super().__init__(f"Invalid project structure at '{relevant_path}': "
                         f"{msg}")
