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
"""This module runs tests that check whether Zoia can correctly detect
filenames that are illegal on Windows."""
import os
from pathlib import Path
from tempfile import TemporaryDirectory

from test.base import ATestProjectFailing

import pytest

from exception import AbstractError

if os.name == 'nt':
    pytest.skip("Skip test_windows_illegal, can't be run on Windows",
                allow_module_level=True)

class _ATestWIFailing(ATestProjectFailing):
    """Base class for failing Windows-illegal file name tests."""
    def _create_files(self, tmp_path: Path):
        """Abstract method that should create the required folder structure
        inside the specified temporary folder.."""
        raise AbstractError()

    def _parse_project(self):
        with TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            self._create_files(tmp_path)
            return self._do_parse_project(tmp_path)

class TestEndsWithPeriod(_ATestWIFailing):
    """Tests that a file with a trailing period causes parsing to fail."""
    _exp_error = ("'test.' ends with a period, which will cause problems on "
                  "Windows")

    def _create_files(self, tmp_path: Path):
        tmp_src = tmp_path / 'src'
        tmp_src.mkdir()
        (tmp_src / 'test.').touch()

class TestIllegalFileName(_ATestWIFailing):
    """Tests that a file with a Windows-illegal filename causes parsing to
    fail."""
    _exp_error = "'aux.zoia' has a filename that is illegal on Windows"

    def _create_files(self, tmp_path: Path):
        tmp_work_path = tmp_path / 'src' / 'work1'
        tmp_work_path.mkdir(parents=True)
        (tmp_work_path / 'aux.zoia').touch()

class TestIllegalChar(_ATestWIFailing):
    """Tests that a file with a Windows-illegal character causes parsing to
    fail."""
    _exp_error = ("'test?.zoia' contains a character that is illegal on "
                  "Windows (?)")

    def _create_files(self, tmp_path: Path):
        tmp_ch_path = tmp_path / 'src' / 'work1' / 'ch1'
        tmp_ch_path.mkdir(parents=True)
        (tmp_ch_path / 'test?.zoia').touch()
