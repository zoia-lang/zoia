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
"""This package houses tests related to the project package."""
from pytest import fail

from exception import ProjectStructureError
from paths import ZPath
from project import Series

def _get_src_path(curr_file: str) -> ZPath:
    """Retrieves the full path to the 'src' folder for this test from the
    specified __file__ value."""
    return ZPath(curr_file).parent.resolve(strict=True) / 'src'

def assert_series_parses(curr_file: str) -> None:
    """Asserts that the series located in the parent package of the specified
    __file__ parses successfully."""
    assert Series.parse_series(_get_src_path(curr_file))

def assert_series_fails(curr_file: str, expected_error_part: str) -> None:
    """Asserts that the series located in the parent package of the specified
    __file__ does not parse successfully. expected_error_part must be part of
    the error message you expect to see."""
    try:
        Series.parse_series(_get_src_path(curr_file))
        fail('Parsing was supposed to fail, but succeeded instead')
    except ProjectStructureError as e:
        assert expected_error_part in str(e)
