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
"""This module runs tests that check whether dictionary_file is correctly
implemented."""
from test.test_project.base import _ATestArbitraryZoiaFiles, \
    _ATestSimpleStructure, _ATestSingleFile, _ATestAncFiles

class _ATestDictionary(_ATestSingleFile):
    """Base class for testing dictionary_file."""
    _file_attr = 'dictionary_file'
    _file_name = 'dictionary.zoia'

    def _cfg_path(self):
        return self._project.config.dictionary.src_path

class TestArbitraryZoiaFilesDictionary(_ATestArbitraryZoiaFiles,
                                       _ATestDictionary, _ATestAncFiles):
    """arbitrary_zoia_file should implement dictionary_file correctly."""

class TestSimpleStructureDictionary(_ATestSimpleStructure, _ATestDictionary):
    """simple_structure should implement dictionary_file correctly."""
