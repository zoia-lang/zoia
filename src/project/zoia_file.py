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
"""Implements .zoia files."""
from dataclasses import dataclass
from enum import Enum
from functools import total_ordering

import log
from ast_nodes import ZoiaFileNode
from exception import ASTConversionError, ParsingError
from paths import ZPath
from zoia_processor import process_zoia_file

# FIXME finish
class FileType(Enum):
    """Represents the various header types that Zoia files can have."""
    ALIASES = 0

@dataclass(slots=True)
@total_ordering
class ZoiaFile:
    """A Zoia file is a file with the .zoia extension, following the layout
    specified by the Zoia grammar."""
    file_path: ZPath
    file_ast: ZoiaFileNode

    def is_main_file(self) -> bool:
        """Checks if this is a main.zoia file."""
        return self.file_path.cname == 'main.zoia'

    def __lt__(self, other) -> bool:
        if not isinstance(other, ZoiaFile):
            return NotImplemented
        return self.file_path < other.file_path

    @classmethod
    def parse_zoia_file(cls, file_path: ZPath, project_folder: ZPath,
                        raise_errors: bool):
        """Parses a Zoia file at the specified path."""
        file_rel = file_path.relative_to(project_folder)
        log.info(log.arrow(4, f'Parsing Zoia file at '
                              f'$fCl${file_rel}$R$'))
        try:
            processed_file = process_zoia_file(file_path)
        except ParsingError as e:
            if raise_errors:
                raise
            p = e.src_pos
            log.error(f'Failed to parse $fWl${p.src_file}$fT$ at line '
                      f'$fWl${p.src_line}$fT$, column $fWl${p.src_char}$fT$: '
                      f'$fRl${e.orig_msg}$fT$')
            return None
        except ASTConversionError as e:
            if raise_errors:
                raise
            p = e.src_pos
            log.error(f'Failed to AST-convert $fWl${p.src_file}$fT$ at line '
                      f'$fWl${p.src_line}$fT$, column $fWl${p.src_char}$fT$: '
                      f'$fRl${e.orig_msg}$fT$')
            return None
        return cls(file_path, processed_file)
