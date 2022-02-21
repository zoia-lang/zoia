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
"""Provides abstract APIs for visiting Zoia ASTs."""
from ast_nodes import AASTNode, ZoiaFileNode, HeaderNode, LineNode, \
    LineElementsNode, ALineElementNode, AEmLineElementNode, \
    Em1LineElementNode, Em2LineElementNode, Em3LineElementNode, \
    TextFragmentNode, AliasNode, CommandNode, AArgumentNode, KwdArgumentNode, \
    StdArgumentNode
from commands import new_state_container

class AASTVisitor:
    """Base class for Zoia AST visitors."""
    __slots__ = ()

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
            if not hasattr(node, node_attr):
                continue # Member descriptor, ignore
            # Do not override a present value with None
            last_tf = self._try_visit_val(getattr(node, node_attr)) or last_tf
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

class ACommandVisitor(AASTVisitor):
    """Version of AASTVisitor meant to be used for visiting commands. Much
    faster than the naive approach since it can skip over things like text
    fragments and aliases. Override visit_command (and visit_header, if
    needed), perform your logic, then call the super method."""
    __slots__ = ()

    def visit_zoia_file(self, node: ZoiaFileNode):
        self.visit_header(node.header)
        for l in node.lines:
            if l_elems := l.elements:
                self.visit_line_elements(l_elems)

    def visit_header(self, node: HeaderNode):
        for a in node.arguments:
            self.visit_line_elements(a.arg_value)

    def visit_line_elements(self, node: LineElementsNode):
        for e in node.elements:
            if isinstance(e, CommandNode):
                self.visit_command(e)
            elif isinstance(e, AEmLineElementNode):
                self._visit_line_elements_inner(e.elements)

    def _visit_line_elements_inner(self, node: LineElementsNode):
        """Version of visit_line_elements that may only be called to handle
        a LineElementsNode that originated from an AEmLineElementNode."""
        for e in node.elements:
            # AEmLineElementNode.elements may not contain another
            # AEmLineElementNode, so no need to check for it
            if isinstance(e, CommandNode):
                self.visit_command(e)

    def visit_command(self, node: CommandNode):
        for a in node.arguments:
            self.visit_line_elements(a.arg_value)

class ACommandEvaluator(ACommandVisitor):
    """Version of ACommandVisitor meant for evaluating commands."""
    __slots__ = ('_state_container',)

    def __init__(self):
        self._state_container = new_state_container()

    def visit_command(self, node: CommandNode):
        node.proc_cmd.exec_command(self._state_container)
        super().visit_command(node)
