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
"""This module runs tests that check whether project structures are being
parsed correctly."""
from pathlib import Path

import pytest

from exception import ProjectStructureError
from project import Series

# Utilities
def _get_src_path(test_name: str) -> Path:
    """Retrieves the full path to the 'src' folder for the test with the
    specified directory name."""
    return Path(__file__).parent.resolve(strict=True) / test_name / 'src'

class _ATestProject:
    _test_name: str

class _ATestProjectPassing(_ATestProject):
    """Base class for passing project directory tests."""
    def test_proj_passes(self) -> None:
        """Asserts that the series located at this test directory parses
        successfully."""
        assert Series.parse_series(_get_src_path(self._test_name),
                                   raise_errors=True)

class _ATestProjectFailing(_ATestProject):
    """Base class for failing project directory tests."""
    _exp_error: str

    def test_proj_fails(self) -> None:
        """Asserts that the series located at the specified test directory does
        not parse successfully."""
        try:
            Series.parse_series(_get_src_path(self._test_name),
                                raise_errors=True)
            pytest.fail('Parsing was supposed to fail, but succeeded instead')
        except ProjectStructureError as e:
            assert self._exp_error in str(e)

# Failing tests begin here
class TestEmptySeries(_ATestProjectFailing):
    """An empty series folder should be rejected."""
    _test_name = 'empty_series'
    _exp_error = "The 'src' folder must contain one or more works"

class TestEmptyWork(_ATestProjectFailing):
    """An empty work folder should be rejected."""
    _test_name = 'empty_work'
    _exp_error = 'Work folders must contain one or more chapters'

class TestIncontiguousChapters(_ATestProjectFailing):
    """A work with chapters whose indices are not contiguous should be
    rejected."""
    _test_name = 'incontiguous_chapters'
    _exp_error = 'Chapter indices must form a contiguous sequence'

class TestIncontiguousWorks(_ATestProjectFailing):
    """A series with works whose indices are not contiguous should be
    rejected."""
    _test_name = 'incontiguous_works'
    _exp_error = 'Work indices must form a contiguous sequence'

class TestNoIndex1Chapter(_ATestProjectFailing):
    """A work without a chapter with index should be rejected."""
    _test_name = 'no_index_1_chapter'
    _exp_error = 'The first chapter in a work must have index 1'

class TestNoIndex1Work(_ATestProjectFailing):
    """A series without a work with index 1 should be rejected."""
    _test_name = 'no_index_1_work'
    _exp_error = 'The first work in a series must have index 1'

class TestNoMainFile(_ATestProjectFailing):
    """A chapter without a main file should be rejected."""
    _test_name = 'no_main_file'
    _exp_error = "Each chapter must contain a 'main.zoia' file"

class TestNoSrc(_ATestProjectFailing):
    """A project without a src folder (i.e. without a series) should be
    rejected."""
    _test_name = 'no_src'
    _exp_error = "No 'src' folder found"

class TestUpperChapter(_ATestProjectFailing):
    """A project with a non-lowercased chapter folder should be rejected."""
    _test_name = 'upper_chapter'
    _exp_error = "'Ch1' is not lowercased"

class TestUpperFile(_ATestProjectFailing):
    """A project with a non-lowercased chapter folder should be rejected."""
    _test_name = 'upper_file'
    _exp_error = "'Main.zoia' is not lowercased"

class TestUpperSrc(_ATestProjectFailing):
    """A project with a non-lowercased 'src' folder should be rejected."""
    _test_name = 'upper_src'
    _exp_error = "No 'src' folder found"

class TestUpperWork(_ATestProjectFailing):
    """A project with a non-lowercased work folder should be rejected."""
    _test_name = 'upper_work'
    _exp_error = "'Work1' is not lowercased"

# Passing tests begin here
class TestSimpleStructure(_ATestProjectPassing):
    """A single work with a single chapter and a valid main.zoia file should be
    accepted."""
    _test_name = 'simple_structure'
