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
"""Implements series folders."""
from dataclasses import dataclass

import log
from project.work import Work, match_work
from paths import ZPath
from utils import is_contiguous, ps_error

@dataclass(slots=True)
class Series:
    """A series is the main 'src' folder, containing one or more works in
    it."""
    works: list[Work]

    @classmethod
    def parse_series(cls, series_folder: ZPath, *, raise_errors: bool = False):
        """Parses a series ('src' folder) at the specified path."""
        # Resolve the path first so all later operations can use full paths and
        # ensure it exists while we're at it
        try:
            series_folder = series_folder.resolve(strict=True)
        except FileNotFoundError:
            return ps_error("No 'src' folder found", series_folder,
                            raise_errors)
        project_folder = series_folder.parent
        series_rel = series_folder.relative_to(project_folder)
        log.info(log.arrow(1, f'Found series at '
                              f'$fYl${series_rel}$R$'))
        works = [Work.parse_work(w, project_folder, raise_errors)
                 for w in series_folder.iterdir() if match_work(w.name)]
        if not all(works):
            # This is just a cascading effect of a real error
            log.warning('Failed to parse series due to errors when parsing '
                        'one or more works')
            return None
        if not works:
            return ps_error("The 'src' folder must contain one or more works",
                            series_folder, raise_errors)
        works.sort() # Blows up on None
        work_indices = [w.work_index for w in works]
        if work_indices[0] != 1:
            return ps_error('The first work in a series must have index 1',
                            series_folder, raise_errors)
        if not is_contiguous(work_indices):
            return ps_error('Work indices must form a contiguous sequence',
                            series_folder, raise_errors)
        return cls(works)
