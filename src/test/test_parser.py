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

class TestAcceptsSpaceArg(_ATestParserPass):
    """An argument may be nothing but spaces. This is unintuitive at first, but
    comes as a side effect of text fragments potentially being nothing but
    spaces."""
    _test_src = '\\cmd[ ]'

class TestAcceptsUnicode(_ATestParserPass):
    """Unicode characters should be accepted."""
    _test_src = '\\cömmänd[😀] 警告'

class TestAcceptsMarkup(_ATestParserPass):
    """Bold, italic and bold-italic markup should be accepted."""
    _test_src = 'This is *italic*, **bold** and ***bold-italic*** text.'

class TestAcceptsMarkupComplex(_ATestParserPass):
    """Markup that contains aliases and commands should be accepted."""
    _test_src = 'This is *markup with @aliases and \\commands*'

# ==== Expect-Fail Tests ======================================================
class _ATestParserFail(ATestParser):
    """Base class for parser tests that are expected to fail."""
    def test_parser(self) -> None:
        """Runs the actual test, ensuring that parsing the Zoia source
        specified in this class' _test_src variable fails."""
        try:
            self._parse_src()
            pytest.fail('Parsing was supposed to fail, but succeeded instead')
        except ParsingError:
            pass

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

class TestRejectsUnclosedBold(_ATestParserFail):
    """Unclosed bold markup should be rejected."""
    _test_src = '**this is bold markup'

class TestRejectsPartiallyClosedBold(_ATestParserFail):
    """Bold markup that is only closed with one asterisk should be rejected."""
    _test_src = '**this is bold markup*'

class TestRejectsUnclosedBoldItalic(_ATestParserFail):
    """Unclosed bold-italic markup should be rejected."""
    _test_src = '***this is bold-italic markup'

class TestRejectsPartiallyClosedBoldItalic1(_ATestParserFail):
    """Bold-italic markup that is only closed with one asterisk should be
    rejected."""
    _test_src = '***this is bold-italic markup*'

class TestRejectsPartiallyClosedBoldItalic2(_ATestParserFail):
    """Bold-italic markup that is only closed with one asterisk should be
    rejected."""
    _test_src = '***this is bold-italic markup**'

class TestRejectsUnclosedItalic(_ATestParserFail):
    """Unclosed italic markup should be rejected."""
    _test_src = '*this is italic markup'

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

class TestRejectsKwdItalic(_ATestParserFail):
    """Italic text should be rejected when used as a keyword."""
    _test_src = '\\cmd[*foo* = bar]'

class TestRejectsKwdBold(_ATestParserFail):
    """Bold text should be rejected when used as a keyword."""
    _test_src = '\\cmd[**foo** = bar]'

class TestRejectsKwdBoldItalic(_ATestParserFail):
    """Bold-italic text should be rejected when used as a keyword."""
    _test_src = '\\cmd[***foo*** = bar]'
