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
"""Implements work folders."""
import re
from collections import defaultdict
from dataclasses import dataclass, field
from functools import total_ordering
from pathlib import Path

import log
from project.chapter import Chapter, match_chapter
from project.dir_base import _ADirBase
from utils import is_contiguous, ps_error, dir_case_is_valid

# Valid work folder names consist of the word 'work' followed by one or more
# digits
match_work = re.compile(r'work(\d+)').fullmatch

@dataclass(slots=True)
@total_ordering
class Work(_ADirBase):
    """A work folder is a folder containing one or more chapters."""
    chapters: list[Chapter]
    work_index: int
    _id_chapters: defaultdict[int, Chapter | None] = field(init=False,
                                                           repr=False)

    def __post_init__(self):
        # @dataclass with slots=True breaks argument-less super
        # pylint: disable=super-with-arguments
        super(Work, self).__post_init__()
        self._id_chapters = defaultdict(lambda: None, {
            c.chapter_index: c for c in self.chapters})

    def __lt__(self, other) -> bool:
        if not isinstance(other, Work):
            return NotImplemented
        return self.work_index < other.work_index

    def get_chapter(self, chapter_name) -> Chapter | None:
        """Returns the chapter matching the specified name or None if such a
        chapter does not exist in this work."""
        chapter_ma = match_chapter(chapter_name)
        if not chapter_ma:
            return None # Invalid chapter name syntax
        return self._id_chapters[int(chapter_ma.group(1))]

    @classmethod
    def parse_work(cls, work_folder: Path, project_folder: Path, /, *,
                   raise_errors: bool):
        """Parses a work folder at the specified path."""
        work_rel = work_folder.relative_to(project_folder)
        log.info(log.arrow(2, f'Found work at $fYl${work_rel}$R$'))
        if not dir_case_is_valid(work_folder, work_rel, raise_errors):
            return None
        aux_files = cls.parse_zoia_files(
            work_folder, project_folder, raise_errors=raise_errors,
            arrow_level=3,
            warning_msg=f'Failed to parse $fYl${work_folder.name}$R$ due to '
                        f'errors when parsing one or more Zoia files')
        if aux_files is None:
            return None # Warning already logged in parse_zoia_files
        chapters = [Chapter.parse_chapter(c, project_folder,
                                          raise_errors=raise_errors)
                    for c in work_folder.iterdir() if match_chapter(c.name)]
        if not all(chapters):
            # This is just a cascading effect of a real error
            log.warning(f'Failed to parse $fYl${work_folder.name}$R$ due to '
                        f'errors when parsing one or more chapters')
            return None
        if not chapters:
            return ps_error('Work folders must contain one or more chapters',
                            work_rel, raise_errors)
        chapters.sort() # Blows up on None
        chapter_indices = [c.chapter_index for c in chapters]
        if chapter_indices[0] != 1:
            return ps_error('The first chapter in a work must have index 1',
                            work_rel, raise_errors)
        if not is_contiguous(chapter_indices):
            return ps_error('Chapter indices must form a contiguous sequence',
                            work_rel, raise_errors)
        # Extract the work index from the name of the work (we know the regex
        # matches at this point)
        wk_index = int(match_work(work_folder.name).group(1))
        # See parse_converter.py for the reasoning
        # noinspection PyArgumentList
        return cls(chapters, wk_index, zoia_files=aux_files)
