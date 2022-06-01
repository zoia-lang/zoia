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
"""This module houses tests related to the Zoia parser."""
from test.base import ATestParser

import pytest

from exception import ParsingError

# ==== Expect-Success Tests ===================================================
class _ATestParserPass(ATestParser):
    """Base class for parser tests that are expected to succeed."""
    def test_parser(self) -> None:
        """Runs the actual test, ensuring that the Zoia source specified in
        this class' _test_src field is parsed successfully."""
        assert self._parse_src()

class TestAcceptsHeader(_ATestParserPass):
    """A simple header should be accepted."""
    _test_src = '\\header[foobar]'

class TestAcceptsFragments(_ATestParserPass):
    """Bare text fragments should be accepted."""
    _test_src = 'foo bar qux'

class TestAcceptsAliases(_ATestParserPass):
    """Bare aliases should be accepted."""
    _test_src = '@a1 @a2 @a3'

class TestAcceptsCommandsNA(_ATestParserPass):
    """Commands without arguments should be accepted."""
    _test_src = '\\cmd1 \\cmd2 \\cmd3'

class TestAcceptsCommandsSA(_ATestParserPass):
    """Commands with a single argument should be accepted."""
    _test_src = '\\cmd1[foo] \\cmd2[bar] \\cmd3[qux]'

class TestAcceptsCommandsMA(_ATestParserPass):
    """Commands with multiple arguments should be accepted."""
    _test_src = '\\cmd[foo; bar; qux] \\a[b; c]'

class TestAcceptsCommandKwd(_ATestParserPass):
    """Commands with keyword arguments should be accepted."""
    _test_src = '\\cmd[a = b; c = d; e]'

class TestAcceptsCommandBar(_ATestParserPass):
    """Commands explicitly ended with a vertical bar should be accepted."""
    _test_src = '\\cmd1|\\cmd2|\\cmd3|'

class TestAcceptsCommandArgBar(_ATestParserPass):
    """Commands with arguments may be ended with a bar as well and that should
    be accepted (though this is wholly useless - the ']' already covers the
    function of the bar)."""
    _test_src = '\\cmd1[a; b = c]|\\cmd2|'

class TestAcceptsMixedLEs(_ATestParserPass):
    """Any mix of line elements should be accepted."""
    _test_src = 'foo \\bar[a;b=c] @qux'

class TestAcceptsComment1(_ATestParserPass):
    """A whole-line comment should be accepted."""
    _test_src = '# This is a whole-line comment'

class TestAcceptsComment2(_ATestParserPass):
    """A comment at the end of a line should be accepted."""
    _test_src = 'foo \\bar @qux # All three types of line element'

class TestAcceptsUnicode(_ATestParserPass):
    """Unicode characters should be accepted."""
    _test_src = '\\cömmänd[😀] 警告'

class TestAcceptsMarkup(_ATestParserPass):
    """Emphasized markup should be accepted."""
    _test_src = 'This is *em1*, **em2** and ***em3*** text.'

class TestAcceptsMarkupComplex(_ATestParserPass):
    """Markup that contains aliases and commands should be accepted."""
    _test_src = 'This is *markup with @aliases and \\commands*'

class TestAcceptsTrailingSpacesEm1(_ATestParserPass):
    """Em1 markup that has trailing spaces should be accepted."""
    _test_src = '*trailing spaces *'

class TestAcceptsTrailingSpacesEm2(_ATestParserPass):
    """Em2 markup that has trailing spaces should be accepted."""
    _test_src = '**trailing spaces **'

class TestAcceptsTrailingSpacesEm3(_ATestParserPass):
    """Em3 markup that has trailing spaces should be accepted."""
    _test_src = '***trailing spaces ***'

# ==== Expect-Fail Tests ======================================================
class _ATestParserFail(ATestParser):
    """Base class for parser tests that are expected to fail."""
    def test_parser(self) -> None:
        """Runs the actual test, ensuring that parsing the Zoia source
        specified in this class' _test_src variable fails."""
        # Note that this error's message is not under our control (comes from
        # ANTLR), so we don't want to check the message
        with pytest.raises(ParsingError):
            self._parse_src()

class TestRejectsNoHeader(_ATestParserFail):
    """Zoia files without a header should be rejected."""
    _test_src = 'foo\n'
    _do_fixups = False

class TestRejectsLackingNL(_ATestParserFail):
    """Zoia files without a terminating newline should be rejected."""
    _test_src = '\\header[foo]\n\nbar'
    _do_fixups = False

class TestRejectsEmptyArgList(_ATestParserFail):
    """Argument lists with no arguments should be rejected."""
    _test_src = '\\cmd[]'

class TestRejectsKwdArgWithoutValue1(_ATestParserFail):
    """Keyword arguments without a value after the '=' should be rejected."""
    _test_src = '\\cmd[a =]'

class TestRejectsKwdArgWithoutValue2(_ATestParserFail):
    """Keyword arguments without a value after the '=' should be rejected."""
    _test_src = '\\cmd[a =; c]'

class TestRejectsUnclosedEm1(_ATestParserFail):
    """Unclosed em1 markup should be rejected."""
    _test_src = '*this is em1 markup'

class TestRejectsUnclosedEm2(_ATestParserFail):
    """Unclosed em2 markup should be rejected."""
    _test_src = '**this is em2 markup'

class TestRejectsPartiallyClosedEm2(_ATestParserFail):
    """Em2 markup that is only closed with one asterisk should be rejected."""
    _test_src = '**this is em2 markup*'

class TestRejectsUnclosedEm3(_ATestParserFail):
    """Unclosed em3 markup should be rejected."""
    _test_src = '***this is em3 markup'

class TestRejectsPartiallyClosedEm31(_ATestParserFail):
    """Em3 markup that is only closed with one asterisk should be rejected."""
    _test_src = '***this is em3 markup*'

class TestRejectsPartiallyClosedEm32(_ATestParserFail):
    """Em3 markup that is only closed with two asterisks should be rejected."""
    _test_src = '***this is em3 markup**'

class TestRejectsLeadingSpacesEm1(_ATestParserFail):
    """Em1 markup that has leading spaces should be rejected."""
    _test_src = '* leading spaces*'

class TestRejectsLeadingSpacesEm2(_ATestParserFail):
    """Em2 markup that has leading spaces should be rejected."""
    _test_src = '** leading spaces**'

class TestRejectsLeadingSpacesEm3(_ATestParserFail):
    """Em3 markup that has leading spaces should be rejected."""
    _test_src = '*** leading spaces***'

class TestRejectsKwdAlias(_ATestParserFail):
    """Aliases should be rejected when used as a keyword."""
    _test_src = '\\cmd[@foo = bar]'

class TestRejectsKwdCommand(_ATestParserFail):
    """Commands should be rejected when used as a keyword."""
    _test_src = '\\cmd[\\foo = bar]'

class TestRejectsKwdTextFragment(_ATestParserFail):
    """Text fragments (text fragments containing more than one word, that is)
    should be rejected when used as a keyword."""
    _test_src = '\\cmd[foo qux = bar]'

class TestRejectsKwdEm1(_ATestParserFail):
    """Em1 text should be rejected when used as a keyword."""
    _test_src = '\\cmd[*foo* = bar]'

class TestRejectsKwdEm2(_ATestParserFail):
    """Em2 text should be rejected when used as a keyword."""
    _test_src = '\\cmd[**foo** = bar]'

class TestRejectsKwdEm3(_ATestParserFail):
    """Em3 text should be rejected when used as a keyword."""
    _test_src = '\\cmd[***foo*** = bar]'

class TestRejectsSpaceArg(_ATestParserFail):
    """An argument may not consist entirely of spaces."""
    _test_src = '\\cmd[ ]'
