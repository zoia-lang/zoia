# -*- coding: utf-8 -*-
#
# GPL License and Copyright Notice ============================================
#
#   This file is part of Zoia, a language for writing fiction.
#   Copyright (C) 2021 Infernio
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
import pytest
from antlr4 import BailErrorStrategy, CommonTokenStream, InputStream
from antlr4.error.Errors import ParseCancellationException

from grammar import zoiaLexer, zoiaParser

# Some common code for both expect-success and expect-fail tests
_default_header = '\\header[fragment]\n\n'

class _ATestParser:
    _test_src: str
    _do_fixups: bool = True

    def _setup_parser(self):
        # For convenience, the \header part can be elided in tests
        if self._do_fixups and '\\header' not in self._test_src:
            self._test_src = _default_header + self._test_src
        # For convenience, an ending \n can be elided in tests
        if self._do_fixups and not self._test_src.endswith('\n'):
            self._test_src += '\n'
        ins = InputStream(self._test_src)
        lexer = zoiaLexer(ins)
        tokens = CommonTokenStream(lexer)
        parser = zoiaParser(tokens)
        # Ugh, why isn't there an API for this?
        parser._errHandler = BailErrorStrategy()
        return parser

# ==== Expect-Success Tests ===================================================
class _ATestParserPass(_ATestParser):
    """Base class for parser tests that are expected to succeed."""
    def test_parser(self):
        self._setup_parser().zoiaFile()

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


# ==== Expect-Fail Tests ======================================================
class _ATestParserFail(_ATestParser):
    """Base class for parser tests that are expected to fail."""
    def test_parser(self):
        try:
            parser = self._setup_parser()
            # We're expecting to fail, don't print to stdout
            parser.removeErrorListeners()
            parser.zoiaFile()
            pytest.fail('Parsing was supposed to fail, but succeeded instead')
        except ParseCancellationException:
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
