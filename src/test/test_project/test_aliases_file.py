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
"""This module runs tests that check whether aliases_file is correctly
implemented."""
from test.test_project.base import _ATestArbitraryZoiaFiles, \
    _ATestSimpleStructure, _ATestSingleFile, _ATestAncFiles

class _ATestAliases(_ATestSingleFile):
    """Base class for testing aliases_file."""
    _file_attr = 'aliases_file'
    _file_name = 'aliases.zoia'

    def _cfg_path(self):
        return self._project.config.aliases.src_path

class TestArbitraryZoiaFilesAliases(_ATestArbitraryZoiaFiles, _ATestAliases,
                                    _ATestAncFiles):
    """arbitrary_zoia_file should implement aliases_file correctly."""

class TestSimpleStructureAliases(_ATestSimpleStructure, _ATestAliases):
    """simple_structure should implement aliases_file correctly."""
