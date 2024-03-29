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
"""Implements chapter folders."""
import re
from dataclasses import dataclass
from functools import total_ordering
from pathlib import Path

import log
from project.dir_base import _ADirBase
from project.zoia_file import ZoiaFile
from utils import ps_error

# Valid chapter folder names consist of the word 'ch' followed by one or more
# digits
match_chapter = re.compile(r'ch(\d+)').fullmatch

@dataclass(slots=True)
@total_ordering
class Chapter(_ADirBase):
    """A chapter is a folder containing a main file (main.zoia) and,
    optionally, any number of ancillary files (*.zoia)."""
    chapter_path: Path
    main_file: ZoiaFile
    chapter_index: int

    def __lt__(self, other) -> bool:
        if not isinstance(other, Chapter):
            return NotImplemented
        return self.chapter_index < other.chapter_index

    def get_zoia_file(self, zoia_name: str) -> ZoiaFile | None:
        if zoia_name == 'main.zoia':
            return self.main_file
        # @dataclass with slots=True breaks argument-less super
        # pylint: disable=super-with-arguments
        return super(Chapter, self).get_zoia_file(zoia_name)

    @classmethod
    def parse_chapter(cls, chapter_folder: Path, project_folder: Path, /, *,
                      raise_errors: bool):
        """Parses a chapter folder at the specified path."""
        chapter_rel = chapter_folder.relative_to(project_folder)
        log.info(log.arrow(3, f'Found chapter at '
                              f'{log.color_dir(chapter_rel)}'))
        cf_contents = list(chapter_folder.iterdir())
        if not cls._file_names_valid(cf_contents, chapter_rel, raise_errors):
            return None
        anc_files = cls._parse_zoia_files(
            cf_contents, project_folder, raise_errors=raise_errors,
            arrow_level=4,
            warning_msg=f'Failed to parse '
                        f'{log.color_dir(chapter_folder.name)} due to errors '
                        f'when parsing one or more Zoia files')
        if anc_files is None:
            return None # Warning already logged in parse_zoia_files
        # There caaaan be only oooooooone
        main_files = [f for f in anc_files if f.is_main_file()]
        if not main_files:
            return ps_error("Each chapter must contain a 'main.zoia' file",
                            chapter_rel, raise_errors)
        # There can't be >1 main file since we disallow non-lowercase names
        main_file = main_files[0]
        anc_files.remove(main_file)
        # Extract the chapter index from the name of the chapter (we know the
        # regex matches at this point)
        ch_index = int(match_chapter(chapter_folder.name).group(1))
        # See parse_converter.py for the reasoning
        # noinspection PyArgumentList
        return cls(chapter_folder, main_file, ch_index, zoia_files=anc_files)
