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
"""Performs validation on a parsed Zoia AST."""
from ast_nodes import ZoiaFileNode, HeaderNode, StdArgumentNode, \
    LineElementsNode, TextFragmentNode, CommandNode, AEmLineElementNode
from ast_visitor import AASTVisitor
from exception import ValidationError

class ASTValidator(AASTVisitor):
    """Performs validation on a Zoia AST, detecting and reporting errors that
    cannot be detected during parsing."""
    def visit_zoia_file(self, node: ZoiaFileNode):
        self.visit_header(node.header)
        for l in node.lines:
            if l_elems := l.elements:
                self.visit_line_elements(l_elems)

    # TODO We're going to have to turn this into a more general system if we
    #  want to validate arbitrary commands - some sort of signature class?
    def visit_header(self, node: HeaderNode):
        # TODO Do we have a use case for >1 argument passed to the header? If
        #  not, add a check here for != 1
        # The grammar guarantees that we have at least one argument
        if not isinstance(node.arguments[0], StdArgumentNode):
            raise ValidationError(
                node.arguments[0].src_pos,
                'The first argument passed to \\header must be a standard '
                'argument')
        arg_elements = node.arguments[0].arg_value.elements
        txt_frag_msg = ('The first argument passed to \\header must be a '
                        'single text fragment containing one word')
        if len(arg_elements) > 1:
            raise ValidationError(arg_elements[1].src_pos, txt_frag_msg)
        txt_frag = arg_elements[0]
        if not isinstance(txt_frag, TextFragmentNode):
            raise ValidationError(txt_frag.src_pos, txt_frag_msg)
        # Strip the text value to be forgiving of trailing whitespace
        txt_frag_val = txt_frag.text_val.strip()
        # TODO This should check that the header type argument is recognized
        node.header_type = txt_frag_val
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
        # TODO This should check that the command exists and that the arguments
        #  passed to it are OK
        for a in node.arguments:
            self.visit_line_elements(a.arg_value)
