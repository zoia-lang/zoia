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
"""This module houses the parse tree visitor that generates an AST from the
ANTLR parse tree."""
# Some performance considerations:
#  - Avoid APIs dependent on getToken (e.g. Word()) - really expensive. Use
#    children[x] directly instead
#  - Avoid getText() outside errors - use symbol.text instead
from io import StringIO

from antlr4.tree.Tree import ParseTree

from ast_nodes import AliasNode, CommandNode, HeaderNode, KwdArgumentNode, \
    LineNode, StdArgumentNode, TextFragmentNode, ZoiaFileNode, \
    LineElementsNode, AArgumentNode, Em1LineElementNode, Em2LineElementNode, \
    Em3LineElementNode
from exception import ParseConversionError
from grammar import zoiaParser, zoiaVisitor
from src_pos import SourcePos

# Currently, PyCharm seems to have a problem with kw_only fields in
# dataclasses. It reports all the src_pos arguments as 'Unexpected argument'
# warnings. Until that's fixed:
# noinspection PyArgumentList

# Ignore the non-PEP8 names, inherited from the generated code
class ParseConverter(zoiaVisitor):
    """Converts an ANTLR parse tree into a Zoia AST."""
    def __init__(self, parsed_file: str) -> None:
        self.parsed_file = parsed_file
        # Avoids a bunch of 'if isinstance' checks in visitLineElements,
        # visitLineElementsInner and visitLineElementsArg
        shared_lookup = {
            zoiaParser.AliasContext: self.visitAlias,
            zoiaParser.CommandContext: self.visitCommand,
        }
        self._line_element_lookup = shared_lookup | {
            zoiaParser.TextFragmentContext: self.visitTextFragment,
            zoiaParser.Em1LineElementContext: self.visitEm1LineElement,
            zoiaParser.Em2LineElementContext: self.visitEm2LineElement,
            zoiaParser.Em3LineElementContext: self.visitEm3LineElement,
        }
        self._line_element_inner_lookup = shared_lookup | {
            zoiaParser.TextFragmentReqContext: self.visitTextFragmentReq,
        }
        self._line_element_arg_lookup = self._line_element_lookup | {
            zoiaParser.TextFragmentWordContext: self.visitTextFragmentWord,
        }

    def make_pos(self, ctx) -> SourcePos:
        """Creates a source position from the specified context object."""
        ctx_start = ctx.start
        return SourcePos(src_file=self.parsed_file, src_line=ctx_start.line,
                         src_char=ctx_start.column)

    # Override to add typing
    def visit(self, tree: ParseTree) -> ZoiaFileNode:
        # pylint: disable=useless-super-delegation
        return super().visit(tree)

    # Sorted by the order in which they are defined in the grammar
    def visitZoiaFile(self, ctx: zoiaParser.ZoiaFileContext) -> ZoiaFileNode:
        header = self.visitHeader(ctx.header())
        lines = [self.visitLine(l) for l in ctx.line()]
        return ZoiaFileNode(header, lines, src_pos=self.make_pos(ctx))

    def visitHeader(self, ctx: zoiaParser.HeaderContext) -> HeaderNode:
        return HeaderNode(self.visitArguments(ctx.arguments()),
                          src_pos=self.make_pos(ctx))

    def visitLine(self, ctx: zoiaParser.LineContext) -> LineNode:
        return LineNode(self.visitLineElements(ctx.lineElements()),
                        src_pos=self.make_pos(ctx))

    def visitLineElements(self, ctx: zoiaParser.LineElementsContext) \
            -> LineElementsNode | None:
        if ctx is None:
            return None # lineElements is optional in line
        return self._visit_line_elements_shared(
            ctx, self._line_element_lookup)

    def visitLineElementsInner(self,
                               ctx: zoiaParser.LineElementsInnerContext) \
            -> LineElementsNode:
        return self._visit_line_elements_shared(
            ctx, self._line_element_inner_lookup)

    def visitLineElementsArg(self, ctx: zoiaParser.LineElementsArgContext) \
            -> LineElementsNode:
        return self._visit_line_elements_shared(
            ctx, self._line_element_arg_lookup)

    def _visit_line_elements_shared(self, ctx, visit_lookup) \
            -> LineElementsNode:
        """Small helper method to deduplicate the shared logic of
        visitLineElements and visitLineElementsInner."""
        elements = []
        for le_child in ctx.children:
            try:
                visit_method = visit_lookup[le_child.__class__]
            except KeyError as e:
                raise ParseConversionError(self.make_pos(le_child),
                                           f"Unknown or invalid line element "
                                           f"'{le_child.getText()}'") from e
            elements.append(visit_method(le_child))
        return LineElementsNode(elements, src_pos=self.make_pos(ctx))

    def visitEm1LineElement(self, ctx: zoiaParser.Em1LineElementContext) \
            -> Em1LineElementNode:
        return Em1LineElementNode(
            self.visitLineElementsInner(ctx.lineElementsInner()),
            src_pos=self.make_pos(ctx))

    def visitEm2LineElement(self, ctx: zoiaParser.Em2LineElementContext) \
            -> Em2LineElementNode:
        return Em2LineElementNode(
            self.visitLineElementsInner(ctx.lineElementsInner()),
            src_pos=self.make_pos(ctx))

    def visitEm3LineElement(self, ctx: zoiaParser.Em3LineElementContext) \
            -> Em3LineElementNode:
        return Em3LineElementNode(
            self.visitLineElementsInner(ctx.lineElementsInner()),
            src_pos=self.make_pos(ctx))

    def visitTextFragment(self, ctx: zoiaParser.TextFragmentContext) \
            -> TextFragmentNode:
        try:
            # First child is either Word or Spaces - same behavior for both
            return TextFragmentNode(ctx.children[0].symbol.text,
                                    src_pos=self.make_pos(ctx))
        except (AttributeError, KeyError, IndexError, TypeError):
            raise ParseConversionError(self.make_pos(ctx),
                                       f"Unknown or invalid text fragment "
                                       f"'{ctx.getText()}'")

    def visitTextFragmentReq(self, ctx: zoiaParser.TextFragmentReqContext) \
            -> TextFragmentNode:
        s = StringIO()
        for tf_child in ctx.children:
            try:
                # One Word, between zero and two Spaces
                s.write(tf_child.symbol.text)
            except (AttributeError, KeyError, IndexError, TypeError):
                raise ParseConversionError(self.make_pos(ctx),
                                           f"Unknown or invalid required "
                                           f"text fragment '{ctx.getText()}'")
        return TextFragmentNode(s.getvalue(), src_pos=self.make_pos(ctx))

    def visitTextFragmentWord(self, ctx: zoiaParser.TextFragmentWordContext) \
            -> TextFragmentNode:
        s = StringIO()
        tf_children = ctx.children
        # First child is Word, second one (if present) is Spaces
        s.write(tf_children[0].symbol.text)
        if len(tf_children) > 1:
            s.write(tf_children[1].symbol.text)
        return TextFragmentNode(s.getvalue(), src_pos=self.make_pos(ctx))

    def visitAlias(self, ctx: zoiaParser.AliasContext) -> AliasNode:
        # First child is At, second child is Word
        return AliasNode(ctx.children[1].symbol.text,
                         src_pos=self.make_pos(ctx))

    def visitCommand(self, ctx: zoiaParser.CommandContext) -> CommandNode:
        # First child is Backslash, the second one is Word
        return CommandNode(ctx.children[1].symbol.text,
                           self.visitArguments(ctx.arguments()),
                           src_pos=self.make_pos(ctx))

    def visitArguments(self, ctx: zoiaParser.ArgumentsContext) \
            -> list[AArgumentNode]:
        if ctx is None:
            return [] # command has an optional arguments param
        return [self.visitArgument(a) for a in ctx.argument()]

    def visitArgument(self, ctx: zoiaParser.ArgumentContext) -> AArgumentNode:
        std_argument = ctx.stdArgument()
        if std_argument is not None:
            return self.visitStdArgument(std_argument)
        kwd_argument = ctx.kwdArgument()
        if kwd_argument is not None:
            return self.visitKwdArgument(kwd_argument)
        else:
            raise ParseConversionError(self.make_pos(ctx),
                                       f"Unknown or invalid argument: "
                                       f"'{ctx.getText()}'")

    def visitKwdArgument(self, ctx: zoiaParser.KwdArgumentContext) \
            -> KwdArgumentNode:
        # First child is Word
        kwd_name = ctx.children[0].symbol.text
        arg_value = self.visitLineElementsArg(ctx.lineElementsArg())
        # Reverse order due to dataclass inheritance
        return KwdArgumentNode(arg_value, kwd_name, src_pos=self.make_pos(ctx))

    def visitStdArgument(self, ctx: zoiaParser.StdArgumentContext) \
            -> StdArgumentNode:
        return StdArgumentNode(
            self.visitLineElementsArg(ctx.lineElementsArg()),
            src_pos=self.make_pos(ctx))
