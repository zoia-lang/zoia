# -*- coding: utf-8 -*-
#
# GPL License and Copyright Notice ============================================
#
#   This file is part of Zoia, a language for writing fiction.
#   Copyright (C) 2021-2023 Infernio
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
"""This module runs tests that check whether relativize is correctly
implemented."""
from pathlib import Path
from tempfile import gettempdir

from test.base import ATestProjectPassing
from test.test_project.base import _ATestArbitraryZoiaFiles, \
    _ATestSimpleStructure

import pytest

class _ATestRelativize(ATestProjectPassing):
    """Base class for passing project structure tests that also want to test
    their relativize implementation."""
    def test_proj_passes(self) -> None:
        """Asserts that relativize is correctly implemented."""
        project = self._parse_project()
        p_rel = project.relativize
        # Simple passing tests
        p_path = project.project_path
        assert p_rel(p_path) == Path('')
        assert p_rel(p_path / 'src') == Path('src')
        assert p_rel(p_path / 'src', strip_src=True) == Path('')
        assert p_rel(p_path / 'foo' / 'bar') == Path('foo') / 'bar'
        assert p_rel(p_path / 'src' / 'foo' / 'bar',
                     strip_src=True) == Path('foo') / 'bar'
        # Paths that cannot be relativized are rejected by raising an error
        tmp_path = Path(gettempdir()) / 'foo'
        # Note that this error is not under our control (comes from Python), so
        # we don't want to check the message
        with pytest.raises(ValueError):
            p_rel(tmp_path)
        # Already relative paths are rejected by raising an error
        rel_path = Path('foo') / 'bar' / 'qux'
        with pytest.raises(ValueError) as exc_info:
            p_rel(rel_path)
        assert str(exc_info.value) == 'relativize needs an absolute path'

class TestArbitraryZoiaFilesRelativize(_ATestArbitraryZoiaFiles,
                                       _ATestRelativize):
    """arbitrary_zoia_file should implement relativize correctly."""

class TestSimpleStructureRelativize(_ATestSimpleStructure, _ATestRelativize):
    """simple_structure should implement relativize correctly."""
