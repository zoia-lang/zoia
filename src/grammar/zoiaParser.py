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
        buf.write("\u00ab\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\3\2\3\2\7\2)\n\2\f\2\16\2,\13\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\3\4\5\4\65\n\4\3\4\3\4\3\5\3\5\6\5;\n\5\r\5\16\5<\3")
        buf.write("\6\6\6@\n\6\r\6\16\6A\3\7\3\7\3\7\5\7G\n\7\3\b\3\b\3\b")
        buf.write("\5\bL\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\6\fa\n\f\r\f\16\f")
        buf.write("b\3\r\3\r\3\r\3\16\3\16\3\16\5\16k\n\16\3\16\5\16n\n\16")
        buf.write("\3\17\3\17\7\17r\n\17\f\17\16\17u\13\17\3\17\3\17\3\17")
        buf.write("\7\17z\n\17\f\17\16\17}\13\17\3\17\7\17\u0080\n\17\f\17")
        buf.write("\16\17\u0083\13\17\3\17\5\17\u0086\n\17\3\17\7\17\u0089")
        buf.write("\n\17\f\17\16\17\u008c\13\17\3\17\3\17\3\20\3\20\5\20")
        buf.write("\u0092\n\20\3\21\3\21\7\21\u0096\n\21\f\21\16\21\u0099")
        buf.write("\13\21\3\21\3\21\7\21\u009d\n\21\f\21\16\21\u00a0\13\21")
        buf.write("\3\21\3\21\3\22\3\22\3\23\6\23\u00a7\n\23\r\23\16\23\u00a8")
        buf.write("\3\23\3\u0081\2\24\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$\2\4\3\2\16\17\4\2\f\f\16\16\2\u00ad\2&\3\2\2\2")
        buf.write("\4/\3\2\2\2\6\64\3\2\2\2\b:\3\2\2\2\n?\3\2\2\2\fF\3\2")
        buf.write("\2\2\16K\3\2\2\2\20M\3\2\2\2\22U\3\2\2\2\24[\3\2\2\2\26")
        buf.write("`\3\2\2\2\30d\3\2\2\2\32g\3\2\2\2\34o\3\2\2\2\36\u0091")
        buf.write("\3\2\2\2 \u0093\3\2\2\2\"\u00a3\3\2\2\2$\u00a6\3\2\2\2")
        buf.write("&*\5\4\3\2\')\5\6\4\2(\'\3\2\2\2),\3\2\2\2*(\3\2\2\2*")
        buf.write("+\3\2\2\2+-\3\2\2\2,*\3\2\2\2-.\7\2\2\3.\3\3\2\2\2/\60")
        buf.write("\7\13\2\2\60\61\5\34\17\2\61\62\7\f\2\2\62\5\3\2\2\2\63")
        buf.write("\65\5\b\5\2\64\63\3\2\2\2\64\65\3\2\2\2\65\66\3\2\2\2")
        buf.write("\66\67\7\f\2\2\67\7\3\2\2\28;\5\16\b\29;\5\n\6\2:8\3\2")
        buf.write("\2\2:9\3\2\2\2;<\3\2\2\2<:\3\2\2\2<=\3\2\2\2=\t\3\2\2")
        buf.write("\2>@\5\f\7\2?>\3\2\2\2@A\3\2\2\2A?\3\2\2\2AB\3\2\2\2B")
        buf.write("\13\3\2\2\2CG\5\26\f\2DG\5\30\r\2EG\5\32\16\2FC\3\2\2")
        buf.write("\2FD\3\2\2\2FE\3\2\2\2G\r\3\2\2\2HL\5\20\t\2IL\5\22\n")
        buf.write("\2JL\5\24\13\2KH\3\2\2\2KI\3\2\2\2KJ\3\2\2\2L\17\3\2\2")
        buf.write("\2MN\7\4\2\2NO\7\4\2\2OP\7\4\2\2PQ\5\n\6\2QR\7\4\2\2R")
        buf.write("S\7\4\2\2ST\7\4\2\2T\21\3\2\2\2UV\7\4\2\2VW\7\4\2\2WX")
        buf.write("\5\n\6\2XY\7\4\2\2YZ\7\4\2\2Z\23\3\2\2\2[\\\7\4\2\2\\")
        buf.write("]\5\n\6\2]^\7\4\2\2^\25\3\2\2\2_a\t\2\2\2`_\3\2\2\2ab")
        buf.write("\3\2\2\2b`\3\2\2\2bc\3\2\2\2c\27\3\2\2\2de\7\5\2\2ef\7")
        buf.write("\17\2\2f\31\3\2\2\2gh\7\6\2\2hj\7\17\2\2ik\5\34\17\2j")
        buf.write("i\3\2\2\2jk\3\2\2\2km\3\2\2\2ln\7\7\2\2ml\3\2\2\2mn\3")
        buf.write("\2\2\2n\33\3\2\2\2os\7\t\2\2pr\5$\23\2qp\3\2\2\2ru\3\2")
        buf.write("\2\2sq\3\2\2\2st\3\2\2\2tv\3\2\2\2us\3\2\2\2v\u0081\5")
        buf.write("\36\20\2w{\7\r\2\2xz\5$\23\2yx\3\2\2\2z}\3\2\2\2{y\3\2")
        buf.write("\2\2{|\3\2\2\2|~\3\2\2\2}{\3\2\2\2~\u0080\5\36\20\2\177")
        buf.write("w\3\2\2\2\u0080\u0083\3\2\2\2\u0081\u0082\3\2\2\2\u0081")
        buf.write("\177\3\2\2\2\u0082\u0085\3\2\2\2\u0083\u0081\3\2\2\2\u0084")
        buf.write("\u0086\7\r\2\2\u0085\u0084\3\2\2\2\u0085\u0086\3\2\2\2")
        buf.write("\u0086\u008a\3\2\2\2\u0087\u0089\5$\23\2\u0088\u0087\3")
        buf.write("\2\2\2\u0089\u008c\3\2\2\2\u008a\u0088\3\2\2\2\u008a\u008b")
        buf.write("\3\2\2\2\u008b\u008d\3\2\2\2\u008c\u008a\3\2\2\2\u008d")
        buf.write("\u008e\7\b\2\2\u008e\35\3\2\2\2\u008f\u0092\5 \21\2\u0090")
        buf.write("\u0092\5\"\22\2\u0091\u008f\3\2\2\2\u0091\u0090\3\2\2")
        buf.write("\2\u0092\37\3\2\2\2\u0093\u0097\7\17\2\2\u0094\u0096\7")
        buf.write("\16\2\2\u0095\u0094\3\2\2\2\u0096\u0099\3\2\2\2\u0097")
        buf.write("\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u009a\3\2\2\2")
        buf.write("\u0099\u0097\3\2\2\2\u009a\u009e\7\n\2\2\u009b\u009d\7")
        buf.write("\16\2\2\u009c\u009b\3\2\2\2\u009d\u00a0\3\2\2\2\u009e")
        buf.write("\u009c\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a1\3\2\2\2")
        buf.write("\u00a0\u009e\3\2\2\2\u00a1\u00a2\5\b\5\2\u00a2!\3\2\2")
        buf.write("\2\u00a3\u00a4\5\b\5\2\u00a4#\3\2\2\2\u00a5\u00a7\t\3")
        buf.write("\2\2\u00a6\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00a6")
        buf.write("\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9%\3\2\2\2\25*\64:<A")
        buf.write("FKbjms{\u0081\u0085\u008a\u0091\u0097\u009e\u00a8")
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
                      "Header", "Newline", "Semicolon", "Space", "Word" ]

    RULE_zoiaFile = 0
    RULE_header = 1
    RULE_line = 2
    RULE_lineElements = 3
    RULE_regularLineElements = 4
    RULE_lineElement = 5
    RULE_markedUpLineElements = 6
    RULE_boldItalicLineElements = 7
    RULE_boldLineElements = 8
    RULE_italicLineElements = 9
    RULE_textFragment = 10
    RULE_alias = 11
    RULE_command = 12
    RULE_arguments = 13
    RULE_argument = 14
    RULE_kwdArgument = 15
    RULE_stdArgument = 16
    RULE_whitespace = 17

    ruleNames =  [ "zoiaFile", "header", "line", "lineElements", "regularLineElements",
                   "lineElement", "markedUpLineElements", "boldItalicLineElements",
                   "boldLineElements", "italicLineElements", "textFragment",
                   "alias", "command", "arguments", "argument", "kwdArgument",
                   "stdArgument", "whitespace" ]

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
    Space=12
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
            self.state = 36
            self.header()
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << zoiaParser.Asterisk) | (1 << zoiaParser.At) | (1 << zoiaParser.Backslash) | (1 << zoiaParser.Newline) | (1 << zoiaParser.Space) | (1 << zoiaParser.Word))) != 0):
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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << zoiaParser.Asterisk) | (1 << zoiaParser.At) | (1 << zoiaParser.Backslash) | (1 << zoiaParser.Space) | (1 << zoiaParser.Word))) != 0):
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

        def markedUpLineElements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(zoiaParser.MarkedUpLineElementsContext)
            else:
                return self.getTypedRuleContext(zoiaParser.MarkedUpLineElementsContext,i)


        def regularLineElements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(zoiaParser.RegularLineElementsContext)
            else:
                return self.getTypedRuleContext(zoiaParser.RegularLineElementsContext,i)


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
            self.state = 56
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 56
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [zoiaParser.Asterisk]:
                        self.state = 54
                        self.markedUpLineElements()
                        pass
                    elif token in [zoiaParser.At, zoiaParser.Backslash, zoiaParser.Space, zoiaParser.Word]:
                        self.state = 55
                        self.regularLineElements()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 58
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RegularLineElementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lineElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(zoiaParser.LineElementContext)
            else:
                return self.getTypedRuleContext(zoiaParser.LineElementContext,i)


        def getRuleIndex(self):
            return zoiaParser.RULE_regularLineElements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegularLineElements" ):
                return visitor.visitRegularLineElements(self)
            else:
                return visitor.visitChildren(self)




    def regularLineElements(self):

        localctx = zoiaParser.RegularLineElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_regularLineElements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 60
                    self.lineElement()

                else:
                    raise NoViableAltException(self)
                self.state = 63
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def textFragment(self):
            return self.getTypedRuleContext(zoiaParser.TextFragmentContext,0)


        def alias(self):
            return self.getTypedRuleContext(zoiaParser.AliasContext,0)


        def command(self):
            return self.getTypedRuleContext(zoiaParser.CommandContext,0)


        def getRuleIndex(self):
            return zoiaParser.RULE_lineElement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLineElement" ):
                return visitor.visitLineElement(self)
            else:
                return visitor.visitChildren(self)




    def lineElement(self):

        localctx = zoiaParser.LineElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_lineElement)
        try:
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [zoiaParser.Space, zoiaParser.Word]:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.textFragment()
                pass
            elif token in [zoiaParser.At]:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.alias()
                pass
            elif token in [zoiaParser.Backslash]:
                self.enterOuterAlt(localctx, 3)
                self.state = 67
                self.command()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MarkedUpLineElementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boldItalicLineElements(self):
            return self.getTypedRuleContext(zoiaParser.BoldItalicLineElementsContext,0)


        def boldLineElements(self):
            return self.getTypedRuleContext(zoiaParser.BoldLineElementsContext,0)


        def italicLineElements(self):
            return self.getTypedRuleContext(zoiaParser.ItalicLineElementsContext,0)


        def getRuleIndex(self):
            return zoiaParser.RULE_markedUpLineElements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMarkedUpLineElements" ):
                return visitor.visitMarkedUpLineElements(self)
            else:
                return visitor.visitChildren(self)




    def markedUpLineElements(self):

        localctx = zoiaParser.MarkedUpLineElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_markedUpLineElements)
        try:
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.boldItalicLineElements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.boldLineElements()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 72
                self.italicLineElements()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoldItalicLineElementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Asterisk(self, i:int=None):
            if i is None:
                return self.getTokens(zoiaParser.Asterisk)
            else:
                return self.getToken(zoiaParser.Asterisk, i)

        def regularLineElements(self):
            return self.getTypedRuleContext(zoiaParser.RegularLineElementsContext,0)


        def getRuleIndex(self):
            return zoiaParser.RULE_boldItalicLineElements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoldItalicLineElements" ):
                return visitor.visitBoldItalicLineElements(self)
            else:
                return visitor.visitChildren(self)




    def boldItalicLineElements(self):

        localctx = zoiaParser.BoldItalicLineElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_boldItalicLineElements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(zoiaParser.Asterisk)
            self.state = 76
            self.match(zoiaParser.Asterisk)
            self.state = 77
            self.match(zoiaParser.Asterisk)
            self.state = 78
            self.regularLineElements()
            self.state = 79
            self.match(zoiaParser.Asterisk)
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


    class BoldLineElementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Asterisk(self, i:int=None):
            if i is None:
                return self.getTokens(zoiaParser.Asterisk)
            else:
                return self.getToken(zoiaParser.Asterisk, i)

        def regularLineElements(self):
            return self.getTypedRuleContext(zoiaParser.RegularLineElementsContext,0)


        def getRuleIndex(self):
            return zoiaParser.RULE_boldLineElements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoldLineElements" ):
                return visitor.visitBoldLineElements(self)
            else:
                return visitor.visitChildren(self)




    def boldLineElements(self):

        localctx = zoiaParser.BoldLineElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_boldLineElements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(zoiaParser.Asterisk)
            self.state = 84
            self.match(zoiaParser.Asterisk)
            self.state = 85
            self.regularLineElements()
            self.state = 86
            self.match(zoiaParser.Asterisk)
            self.state = 87
            self.match(zoiaParser.Asterisk)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItalicLineElementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Asterisk(self, i:int=None):
            if i is None:
                return self.getTokens(zoiaParser.Asterisk)
            else:
                return self.getToken(zoiaParser.Asterisk, i)

        def regularLineElements(self):
            return self.getTypedRuleContext(zoiaParser.RegularLineElementsContext,0)


        def getRuleIndex(self):
            return zoiaParser.RULE_italicLineElements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItalicLineElements" ):
                return visitor.visitItalicLineElements(self)
            else:
                return visitor.visitChildren(self)




    def italicLineElements(self):

        localctx = zoiaParser.ItalicLineElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_italicLineElements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(zoiaParser.Asterisk)
            self.state = 90
            self.regularLineElements()
            self.state = 91
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

        def Word(self, i:int=None):
            if i is None:
                return self.getTokens(zoiaParser.Word)
            else:
                return self.getToken(zoiaParser.Word, i)

        def Space(self, i:int=None):
            if i is None:
                return self.getTokens(zoiaParser.Space)
            else:
                return self.getToken(zoiaParser.Space, i)

        def getRuleIndex(self):
            return zoiaParser.RULE_textFragment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTextFragment" ):
                return visitor.visitTextFragment(self)
            else:
                return visitor.visitChildren(self)




    def textFragment(self):

        localctx = zoiaParser.TextFragmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_textFragment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 93
                    _la = self._input.LA(1)
                    if not(_la==zoiaParser.Space or _la==zoiaParser.Word):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 96
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

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
        self.enterRule(localctx, 22, self.RULE_alias)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(zoiaParser.At)
            self.state = 99
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
        self.enterRule(localctx, 24, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(zoiaParser.Backslash)
            self.state = 102
            self.match(zoiaParser.Word)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==zoiaParser.BracketsOpen:
                self.state = 103
                self.arguments()


            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==zoiaParser.Bar:
                self.state = 106
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
            self.state = 109
            self.match(zoiaParser.BracketsOpen)
            self.state = 113
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 110
                    self.whitespace()
                self.state = 115
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 116
            self.argument()
            self.state = 127
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 117
                    self.match(zoiaParser.Semicolon)
                    self.state = 121
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 118
                            self.whitespace()
                        self.state = 123
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                    self.state = 124
                    self.argument()
                self.state = 129
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==zoiaParser.Semicolon:
                self.state = 130
                self.match(zoiaParser.Semicolon)


            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==zoiaParser.Newline or _la==zoiaParser.Space:
                self.state = 133
                self.whitespace()
                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 139
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
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.kwdArgument()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
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


        def Space(self, i:int=None):
            if i is None:
                return self.getTokens(zoiaParser.Space)
            else:
                return self.getToken(zoiaParser.Space, i)

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
            self.state = 145
            self.match(zoiaParser.Word)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==zoiaParser.Space:
                self.state = 146
                self.match(zoiaParser.Space)
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 152
            self.match(zoiaParser.Equals)
            self.state = 156
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 153
                    self.match(zoiaParser.Space)
                self.state = 158
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

            self.state = 159
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
        self.enterRule(localctx, 32, self.RULE_stdArgument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
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

        def Space(self, i:int=None):
            if i is None:
                return self.getTokens(zoiaParser.Space)
            else:
                return self.getToken(zoiaParser.Space, i)

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
            self.state = 164
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 163
                    _la = self._input.LA(1)
                    if not(_la==zoiaParser.Newline or _la==zoiaParser.Space):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 166
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
