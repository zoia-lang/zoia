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
"""This module houses code shared by multiple project test files."""
from pathlib import Path
from tempfile import mkdtemp
import os
import shutil

from test.base import ATestProjectPassing

import pytest

from exception import AbstractError
from project import Project

class _ACurrentFile(ATestProjectPassing):
    """Base class for tests in the test_project package."""
    _py_file_path = __file__

class _ATestArbitraryZoiaFiles(_ACurrentFile):
    """Base class for tests that want to make use of the arbitrary_zoia_files
    test project."""
    _test_name = 'arbitrary_zoia_files'

class _ATestSimpleStructure(_ACurrentFile):
    """Base class for tests that want to make use of the simple_structure test
    project."""
    _test_name = 'simple_structure'

class _ATestSingleFile(_ACurrentFile):
    """Base class for testing single files like aliases_file and
    dictionary_file."""
    _project: Project
    _file_attr: str
    _file_name: str

    def _cfg_path(self):
        """"""
        raise AbstractError()

    def _assert_file_passes(self):
        single_file = getattr(self._project, self._file_attr)
        # Check is only here to shut linters up
        assert single_file.file_path.suffix == '.zoia'

    def _assert_file_fails(self):
        with pytest.raises(FileNotFoundError):
            single_file = getattr(self._project, self._file_attr)
            single_file.is_main_file() # Call is only here to shut linters up

    def test_proj_passes(self) -> None:
        """Asserts that correct uses of the file pass."""
        self._project = self._parse_project()
        cfg_path = self._cfg_path()
        # Default - absolute path that exists
        self._assert_file_passes()
        # Path relative to the src folder that exists
        cfg_path.option_value = Path(self._file_name)
        self._assert_file_passes()
        # Path relative to the project folder that exists (but doesn't
        # exist relative to the src folder)
        cfg_path.option_value = Path('src') / self._file_name
        self._assert_file_passes()
        # The first chapter's main.zoia file, which must always exist
        cfg_path.option_value = Path('work1') / 'ch1' / 'main.zoia'
        self._assert_file_passes()

    def test_proj_fails(self) -> None:
        """Asserts that various incorrect uses of the file fail."""
        self._project = self._parse_project()
        cfg_path = self._cfg_path()
        p_path = self._project.project_path
        temp_dir = Path(mkdtemp())
        try:
            # Absolute path that doesn't exist
            cfg_path.option_value = temp_dir / self._file_name
            self._assert_file_fails()
        finally:
            shutil.rmtree(temp_dir)
        upper_path = p_path / 'src' / self._file_name.capitalize()
        upper_path.touch()
        try:
            # Invalid Zoia path - not lowercased
            cfg_path.option_value = upper_path
            self._assert_file_fails()
        finally:
            os.remove(upper_path)
        txt_path = p_path / 'src' / self._file_name.replace('.zoia', '.txt')
        txt_path.touch()
        try:
            # Invalid Zoia path - does not end in .zoia
            cfg_path.option_value = txt_path
            self._assert_file_fails()
        finally:
            os.remove(txt_path)
        too_long_dir = p_path / 'src' / 'work1' / 'ch1' / 'foo'
        too_long_dir.mkdir()
        too_long_path = too_long_dir / 'main.zoia'
        too_long_path.touch()
        try:
            # Path is too long - we don't support subfolders in chapters
            cfg_path.option_value = too_long_path
            self._assert_file_fails()
        finally:
            shutil.rmtree(too_long_dir)

    def test_invalid_path_fails(self):
        """Asserts that uses with incorrect chapter or work names fail."""
        self._project = self._parse_project()
        cfg_path = self._cfg_path()
        p_path = self._project.project_path
        invalid_chapter_path = p_path / 'src' / 'work1' / 'cha'
        invalid_chapter_path.mkdir()
        invalid_chapter_zoia_path = invalid_chapter_path / 'main.zoia'
        invalid_chapter_zoia_path.touch()
        try:
            # Invalid chapter path - 'ch' not followed by a number
            cfg_path.option_value = invalid_chapter_zoia_path
            self._assert_file_fails()
        finally:
            shutil.rmtree(invalid_chapter_path)
        invalid_work_path = p_path / 'src' / 'worka'
        invalid_work_path.mkdir()
        invalid_work_zoia_path = invalid_work_path / 'aux.zoia'
        invalid_work_zoia_path.touch()
        invalid_chapter_path = invalid_work_path / 'cha'
        invalid_chapter_path.mkdir()
        invalid_chapter_zoia_path = invalid_chapter_path / 'main.zoia'
        invalid_chapter_zoia_path.touch()
        try:
            # Invalid work path - 'work' not followed by a number
            cfg_path.option_value = invalid_work_zoia_path
            self._assert_file_fails()
            # Invalid chapter path - 'work' not followed by a number
            cfg_path.option_value = invalid_chapter_zoia_path
            self._assert_file_fails()
        finally:
            shutil.rmtree(invalid_work_path)

class _ATestAuxFiles(_ATestSingleFile):
    """Variant of _ATestSingleFile that also tests for aux files in various
    places."""
    def test_aux_file(self):
        """Asserts that aliases_file works correctly for aux files in various
        places too."""
        self._project = self._parse_project()
        cfg_path = self._cfg_path()
        # An auxiliary .zoia file in the src folder
        for f in ('aux.zoia', self._file_name):
            cfg_path.option_value = Path(f)
            self._assert_file_passes()
        # An auxiliary .zoia file in a work
        for w in ('work1', 'work2'):
            cfg_path.option_value = Path(w) / 'aux.zoia'
            self._assert_file_passes()
        # An auxiliary .zoia file in a chapter
        for c in ('ch1', 'ch2'):
            cfg_path.option_value = Path('work1') / c / 'aux.zoia'
            self._assert_file_passes()
