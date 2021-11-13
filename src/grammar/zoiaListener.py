# Generated from grammar/zoia.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .zoiaParser import zoiaParser
else:
    from zoiaParser import zoiaParser

# This class defines a complete listener for a parse tree produced by zoiaParser.
class zoiaListener(ParseTreeListener):

    # Enter a parse tree produced by zoiaParser#zoiaFile.
    def enterZoiaFile(self, ctx:zoiaParser.ZoiaFileContext):
        pass

    # Exit a parse tree produced by zoiaParser#zoiaFile.
    def exitZoiaFile(self, ctx:zoiaParser.ZoiaFileContext):
        pass


    # Enter a parse tree produced by zoiaParser#header.
    def enterHeader(self, ctx:zoiaParser.HeaderContext):
        pass

    # Exit a parse tree produced by zoiaParser#header.
    def exitHeader(self, ctx:zoiaParser.HeaderContext):
        pass


    # Enter a parse tree produced by zoiaParser#line.
    def enterLine(self, ctx:zoiaParser.LineContext):
        pass

    # Exit a parse tree produced by zoiaParser#line.
    def exitLine(self, ctx:zoiaParser.LineContext):
        pass


    # Enter a parse tree produced by zoiaParser#lineElement.
    def enterLineElement(self, ctx:zoiaParser.LineElementContext):
        pass

    # Exit a parse tree produced by zoiaParser#lineElement.
    def exitLineElement(self, ctx:zoiaParser.LineElementContext):
        pass


    # Enter a parse tree produced by zoiaParser#textFragment.
    def enterTextFragment(self, ctx:zoiaParser.TextFragmentContext):
        pass

    # Exit a parse tree produced by zoiaParser#textFragment.
    def exitTextFragment(self, ctx:zoiaParser.TextFragmentContext):
        pass


    # Enter a parse tree produced by zoiaParser#word.
    def enterWord(self, ctx:zoiaParser.WordContext):
        pass

    # Exit a parse tree produced by zoiaParser#word.
    def exitWord(self, ctx:zoiaParser.WordContext):
        pass


    # Enter a parse tree produced by zoiaParser#alias.
    def enterAlias(self, ctx:zoiaParser.AliasContext):
        pass

    # Exit a parse tree produced by zoiaParser#alias.
    def exitAlias(self, ctx:zoiaParser.AliasContext):
        pass


    # Enter a parse tree produced by zoiaParser#command.
    def enterCommand(self, ctx:zoiaParser.CommandContext):
        pass

    # Exit a parse tree produced by zoiaParser#command.
    def exitCommand(self, ctx:zoiaParser.CommandContext):
        pass


    # Enter a parse tree produced by zoiaParser#arguments.
    def enterArguments(self, ctx:zoiaParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by zoiaParser#arguments.
    def exitArguments(self, ctx:zoiaParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by zoiaParser#argument.
    def enterArgument(self, ctx:zoiaParser.ArgumentContext):
        pass

    # Exit a parse tree produced by zoiaParser#argument.
    def exitArgument(self, ctx:zoiaParser.ArgumentContext):
        pass


    # Enter a parse tree produced by zoiaParser#kwdArgument.
    def enterKwdArgument(self, ctx:zoiaParser.KwdArgumentContext):
        pass

    # Exit a parse tree produced by zoiaParser#kwdArgument.
    def exitKwdArgument(self, ctx:zoiaParser.KwdArgumentContext):
        pass


    # Enter a parse tree produced by zoiaParser#stdArgument.
    def enterStdArgument(self, ctx:zoiaParser.StdArgumentContext):
        pass

    # Exit a parse tree produced by zoiaParser#stdArgument.
    def exitStdArgument(self, ctx:zoiaParser.StdArgumentContext):
        pass


    # Enter a parse tree produced by zoiaParser#whitespace.
    def enterWhitespace(self, ctx:zoiaParser.WhitespaceContext):
        pass

    # Exit a parse tree produced by zoiaParser#whitespace.
    def exitWhitespace(self, ctx:zoiaParser.WhitespaceContext):
        pass



del zoiaParser