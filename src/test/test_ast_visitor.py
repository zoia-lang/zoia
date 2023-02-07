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
"""This module houses tests related to ast_visitor."""
from test.base import ATestParser

from ast_nodes import AASTNode
from ast_visitor import AASTVisitor

class _VisitorTest(AASTVisitor):
    """Test visitor implementation that simply logs the class names of every
    node it visits."""
    def __init__(self) -> None:
        self.visit_log = []

    def _visit_default(self, node: AASTNode):
        self.visit_log.append(node.__class__.__name__)
        return super()._visit_default(node)

_DEFAULT_HEADER_NODES = ['ZoiaFileNode', 'HeaderNode', 'StdArgumentNode',
                         'LineElementsNode', 'TextFragmentNode', 'LineNode']

class _ATestASTVisitor(ATestParser):
    """Base class for AASTVisitor tests."""
    _expected_log: list[str]

    def test_ast_visitor(self):
        """Runs the actual test: parsing the source, visiting the AST and
        comparing the visit log."""
        visitor = _VisitorTest()
        visitor.visit(self._parse_src())
        final_log = visitor.visit_log
        if self._added_header:
            # We added a header, so we need to remove the nodes that got added
            # to the log as a result. Thankfully these are always the same (but
            # assert to make sure just in case).
            initial_nodes = final_log[:len(_DEFAULT_HEADER_NODES)]
            assert initial_nodes == _DEFAULT_HEADER_NODES
            final_log = final_log[len(_DEFAULT_HEADER_NODES):]
        assert final_log == self._expected_log

class TestEmpty(_ATestASTVisitor):
    """An empty source should produce no nodes for visiting."""
    _test_src = ''
    _expected_log = []

class TestAlias(_ATestASTVisitor):
    """An alias should produce an AliasNode (along with the necessary nodes for
    placing an alias on a line)."""
    _test_src = '@test'
    _expected_log = ['LineNode', 'LineElementsNode', 'AliasNode']

class TestCommand(_ATestASTVisitor):
    """A command should produce a CommandNode and nodes for its arguments
    (along with the necessary nodes for placing a command on a line and storing
    the argument nodes)."""
    _test_src = r'\foo[a; b = c]'
    _expected_log = ['LineNode', 'LineElementsNode',
                     # \foo
                     'CommandNode',
                     # a
                     'StdArgumentNode', 'LineElementsNode', 'TextFragmentNode',
                     # b = c
                     'KwdArgumentNode', 'LineElementsNode', 'TextFragmentNode']

class TestMarkup(_ATestASTVisitor):
    """All types of markup should produce the appropriate nodes (along with the
    necessary nodes for placing markup on a line and storing the spaces in
    between)."""
    _test_src = '*em1* **em2** ***em3***'
    _expected_log = ['LineNode', 'LineElementsNode',
                     # *em1*, TextFragmentNode is 'em1'
                     'Em1LineElementNode', 'LineElementsNode',
                     'TextFragmentNode',
                     # ' ' (space) between *em1* and **em2**
                     'TextFragmentNode',
                     # **em2**, TextFragmentNode is 'em2'
                     'Em2LineElementNode', 'LineElementsNode',
                     'TextFragmentNode',
                     # ' ' (space) between **em2** and ***em3***
                     'TextFragmentNode',
                     # ***em3***, TextFragmentNode is 'em3'
                     'Em3LineElementNode', 'LineElementsNode',
                     'TextFragmentNode']
