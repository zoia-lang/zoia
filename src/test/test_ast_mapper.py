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
"""This module houses tests related to ast_mapper."""
from test.base import mks
from test.test_canonical import ATestCanonicalRepr, TestHeaderCR, \
    TestCommentCR, TestTextFragmentCR, TestAliasCR, TestAliasBarCR, \
    TestCommandNoArgCR, TestCommandWithArgCR, TestKeywordArgsCR, \
    TestCommandWhitespaceCR, TestCommandMarkupCR, TestCommandNestedSACR, \
    TestUnicodeCR, TestEm1CR, TestEm2CR, TestEm3CR, TestEm1ComplexCR, \
    TestEm2ComplexCR, TestEm3ComplexCR, TestMarkupCombinedCR, \
    TestCommandNestedMACR

from ast_mapper import AASTMapper
from ast_nodes import AliasNode, TextFragmentNode

class _TestMapper(AASTMapper):
    """Test mapper implementation that simply replaces AliasNodes with
    TextFragmentNodes (without changing the text)."""
    def visit_alias(self, node: AliasNode):
        # See parse_converter.py for the reasoning
        # noinspection PyArgumentList
        return TextFragmentNode(node.alias_key, src_pos=node.src_pos)

class _ATestASTMapper(ATestCanonicalRepr):
    """Base class for AASTMapper tests."""
    def _get_canonical(self, test_src: str) -> str:
        tree = self._parse_src(test_src)
        mapper = _TestMapper()
        tree_tf = mapper.visit(tree)
        return tree_tf.canonical()

# Canonical repr tests without aliases in it should run identically
class TestMapHeaderCR(_ATestASTMapper, TestHeaderCR):
    """Version of TestHeaderCR that maps before testing."""

class TestMapCommentCR(_ATestASTMapper, TestCommentCR):
    """Version of TestCommentCR that maps before testing."""

class TestMapTextFragmentCR(_ATestASTMapper, TestTextFragmentCR):
    """Version of TestTextFragmentCR that maps before testing."""

class TestMapCommandNoArgCR(_ATestASTMapper, TestCommandNoArgCR):
    """Version of TestCommandNoArgCR that maps before testing."""

class TestMapCommandWithArgCR(_ATestASTMapper, TestCommandWithArgCR):
    """Version of TestCommandWithArgCR that maps before testing."""

class TestMapKeywordArgsCR(_ATestASTMapper, TestKeywordArgsCR):
    """Version of TestKeywordArgsCR that maps before testing."""

class TestMapCommandWhitespaceCR(_ATestASTMapper, TestCommandWhitespaceCR):
    """Version of TestCommandWhitespaceCR that maps before testing."""

class TestMapCommandMarkupCR(_ATestASTMapper, TestCommandMarkupCR):
    """Version of TestCommandMarkupCR that maps before testing."""

class TestMapCommandNestedSACR(_ATestASTMapper, TestCommandNestedSACR):
    """Version of TestCommandNestedSACR that maps before testing."""

class TestMapCommandNestedMACR(_ATestASTMapper, TestCommandNestedMACR):
    """Version of TestCommandNestedMACR that maps before testing."""

class TestMapUnicodeCR(_ATestASTMapper, TestUnicodeCR):
    """Version of TestUnicodeCR that maps before testing."""

class TestMapEm1CR(_ATestASTMapper, TestEm1CR):
    """Version of TestEm1CR that maps before testing."""

class TestMapEm2CR(_ATestASTMapper, TestEm2CR):
    """Version of TestEm2CR that maps before testing."""

class TestMapEm3CR(_ATestASTMapper, TestEm3CR):
    """Version of TestEm3CR that maps before testing."""

class TestMapMarkupCombinedCR(_ATestASTMapper, TestMarkupCombinedCR):
    """Version of TestMarkupCombinedCR that maps before testing."""

# Canonical repr tests with aliases in it should remove the '@' and '|'
class TestMapAliasCR(_ATestASTMapper, TestAliasCR):
    """@foo| -> 'foo', @bar| -> 'bar', @qux| -> 'qux'"""
    _test_rep = mks('foobar  qux')

class TestMapAliasBarCR(_ATestASTMapper, TestAliasBarCR):
    """@A -> 'A', @B| -> 'B', @C, -> 'C,', @D| -> D"""
    _test_rep = mks('A ran into B, C, and D. Bs or Bs, C1 or C1?')

class TestMapEm1ComplexCR(_ATestASTMapper, TestEm1ComplexCR):
    """@aliases -> aliases"""
    _test_rep = mks('*Em1 with aliases and \\commands|*')

class TestMapEm2ComplexCR(_ATestASTMapper, TestEm2ComplexCR):
    """@aliases -> aliases"""
    _test_rep = mks('**Em2 with aliases and \\commands|**')

class TestMapEm3ComplexCR(_ATestASTMapper, TestEm3ComplexCR):
    """@aliases -> aliases"""
    _test_rep = mks('***Em3 with aliases and \\commands|***')

# Delete these, otherwise pytest will see them in scope and run them again
del ATestCanonicalRepr, TestHeaderCR, TestCommentCR, TestTextFragmentCR, \
    TestAliasCR, TestAliasBarCR, TestCommandNoArgCR, TestCommandWithArgCR, \
    TestKeywordArgsCR, TestCommandWhitespaceCR, TestCommandMarkupCR, \
    TestCommandNestedSACR, TestUnicodeCR, TestEm1CR, TestEm2CR, TestEm3CR, \
    TestEm1ComplexCR, TestEm2ComplexCR, TestEm3ComplexCR, \
    TestMarkupCombinedCR, TestCommandNestedMACR
