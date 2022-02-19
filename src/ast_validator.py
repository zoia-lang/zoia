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
from ast_nodes import ZoiaFileNode, HeaderNode, StdArgumentNode, LineNode, \
    LineElementsNode, Em1LineElementNode, Em2LineElementNode, \
    Em3LineElementNode, TextFragmentNode, AliasNode, CommandNode, \
    KwdArgumentNode
from ast_visitor import AASTVisitor
from exception import ValidationError

class ASTValidator(AASTVisitor):
    """Performs validation on a Zoia AST, detecting and reporting errors that
    cannot be detected during parsing."""
    def visit_zoia_file(self, node: ZoiaFileNode):
        self.visit_header(node.header)
        for l in node.lines:
            self.visit_line(l)

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
            self.visit(a)

    def visit_line(self, node: LineNode):
        if n_elements := node.elements:
            self.visit_line_elements(n_elements)

    def visit_line_elements(self, node: LineElementsNode):
        for e in node.elements:
            self.visit(e)

    def visit_em1_line_element(self, node: Em1LineElementNode):
        self.visit_line_elements(node.elements)

    def visit_em2_line_element(self, node: Em2LineElementNode):
        self.visit_line_elements(node.elements)

    def visit_em3_line_element(self, node: Em3LineElementNode):
        self.visit_line_elements(node.elements)

    def visit_text_fragment(self, node: TextFragmentNode):
        pass

    def visit_alias(self, node: AliasNode):
        pass

    def visit_command(self, node: CommandNode):
        # TODO This should check that the command exists and that the arguments
        #  passed to it are OK
        for a in node.arguments:
            self.visit(a)

    def visit_kwd_argument(self, node: KwdArgumentNode):
        self.visit_line_elements(node.arg_value)

    def visit_std_argument(self, node: StdArgumentNode):
        self.visit_line_elements(node.arg_value)
