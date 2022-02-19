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
"""Implements the main Project class that oversees all operations on a project
written in Zoia."""
from dataclasses import dataclass
from pathlib import Path

import log
from project.config import ZoiaToml
from project.series import Series
from project.zoia_file import ZoiaFile
from utils import ps_error, valid_zoia_path

@dataclass(slots=True)
class Project:
    """The Project class oversees all operations on a project written in
    Zoia. To obtain a Project instance, use the parse_project classmethod."""
    project_path: Path
    series: Series
    config: ZoiaToml

    def find_zoia_file(self, file_path: Path) -> ZoiaFile | None:
        """Finds a ZoiaFile by its path. The path may be relative to the src
        folder, relative to the project folder, or absolute. Returns None if
        the file could not be found."""
        # First make sure the path exists and make it absolute
        try:
            if not file_path.is_absolute():
                # Not absolute, so relative to either the src or project folder
                altered_path = self.project_path / 'src' / file_path
                if not altered_path.exists():
                    altered_path = self.project_path / file_path
            else:
                # Already absolute, just check that it exists
                altered_path = file_path
            file_path = altered_path.resolve(strict=True)
        except FileNotFoundError:
            return None
        # Then relativize it and make sure it's a valid Zoia path
        rel_path = self.relativize(file_path, strip_src=True)
        if not valid_zoia_path(str(rel_path)):
            return None
        # Then we can parse it by parts and look for the file
        #path_parts =
        match rel_path.parts:
            case (zoia_name,): # a.zoia
                return self.series.get_zoia_file(zoia_name)
            case (work_name, zoia_name): # work1/a.zoia
                work = self.series.get_work(work_name)
                # PEP 505 or something similar sorely missed
                if work is None:
                    return None
                return work.get_zoia_file(zoia_name)
            case (work_name, chapter_name, zoia_name): # work1/ch1/a.zoia
                work = self.series.get_work(work_name)
                if work is None:
                    return None
                chapter = work.get_chapter(chapter_name)
                if chapter is None:
                    return None
                return chapter.get_zoia_file(zoia_name)
            case _: # Some kind of unsupported location
                return None

    def _find_zoia_or_raise(self, file_path: Path) -> ZoiaFile:
        """Internal version of find_zoia_file that raises an error if the file
        could not be found. Meant to be used for required Zoia files, e.g.
        aliases.zoia and dictionary.zoia."""
        ret_zoia = self.find_zoia_file(file_path)
        if ret_zoia is None:
            raise FileNotFoundError(f"Failed to find required Zoia file "
                                    f"'{file_path}'")
        return ret_zoia

    def relativize(self, absolute_path: Path, /, *,
                   strip_src: bool = False) -> Path:
        """Returns a version of the specified absolute path relative to the
        path at which this project is located. If the specified path is not
        absolute or not relative to this project, a ValueError is raised.

        :param absolute_path: The path to relativize.
        :param strip_src: If True, remove the leading 'src' from the resulting
            relative path. In other words, relativize to the src path instead
            of the project path."""
        if not absolute_path.is_absolute():
            raise ValueError('relativize needs an absolute path')
        rel_target = self.project_path
        if strip_src:
            rel_target /= 'src'
        return absolute_path.relative_to(rel_target)

    @property
    def aliases_file(self) -> ZoiaFile:
        """Returns the ZoiaFile object corresponding to the aliases file. This
        takes any changes made by the config file into account."""
        return self._find_zoia_or_raise(
            self.config.aliases.src_path.option_value)

    @property
    def dictionary_file(self) -> ZoiaFile:
        """Returns the ZoiaFile object corresponding to the dictionary file.
        This takes any changes made by the config file into account."""
        return self._find_zoia_or_raise(
            self.config.dictionary.src_path.option_value)

    @classmethod
    def parse_project(cls, project_folder: Path, /, *,
                      raise_errors: bool = False):
        """Parses a project at the specified path."""
        # Resolve the path first so all later operations can use full paths and
        # ensure it exists while we're at it
        try:
            project_folder = project_folder.resolve(strict=True)
        except FileNotFoundError as e:
            return ps_error('Project folder not found',
                            project_folder.resolve(), raise_errors,
                            orig_error=e)
        log.info(f'Project folder is $fWl${project_folder}$R$')
        # Parse the series folder 'src', which must exist
        series_rel = 'src'
        series_folder = project_folder / series_rel
        try:
            series_folder = series_folder.resolve(strict=True)
        except FileNotFoundError as e:
            return ps_error(f"No '{series_rel}' folder found", Path(''),
                            raise_errors, orig_error=e)
        parsed_series = Series.parse_series(series_folder, project_folder,
                                     raise_errors=raise_errors)
        if parsed_series is None:
            log.warning(f'Failed to parse project due to errors when parsing '
                        f'$fYl${series_rel}$R$')
            return None
        # Parse the config file 'zoia.toml', if it exists
        zoia_toml_rel = 'zoia.toml'
        parsed_config = ZoiaToml.parse_zoia_toml(
            project_folder / zoia_toml_rel, project_folder,
            raise_errors=raise_errors)
        if parsed_config is None:
            log.warning(f'Failed to parse project due to errors when parsing '
                        f'$fCl${zoia_toml_rel}$R$')
            return None
        return cls(project_folder, parsed_series, parsed_config)
