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
"""This module houses tests related to ast_validator."""
from test.base import ATestParser

import pytest

from exception import ValidationError

class _ATestValidatorPass(ATestParser):
    """Base class for passing validator tests."""
    def test_validator_passes(self):
        """Asserts that parsing and validating the source works."""
        assert self._parse_src()

class _ATestValidatorFail(ATestParser):
    """Base class for failing validator tests."""
    _exp_error: str

    def test_validator_fails(self):
        """Asserts that parsing the source works, but validation fails."""
        try:
            self._parse_src()
            pytest.fail('Validation was supposed to fail, but succeeded '
                        'instead')
        except ValidationError as e:
            assert self._exp_error in str(e)

# Passing tests begin here
class TestHeaderSimple(_ATestValidatorPass):
    """A header with a single-word text fragment as the type should be
    accepted."""
    _test_src = '\\header[fragment]'

# TODO See ast_validator re: if we even want this behavior
class TestHeaderMultiArgStd(_ATestValidatorPass):
    """A header with a valid type and a second standard argument should be
    accepted."""
    _test_src = '\\header[fragment; second arg]'

class TestHeaderMultiArgKwd(_ATestValidatorPass):
    """A header with a valid type and a second keyword argument should be
    accepted."""
    _test_src = '\\header[fragment; arg2 = two]'

# Failing tests begin here
class TestHeaderKwdArg(_ATestValidatorFail):
    """A header with a keyword argument as its first argument should be
    rejected."""
    _test_src = '\\header[type = fragment]'
    _exp_error = ('The first argument passed to \\header must be a standard '
                  'argument')

class TestHeaderMultiStdArg(_ATestValidatorFail):
    """A header with a multi-word text fragment as its first argument should be
    rejected."""
    _test_src = '\\header[fragment one]'
    _exp_error = ('The first argument passed to \\header must be a single '
                  'text fragment containing one word')

class TestHeaderNoTextFragment(_ATestValidatorFail):
    """A header with something other than a text fragment as its first argument
    should be rejected."""
    _test_src = '\\header[@some_alias]'
    _exp_error = ('The first argument passed to \\header must be a single '
                  'text fragment containing one word')
