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
"""Houses the parse tree visitor that generates an AST from the ANTLR parse
tree."""
from .ast_nodes import HeaderNode, LineNode, ZoiaFileNode
from .exception import ASTConversionError
from .grammar import zoiaParser, zoiaVisitor

# FIXME Add token source locations -> edits to ast_nodes too

# Ignore the non-PEP8 names, inherited from the generated code
class ASTConverter(zoiaVisitor):
    # Sorted by the order in which they are defined in the grammar
    def visitZoiaFile(self, ctx: zoiaParser.ZoiaFileContext):
        header = self.visitHeader(ctx.header())
        lines = [self.visitLine(l) for l in ctx.line()]
        return ZoiaFileNode(header, lines)

    def visitHeader(self, ctx: zoiaParser.HeaderContext):
        return HeaderNode(self.visitArguments(ctx.arguments()))

    def visitLine(self, ctx: zoiaParser.LineContext):
        elements = [self.visitLineElement(e) for e in ctx.lineElement()]
        return LineNode(elements)

    def visitLineElement(self, ctx: zoiaParser.LineElementContext):
        text_fragment = ctx.textFragment()
        if text_fragment is not None:
            return self.visitTextFragment(text_fragment)
        alias = ctx.alias()
        if alias is not None:
            return self.visitAlias(alias)
        command = ctx.command()
        if command is not None:
            return self.visitCommand(command)
        else:
            raise ASTConversionError(f"Unknown line element '{ctx}'")
