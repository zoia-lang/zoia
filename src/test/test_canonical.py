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
"""This module houses tests related to canonical representations."""
from test.base import ATestParser, mks

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

class TestHeaderCR(ATestCanonicalRepr):
    """Headers should be formatted like commands (see TestCommandWithArgCR)."""
    _test_src = mks()
    _test_rep = mks()

class TestCommentCR(ATestCanonicalRepr):
    """Comments should be gone (since they get stripped during parsing)."""
    _test_src = mks('This is a line# with a comment')
    _test_rep = mks('This is a line')

class TestTextFragmentCR(ATestCanonicalRepr):
    """Text fragments should be reproduced verbatim, including all spaces."""
    _test_src = mks('This   is a text  fragment')
    _test_rep = mks('This   is a text  fragment')

class TestAliasCR(ATestCanonicalRepr):
    """Aliases should be reproduced verbatim, barring the added vertical bar
    terminator at the end (which is optional for aliases, see test below).
    Spaces are not required to separate them (and may in fact be unwanted for
    some alias usages). The two spaces below become text fragments and are
    hence reproduced verbatim as well."""
    _test_src = mks('@foo@bar  @qux')
    _test_rep = mks('@foo|@bar|  @qux|')

class TestAliasBarCR(ATestCanonicalRepr):
    """The optional vertical bar terminator for aliases should be handled
    and reproduced correctly. Note how @C, and @D. are handled correctly, but
    @Bs becomes @Bs| and @C1 becomes @C1| since the previous ones all used
    punctuation, whereas these use letters and numbers."""
    _test_src = mks('@A ran into @B|, @C, and @D. @Bs or @B|s, @C1 or @C|1?')
    _test_rep = mks('@A| ran into @B|, @C|, and @D|. @Bs| or @B|s, @C1| or '
                    '@C|1?')

class TestCommandNoArgCR(ATestCanonicalRepr):
    """Commands without arguments should receive the vertical bar as a
    terminator."""
    _test_src = mks('\\cmd')
    _test_rep = mks('\\cmd|')

class TestCommandWithArgCR(ATestCanonicalRepr):
    """Commands with arguments should become multiline and have trailing
    semicolons added if missing."""
    _test_src = mks('\\cmd[a; b; c]')
    _test_rep = mks('\\cmd[',
                     '    a;',
                     '    b;',
                     '    c;',
                     ']')

class TestKeywordArgsCR(ATestCanonicalRepr):
    """Keyword arguments should be displayed with exactly one space before and
    after the equals sign."""
    _test_src = mks('\\cmd[a=b;c  =  d;e =f]')
    _test_rep = mks('\\cmd[',
                     '    a = b;',
                     '    c = d;',
                     '    e = f;',
                     ']')

class TestCommandWhitespaceCR(ATestCanonicalRepr):
    """A complex case of whitespace handling that was failing to parse
    correctly in earlier version of the parser."""
    _test_src = mks('\\qux[foo ;',
                     '    bar = rab ; ]')
    _test_rep = mks('\\qux[',
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
    _test_rep = mks('\\foo[',
                     '    *em1*;',
                     '    bar = **em2**;',
                     '    qux = Text that is ***em3***.;',
                     ']')

class TestCommandNestedSACR(ATestCanonicalRepr):
    """Single-argument nested commands should be handled correctly."""
    _test_src = mks('\\foo[',
                     '    \\bar[',
                     '        \\qux;',
                     '    ];'
                     ']')
    _test_rep = mks('\\foo[\\bar[\\qux|]]')

class TestCommandNestedMACR(ATestCanonicalRepr):
    """Single-argument nested commands should be handled correctly."""
    _test_src = mks('\\foo[',
                     '    \\bar[',
                     '        \\qux; \\qux',
                     '    ]; \\qux;'
                     ']')
    # TODO This is ugly, see #18
    _test_rep = mks('\\foo[',
                     '    \\bar[',
                     '    \\qux|;',
                     '    \\qux|;',
                     '];',
                     '    \\qux|;',
                     ']')

class TestUnicodeCR(ATestCanonicalRepr):
    """Canonical representations should handle unicode characters correctly."""
    _test_src = mks('Внимание \\cömmänd[😀] 警告')
    _test_rep = mks('Внимание \\cömmänd[😀] 警告')

class TestEm1CR(ATestCanonicalRepr):
    """Em1 text should have an unchanged canonical representation."""
    _test_src = mks('This is *em1 text*.')
    _test_rep = mks('This is *em1 text*.')

class TestEm2CR(ATestCanonicalRepr):
    """Em2 text should have an unchanged canonical representation."""
    _test_src = mks('This is **em2 text**.')
    _test_rep = mks('This is **em2 text**.')

class TestEm3CR(ATestCanonicalRepr):
    """Em3 text should have an unchanged canonical representation."""
    _test_src = mks('This is ***em3 text***.')
    _test_rep = mks('This is ***em3 text***.')

class TestEm1ComplexCR(ATestCanonicalRepr):
    """Aliases and commands in em1 text should be handled correctly."""
    _test_src = mks('*Em1 with @aliases and \\commands*')
    _test_rep = mks('*Em1 with @aliases| and \\commands|*')

class TestEm2ComplexCR(ATestCanonicalRepr):
    """Aliases and commands in em2 text should be handled correctly."""
    _test_src = mks('**Em2 with @aliases and \\commands**')
    _test_rep = mks('**Em2 with @aliases| and \\commands|**')

class TestEm3ComplexCR(ATestCanonicalRepr):
    """Aliases and commands in em3 text should be handled correctly."""
    _test_src = mks('***Em3 with @aliases and \\commands***')
    _test_rep = mks('***Em3 with @aliases| and \\commands|***')

class TestMarkupCombinedCR(ATestCanonicalRepr):
    """As horrible as this looks, any level of markup should be able to follow
    any other level of markup without issues."""
    _test_src = mks('*a***b*****c****d***e**')
    _test_rep = mks('*a***b*****c****d***e**')
