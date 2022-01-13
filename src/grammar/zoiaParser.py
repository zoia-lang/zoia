# Generated from grammar/zoia.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("\u009a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\3\2")
        buf.write("\7\2\'\n\2\f\2\16\2*\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4")
        buf.write("\5\4\63\n\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\6\5=\n\5\r")
        buf.write("\5\16\5>\3\6\3\6\3\6\6\6D\n\6\r\6\16\6E\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\t\3\n\3\n\3\13\5\13]\n\13\3\13\3\13\5\13a\n\13\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\5\ri\n\r\3\r\5\rl\n\r\3\16\3\16\5")
        buf.write("\16p\n\16\3\16\3\16\3\16\5\16u\n\16\3\16\7\16x\n\16\f")
        buf.write("\16\16\16{\13\16\3\16\5\16~\n\16\3\16\5\16\u0081\n\16")
        buf.write("\3\16\3\16\3\17\3\17\5\17\u0087\n\17\3\20\3\20\5\20\u008b")
        buf.write("\n\20\3\20\3\20\5\20\u008f\n\20\3\20\3\20\3\21\3\21\3")
        buf.write("\22\6\22\u0096\n\22\r\22\16\22\u0097\3\22\3y\2\23\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\32\34\36 \"\2\4\3\2\16\17\4")
        buf.write("\2\f\f\16\16\2\u00a0\2$\3\2\2\2\4-\3\2\2\2\6\62\3\2\2")
        buf.write("\2\b<\3\2\2\2\nC\3\2\2\2\fG\3\2\2\2\16O\3\2\2\2\20U\3")
        buf.write("\2\2\2\22Y\3\2\2\2\24\\\3\2\2\2\26b\3\2\2\2\30e\3\2\2")
        buf.write("\2\32m\3\2\2\2\34\u0086\3\2\2\2\36\u0088\3\2\2\2 \u0092")
        buf.write("\3\2\2\2\"\u0095\3\2\2\2$(\5\4\3\2%\'\5\6\4\2&%\3\2\2")
        buf.write("\2\'*\3\2\2\2(&\3\2\2\2()\3\2\2\2)+\3\2\2\2*(\3\2\2\2")
        buf.write("+,\7\2\2\3,\3\3\2\2\2-.\7\13\2\2./\5\32\16\2/\60\7\f\2")
        buf.write("\2\60\5\3\2\2\2\61\63\5\b\5\2\62\61\3\2\2\2\62\63\3\2")
        buf.write("\2\2\63\64\3\2\2\2\64\65\7\f\2\2\65\7\3\2\2\2\66=\5\22")
        buf.write("\n\2\67=\5\26\f\28=\5\30\r\29=\5\20\t\2:=\5\16\b\2;=\5")
        buf.write("\f\7\2<\66\3\2\2\2<\67\3\2\2\2<8\3\2\2\2<9\3\2\2\2<:\3")
        buf.write("\2\2\2<;\3\2\2\2=>\3\2\2\2><\3\2\2\2>?\3\2\2\2?\t\3\2")
        buf.write("\2\2@D\5\24\13\2AD\5\26\f\2BD\5\30\r\2C@\3\2\2\2CA\3\2")
        buf.write("\2\2CB\3\2\2\2DE\3\2\2\2EC\3\2\2\2EF\3\2\2\2F\13\3\2\2")
        buf.write("\2GH\7\4\2\2HI\7\4\2\2IJ\7\4\2\2JK\5\n\6\2KL\7\4\2\2L")
        buf.write("M\7\4\2\2MN\7\4\2\2N\r\3\2\2\2OP\7\4\2\2PQ\7\4\2\2QR\5")
        buf.write("\n\6\2RS\7\4\2\2ST\7\4\2\2T\17\3\2\2\2UV\7\4\2\2VW\5\n")
        buf.write("\6\2WX\7\4\2\2X\21\3\2\2\2YZ\t\2\2\2Z\23\3\2\2\2[]\7\16")
        buf.write("\2\2\\[\3\2\2\2\\]\3\2\2\2]^\3\2\2\2^`\7\17\2\2_a\7\16")
        buf.write("\2\2`_\3\2\2\2`a\3\2\2\2a\25\3\2\2\2bc\7\5\2\2cd\7\17")
        buf.write("\2\2d\27\3\2\2\2ef\7\6\2\2fh\7\17\2\2gi\5\32\16\2hg\3")
        buf.write("\2\2\2hi\3\2\2\2ik\3\2\2\2jl\7\7\2\2kj\3\2\2\2kl\3\2\2")
        buf.write("\2l\31\3\2\2\2mo\7\t\2\2np\5\"\22\2on\3\2\2\2op\3\2\2")
        buf.write("\2pq\3\2\2\2qy\5\34\17\2rt\7\r\2\2su\5\"\22\2ts\3\2\2")
        buf.write("\2tu\3\2\2\2uv\3\2\2\2vx\5\34\17\2wr\3\2\2\2x{\3\2\2\2")
        buf.write("yz\3\2\2\2yw\3\2\2\2z}\3\2\2\2{y\3\2\2\2|~\7\r\2\2}|\3")
        buf.write("\2\2\2}~\3\2\2\2~\u0080\3\2\2\2\177\u0081\5\"\22\2\u0080")
        buf.write("\177\3\2\2\2\u0080\u0081\3\2\2\2\u0081\u0082\3\2\2\2\u0082")
        buf.write("\u0083\7\b\2\2\u0083\33\3\2\2\2\u0084\u0087\5\36\20\2")
        buf.write("\u0085\u0087\5 \21\2\u0086\u0084\3\2\2\2\u0086\u0085\3")
        buf.write("\2\2\2\u0087\35\3\2\2\2\u0088\u008a\7\17\2\2\u0089\u008b")
        buf.write("\7\16\2\2\u008a\u0089\3\2\2\2\u008a\u008b\3\2\2\2\u008b")
        buf.write("\u008c\3\2\2\2\u008c\u008e\7\n\2\2\u008d\u008f\7\16\2")
        buf.write("\2\u008e\u008d\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0090")
        buf.write("\3\2\2\2\u0090\u0091\5\b\5\2\u0091\37\3\2\2\2\u0092\u0093")
        buf.write("\5\b\5\2\u0093!\3\2\2\2\u0094\u0096\t\3\2\2\u0095\u0094")
        buf.write("\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0095\3\2\2\2\u0097")
        buf.write("\u0098\3\2\2\2\u0098#\3\2\2\2\25(\62<>CE\\`hkoty}\u0080")
        buf.write("\u0086\u008a\u008e\u0097")
        return buf.getvalue()


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
    RULE_em3LineElement = 5
    RULE_em2LineElement = 6
    RULE_em1LineElement = 7
    RULE_textFragment = 8
    RULE_textFragmentReq = 9
    RULE_alias = 10
    RULE_command = 11
    RULE_arguments = 12
    RULE_argument = 13
    RULE_kwdArgument = 14
    RULE_stdArgument = 15
    RULE_whitespace = 16

    ruleNames =  [ "zoiaFile", "header", "line", "lineElements", "lineElementsInner",
                   "em3LineElement", "em2LineElement", "em1LineElement",
                   "textFragment", "textFragmentReq", "alias", "command",
                   "arguments", "argument", "kwdArgument", "stdArgument",
                   "whitespace" ]

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
        self.checkVersion("4.9.3")
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
            self.state = 34
            self.header()
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << zoiaParser.Asterisk) | (1 << zoiaParser.At) | (1 << zoiaParser.Backslash) | (1 << zoiaParser.Newline) | (1 << zoiaParser.Spaces) | (1 << zoiaParser.Word))) != 0):
                self.state = 35
                self.line()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 41
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
            self.state = 43
            self.match(zoiaParser.Header)
            self.state = 44
            self.arguments()
            self.state = 45
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
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << zoiaParser.Asterisk) | (1 << zoiaParser.At) | (1 << zoiaParser.Backslash) | (1 << zoiaParser.Spaces) | (1 << zoiaParser.Word))) != 0):
                self.state = 47
                self.lineElements()


            self.state = 50
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 58
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        self.state = 52
                        self.textFragment()
                        pass

                    elif la_ == 2:
                        self.state = 53
                        self.alias()
                        pass

                    elif la_ == 3:
                        self.state = 54
                        self.command()
                        pass

                    elif la_ == 4:
                        self.state = 55
                        self.em1LineElement()
                        pass

                    elif la_ == 5:
                        self.state = 56
                        self.em2LineElement()
                        pass

                    elif la_ == 6:
                        self.state = 57
                        self.em3LineElement()
                        pass



                else:
                    raise NoViableAltException(self)
                self.state = 60
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 65
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [zoiaParser.Spaces, zoiaParser.Word]:
                    self.state = 62
                    self.textFragmentReq()
                    pass
                elif token in [zoiaParser.At]:
                    self.state = 63
                    self.alias()
                    pass
                elif token in [zoiaParser.Backslash]:
                    self.state = 64
                    self.command()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 67
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
        self.enterRule(localctx, 10, self.RULE_em3LineElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(zoiaParser.Asterisk)
            self.state = 70
            self.match(zoiaParser.Asterisk)
            self.state = 71
            self.match(zoiaParser.Asterisk)
            self.state = 72
            self.lineElementsInner()
            self.state = 73
            self.match(zoiaParser.Asterisk)
            self.state = 74
            self.match(zoiaParser.Asterisk)
            self.state = 75
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
        self.enterRule(localctx, 12, self.RULE_em2LineElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(zoiaParser.Asterisk)
            self.state = 78
            self.match(zoiaParser.Asterisk)
            self.state = 79
            self.lineElementsInner()
            self.state = 80
            self.match(zoiaParser.Asterisk)
            self.state = 81
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
        self.enterRule(localctx, 14, self.RULE_em1LineElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(zoiaParser.Asterisk)
            self.state = 84
            self.lineElementsInner()
            self.state = 85
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
        self.enterRule(localctx, 16, self.RULE_textFragment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
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
        self.enterRule(localctx, 18, self.RULE_textFragmentReq)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==zoiaParser.Spaces:
                self.state = 89
                self.match(zoiaParser.Spaces)


            self.state = 92
            self.match(zoiaParser.Word)
            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 93
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

        def getRuleIndex(self):
            return zoiaParser.RULE_alias

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlias" ):
                return visitor.visitAlias(self)
            else:
                return visitor.visitChildren(self)




    def alias(self):

        localctx = zoiaParser.AliasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_alias)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(zoiaParser.At)
            self.state = 97
            self.match(zoiaParser.Word)
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

        def Backslash(self):
            return self.getToken(zoiaParser.Backslash, 0)

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
        self.enterRule(localctx, 22, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(zoiaParser.Backslash)
            self.state = 100
            self.match(zoiaParser.Word)
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==zoiaParser.BracketsOpen:
                self.state = 101
                self.arguments()


            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==zoiaParser.Bar:
                self.state = 104
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
        self.enterRule(localctx, 24, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(zoiaParser.BracketsOpen)
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 108
                self.whitespace()


            self.state = 111
            self.argument()
            self.state = 119
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 112
                    self.match(zoiaParser.Semicolon)
                    self.state = 114
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        self.state = 113
                        self.whitespace()


                    self.state = 116
                    self.argument()
                self.state = 121
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==zoiaParser.Semicolon:
                self.state = 122
                self.match(zoiaParser.Semicolon)


            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==zoiaParser.Newline or _la==zoiaParser.Spaces:
                self.state = 125
                self.whitespace()


            self.state = 128
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
        self.enterRule(localctx, 26, self.RULE_argument)
        try:
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.kwdArgument()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
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

        def lineElements(self):
            return self.getTypedRuleContext(zoiaParser.LineElementsContext,0)


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
        self.enterRule(localctx, 28, self.RULE_kwdArgument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(zoiaParser.Word)
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==zoiaParser.Spaces:
                self.state = 135
                self.match(zoiaParser.Spaces)


            self.state = 138
            self.match(zoiaParser.Equals)
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 139
                self.match(zoiaParser.Spaces)


            self.state = 142
            self.lineElements()
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

        def lineElements(self):
            return self.getTypedRuleContext(zoiaParser.LineElementsContext,0)


        def getRuleIndex(self):
            return zoiaParser.RULE_stdArgument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStdArgument" ):
                return visitor.visitStdArgument(self)
            else:
                return visitor.visitChildren(self)




    def stdArgument(self):

        localctx = zoiaParser.StdArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_stdArgument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.lineElements()
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
        self.enterRule(localctx, 32, self.RULE_whitespace)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 146
                    _la = self._input.LA(1)
                    if not(_la==zoiaParser.Newline or _la==zoiaParser.Spaces):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 149
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
