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
"""Implements chapter folders."""
from dataclasses import dataclass

from files_src.zoia_file import ZoiaFile
from paths import ZPath

@dataclass(slots=True)
class Chapter:
    """A chapter is a folder containing a main file (main.zoia) and one or more
    auxiliary files (*.zoia)."""
    main_file: ZoiaFile
    aux_files: list[ZoiaFile]

    @classmethod
    def parse_chapter(cls, chapter_folder: ZPath):
        aux_files = [ZoiaFile(f) for f in chapter_folder.iterdir()
                 if f.csuffix == '.zoia']
        try:
            main_file = next(f for f in aux_files if f.is_main_file())
        # TODO Custom exception - malformed project structure
        except StopIteration:
            raise RuntimeError
        aux_files.remove(main_file)
        return cls(main_file, aux_files)
