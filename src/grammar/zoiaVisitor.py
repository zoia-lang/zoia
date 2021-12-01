# Generated from grammar/zoia.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .zoiaParser import zoiaParser
else:
    from zoiaParser import zoiaParser

# This class defines a complete generic visitor for a parse tree produced by zoiaParser.

class zoiaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by zoiaParser#zoiaFile.
    def visitZoiaFile(self, ctx:zoiaParser.ZoiaFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by zoiaParser#header.
    def visitHeader(self, ctx:zoiaParser.HeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by zoiaParser#line.
    def visitLine(self, ctx:zoiaParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by zoiaParser#lineElements.
    def visitLineElements(self, ctx:zoiaParser.LineElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by zoiaParser#regularLineElements.
    def visitRegularLineElements(self, ctx:zoiaParser.RegularLineElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by zoiaParser#lineElement.
    def visitLineElement(self, ctx:zoiaParser.LineElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by zoiaParser#markedUpLineElements.
    def visitMarkedUpLineElements(self, ctx:zoiaParser.MarkedUpLineElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by zoiaParser#boldItalicLineElements.
    def visitBoldItalicLineElements(self, ctx:zoiaParser.BoldItalicLineElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by zoiaParser#boldLineElements.
    def visitBoldLineElements(self, ctx:zoiaParser.BoldLineElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by zoiaParser#italicLineElements.
    def visitItalicLineElements(self, ctx:zoiaParser.ItalicLineElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by zoiaParser#textFragment.
    def visitTextFragment(self, ctx:zoiaParser.TextFragmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by zoiaParser#word.
    def visitWord(self, ctx:zoiaParser.WordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by zoiaParser#alias.
    def visitAlias(self, ctx:zoiaParser.AliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by zoiaParser#command.
    def visitCommand(self, ctx:zoiaParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by zoiaParser#arguments.
    def visitArguments(self, ctx:zoiaParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by zoiaParser#argument.
    def visitArgument(self, ctx:zoiaParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by zoiaParser#kwdArgument.
    def visitKwdArgument(self, ctx:zoiaParser.KwdArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by zoiaParser#stdArgument.
    def visitStdArgument(self, ctx:zoiaParser.StdArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by zoiaParser#whitespace.
    def visitWhitespace(self, ctx:zoiaParser.WhitespaceContext):
        return self.visitChildren(ctx)



del zoiaParser