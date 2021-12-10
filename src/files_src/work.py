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

from exception import ProjectStructureError
from files_src.chapter import Chapter, is_valid_chapter
from paths import ZPath

# Valid work folder names consist of the word 'work' followed by one or more
# digits
is_valid_work = re.compile(r'work\d+', re.I).fullmatch

@dataclass(slots=True)
class Work:
    """A work folder is a folder containing one or more chapters."""
    chapters: list[Chapter]

    @classmethod
    def parse_work(cls, work_folder: ZPath):
        chapters = [Chapter.parse_chapter(c) for c in work_folder.iterdir()
                 if is_valid_chapter(c.name)]
        if not chapters:
            raise ProjectStructureError(
                work_folder, 'Work folders must contain one or more chapters')
        return cls(chapters)
