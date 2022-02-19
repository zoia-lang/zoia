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
"""This module houses code shared by multiple test files."""
from pathlib import Path

import pytest

from ast_nodes import ZoiaFileNode
from exception import ProjectStructureError
from project import Project
from zoia_processor import process_zoia_string

_DEFAULT_HEADER = '\\header[fragment]\n\n'

def mks(*lines):
    """Makes a Zoia string using the specified lines (with a header
    prepended)."""
    return _DEFAULT_HEADER + '\n'.join(lines) + '\n'

class ATestParser:
    """Base class for all tests that need to parse Zoia code."""
    _test_src: str
    _do_fixups: bool = True
    # Set in _parse_src if a fixup to the header was performed
    _added_header: bool = False

    def _parse_src(self, test_src: str = None) -> ZoiaFileNode:
        """Creates a new zoiaParser instance with the specified source code
        (falling back to self._test_src if it is None)."""
        if test_src is None:
            test_src = self._test_src
        # For convenience, the \header part can be elided in tests
        if self._do_fixups and '\\header' not in test_src:
            self._added_header = True
            test_src = _DEFAULT_HEADER + test_src
        # For convenience, an ending \n can be elided in tests
        if self._do_fixups and not test_src.endswith('\n'):
            test_src += '\n'
        return process_zoia_string(test_src, f"<{self.__class__.__name__}>")

def _get_proj_path(test_name: str, py_file_path: str) -> Path:
    """Retrieves the full path to the project folder for the test with the
    specified directory name."""
    return Path(py_file_path).parent.resolve(strict=True) / test_name

class _ATestProject:
    """Base class for tests that need to parse a project."""
    _test_name: str
    _py_file_path: str

    def _parse_project(self):
        return Project.parse_project(_get_proj_path(self._test_name,
                                                    self._py_file_path),
                                     raise_errors=True)

class ATestProjectPassing(_ATestProject):
    """Base class for passing tests that need to parse a project."""
    def test_proj_passes(self) -> None:
        """Asserts that the series located at this test directory parses
        successfully."""
        assert self._parse_project() is not None

class ATestProjectFailing(_ATestProject):
    """Base class for failing tests that need to parse a project."""
    _exp_error: str

    def test_proj_fails(self) -> None:
        """Asserts that the series located at the specified test directory does
        not parse successfully."""
        try:
            self._parse_project()
            pytest.fail('Parsing was supposed to fail, but succeeded instead')
        except ProjectStructureError as e:
            assert self._exp_error in str(e)
