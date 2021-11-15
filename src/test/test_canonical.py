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
"""This module houses tests related to canonical representations."""
from ast_converter import ASTConverter
from test.base import ATestParser

class _ATestCanonicalRepr(ATestParser):
    _do_fixups = False
    _test_rep: str

    def _get_canonical(self, test_src: str):
        parse_tree = self._make_parser(test_src).zoiaFile()
        zoia_conv = ASTConverter(f"<test '{self.__class__.__name__}'>")
        return zoia_conv.visit(parse_tree).canonical()

    def test_parse_src(self):
        """Parsing the source should produce the canonical representation."""
        assert self._get_canonical(self._test_src) == self._test_rep

    def test_parse_repr(self):
        """Parsing the canonical representation should produce the canonical
        representation itself again."""
        assert self._get_canonical(self._test_rep) == self._test_rep


# Some helpers for easily making sources and canonical representations
def _mk_shared(*lines):
    return '\n'.join(lines) + '\n'

_common_s = _mk_shared('\\header[foo]') + '\n'
_common_r = _mk_shared('\\header[',
                       '    foo;',
                       ']',
                       '')

def _mks(*lines):
    return _common_s + _mk_shared(*lines)
def _mkr(*lines):
    return _common_r + _mk_shared(*lines)

class TestHeaderCR(_ATestCanonicalRepr):
    """Headers should be formatted like commands (see TestCommandWithArgCR)."""
    _test_src = _mks()
    _test_rep = _mkr()

class TestCommentCR(_ATestCanonicalRepr):
    """Comments should be gone (since they get stripped during parsing)."""
    _test_src = _mks('This is a line# with a comment')
    _test_rep = _mkr('This is a line')

class TestTextFragmentCR(_ATestCanonicalRepr):
    """Text fragments should be reproduced verbatim, including all spaces."""
    _test_src = _mks('This   is a text  fragment')
    _test_rep = _mkr('This   is a text  fragment')

class TestAliasCR(_ATestCanonicalRepr):
    """Aliases should be reproduced verbatim. Spaces are not required to
    separate them (and may in fact be unwanted for some alias usages). The
    two spaces below become text fragments and are hence reproduced verbatim as
    well."""
    _test_src = _mks('@foo@bar  @qux')
    _test_rep = _mkr('@foo@bar  @qux')

class TestCommandNoArgCR(_ATestCanonicalRepr):
    """Commands without arguments should receive the vertical bar as a
    terminator."""
    _test_src = _mks('\\cmd')
    _test_rep = _mkr('\\cmd|')

class TestCommandWithArgCR(_ATestCanonicalRepr):
    """Commands with arguments should become multiline and have trailing
    semicolons added if missing."""
    _test_src = _mks('\\cmd[a; b; c]')
    _test_rep = _mkr('\\cmd[',
                     '    a;',
                     '    b;',
                     '    c;',
                     ']')

class TestKeywordArgsCR(_ATestCanonicalRepr):
    """Keyword arguments should be displayed with exactly one space before and
    after the equals sign."""
    _test_src = _mks('\\cmd[a=b;c  =  d;e =f]')
    _test_rep = _mkr('\\cmd[',
                     '    a = b;',
                     '    c = d;',
                     '    e = f;',
                     ']')

class TestCommandWhitespaceCR(_ATestCanonicalRepr):
    """A complex case of whitespace handling that was failing to parse
    correctly in earlier version of the parser."""
    _test_src = _mks('\\qux[foo ;',
                     '    bar = rab ; ]')
    _test_rep = _mkr('\\qux[',
                     '    foo ;',
                     '    bar = rab ;',
                     ']')

class TestUnicodeCR(_ATestCanonicalRepr):
    """Canonical representations should handle unicode characters correctly."""
    _test_src = _mks('Внимание \\cömmänd[😀] 警告')
    _test_rep = _mkr('Внимание \\cömmänd[',
                     '    😀;',
                     '] 警告')