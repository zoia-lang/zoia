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
"""This module houses tests related to canonical representations."""
from test.base import ATestParser

class ATestCanonicalRepr(ATestParser):
    """Base class for tests that check canonical representations."""
    _do_fixups = False
    _test_rep: str

    def _get_canonical(self, test_src: str) -> str:
        return self._parse_src(test_src).canonical()

    def test_parse_src(self) -> None:
        """Parsing the source should produce the canonical representation."""
        assert self._get_canonical(self._test_src) == self._test_rep

    def test_parse_repr(self) -> None:
        """Parsing the canonical representation should produce the canonical
        representation itself again."""
        assert self._get_canonical(self._test_rep) == self._test_rep


# Some helpers for easily making sources and canonical representations
def _mk_shared(*lines) -> str:
    """Adds newlines to the specified lines and adds a trailing one to the
    end."""
    return '\n'.join(lines) + '\n'

_COMMON_S = _mk_shared('\\header[foo]') + '\n'
_COMMON_R = _mk_shared('\\header[',
                       '    foo;',
                       ']',
                       '')

def mks(*lines):
    """Makes a source 'file' using the specified lines (with a header
    prepended)."""
    return _COMMON_S + _mk_shared(*lines)
def mkr(*lines):
    """Makes a canonical representation 'file' using the specified lines (with
    a header prepended)."""
    return _COMMON_R + _mk_shared(*lines)

class TestHeaderCR(ATestCanonicalRepr):
    """Headers should be formatted like commands (see TestCommandWithArgCR)."""
    _test_src = mks()
    _test_rep = mkr()

class TestCommentCR(ATestCanonicalRepr):
    """Comments should be gone (since they get stripped during parsing)."""
    _test_src = mks('This is a line# with a comment')
    _test_rep = mkr('This is a line')

class TestTextFragmentCR(ATestCanonicalRepr):
    """Text fragments should be reproduced verbatim, including all spaces."""
    _test_src = mks('This   is a text  fragment')
    _test_rep = mkr('This   is a text  fragment')

class TestAliasCR(ATestCanonicalRepr):
    """Aliases should be reproduced verbatim, barring the added vertical bar
    terminator at the end (which is optional for aliases, see test below).
    Spaces are not required to separate them (and may in fact be unwanted for
    some alias usages). The two spaces below become text fragments and are
    hence reproduced verbatim as well."""
    _test_src = mks('@foo@bar  @qux')
    _test_rep = mkr('@foo|@bar|  @qux|')

class TestAliasBarCR(ATestCanonicalRepr):
    """The optional vertical bar terminator for aliases should be handled
    and reproduced correctly - note the comma after @C becoming part of the
    alias (since a comma is perfectly valid as part of a word and hence
    perfectly valid as part of an alias name too)."""
    _test_src = mks('@A ran into @B|, @C, and @D|.')
    _test_rep = mkr('@A| ran into @B|, @C,| and @D|.')

class TestCommandNoArgCR(ATestCanonicalRepr):
    """Commands without arguments should receive the vertical bar as a
    terminator."""
    _test_src = mks('\\cmd')
    _test_rep = mkr('\\cmd|')

class TestCommandWithArgCR(ATestCanonicalRepr):
    """Commands with arguments should become multiline and have trailing
    semicolons added if missing."""
    _test_src = mks('\\cmd[a; b; c]')
    _test_rep = mkr('\\cmd[',
                     '    a;',
                     '    b;',
                     '    c;',
                     ']')

class TestKeywordArgsCR(ATestCanonicalRepr):
    """Keyword arguments should be displayed with exactly one space before and
    after the equals sign."""
    _test_src = mks('\\cmd[a=b;c  =  d;e =f]')
    _test_rep = mkr('\\cmd[',
                     '    a = b;',
                     '    c = d;',
                     '    e = f;',
                     ']')

class TestCommandWhitespaceCR(ATestCanonicalRepr):
    """A complex case of whitespace handling that was failing to parse
    correctly in earlier version of the parser."""
    _test_src = mks('\\qux[foo ;',
                     '    bar = rab ; ]')
    _test_rep = mkr('\\qux[',
                     '    foo ;',
                     '    bar = rab ;',
                     ']')

class TestCommandMarkupCR(ATestCanonicalRepr):
    """Markup should be handled correctly inside commands."""
    _test_src = mks('\\foo[',
                     '    *em1*;',
                     '    bar = **em2**;',
                     '    qux = Text that is ***em3***.;',
                     ']')
    _test_rep = mkr('\\foo[',
                     '    *em1*;',
                     '    bar = **em2**;',
                     '    qux = Text that is ***em3***.;',
                     ']')

class TestCommandNestedCR(ATestCanonicalRepr):
    """Nested commands should be handled correctly."""
    _test_src = mks('\\foo[',
                     '    \\bar[',
                     '        \\qux;',
                     '    ];'
                     ']')
    # TODO This is ugly, should somehow come up with a way to fix it
    _test_rep = mkr('\\foo[',
                     '    \\bar[',
                     '    \\qux|;',
                     '];',
                     ']')

class TestUnicodeCR(ATestCanonicalRepr):
    """Canonical representations should handle unicode characters correctly."""
    _test_src = mks('Внимание \\cömmänd[😀] 警告')
    _test_rep = mkr('Внимание \\cömmänd[',
                     '    😀;',
                     '] 警告')

class TestEm1CR(ATestCanonicalRepr):
    """Em1 text should have an unchanged canonical representation."""
    _test_src = mks('This is *em1 text*.')
    _test_rep = mkr('This is *em1 text*.')

class TestEm2CR(ATestCanonicalRepr):
    """Em2 text should have an unchanged canonical representation."""
    _test_src = mks('This is **em2 text**.')
    _test_rep = mkr('This is **em2 text**.')

class TestEm3CR(ATestCanonicalRepr):
    """Em3 text should have an unchanged canonical representation."""
    _test_src = mks('This is ***em3 text***.')
    _test_rep = mkr('This is ***em3 text***.')

class TestEm1ComplexCR(ATestCanonicalRepr):
    """Aliases and commands in em1 text should be handled correctly."""
    _test_src = mks('*Em1 with @aliases and \\commands*')
    _test_rep = mkr('*Em1 with @aliases| and \\commands|*')

class TestEm2ComplexCR(ATestCanonicalRepr):
    """Aliases and commands in em2 text should be handled correctly."""
    _test_src = mks('**Em2 with @aliases and \\commands**')
    _test_rep = mkr('**Em2 with @aliases| and \\commands|**')

class TestEm3ComplexCR(ATestCanonicalRepr):
    """Aliases and commands in em3 text should be handled correctly."""
    _test_src = mks('***Em3 with @aliases and \\commands***')
    _test_rep = mkr('***Em3 with @aliases| and \\commands|***')

class TestMarkupCombinedCR(ATestCanonicalRepr):
    """As horrible as this looks, any level of markup should be able to follow
    any other level of markup without issues."""
    _test_src = mks('*a***b*****c****d***e**')
    _test_rep = mkr('*a***b*****c****d***e**')
