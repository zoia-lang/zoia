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
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

import log
from project.dir_base import _ADirBase
from project.work import Work, match_work
from utils import is_contiguous, ps_error, dir_case_is_valid

@dataclass(slots=True)
class Series(_ADirBase):
    """A series is the main 'src' folder, containing one or more works in
    it."""
    works: list[Work]
    _id_works: defaultdict[int, Work | None] = field(init=False)

    def __post_init__(self):
        # @dataclass with slots=True breaks argument-less super
        # pylint: disable=super-with-arguments
        super(Series, self).__post_init__()
        self._id_works = defaultdict(lambda: None, {
            w.work_index: w for w in self.works})

    def get_work(self, work_name: str) -> Work | None:
        """Returns the work matching the specified name or None if such a work
        does not exist in this series."""
        work_ma = match_work(work_name)
        if not work_ma:
            return None # Invalid work name syntax
        return self._id_works[int(work_ma.group(1))]

    @classmethod
    def parse_series(cls, series_folder: Path, project_folder: Path, /, *,
                     raise_errors: bool):
        """Parses a series ('src' folder) at the specified path."""
        series_rel = series_folder.relative_to(project_folder)
        log.info(log.arrow(1, f'Found series at '
                              f'$fYl${series_rel}$R$'))
        if not dir_case_is_valid(series_folder, series_rel, raise_errors):
            return None
        aux_files = cls.parse_zoia_files(
            series_folder, project_folder, raise_errors=raise_errors,
            arrow_level=2,
            warning_msg=f'Failed to parse $fYl${series_folder.name}$R$ due to '
                        f'errors when parsing one or more Zoia files')
        if aux_files is None:
            return None # Warning already logged in parse_zoia_files
        works = [Work.parse_work(w, project_folder, raise_errors=raise_errors)
                 for w in series_folder.iterdir() if match_work(w.name)]
        if not all(works):
            # This is just a cascading effect of a real error
            log.warning(f'Failed to parse $fYl${series_folder.name}$R$ '
                        f'due to errors when parsing one or more works')
            return None
        if not works:
            return ps_error(f"The '{series_folder.name}' folder must contain "
                            f"one or more works",
                            series_rel, raise_errors)
        works.sort() # Blows up on None
        work_indices = [w.work_index for w in works]
        if work_indices[0] != 1:
            return ps_error('The first work in a series must have index 1',
                            series_rel, raise_errors)
        if not is_contiguous(work_indices):
            return ps_error('Work indices must form a contiguous sequence',
                            series_rel, raise_errors)
        # See parse_converter.py for the reasoning
        # noinspection PyArgumentList
        return cls(works, zoia_files=aux_files)
