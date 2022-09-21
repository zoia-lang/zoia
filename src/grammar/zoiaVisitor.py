# Generated from grammar/zoia.g4 by ANTLR 4.11.1
from _vendor.antlr4 import *
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


    # Visit a parse tree produced by zoiaParser#lineElementsInner.
    def visitLineElementsInner(self, ctx:zoiaParser.LineElementsInnerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by zoiaParser#lineElementsArg.
    def visitLineElementsArg(self, ctx:zoiaParser.LineElementsArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by zoiaParser#em3LineElement.
    def visitEm3LineElement(self, ctx:zoiaParser.Em3LineElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by zoiaParser#em2LineElement.
    def visitEm2LineElement(self, ctx:zoiaParser.Em2LineElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by zoiaParser#em1LineElement.
    def visitEm1LineElement(self, ctx:zoiaParser.Em1LineElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by zoiaParser#textFragment.
    def visitTextFragment(self, ctx:zoiaParser.TextFragmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by zoiaParser#textFragmentWord.
    def visitTextFragmentWord(self, ctx:zoiaParser.TextFragmentWordContext):
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