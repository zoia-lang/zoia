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
from ast_nodes import ZoiaFileNode
from zoia_processor import process_zoia_string

_DEFAULT_HEADER = '\\header[fragment]\n\n'

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
