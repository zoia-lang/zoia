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

from exception import ProjectStructureError
from project.work import Work, match_work
from paths import ZPath
from utils import is_contiguous

@dataclass(slots=True)
class Series:
    """A series is the main 'src' folder, containing one or more works in
    it."""
    works: list[Work]

    @classmethod
    def parse_series(cls, series_folder: ZPath):
        """Parses a series ('src' folder) at the specified path."""
        # Resolve the path first so all later operations can use full paths and
        # ensure it exists while we're at it
        try:
            series_folder = series_folder.resolve(strict=True)
        except FileNotFoundError:
            raise ProjectStructureError(series_folder, "No 'src' folder found")
        works = sorted(Work.parse_work(w) for w in series_folder.iterdir()
                       if match_work(w.name))
        if not works:
            raise ProjectStructureError(
                series_folder, "The 'src' folder must contain one or more "
                               "works")
        work_indices = [w.work_index for w in works]
        if work_indices[0] != 1:
            raise ProjectStructureError(
                series_folder, 'The first work in a series must have index 1')
        if not is_contiguous(work_indices):
            raise ProjectStructureError(
                series_folder, 'Work indices must form a contiguous sequence')
        return cls(works)
