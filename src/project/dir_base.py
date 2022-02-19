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
"""Implements shared code for all types of project folders."""
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

import log
from project.zoia_file import ZoiaFile

@dataclass(slots=True)
class _ADirBase:
    """Base class for all project folders."""
    zoia_files: list[ZoiaFile] = field(kw_only=True)
    _id_zoia: defaultdict[str, ZoiaFile | None] = field(init=False)

    def __post_init__(self):
        self._id_zoia = defaultdict(lambda: None, {
            z.file_path.name: z for z in self.zoia_files})

    def get_zoia_file(self, zoia_name: str) -> ZoiaFile | None:
        """Returns the ZoiaFile matching the specified name or None if such a
        ZoiaFile does not exist in this folder."""
        return self._id_zoia[zoia_name]

    @staticmethod
    def parse_zoia_files(curr_folder: Path, project_folder: Path, /, *,
                         raise_errors: bool, arrow_level: int,
                         warning_msg: str) -> list[ZoiaFile] | None:
        """Parses .zoia files in the specified folder. The remaining arguments
        are passed to parse_zoia_file, except for warning_msg, which is used
        for raising a warning if one or more files fails to parse."""
        ret_files = [ZoiaFile.parse_zoia_file(f, project_folder,
                                              raise_errors=raise_errors,
                                              arrow_level=arrow_level)
                     for f in curr_folder.iterdir() if f.suffix == '.zoia']
        if not all(ret_files):
            # This is just a cascading effect of a real error
            log.warning(warning_msg)
            return None
        return sorted(ret_files) # Blows up on None, see above
