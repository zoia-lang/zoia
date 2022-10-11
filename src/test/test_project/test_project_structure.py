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
from test.base import ATestProjectFailing
from test.test_project.base import _ATestArbitraryZoiaFiles, \
    _ATestSimpleStructure

class _ATestPSFailing(ATestProjectFailing):
    """Base class for failing project structure tests. Needed since these don't
    derive from _ACurrentFile (yet)."""
    _py_file_path = __file__

# Failing tests begin here
class TestEmptySeries(_ATestPSFailing):
    """An empty series folder should be rejected."""
    _test_name = 'empty_series'
    _exp_error = "The 'src' folder must contain one or more works"

class TestEmptyWork(_ATestPSFailing):
    """An empty work folder should be rejected."""
    _test_name = 'empty_work'
    _exp_error = 'Work folders must contain one or more chapters'

class TestIncontiguousChapters(_ATestPSFailing):
    """A work with chapters whose indices are not contiguous should be
    rejected."""
    _test_name = 'incontiguous_chapters'
    _exp_error = 'Chapter indices must form a contiguous sequence'

class TestIncontiguousWorks(_ATestPSFailing):
    """A series with works whose indices are not contiguous should be
    rejected."""
    _test_name = 'incontiguous_works'
    _exp_error = 'Work indices must form a contiguous sequence'

class TestNoIndex1Chapter(_ATestPSFailing):
    """A work without a chapter with index should be rejected."""
    _test_name = 'no_index_1_chapter'
    _exp_error = 'The first chapter in a work must have index 1'

class TestNoIndex1Work(_ATestPSFailing):
    """A series without a work with index 1 should be rejected."""
    _test_name = 'no_index_1_work'
    _exp_error = 'The first work in a series must have index 1'

class TestNoMainFile(_ATestPSFailing):
    """A chapter without a main file should be rejected."""
    _test_name = 'no_main_file'
    _exp_error = "Each chapter must contain a 'main.zoia' file"

class TestNoProject(_ATestPSFailing):
    """A project without a project folder (i.e. one where the target path
    points to a non-existent folder) should be rejected."""
    _test_name = 'no_project'
    _exp_error = "Project folder not found"

class TestNoSrc(_ATestPSFailing):
    """A project without a src folder (i.e. without a series) should be
    rejected."""
    _test_name = 'no_src'
    _exp_error = "'src' folder could not be found"

class TestUpperChapter(_ATestPSFailing):
    """A project with a non-lowercased chapter folder should be rejected."""
    _test_name = 'upper_chapter'
    _exp_error = "'Ch1' is not lowercased"

class TestUpperFile(_ATestPSFailing):
    """A project with a non-lowercased chapter folder should be rejected."""
    _test_name = 'upper_file'
    _exp_error = "'Main.zoia' is not lowercased"

class TestUpperSrc(_ATestPSFailing):
    """A project with a non-lowercased 'src' folder should be rejected."""
    _test_name = 'upper_src'
    _exp_error = "Found a 'src' folder at 'Src', but it is not lowercased"

class TestUpperWork(_ATestPSFailing):
    """A project with a non-lowercased work folder should be rejected."""
    _test_name = 'upper_work'
    _exp_error = "'Work1' is not lowercased"

# Passing tests begin here
class TestArbitraryZoiaFilesParses(_ATestArbitraryZoiaFiles):
    """arbitrary_zoia_file should parse."""

class TestSimpleStructureParses(_ATestSimpleStructure):
    """simple_structure should parse."""
