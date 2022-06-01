# Generated from grammar/zoia.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,181,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,1,0,5,0,41,
        8,0,10,0,12,0,44,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,3,2,53,8,2,1,2,
        1,2,1,3,1,3,1,3,1,3,1,3,1,3,4,3,63,8,3,11,3,12,3,64,1,4,1,4,1,4,
        4,4,70,8,4,11,4,12,4,71,1,5,1,5,1,5,1,5,1,5,1,5,3,5,80,8,5,1,5,1,
        5,1,5,1,5,1,5,1,5,5,5,88,8,5,10,5,12,5,91,9,5,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,
        10,3,10,114,8,10,1,10,1,10,3,10,118,8,10,1,11,1,11,3,11,122,8,11,
        1,12,1,12,1,12,3,12,127,8,12,1,13,1,13,1,13,3,13,132,8,13,1,13,3,
        13,135,8,13,1,14,1,14,3,14,139,8,14,1,14,1,14,1,14,3,14,144,8,14,
        1,14,5,14,147,8,14,10,14,12,14,150,9,14,1,14,3,14,153,8,14,1,14,
        3,14,156,8,14,1,14,1,14,1,15,1,15,3,15,162,8,15,1,16,1,16,3,16,166,
        8,16,1,16,1,16,3,16,170,8,16,1,16,1,16,1,17,1,17,1,18,4,18,177,8,
        18,11,18,12,18,178,1,18,1,148,0,19,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,36,0,3,1,0,12,13,2,0,4,4,13,13,2,0,10,10,12,12,
        198,0,38,1,0,0,0,2,47,1,0,0,0,4,52,1,0,0,0,6,62,1,0,0,0,8,69,1,0,
        0,0,10,79,1,0,0,0,12,92,1,0,0,0,14,100,1,0,0,0,16,106,1,0,0,0,18,
        110,1,0,0,0,20,113,1,0,0,0,22,119,1,0,0,0,24,123,1,0,0,0,26,128,
        1,0,0,0,28,136,1,0,0,0,30,161,1,0,0,0,32,163,1,0,0,0,34,173,1,0,
        0,0,36,176,1,0,0,0,38,42,3,2,1,0,39,41,3,4,2,0,40,39,1,0,0,0,41,
        44,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,45,1,0,0,0,44,42,1,0,0,
        0,45,46,5,0,0,1,46,1,1,0,0,0,47,48,5,9,0,0,48,49,3,28,14,0,49,50,
        5,10,0,0,50,3,1,0,0,0,51,53,3,6,3,0,52,51,1,0,0,0,52,53,1,0,0,0,
        53,54,1,0,0,0,54,55,5,10,0,0,55,5,1,0,0,0,56,63,3,18,9,0,57,63,3,
        24,12,0,58,63,3,26,13,0,59,63,3,16,8,0,60,63,3,14,7,0,61,63,3,12,
        6,0,62,56,1,0,0,0,62,57,1,0,0,0,62,58,1,0,0,0,62,59,1,0,0,0,62,60,
        1,0,0,0,62,61,1,0,0,0,63,64,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,
        65,7,1,0,0,0,66,70,3,20,10,0,67,70,3,24,12,0,68,70,3,26,13,0,69,
        66,1,0,0,0,69,67,1,0,0,0,69,68,1,0,0,0,70,71,1,0,0,0,71,69,1,0,0,
        0,71,72,1,0,0,0,72,9,1,0,0,0,73,80,3,22,11,0,74,80,3,24,12,0,75,
        80,3,26,13,0,76,80,3,16,8,0,77,80,3,14,7,0,78,80,3,12,6,0,79,73,
        1,0,0,0,79,74,1,0,0,0,79,75,1,0,0,0,79,76,1,0,0,0,79,77,1,0,0,0,
        79,78,1,0,0,0,80,89,1,0,0,0,81,88,3,18,9,0,82,88,3,24,12,0,83,88,
        3,26,13,0,84,88,3,16,8,0,85,88,3,14,7,0,86,88,3,12,6,0,87,81,1,0,
        0,0,87,82,1,0,0,0,87,83,1,0,0,0,87,84,1,0,0,0,87,85,1,0,0,0,87,86,
        1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,11,1,0,0,0,
        91,89,1,0,0,0,92,93,5,2,0,0,93,94,5,2,0,0,94,95,5,2,0,0,95,96,3,
        8,4,0,96,97,5,2,0,0,97,98,5,2,0,0,98,99,5,2,0,0,99,13,1,0,0,0,100,
        101,5,2,0,0,101,102,5,2,0,0,102,103,3,8,4,0,103,104,5,2,0,0,104,
        105,5,2,0,0,105,15,1,0,0,0,106,107,5,2,0,0,107,108,3,8,4,0,108,109,
        5,2,0,0,109,17,1,0,0,0,110,111,7,0,0,0,111,19,1,0,0,0,112,114,5,
        12,0,0,113,112,1,0,0,0,113,114,1,0,0,0,114,115,1,0,0,0,115,117,5,
        13,0,0,116,118,5,12,0,0,117,116,1,0,0,0,117,118,1,0,0,0,118,21,1,
        0,0,0,119,121,5,13,0,0,120,122,5,12,0,0,121,120,1,0,0,0,121,122,
        1,0,0,0,122,23,1,0,0,0,123,124,5,3,0,0,124,126,5,13,0,0,125,127,
        5,5,0,0,126,125,1,0,0,0,126,127,1,0,0,0,127,25,1,0,0,0,128,129,5,
        4,0,0,129,131,7,1,0,0,130,132,3,28,14,0,131,130,1,0,0,0,131,132,
        1,0,0,0,132,134,1,0,0,0,133,135,5,5,0,0,134,133,1,0,0,0,134,135,
        1,0,0,0,135,27,1,0,0,0,136,138,5,7,0,0,137,139,3,36,18,0,138,137,
        1,0,0,0,138,139,1,0,0,0,139,140,1,0,0,0,140,148,3,30,15,0,141,143,
        5,11,0,0,142,144,3,36,18,0,143,142,1,0,0,0,143,144,1,0,0,0,144,145,
        1,0,0,0,145,147,3,30,15,0,146,141,1,0,0,0,147,150,1,0,0,0,148,149,
        1,0,0,0,148,146,1,0,0,0,149,152,1,0,0,0,150,148,1,0,0,0,151,153,
        5,11,0,0,152,151,1,0,0,0,152,153,1,0,0,0,153,155,1,0,0,0,154,156,
        3,36,18,0,155,154,1,0,0,0,155,156,1,0,0,0,156,157,1,0,0,0,157,158,
        5,6,0,0,158,29,1,0,0,0,159,162,3,32,16,0,160,162,3,34,17,0,161,159,
        1,0,0,0,161,160,1,0,0,0,162,31,1,0,0,0,163,165,5,13,0,0,164,166,
        5,12,0,0,165,164,1,0,0,0,165,166,1,0,0,0,166,167,1,0,0,0,167,169,
        5,8,0,0,168,170,5,12,0,0,169,168,1,0,0,0,169,170,1,0,0,0,170,171,
        1,0,0,0,171,172,3,10,5,0,172,33,1,0,0,0,173,174,3,10,5,0,174,35,
        1,0,0,0,175,177,7,2,0,0,176,175,1,0,0,0,177,178,1,0,0,0,178,176,
        1,0,0,0,178,179,1,0,0,0,179,37,1,0,0,0,24,42,52,62,64,69,71,79,87,
        89,113,117,121,126,131,134,138,143,148,152,155,161,165,169,178
    ]

class zoiaParser ( Parser ):

    grammarFileName = "zoia.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'*'", "'@'", "'\\'", "'|'",
                     "']'", "'['", "'='", "'\\header'", "<INVALID>", "';'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "Asterisk", "At", "Backslash",
                      "Bar", "BracketsClose", "BracketsOpen", "Equals",
                      "Header", "Newline", "Semicolon", "Spaces", "Word" ]

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
    RULE_textFragmentReq = 10
    RULE_textFragmentWord = 11
    RULE_alias = 12
    RULE_command = 13
    RULE_arguments = 14
    RULE_argument = 15
    RULE_kwdArgument = 16
    RULE_stdArgument = 17
    RULE_whitespace = 18

    ruleNames =  [ "zoiaFile", "header", "line", "lineElements", "lineElementsInner",
                   "lineElementsArg", "em3LineElement", "em2LineElement",
                   "em1LineElement", "textFragment", "textFragmentReq",
                   "textFragmentWord", "alias", "command", "arguments",
                   "argument", "kwdArgument", "stdArgument", "whitespace" ]

    EOF = Token.EOF
    COMMENT=1
    Asterisk=2
    At=3
    Backslash=4
    Bar=5
    BracketsClose=6
    BracketsOpen=7
    Equals=8
    Header=9
    Newline=10
    Semicolon=11
    Spaces=12
    Word=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
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
            self.state = 38
            self.header()
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << zoiaParser.Asterisk) | (1 << zoiaParser.At) | (1 << zoiaParser.Backslash) | (1 << zoiaParser.Newline) | (1 << zoiaParser.Spaces) | (1 << zoiaParser.Word))) != 0):
                self.state = 39
                self.line()
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 45
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
            self.state = 47
            self.match(zoiaParser.Header)
            self.state = 48
            self.arguments()
            self.state = 49
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
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << zoiaParser.Asterisk) | (1 << zoiaParser.At) | (1 << zoiaParser.Backslash) | (1 << zoiaParser.Spaces) | (1 << zoiaParser.Word))) != 0):
                self.state = 51
                self.lineElements()


            self.state = 54
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
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 62
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 56
                    self.textFragment()
                    pass

                elif la_ == 2:
                    self.state = 57
                    self.alias()
                    pass

                elif la_ == 3:
                    self.state = 58
                    self.command()
                    pass

                elif la_ == 4:
                    self.state = 59
                    self.em1LineElement()
                    pass

                elif la_ == 5:
                    self.state = 60
                    self.em2LineElement()
                    pass

                elif la_ == 6:
                    self.state = 61
                    self.em3LineElement()
                    pass


                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << zoiaParser.Asterisk) | (1 << zoiaParser.At) | (1 << zoiaParser.Backslash) | (1 << zoiaParser.Spaces) | (1 << zoiaParser.Word))) != 0)):
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

        def textFragmentReq(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(zoiaParser.TextFragmentReqContext)
            else:
                return self.getTypedRuleContext(zoiaParser.TextFragmentReqContext,i)


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
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 69
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [zoiaParser.Spaces, zoiaParser.Word]:
                    self.state = 66
                    self.textFragmentReq()
                    pass
                elif token in [zoiaParser.At]:
                    self.state = 67
                    self.alias()
                    pass
                elif token in [zoiaParser.Backslash]:
                    self.state = 68
                    self.command()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << zoiaParser.At) | (1 << zoiaParser.Backslash) | (1 << zoiaParser.Spaces) | (1 << zoiaParser.Word))) != 0)):
                    break

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
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 73
                self.textFragmentWord()
                pass

            elif la_ == 2:
                self.state = 74
                self.alias()
                pass

            elif la_ == 3:
                self.state = 75
                self.command()
                pass

            elif la_ == 4:
                self.state = 76
                self.em1LineElement()
                pass

            elif la_ == 5:
                self.state = 77
                self.em2LineElement()
                pass

            elif la_ == 6:
                self.state = 78
                self.em3LineElement()
                pass


            self.state = 89
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 87
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        self.state = 81
                        self.textFragment()
                        pass

                    elif la_ == 2:
                        self.state = 82
                        self.alias()
                        pass

                    elif la_ == 3:
                        self.state = 83
                        self.command()
                        pass

                    elif la_ == 4:
                        self.state = 84
                        self.em1LineElement()
                        pass

                    elif la_ == 5:
                        self.state = 85
                        self.em2LineElement()
                        pass

                    elif la_ == 6:
                        self.state = 86
                        self.em3LineElement()
                        pass


                self.state = 91
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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
            self.state = 92
            self.match(zoiaParser.Asterisk)
            self.state = 93
            self.match(zoiaParser.Asterisk)
            self.state = 94
            self.match(zoiaParser.Asterisk)
            self.state = 95
            self.lineElementsInner()
            self.state = 96
            self.match(zoiaParser.Asterisk)
            self.state = 97
            self.match(zoiaParser.Asterisk)
            self.state = 98
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
            self.state = 100
            self.match(zoiaParser.Asterisk)
            self.state = 101
            self.match(zoiaParser.Asterisk)
            self.state = 102
            self.lineElementsInner()
            self.state = 103
            self.match(zoiaParser.Asterisk)
            self.state = 104
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
            self.state = 106
            self.match(zoiaParser.Asterisk)
            self.state = 107
            self.lineElementsInner()
            self.state = 108
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
            self.state = 110
            _la = self._input.LA(1)
            if not(_la==zoiaParser.Spaces or _la==zoiaParser.Word):
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


    class TextFragmentReqContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Word(self):
            return self.getToken(zoiaParser.Word, 0)

        def Spaces(self, i:int=None):
            if i is None:
                return self.getTokens(zoiaParser.Spaces)
            else:
                return self.getToken(zoiaParser.Spaces, i)

        def getRuleIndex(self):
            return zoiaParser.RULE_textFragmentReq

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTextFragmentReq" ):
                return visitor.visitTextFragmentReq(self)
            else:
                return visitor.visitChildren(self)




    def textFragmentReq(self):

        localctx = zoiaParser.TextFragmentReqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_textFragmentReq)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==zoiaParser.Spaces:
                self.state = 112
                self.match(zoiaParser.Spaces)


            self.state = 115
            self.match(zoiaParser.Word)
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 116
                self.match(zoiaParser.Spaces)


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

        def Spaces(self):
            return self.getToken(zoiaParser.Spaces, 0)

        def getRuleIndex(self):
            return zoiaParser.RULE_textFragmentWord

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTextFragmentWord" ):
                return visitor.visitTextFragmentWord(self)
            else:
                return visitor.visitChildren(self)




    def textFragmentWord(self):

        localctx = zoiaParser.TextFragmentWordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_textFragmentWord)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(zoiaParser.Word)
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 120
                self.match(zoiaParser.Spaces)


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

        def At(self):
            return self.getToken(zoiaParser.At, 0)

        def Word(self):
            return self.getToken(zoiaParser.Word, 0)

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
        self.enterRule(localctx, 24, self.RULE_alias)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(zoiaParser.At)
            self.state = 124
            self.match(zoiaParser.Word)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==zoiaParser.Bar:
                self.state = 125
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
        self.enterRule(localctx, 26, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(zoiaParser.Backslash)
            self.state = 129
            _la = self._input.LA(1)
            if not(_la==zoiaParser.Backslash or _la==zoiaParser.Word):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==zoiaParser.BracketsOpen:
                self.state = 130
                self.arguments()


            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==zoiaParser.Bar:
                self.state = 133
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
        self.enterRule(localctx, 28, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(zoiaParser.BracketsOpen)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==zoiaParser.Newline or _la==zoiaParser.Spaces:
                self.state = 137
                self.whitespace()


            self.state = 140
            self.argument()
            self.state = 148
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 141
                    self.match(zoiaParser.Semicolon)
                    self.state = 143
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==zoiaParser.Newline or _la==zoiaParser.Spaces:
                        self.state = 142
                        self.whitespace()


                    self.state = 145
                    self.argument()
                self.state = 150
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==zoiaParser.Semicolon:
                self.state = 151
                self.match(zoiaParser.Semicolon)


            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==zoiaParser.Newline or _la==zoiaParser.Spaces:
                self.state = 154
                self.whitespace()


            self.state = 157
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
        self.enterRule(localctx, 30, self.RULE_argument)
        try:
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.kwdArgument()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
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
        self.enterRule(localctx, 32, self.RULE_kwdArgument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(zoiaParser.Word)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==zoiaParser.Spaces:
                self.state = 164
                self.match(zoiaParser.Spaces)


            self.state = 167
            self.match(zoiaParser.Equals)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==zoiaParser.Spaces:
                self.state = 168
                self.match(zoiaParser.Spaces)


            self.state = 171
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
        self.enterRule(localctx, 34, self.RULE_stdArgument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
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
        self.enterRule(localctx, 36, self.RULE_whitespace)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 175
                _la = self._input.LA(1)
                if not(_la==zoiaParser.Newline or _la==zoiaParser.Spaces):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==zoiaParser.Newline or _la==zoiaParser.Spaces):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
