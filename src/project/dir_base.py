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
from utils import ps_error

# https://learn.microsoft.com/en-us/windows/win32/fileio/naming-a-file
_ILLEGAL_FILE_NAMES = ({'con', 'prn', 'aux', 'nul', 'conin$', 'conout$'} |
                       {f'com{x}' for x in '123456789\xb9\xb2\xb3'} |
                       {f'lpt{x}' for x in '123456789\xb9\xb2\xb3'})
_ILLEGAL_FILE_CHARS = set(r'<>:"/\|?*') | {chr(x) for x in range(32)}

@dataclass(slots=True)
class _ADirBase:
    """Base class for all project folders."""
    zoia_files: list[ZoiaFile] = field(kw_only=True)
    _id_zoia: defaultdict[str, ZoiaFile | None] = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._id_zoia = defaultdict(lambda: None, {
            z.file_path.name: z for z in self.zoia_files})

    def get_zoia_file(self, zoia_name: str) -> ZoiaFile | None:
        """Returns the ZoiaFile matching the specified name or None if such a
        ZoiaFile does not exist in this folder."""
        return self._id_zoia[zoia_name]

    @staticmethod
    def _parse_zoia_files(dir_contents: list[Path], project_folder: Path, /, *,
                          raise_errors: bool, arrow_level: int,
                          warning_msg: str) -> list[ZoiaFile] | None:
        """Parses .zoia files from the specified folder contents. The remaining
        arguments are passed to parse_zoia_file, except for warning_msg, which
        is used for raising a warning if one or more files fails to parse."""
        ret_files = [ZoiaFile.parse_zoia_file(f, project_folder,
                                              raise_errors=raise_errors,
                                              arrow_level=arrow_level)
                     for f in dir_contents if f.suffix == '.zoia']
        if not all(ret_files):
            # This is just a cascading effect of a real error
            log.warning(warning_msg)
            return None
        return sorted(ret_files) # Blows up on None, see above

    @staticmethod
    def _file_names_valid(dir_contents: list[Path], rel_dir_path: Path,
                          raise_errors: bool) -> bool:
        """Checks that the specified folder contents are in lower case and do
        not contain any illegal filenames and returns True. If not, calls
        ps_error with an error message and returns False."""
        no_illegal_fns = True
        for f in dir_contents:
            if f.name != f.name.lower():
                ps_error(f"'{f.name}' is not lowercased", rel_dir_path,
                         raise_errors)
                no_illegal_fns = False
            if f.name.endswith('.'):
                ps_error(f"'{f.name}' ends with a period, which will cause "
                         f"problems on Windows", rel_dir_path, raise_errors)
                no_illegal_fns = False
            if f.stem.lower() in _ILLEGAL_FILE_NAMES:
                ps_error(f"'{f.name}' has a filename that is illegal on "
                         f"Windows", rel_dir_path, raise_errors)
                no_illegal_fns = False
            for ic in _ILLEGAL_FILE_CHARS:
                if ic in f.name:
                    ps_error(f"'{f.name}' contains a character that is "
                             f"illegal on Windows ({ic})", rel_dir_path,
                             raise_errors)
                    no_illegal_fns = False
        return no_illegal_fns
