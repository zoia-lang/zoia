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
"""Provides an API for visiting Zoia AST nodes."""
from ast_nodes import AASTNode, ZoiaFileNode, HeaderNode, LineNode, \
    LineElementsNode, ALineElementNode, AEmLineElementNode, \
    Em1LineElementNode, Em2LineElementNode, Em3LineElementNode, \
    TextFragmentNode, AliasNode, CommandNode, AArgumentNode, KwdArgumentNode, \
    StdArgumentNode

class AASTVisitor:
    """Base class for Zoia AST visitors."""
    def visit(self, tree: AASTNode):
        """Begins visiting an AST (which need not be a full tree beginning at
        ZoiaFileNode)."""
        return tree.accept(self)

    def _try_visit_val(self, node_val):
        """Internal recursive method that attempts to visit the specified
        value."""
        if isinstance(node_val, AASTNode):
            return node_val.accept(self)
        elif isinstance(node_val, list):
            last_tf = None
            for list_el in node_val:
                # Do not override a present value with None
                last_tf = self._try_visit_val(list_el) or last_tf
            return last_tf
        return None # Nothing to do here

    # API that is intended for overriding by end users begins here
    def _visit_default(self, node: AASTNode):
        """Called when a non-overriden visit_* method is called. Visits all
        child nodes and returns the last value. You can override it if you want
        to do something different."""
        last_tf = None
        for node_attr in node.__slots__:
            node_val = getattr(node, node_attr)
            # Do not override a present value with None
            last_tf = self._try_visit_val(node_val) or last_tf
        return last_tf

    def _visit_line_element(self, node: ALineElementNode):
        """Called as default behavior by visit_em_line_element,
        visit_text_fragment, visit_alias and visit_command."""
        return self._visit_default(node)

    def _visit_em_line_element(self, node: AEmLineElementNode):
        """Called as default behavior by visit_em1_line_element,
        visit_em2_line_element and visit_em3_line_element."""
        return self._visit_line_element(node)

    def _visit_argument(self, node: AArgumentNode):
        """Called as default behavior by visit_kwd_argument and
        visit_std_argument."""
        return self._visit_default(node)

    # These are public because they get called by nodes' accept() methods
    def visit_zoia_file(self, node: ZoiaFileNode):
        """Visits a ZoiaFileNode."""
        return self._visit_default(node)

    def visit_header(self, node: HeaderNode):
        """Visits a HeaderNode."""
        return self._visit_default(node)

    def visit_line(self, node: LineNode):
        """Visits a LineNode."""
        return self._visit_default(node)

    def visit_line_elements(self, node: LineElementsNode):
        """Visits a LineElementsNode."""
        return self._visit_default(node)

    def visit_em1_line_element(self, node: Em1LineElementNode):
        """Visits a Em1LineElementNode."""
        return self._visit_em_line_element(node)

    def visit_em2_line_element(self, node: Em2LineElementNode):
        """Visits a Em2LineElementNode."""
        return self._visit_em_line_element(node)

    def visit_em3_line_element(self, node: Em3LineElementNode):
        """Visits a Em3LineElementNode."""
        return self._visit_em_line_element(node)

    def visit_text_fragment(self, node: TextFragmentNode):
        """Visits a HeaderNode."""
        return self._visit_line_element(node)

    def visit_alias(self, node: AliasNode):
        """Visits an AliasNode."""
        return self._visit_line_element(node)

    def visit_command(self, node: CommandNode):
        """Visits a CommandNode."""
        return self._visit_line_element(node)

    def visit_kwd_argument(self, node: KwdArgumentNode):
        """Visits a KwdArgumentNode."""
        return self._visit_argument(node)

    def visit_std_argument(self, node: StdArgumentNode):
        """Visits a StdArgumentNode."""
        return self._visit_argument(node)
