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
"""This module runs the actual project tests on the ."""
from pytest import fail

from exception import ProjectStructureError
from paths import ZPath
from project import Series

# Utilities
def _get_src_path(test_name: str) -> ZPath:
    """Retrieves the full path to the 'src' folder for the test with the
    specified directory name."""
    return ZPath(__file__).parent.resolve(strict=True) / test_name / 'src'

class _ATestProject:
    _test_name: str

class _ATestProjectPassing(_ATestProject):
    """Base class for passing project directory tests."""
    def test_proj_passes(self) -> None:
        """Asserts that the series located at this test directory parses
        successfully."""
        assert Series.parse_series(_get_src_path(self._test_name))

class _ATestProjectFailing(_ATestProject):
    """Base class for failing project directory tests."""
    _exp_error: str

    def test_proj_fails(self) -> None:
        """Asserts that the series located at the specified test directory does
        not parse successfully."""
        try:
            Series.parse_series(_get_src_path(self._test_name))
            fail('Parsing was supposed to fail, but succeeded instead')
        except ProjectStructureError as e:
            assert self._exp_error in str(e)

# Actual tests begin here
class TestEmptySeries(_ATestProjectFailing):
    """An empty series folder should not be accepted."""
    _test_name = 'empty_series'
    _exp_error = "The 'src' folder must contain one or more works"

class TestNoIndex1Work(_ATestProjectFailing):
    """A series without a work with index 1 should not be accepted."""
    _test_name = 'no_index_1_work'
    _exp_error = 'The first work in a series must have index 1'
