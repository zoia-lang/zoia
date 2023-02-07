# Generated from grammar/zoia.g4 by ANTLR 4.11.1
# encoding: utf-8
from _vendor.antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,175,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,5,0,39,8,0,10,0,
        12,0,42,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,3,2,51,8,2,1,2,1,2,1,3,1,
        3,1,3,1,3,1,3,1,3,4,3,61,8,3,11,3,12,3,62,1,4,1,4,1,4,3,4,68,8,4,
        1,4,1,4,1,4,5,4,73,8,4,10,4,12,4,76,9,4,1,5,1,5,1,5,1,5,1,5,1,5,
        3,5,84,8,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,92,8,5,10,5,12,5,95,9,5,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,
        8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,3,11,121,8,11,1,12,1,12,1,12,3,
        12,126,8,12,1,12,3,12,129,8,12,1,13,1,13,3,13,133,8,13,1,13,1,13,
        1,13,3,13,138,8,13,1,13,5,13,141,8,13,10,13,12,13,144,9,13,1,13,
        3,13,147,8,13,1,13,3,13,150,8,13,1,13,1,13,1,14,1,14,3,14,156,8,
        14,1,15,1,15,3,15,160,8,15,1,15,1,15,3,15,164,8,15,1,15,1,15,1,16,
        1,16,1,17,4,17,171,8,17,11,17,12,17,172,1,17,1,142,0,18,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,32,34,0,3,2,0,11,11,13,13,2,0,
        3,3,13,13,2,0,9,9,11,11,192,0,36,1,0,0,0,2,45,1,0,0,0,4,50,1,0,0,
        0,6,60,1,0,0,0,8,67,1,0,0,0,10,83,1,0,0,0,12,96,1,0,0,0,14,104,1,
        0,0,0,16,110,1,0,0,0,18,114,1,0,0,0,20,116,1,0,0,0,22,118,1,0,0,
        0,24,122,1,0,0,0,26,130,1,0,0,0,28,155,1,0,0,0,30,157,1,0,0,0,32,
        167,1,0,0,0,34,170,1,0,0,0,36,40,3,2,1,0,37,39,3,4,2,0,38,37,1,0,
        0,0,39,42,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,43,1,0,0,0,42,40,
        1,0,0,0,43,44,5,0,0,1,44,1,1,0,0,0,45,46,5,8,0,0,46,47,3,26,13,0,
        47,48,5,9,0,0,48,3,1,0,0,0,49,51,3,6,3,0,50,49,1,0,0,0,50,51,1,0,
        0,0,51,52,1,0,0,0,52,53,5,9,0,0,53,5,1,0,0,0,54,61,3,18,9,0,55,61,
        3,22,11,0,56,61,3,24,12,0,57,61,3,16,8,0,58,61,3,14,7,0,59,61,3,
        12,6,0,60,54,1,0,0,0,60,55,1,0,0,0,60,56,1,0,0,0,60,57,1,0,0,0,60,
        58,1,0,0,0,60,59,1,0,0,0,61,62,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,
        0,63,7,1,0,0,0,64,68,3,20,10,0,65,68,3,22,11,0,66,68,3,24,12,0,67,
        64,1,0,0,0,67,65,1,0,0,0,67,66,1,0,0,0,68,74,1,0,0,0,69,73,3,18,
        9,0,70,73,3,22,11,0,71,73,3,24,12,0,72,69,1,0,0,0,72,70,1,0,0,0,
        72,71,1,0,0,0,73,76,1,0,0,0,74,72,1,0,0,0,74,75,1,0,0,0,75,9,1,0,
        0,0,76,74,1,0,0,0,77,84,3,20,10,0,78,84,3,22,11,0,79,84,3,24,12,
        0,80,84,3,16,8,0,81,84,3,14,7,0,82,84,3,12,6,0,83,77,1,0,0,0,83,
        78,1,0,0,0,83,79,1,0,0,0,83,80,1,0,0,0,83,81,1,0,0,0,83,82,1,0,0,
        0,84,93,1,0,0,0,85,92,3,18,9,0,86,92,3,22,11,0,87,92,3,24,12,0,88,
        92,3,16,8,0,89,92,3,14,7,0,90,92,3,12,6,0,91,85,1,0,0,0,91,86,1,
        0,0,0,91,87,1,0,0,0,91,88,1,0,0,0,91,89,1,0,0,0,91,90,1,0,0,0,92,
        95,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,11,1,0,0,0,95,93,1,0,0,
        0,96,97,5,2,0,0,97,98,5,2,0,0,98,99,5,2,0,0,99,100,3,8,4,0,100,101,
        5,2,0,0,101,102,5,2,0,0,102,103,5,2,0,0,103,13,1,0,0,0,104,105,5,
        2,0,0,105,106,5,2,0,0,106,107,3,8,4,0,107,108,5,2,0,0,108,109,5,
        2,0,0,109,15,1,0,0,0,110,111,5,2,0,0,111,112,3,8,4,0,112,113,5,2,
        0,0,113,17,1,0,0,0,114,115,7,0,0,0,115,19,1,0,0,0,116,117,5,13,0,
        0,117,21,1,0,0,0,118,120,5,12,0,0,119,121,5,4,0,0,120,119,1,0,0,
        0,120,121,1,0,0,0,121,23,1,0,0,0,122,123,5,3,0,0,123,125,7,1,0,0,
        124,126,3,26,13,0,125,124,1,0,0,0,125,126,1,0,0,0,126,128,1,0,0,
        0,127,129,5,4,0,0,128,127,1,0,0,0,128,129,1,0,0,0,129,25,1,0,0,0,
        130,132,5,6,0,0,131,133,3,34,17,0,132,131,1,0,0,0,132,133,1,0,0,
        0,133,134,1,0,0,0,134,142,3,28,14,0,135,137,5,10,0,0,136,138,3,34,
        17,0,137,136,1,0,0,0,137,138,1,0,0,0,138,139,1,0,0,0,139,141,3,28,
        14,0,140,135,1,0,0,0,141,144,1,0,0,0,142,143,1,0,0,0,142,140,1,0,
        0,0,143,146,1,0,0,0,144,142,1,0,0,0,145,147,5,10,0,0,146,145,1,0,
        0,0,146,147,1,0,0,0,147,149,1,0,0,0,148,150,3,34,17,0,149,148,1,
        0,0,0,149,150,1,0,0,0,150,151,1,0,0,0,151,152,5,5,0,0,152,27,1,0,
        0,0,153,156,3,30,15,0,154,156,3,32,16,0,155,153,1,0,0,0,155,154,
        1,0,0,0,156,29,1,0,0,0,157,159,5,13,0,0,158,160,5,11,0,0,159,158,
        1,0,0,0,159,160,1,0,0,0,160,161,1,0,0,0,161,163,5,7,0,0,162,164,
        5,11,0,0,163,162,1,0,0,0,163,164,1,0,0,0,164,165,1,0,0,0,165,166,
        3,10,5,0,166,31,1,0,0,0,167,168,3,10,5,0,168,33,1,0,0,0,169,171,
        7,2,0,0,170,169,1,0,0,0,171,172,1,0,0,0,172,170,1,0,0,0,172,173,
        1,0,0,0,173,35,1,0,0,0,22,40,50,60,62,67,72,74,83,91,93,120,125,
        128,132,137,142,146,149,155,159,163,172
    ]

class zoiaParser ( Parser ):

    grammarFileName = "zoia.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'*'", "'\\'", "'|'", "']'",
                     "'['", "'='", "'\\header'", "<INVALID>", "';'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "Asterisk", "Backslash", "Bar",
                      "BracketsClose", "BracketsOpen", "Equals", "Header",
                      "Newline", "Semicolon", "Spaces", "Alias", "Word" ]

    RULE_zoiaFile = 0
    RULE_header = 1
    RULE_line = 2
    RULE_lineElements = 3
    RULE_lineElementsInner = 4
    RULE_lineElementsArg = 5
    RULE_em3LineElement = 6
    RULE_em2LineElement = 7
    RULE_em1LineElement = 8
    RULE_textFragment = 9
    RULE_textFragmentWord = 10
    RULE_alias = 11
    RULE_command = 12
    RULE_arguments = 13
    RULE_argument = 14
    RULE_kwdArgument = 15
    RULE_stdArgument = 16
    RULE_whitespace = 17

    ruleNames =  [ "zoiaFile", "header", "line", "lineElements", "lineElementsInner",
                   "lineElementsArg", "em3LineElement", "em2LineElement",
                   "em1LineElement", "textFragment", "textFragmentWord",
                   "alias", "command", "arguments", "argument", "kwdArgument",
                   "stdArgument", "whitespace" ]

    EOF = Token.EOF
    COMMENT=1
    Asterisk=2
    Backslash=3
    Bar=4
    BracketsClose=5
    BracketsOpen=6
    Equals=7
    Header=8
    Newline=9
    Semicolon=10
    Spaces=11
    Alias=12
    Word=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ZoiaFileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def header(self):
            return self.getTypedRuleContext(zoiaParser.HeaderContext,0)


        def EOF(self):
            return self.getToken(zoiaParser.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(zoiaParser.LineContext)
            else:
                return self.getTypedRuleContext(zoiaParser.LineContext,i)


        def getRuleIndex(self):
            return zoiaParser.RULE_zoiaFile

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitZoiaFile" ):
                return visitor.visitZoiaFile(self)
            else:
                return visitor.visitChildren(self)




    def zoiaFile(self):

        localctx = zoiaParser.ZoiaFileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_zoiaFile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.header()
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 14860) != 0:
                self.state = 37
                self.line()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 43
            self.match(zoiaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HeaderContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Header(self):
            return self.getToken(zoiaParser.Header, 0)

        def arguments(self):
            return self.getTypedRuleContext(zoiaParser.ArgumentsContext,0)


        def Newline(self):
            return self.getToken(zoiaParser.Newline, 0)

        def getRuleIndex(self):
            return zoiaParser.RULE_header

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHeader" ):
                return visitor.visitHeader(self)
            else:
                return visitor.visitChildren(self)




    def header(self):

        localctx = zoiaParser.HeaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(zoiaParser.Header)
            self.state = 46
            self.arguments()
            self.state = 47
            self.match(zoiaParser.Newline)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Newline(self):
            return self.getToken(zoiaParser.Newline, 0)

        def lineElements(self):
            return self.getTypedRuleContext(zoiaParser.LineElementsContext,0)


        def getRuleIndex(self):
            return zoiaParser.RULE_line

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = zoiaParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 14348) != 0:
                self.state = 49
                self.lineElements()


            self.state = 52
            self.match(zoiaParser.Newline)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineElementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def textFragment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(zoiaParser.TextFragmentContext)
            else:
                return self.getTypedRuleContext(zoiaParser.TextFragmentContext,i)


        def alias(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(zoiaParser.AliasContext)
            else:
                return self.getTypedRuleContext(zoiaParser.AliasContext,i)


        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(zoiaParser.CommandContext)
            else:
                return self.getTypedRuleContext(zoiaParser.CommandContext,i)


        def em1LineElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(zoiaParser.Em1LineElementContext)
            else:
                return self.getTypedRuleContext(zoiaParser.Em1LineElementContext,i)


        def em2LineElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(zoiaParser.Em2LineElementContext)
            else:
                return self.getTypedRuleContext(zoiaParser.Em2LineElementContext,i)


        def em3LineElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(zoiaParser.Em3LineElementContext)
            else:
                return self.getTypedRuleContext(zoiaParser.Em3LineElementContext,i)


        def getRuleIndex(self):
            return zoiaParser.RULE_lineElements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLineElements" ):
                return visitor.visitLineElements(self)
            else:
                return visitor.visitChildren(self)




    def lineElements(self):

        localctx = zoiaParser.LineElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_lineElements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 60
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 54
                    self.textFragment()
                    pass

                elif la_ == 2:
                    self.state = 55
                    self.alias()
                    pass

                elif la_ == 3:
                    self.state = 56
                    self.command()
                    pass

                elif la_ == 4:
                    self.state = 57
                    self.em1LineElement()
                    pass

                elif la_ == 5:
                    self.state = 58
                    self.em2LineElement()
                    pass

                elif la_ == 6:
                    self.state = 59
                    self.em3LineElement()
                    pass


                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 14348) != 0):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineElementsInnerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def textFragmentWord(self):
            return self.getTypedRuleContext(zoiaParser.TextFragmentWordContext,0)


        def alias(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(zoiaParser.AliasContext)
            else:
                return self.getTypedRuleContext(zoiaParser.AliasContext,i)


        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(zoiaParser.CommandContext)
            else:
                return self.getTypedRuleContext(zoiaParser.CommandContext,i)


        def textFragment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(zoiaParser.TextFragmentContext)
            else:
                return self.getTypedRuleContext(zoiaParser.TextFragmentContext,i)


        def getRuleIndex(self):
            return zoiaParser.RULE_lineElementsInner

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLineElementsInner" ):
                return visitor.visitLineElementsInner(self)
            else:
                return visitor.visitChildren(self)




    def lineElementsInner(self):

        localctx = zoiaParser.LineElementsInnerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_lineElementsInner)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.state = 64
                self.textFragmentWord()
                pass
            elif token in [12]:
                self.state = 65
                self.alias()
                pass
            elif token in [3]:
                self.state = 66
                self.command()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 14344) != 0:
                self.state = 72
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [11, 13]:
                    self.state = 69
                    self.textFragment()
                    pass
                elif token in [12]:
                    self.state = 70
                    self.alias()
                    pass
                elif token in [3]:
                    self.state = 71
                    self.command()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineElementsArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def textFragmentWord(self):
            return self.getTypedRuleContext(zoiaParser.TextFragmentWordContext,0)


        def alias(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(zoiaParser.AliasContext)
            else:
                return self.getTypedRuleContext(zoiaParser.AliasContext,i)


        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(zoiaParser.CommandContext)
            else:
                return self.getTypedRuleContext(zoiaParser.CommandContext,i)


        def em1LineElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(zoiaParser.Em1LineElementContext)
            else:
                return self.getTypedRuleContext(zoiaParser.Em1LineElementContext,i)


        def em2LineElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(zoiaParser.Em2LineElementContext)
            else:
                return self.getTypedRuleContext(zoiaParser.Em2LineElementContext,i)


        def em3LineElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(zoiaParser.Em3LineElementContext)
            else:
                return self.getTypedRuleContext(zoiaParser.Em3LineElementContext,i)


        def textFragment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(zoiaParser.TextFragmentContext)
            else:
                return self.getTypedRuleContext(zoiaParser.TextFragmentContext,i)


        def getRuleIndex(self):
            return zoiaParser.RULE_lineElementsArg

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLineElementsArg" ):
                return visitor.visitLineElementsArg(self)
            else:
                return visitor.visitChildren(self)




    def lineElementsArg(self):

        localctx = zoiaParser.LineElementsArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_lineElementsArg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 77
                self.textFragmentWord()
                pass

            elif la_ == 2:
                self.state = 78
                self.alias()
                pass

            elif la_ == 3:
                self.state = 79
                self.command()
                pass

            elif la_ == 4:
                self.state = 80
                self.em1LineElement()
                pass

            elif la_ == 5:
                self.state = 81
                self.em2LineElement()
                pass

            elif la_ == 6:
                self.state = 82
                self.em3LineElement()
                pass


            self.state = 93
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 91
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        self.state = 85
                        self.textFragment()
                        pass

                    elif la_ == 2:
                        self.state = 86
                        self.alias()
                        pass

                    elif la_ == 3:
                        self.state = 87
                        self.command()
                        pass

                    elif la_ == 4:
                        self.state = 88
                        self.em1LineElement()
                        pass

                    elif la_ == 5:
                        self.state = 89
                        self.em2LineElement()
                        pass

                    elif la_ == 6:
                        self.state = 90
                        self.em3LineElement()
                        pass


                self.state = 95
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Em3LineElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Asterisk(self, i:int=None):
            if i is None:
                return self.getTokens(zoiaParser.Asterisk)
            else:
                return self.getToken(zoiaParser.Asterisk, i)

        def lineElementsInner(self):
            return self.getTypedRuleContext(zoiaParser.LineElementsInnerContext,0)


        def getRuleIndex(self):
            return zoiaParser.RULE_em3LineElement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEm3LineElement" ):
                return visitor.visitEm3LineElement(self)
            else:
                return visitor.visitChildren(self)




    def em3LineElement(self):

        localctx = zoiaParser.Em3LineElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_em3LineElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(zoiaParser.Asterisk)
            self.state = 97
            self.match(zoiaParser.Asterisk)
            self.state = 98
            self.match(zoiaParser.Asterisk)
            self.state = 99
            self.lineElementsInner()
            self.state = 100
            self.match(zoiaParser.Asterisk)
            self.state = 101
            self.match(zoiaParser.Asterisk)
            self.state = 102
            self.match(zoiaParser.Asterisk)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Em2LineElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Asterisk(self, i:int=None):
            if i is None:
                return self.getTokens(zoiaParser.Asterisk)
            else:
                return self.getToken(zoiaParser.Asterisk, i)

        def lineElementsInner(self):
            return self.getTypedRuleContext(zoiaParser.LineElementsInnerContext,0)


        def getRuleIndex(self):
            return zoiaParser.RULE_em2LineElement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEm2LineElement" ):
                return visitor.visitEm2LineElement(self)
            else:
                return visitor.visitChildren(self)




    def em2LineElement(self):

        localctx = zoiaParser.Em2LineElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_em2LineElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(zoiaParser.Asterisk)
            self.state = 105
            self.match(zoiaParser.Asterisk)
            self.state = 106
            self.lineElementsInner()
            self.state = 107
            self.match(zoiaParser.Asterisk)
            self.state = 108
            self.match(zoiaParser.Asterisk)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Em1LineElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Asterisk(self, i:int=None):
            if i is None:
                return self.getTokens(zoiaParser.Asterisk)
            else:
                return self.getToken(zoiaParser.Asterisk, i)

        def lineElementsInner(self):
            return self.getTypedRuleContext(zoiaParser.LineElementsInnerContext,0)


        def getRuleIndex(self):
            return zoiaParser.RULE_em1LineElement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEm1LineElement" ):
                return visitor.visitEm1LineElement(self)
            else:
                return visitor.visitChildren(self)




    def em1LineElement(self):

        localctx = zoiaParser.Em1LineElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_em1LineElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(zoiaParser.Asterisk)
            self.state = 111
            self.lineElementsInner()
            self.state = 112
            self.match(zoiaParser.Asterisk)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TextFragmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Word(self):
            return self.getToken(zoiaParser.Word, 0)

        def Spaces(self):
            return self.getToken(zoiaParser.Spaces, 0)

        def getRuleIndex(self):
            return zoiaParser.RULE_textFragment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTextFragment" ):
                return visitor.visitTextFragment(self)
            else:
                return visitor.visitChildren(self)




    def textFragment(self):

        localctx = zoiaParser.TextFragmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_textFragment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            _la = self._input.LA(1)
            if not(_la==11 or _la==13):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TextFragmentWordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Word(self):
            return self.getToken(zoiaParser.Word, 0)

        def getRuleIndex(self):
            return zoiaParser.RULE_textFragmentWord

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTextFragmentWord" ):
                return visitor.visitTextFragmentWord(self)
            else:
                return visitor.visitChildren(self)




    def textFragmentWord(self):

        localctx = zoiaParser.TextFragmentWordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_textFragmentWord)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(zoiaParser.Word)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AliasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Alias(self):
            return self.getToken(zoiaParser.Alias, 0)

        def Bar(self):
            return self.getToken(zoiaParser.Bar, 0)

        def getRuleIndex(self):
            return zoiaParser.RULE_alias

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlias" ):
                return visitor.visitAlias(self)
            else:
                return visitor.visitChildren(self)




    def alias(self):

        localctx = zoiaParser.AliasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_alias)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(zoiaParser.Alias)
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 119
                self.match(zoiaParser.Bar)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Backslash(self, i:int=None):
            if i is None:
                return self.getTokens(zoiaParser.Backslash)
            else:
                return self.getToken(zoiaParser.Backslash, i)

        def Word(self):
            return self.getToken(zoiaParser.Word, 0)

        def arguments(self):
            return self.getTypedRuleContext(zoiaParser.ArgumentsContext,0)


        def Bar(self):
            return self.getToken(zoiaParser.Bar, 0)

        def getRuleIndex(self):
            return zoiaParser.RULE_command

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = zoiaParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(zoiaParser.Backslash)
            self.state = 123
            _la = self._input.LA(1)
            if not(_la==3 or _la==13):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 124
                self.arguments()


            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 127
                self.match(zoiaParser.Bar)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BracketsOpen(self):
            return self.getToken(zoiaParser.BracketsOpen, 0)

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(zoiaParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(zoiaParser.ArgumentContext,i)


        def BracketsClose(self):
            return self.getToken(zoiaParser.BracketsClose, 0)

        def whitespace(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(zoiaParser.WhitespaceContext)
            else:
                return self.getTypedRuleContext(zoiaParser.WhitespaceContext,i)


        def Semicolon(self, i:int=None):
            if i is None:
                return self.getTokens(zoiaParser.Semicolon)
            else:
                return self.getToken(zoiaParser.Semicolon, i)

        def getRuleIndex(self):
            return zoiaParser.RULE_arguments

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArguments" ):
                return visitor.visitArguments(self)
            else:
                return visitor.visitChildren(self)




    def arguments(self):

        localctx = zoiaParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(zoiaParser.BracketsOpen)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9 or _la==11:
                self.state = 131
                self.whitespace()


            self.state = 134
            self.argument()
            self.state = 142
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 135
                    self.match(zoiaParser.Semicolon)
                    self.state = 137
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==9 or _la==11:
                        self.state = 136
                        self.whitespace()


                    self.state = 139
                    self.argument()
                self.state = 144
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 145
                self.match(zoiaParser.Semicolon)


            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9 or _la==11:
                self.state = 148
                self.whitespace()


            self.state = 151
            self.match(zoiaParser.BracketsClose)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def kwdArgument(self):
            return self.getTypedRuleContext(zoiaParser.KwdArgumentContext,0)


        def stdArgument(self):
            return self.getTypedRuleContext(zoiaParser.StdArgumentContext,0)


        def getRuleIndex(self):
            return zoiaParser.RULE_argument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = zoiaParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_argument)
        try:
            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.kwdArgument()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.stdArgument()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KwdArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Word(self):
            return self.getToken(zoiaParser.Word, 0)

        def Equals(self):
            return self.getToken(zoiaParser.Equals, 0)

        def lineElementsArg(self):
            return self.getTypedRuleContext(zoiaParser.LineElementsArgContext,0)


        def Spaces(self, i:int=None):
            if i is None:
                return self.getTokens(zoiaParser.Spaces)
            else:
                return self.getToken(zoiaParser.Spaces, i)

        def getRuleIndex(self):
            return zoiaParser.RULE_kwdArgument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKwdArgument" ):
                return visitor.visitKwdArgument(self)
            else:
                return visitor.visitChildren(self)




    def kwdArgument(self):

        localctx = zoiaParser.KwdArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_kwdArgument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(zoiaParser.Word)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 158
                self.match(zoiaParser.Spaces)


            self.state = 161
            self.match(zoiaParser.Equals)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 162
                self.match(zoiaParser.Spaces)


            self.state = 165
            self.lineElementsArg()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StdArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lineElementsArg(self):
            return self.getTypedRuleContext(zoiaParser.LineElementsArgContext,0)


        def getRuleIndex(self):
            return zoiaParser.RULE_stdArgument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStdArgument" ):
                return visitor.visitStdArgument(self)
            else:
                return visitor.visitChildren(self)




    def stdArgument(self):

        localctx = zoiaParser.StdArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_stdArgument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.lineElementsArg()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhitespaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Newline(self, i:int=None):
            if i is None:
                return self.getTokens(zoiaParser.Newline)
            else:
                return self.getToken(zoiaParser.Newline, i)

        def Spaces(self, i:int=None):
            if i is None:
                return self.getTokens(zoiaParser.Spaces)
            else:
                return self.getToken(zoiaParser.Spaces, i)

        def getRuleIndex(self):
            return zoiaParser.RULE_whitespace

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhitespace" ):
                return visitor.visitWhitespace(self)
            else:
                return visitor.visitChildren(self)




    def whitespace(self):

        localctx = zoiaParser.WhitespaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_whitespace)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 169
                _la = self._input.LA(1)
                if not(_la==9 or _la==11):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==9 or _la==11):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
