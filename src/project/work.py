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
"""Implements work folders."""
import re
from dataclasses import dataclass
from functools import total_ordering

import log
from project.chapter import Chapter, match_chapter
from paths import ZPath
from utils import arrow, is_contiguous, ps_error

# Valid work folder names consist of the word 'work' followed by one or more
# digits
match_work = re.compile(r'work(\d+)', re.I).fullmatch

@dataclass(slots=True)
@total_ordering
class Work:
    """A work folder is a folder containing one or more chapters."""
    chapters: list[Chapter]
    work_index: int

    def __init__(self, work_name: str, chapters: list[Chapter]) -> None:
        self.chapters = chapters
        # Extract the work index from the name of the work (we know the regex
        # matches at this point)
        self.work_index = int(match_work(work_name).group(1))

    def __lt__(self, other) -> bool:
        if not isinstance(other, Work):
            return NotImplemented
        return self.work_index < other.work_index

    @classmethod
    def parse_work(cls, work_folder: ZPath, project_folder: ZPath,
                   raise_errors: bool):
        """Parses a work folder at the specified path."""
        work_rel = work_folder.relative_to(project_folder)
        log.info(arrow(2, f'Found work at $fYl${work_rel}$R$'))
        chapters = [Chapter.parse_chapter(c, project_folder, raise_errors)
                    for c in work_folder.iterdir() if match_chapter(c.name)]
        if not all(chapters):
            # This error isn't the cause you should be investigating for why
            # your build is failing, so show it in gray
            log.error('$fDl$Failed to parse work due to errors when parsing '
                      'one or more chapters$R$')
            return None
        if not chapters:
            return ps_error('Work folders must contain one or more chapters',
                            work_folder, raise_errors)
        chapters.sort() # Blows up on None
        chapter_indices = [c.chapter_index for c in chapters]
        if chapter_indices[0] != 1:
            return ps_error('The first chapter in a work must have index 1',
                            work_folder, raise_errors)
        if not is_contiguous(chapter_indices):
            return ps_error('Chapter indices must form a contiguous sequence',
                            work_folder, raise_errors)
        return cls(work_folder.name, chapters)
