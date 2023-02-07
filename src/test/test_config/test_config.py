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
"""This module runs tests that check whether config parsing works correctly."""
from test.base import ATestProjectFailing, ATestProjectPassing

class _ATestCfgFailing(ATestProjectFailing):
    """Base class for failing config tests."""
    _py_file_path = __file__

class _ATestCfgPassing(ATestProjectPassing):
    """Base class for passing config tests."""
    _py_file_path = __file__

# Failing tests begin here
class TestMissingSesaila(_ATestCfgFailing):
    """A config file which changes the expected name for the aliases file to
    'sesaila.zoia' is present here. That file does not exist (but the default
    'aliases.zoia' does). Ensure we fail expecting the new file."""
    _test_name = 'missing_sesaila'
    _exp_error = "Specified path 'sesaila.zoia' does not exist"

class TestMissingYranoitcid(_ATestCfgFailing):
    """A config file which changes the expected name for the dictionary file to
    'yranoitcid.zoia' is present here. That file does not exist (but the
    default 'dictionary.zoia' does). Ensure we fail expecting the new file."""
    _test_name = 'missing_yranoitcid'
    _exp_error = "Specified path 'yranoitcid.zoia' does not exist"

class TestNoConfigF1(_ATestCfgFailing):
    """A test with no config where aliases.zoia and dictionary.zoia are
    missing."""
    _test_name = 'no_config_f1'
    _exp_error = "Specified path 'aliases.zoia' does not exist"

class TestNoConfigF2(_ATestCfgFailing):
    """A test with no config where aliases.zoia and dictionary.zoia are
    missing."""
    _test_name = 'no_config_f2'
    _exp_error = "Specified path 'dictionary.zoia' does not exist"

class TestNoZoiaExt(_ATestCfgFailing):
    """A Zoia path specified in a config file that doesn't end in .zoia should
    be rejected."""
    _test_name = 'no_zoia_ext'
    _exp_error = "Specified path 'aliases.txt' does not end in '.zoia'"

class TestTOMLSyntaxError1(_ATestCfgFailing):
    """Invalid syntax in a TOML config file should be caught and rejected."""
    _test_name = 'toml_syntax_error_1'
    _exp_error = ("Invalid TOML syntax: Expected ']' at the end of a table "
                  "declaration",
                  'Invalid TOML syntax: Expected "]" at the end of a table '
                  'declaration')

class TestTOMLSyntaxError2(_ATestCfgFailing):
    """Invalid syntax in a TOML config file should be caught and rejected."""
    _test_name = 'toml_syntax_error_2'
    _exp_error = ("Invalid TOML syntax: Illegal character '\\n'",
                  'Invalid TOML syntax: Illegal character "\\n"')

class TestUpperPath(_ATestCfgFailing):
    """A src-relative path specified in a config file that isn't entirely
    lowercased should be rejected."""
    _test_name = 'upper_path'
    _exp_error = "'Aliases.zoia' is not lowercased"

# Passing tests begin here
class TestNoConfigP(_ATestCfgPassing):
    """Similar to test_project_structure.TestSimpleStructure. No config means
    the default paths src/aliases.zoia and src/dictionary.zoia have to
    exist."""
    _test_name = 'no_config_p'

class TestPresentSesailaYranoitcid(_ATestCfgPassing):
    """A config file which combines the changes from TestMissingSesaila and
    TestMissingYranoitcid is present here, but the two files are now present
    (and the default files missing). Ensure that this passes."""
    _test_name = 'present_sesaila_yranoitcid'

class TestUnknownSectionsOptions(_ATestCfgPassing):
    """Unknown sections and options should not make parsing fail. They do
    generate warnings, but we have no way to test for those right now (we need
    a way to test our log framework first)."""
    _test_name = 'unknown_sections_options'
