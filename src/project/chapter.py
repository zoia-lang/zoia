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
"""Implements chapter folders."""
import re
from dataclasses import dataclass
from functools import total_ordering

import log
from project.zoia_file import ZoiaFile
from paths import ZPath
from utils import ps_error

# Valid chapter folder names consist of the word 'ch' followed by one or more
# digits
match_chapter = re.compile(r'ch(\d+)', re.I).fullmatch

@dataclass(slots=True)
@total_ordering
class Chapter:
    """A chapter is a folder containing a main file (main.zoia) and,
    optionally, any number of auxiliary files (*.zoia)."""
    main_file: ZoiaFile
    aux_files: list[ZoiaFile]
    chapter_index: int

    def __init__(self, chapter_name: str, main_file: ZoiaFile,
                 aux_files: list[ZoiaFile]) -> None:
        self.main_file = main_file
        self.aux_files = aux_files
        # Extract the chapter index from the name of the chapter (we know the
        # regex matches at this point)
        self.chapter_index = int(match_chapter(chapter_name).group(1))

    def __lt__(self, other) -> bool:
        if not isinstance(other, Chapter):
            return NotImplemented
        return self.chapter_index < other.chapter_index

    @classmethod
    def parse_chapter(cls, chapter_folder: ZPath, project_folder: ZPath,
                      raise_errors: bool):
        """Parses a chapter folder at the specified path."""
        chapter_rel = chapter_folder.relative_to(project_folder)
        log.info(log.arrow(3, f'Found chapter at '
                              f'$fYl${chapter_rel}$R$'))
        aux_files = [ZoiaFile.parse_zoia_file(f, project_folder, raise_errors)
                     for f in chapter_folder.iterdir()
                     if f.csuffix == '.zoia']
        if not all(aux_files):
            # This error isn't the cause you should be investigating for why
            # your build is failing, so show it in gray
            log.error('$fDl$Failed to parse chapter due to errors when '
                      'parsing one or more Zoia files$R$')
            return None
        aux_files.sort() # Blows up on None
        # Ensure there is exactly one main file (on case-sensitive file
        # systems, there can be >1 file with the case-insensitive name
        # 'main.zoia')
        main_files = [f for f in aux_files if f.is_main_file()]
        if not main_files:
            return ps_error("Each chapter must contain a 'main.zoia' file",
                            chapter_folder, raise_errors)
        if len(main_files) != 1:
            return ps_error("There may only be one 'main.zoia' file per "
                            "chapter", chapter_folder, raise_errors)
        main_file = main_files[0]
        aux_files.remove(main_file)
        return cls(chapter_folder.name, main_file, aux_files)
