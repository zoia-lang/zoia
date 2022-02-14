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
from utils import ps_error

@dataclass(slots=True)
class Project:
    """The Project class oversees all operations on a project written in
    Zoia. To obtain a Project instance, use the parse_project classmethod."""
    series: Series
    config: ZoiaToml

    @classmethod
    def parse_project(cls, project_folder: Path, /, *,
                      raise_errors: bool = False):
        """Parses a project at the specified path."""
        log.info(f'Wanted project folder is $fWl${project_folder}$R$')
        # Resolve the path first so all later operations can use full paths and
        # ensure it exists while we're at it
        try:
            project_folder = project_folder.resolve(strict=True)
        except FileNotFoundError as e:
            return ps_error('No project folder found', Path(''),
                            raise_errors, orig_error=e)
        log.info(f'Actual project folder is $fWl${project_folder}$R$')
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
        return cls(parsed_series, parsed_config)
