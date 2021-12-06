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
"""Implements series folders."""
from dataclasses import dataclass

from files_src.work import Work
from paths import ZPath

@dataclass(slots=True)
class Series:
    """The series is the main 'src' folder, containing one or more works in
    it."""
    works: list[Work]

    @classmethod
    def parse_series(cls, series_folder: ZPath):
        works = [Work.parse_work(w) for w in series_folder.iterdir()
                 if w.cname.startswith('work')]
        return cls(works)
