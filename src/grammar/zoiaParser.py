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
        buf.write("\u00b3\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\3\2\7\2+\n\2\f\2\16\2.\13\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\4\5\4\67\n\4\3\4\3\4\3\5\3\5\6\5=\n\5\r")
        buf.write("\5\16\5>\3\6\6\6B\n\6\r\6\16\6C\3\7\3\7\3\7\5\7I\n\7\3")
        buf.write("\b\3\b\3\b\5\bN\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\6\f")
        buf.write("d\n\f\r\f\16\fe\3\r\6\ri\n\r\r\r\16\rj\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\5\17s\n\17\3\17\5\17v\n\17\3\20\3\20\7")
        buf.write("\20z\n\20\f\20\16\20}\13\20\3\20\3\20\3\20\7\20\u0082")
        buf.write("\n\20\f\20\16\20\u0085\13\20\3\20\7\20\u0088\n\20\f\20")
        buf.write("\16\20\u008b\13\20\3\20\5\20\u008e\n\20\3\20\7\20\u0091")
        buf.write("\n\20\f\20\16\20\u0094\13\20\3\20\3\20\3\21\3\21\5\21")
        buf.write("\u009a\n\21\3\22\3\22\7\22\u009e\n\22\f\22\16\22\u00a1")
        buf.write("\13\22\3\22\3\22\7\22\u00a5\n\22\f\22\16\22\u00a8\13\22")
        buf.write("\3\22\3\22\3\23\3\23\3\24\6\24\u00af\n\24\r\24\16\24\u00b0")
        buf.write("\3\24\3\u0089\2\25\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&\2\3\3\2\r\16\2\u00b6\2(\3\2\2\2\4\61\3\2\2\2")
        buf.write("\6\66\3\2\2\2\b<\3\2\2\2\nA\3\2\2\2\fH\3\2\2\2\16M\3\2")
        buf.write("\2\2\20O\3\2\2\2\22W\3\2\2\2\24]\3\2\2\2\26c\3\2\2\2\30")
        buf.write("h\3\2\2\2\32l\3\2\2\2\34o\3\2\2\2\36w\3\2\2\2 \u0099\3")
        buf.write("\2\2\2\"\u009b\3\2\2\2$\u00ab\3\2\2\2&\u00ae\3\2\2\2(")
        buf.write(",\5\4\3\2)+\5\6\4\2*)\3\2\2\2+.\3\2\2\2,*\3\2\2\2,-\3")
        buf.write("\2\2\2-/\3\2\2\2.,\3\2\2\2/\60\7\2\2\3\60\3\3\2\2\2\61")
        buf.write("\62\7\3\2\2\62\63\5\36\20\2\63\64\7\r\2\2\64\5\3\2\2\2")
        buf.write("\65\67\5\b\5\2\66\65\3\2\2\2\66\67\3\2\2\2\678\3\2\2\2")
        buf.write("89\7\r\2\29\7\3\2\2\2:=\5\16\b\2;=\5\n\6\2<:\3\2\2\2<")
        buf.write(";\3\2\2\2=>\3\2\2\2><\3\2\2\2>?\3\2\2\2?\t\3\2\2\2@B\5")
        buf.write("\f\7\2A@\3\2\2\2BC\3\2\2\2CA\3\2\2\2CD\3\2\2\2D\13\3\2")
        buf.write("\2\2EI\5\26\f\2FI\5\32\16\2GI\5\34\17\2HE\3\2\2\2HF\3")
        buf.write("\2\2\2HG\3\2\2\2I\r\3\2\2\2JN\5\20\t\2KN\5\22\n\2LN\5")
        buf.write("\24\13\2MJ\3\2\2\2MK\3\2\2\2ML\3\2\2\2N\17\3\2\2\2OP\7")
        buf.write("\f\2\2PQ\7\f\2\2QR\7\f\2\2RS\5\n\6\2ST\7\f\2\2TU\7\f\2")
        buf.write("\2UV\7\f\2\2V\21\3\2\2\2WX\7\f\2\2XY\7\f\2\2YZ\5\n\6\2")
        buf.write("Z[\7\f\2\2[\\\7\f\2\2\\\23\3\2\2\2]^\7\f\2\2^_\5\n\6\2")
        buf.write("_`\7\f\2\2`\25\3\2\2\2ad\5\30\r\2bd\7\16\2\2ca\3\2\2\2")
        buf.write("cb\3\2\2\2de\3\2\2\2ec\3\2\2\2ef\3\2\2\2f\27\3\2\2\2g")
        buf.write("i\7\17\2\2hg\3\2\2\2ij\3\2\2\2jh\3\2\2\2jk\3\2\2\2k\31")
        buf.write("\3\2\2\2lm\7\4\2\2mn\5\30\r\2n\33\3\2\2\2op\7\5\2\2pr")
        buf.write("\5\30\r\2qs\5\36\20\2rq\3\2\2\2rs\3\2\2\2su\3\2\2\2tv")
        buf.write("\7\6\2\2ut\3\2\2\2uv\3\2\2\2v\35\3\2\2\2w{\7\7\2\2xz\5")
        buf.write("&\24\2yx\3\2\2\2z}\3\2\2\2{y\3\2\2\2{|\3\2\2\2|~\3\2\2")
        buf.write("\2}{\3\2\2\2~\u0089\5 \21\2\177\u0083\7\b\2\2\u0080\u0082")
        buf.write("\5&\24\2\u0081\u0080\3\2\2\2\u0082\u0085\3\2\2\2\u0083")
        buf.write("\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0086\3\2\2\2")
        buf.write("\u0085\u0083\3\2\2\2\u0086\u0088\5 \21\2\u0087\177\3\2")
        buf.write("\2\2\u0088\u008b\3\2\2\2\u0089\u008a\3\2\2\2\u0089\u0087")
        buf.write("\3\2\2\2\u008a\u008d\3\2\2\2\u008b\u0089\3\2\2\2\u008c")
        buf.write("\u008e\7\b\2\2\u008d\u008c\3\2\2\2\u008d\u008e\3\2\2\2")
        buf.write("\u008e\u0092\3\2\2\2\u008f\u0091\5&\24\2\u0090\u008f\3")
        buf.write("\2\2\2\u0091\u0094\3\2\2\2\u0092\u0090\3\2\2\2\u0092\u0093")
        buf.write("\3\2\2\2\u0093\u0095\3\2\2\2\u0094\u0092\3\2\2\2\u0095")
        buf.write("\u0096\7\t\2\2\u0096\37\3\2\2\2\u0097\u009a\5\"\22\2\u0098")
        buf.write("\u009a\5$\23\2\u0099\u0097\3\2\2\2\u0099\u0098\3\2\2\2")
        buf.write("\u009a!\3\2\2\2\u009b\u009f\5\30\r\2\u009c\u009e\7\16")
        buf.write("\2\2\u009d\u009c\3\2\2\2\u009e\u00a1\3\2\2\2\u009f\u009d")
        buf.write("\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a2\3\2\2\2\u00a1")
        buf.write("\u009f\3\2\2\2\u00a2\u00a6\7\n\2\2\u00a3\u00a5\7\16\2")
        buf.write("\2\u00a4\u00a3\3\2\2\2\u00a5\u00a8\3\2\2\2\u00a6\u00a4")
        buf.write("\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a9\3\2\2\2\u00a8")
        buf.write("\u00a6\3\2\2\2\u00a9\u00aa\5\b\5\2\u00aa#\3\2\2\2\u00ab")
        buf.write("\u00ac\5\b\5\2\u00ac%\3\2\2\2\u00ad\u00af\t\2\2\2\u00ae")
        buf.write("\u00ad\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00ae\3\2\2\2")
        buf.write("\u00b0\u00b1\3\2\2\2\u00b1\'\3\2\2\2\27,\66<>CHMcejru")
        buf.write("{\u0083\u0089\u008d\u0092\u0099\u009f\u00a6\u00b0")
        return buf.getvalue()


class zoiaParser ( Parser ):

    grammarFileName = "zoia.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\header'", "'@'", "'\\'", "'|'", "'['",
                     "';'", "']'", "'='", "<INVALID>", "'*'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "COMMENT", "Asterisk", "Newline", "Space",
                      "Char" ]

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
    RULE_word = 11
    RULE_alias = 12
    RULE_command = 13
    RULE_arguments = 14
    RULE_argument = 15
    RULE_kwdArgument = 16
    RULE_stdArgument = 17
    RULE_whitespace = 18

    ruleNames =  [ "zoiaFile", "header", "line", "lineElements", "regularLineElements",
                   "lineElement", "markedUpLineElements", "boldItalicLineElements",
                   "boldLineElements", "italicLineElements", "textFragment",
                   "word", "alias", "command", "arguments", "argument",
                   "kwdArgument", "stdArgument", "whitespace" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    COMMENT=9
    Asterisk=10
    Newline=11
    Space=12
    Char=13

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
            self.state = 38
            self.header()
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << zoiaParser.T__1) | (1 << zoiaParser.T__2) | (1 << zoiaParser.Asterisk) | (1 << zoiaParser.Newline) | (1 << zoiaParser.Space) | (1 << zoiaParser.Char))) != 0):
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
            self.match(zoiaParser.T__0)
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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << zoiaParser.T__1) | (1 << zoiaParser.T__2) | (1 << zoiaParser.Asterisk) | (1 << zoiaParser.Space) | (1 << zoiaParser.Char))) != 0):
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
            self.state = 58
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 58
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [zoiaParser.Asterisk]:
                        self.state = 56
                        self.markedUpLineElements()
                        pass
                    elif token in [zoiaParser.T__1, zoiaParser.T__2, zoiaParser.Space, zoiaParser.Char]:
                        self.state = 57
                        self.regularLineElements()
                        pass
                    else:
                        raise NoViableAltException(self)


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
            self.state = 63
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 62
                    self.lineElement()

                else:
                    raise NoViableAltException(self)
                self.state = 65
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
            self.state = 70
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [zoiaParser.Space, zoiaParser.Char]:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.textFragment()
                pass
            elif token in [zoiaParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.alias()
                pass
            elif token in [zoiaParser.T__2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 69
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
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.boldItalicLineElements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.boldLineElements()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 74
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
            self.state = 77
            self.match(zoiaParser.Asterisk)
            self.state = 78
            self.match(zoiaParser.Asterisk)
            self.state = 79
            self.match(zoiaParser.Asterisk)
            self.state = 80
            self.regularLineElements()
            self.state = 81
            self.match(zoiaParser.Asterisk)
            self.state = 82
            self.match(zoiaParser.Asterisk)
            self.state = 83
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
            self.state = 85
            self.match(zoiaParser.Asterisk)
            self.state = 86
            self.match(zoiaParser.Asterisk)
            self.state = 87
            self.regularLineElements()
            self.state = 88
            self.match(zoiaParser.Asterisk)
            self.state = 89
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
            self.state = 91
            self.match(zoiaParser.Asterisk)
            self.state = 92
            self.regularLineElements()
            self.state = 93
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

        def word(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(zoiaParser.WordContext)
            else:
                return self.getTypedRuleContext(zoiaParser.WordContext,i)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 97
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [zoiaParser.Char]:
                        self.state = 95
                        self.word()
                        pass
                    elif token in [zoiaParser.Space]:
                        self.state = 96
                        self.match(zoiaParser.Space)
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 99
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Char(self, i:int=None):
            if i is None:
                return self.getTokens(zoiaParser.Char)
            else:
                return self.getToken(zoiaParser.Char, i)

        def getRuleIndex(self):
            return zoiaParser.RULE_word

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWord" ):
                return visitor.visitWord(self)
            else:
                return visitor.visitChildren(self)




    def word(self):

        localctx = zoiaParser.WordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_word)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 101
                    self.match(zoiaParser.Char)

                else:
                    raise NoViableAltException(self)
                self.state = 104
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

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

        def word(self):
            return self.getTypedRuleContext(zoiaParser.WordContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(zoiaParser.T__1)
            self.state = 107
            self.word()
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

        def word(self):
            return self.getTypedRuleContext(zoiaParser.WordContext,0)


        def arguments(self):
            return self.getTypedRuleContext(zoiaParser.ArgumentsContext,0)


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
            self.state = 109
            self.match(zoiaParser.T__2)
            self.state = 110
            self.word()
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==zoiaParser.T__4:
                self.state = 111
                self.arguments()


            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==zoiaParser.T__3:
                self.state = 114
                self.match(zoiaParser.T__3)


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

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(zoiaParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(zoiaParser.ArgumentContext,i)


        def whitespace(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(zoiaParser.WhitespaceContext)
            else:
                return self.getTypedRuleContext(zoiaParser.WhitespaceContext,i)


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
            self.state = 117
            self.match(zoiaParser.T__4)
            self.state = 121
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 118
                    self.whitespace()
                self.state = 123
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

            self.state = 124
            self.argument()
            self.state = 135
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 125
                    self.match(zoiaParser.T__5)
                    self.state = 129
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 126
                            self.whitespace()
                        self.state = 131
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

                    self.state = 132
                    self.argument()
                self.state = 137
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==zoiaParser.T__5:
                self.state = 138
                self.match(zoiaParser.T__5)


            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==zoiaParser.Newline or _la==zoiaParser.Space:
                self.state = 141
                self.whitespace()
                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 147
            self.match(zoiaParser.T__6)
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
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.kwdArgument()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
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

        def word(self):
            return self.getTypedRuleContext(zoiaParser.WordContext,0)


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
        self.enterRule(localctx, 32, self.RULE_kwdArgument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.word()
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==zoiaParser.Space:
                self.state = 154
                self.match(zoiaParser.Space)
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 160
            self.match(zoiaParser.T__7)
            self.state = 164
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 161
                    self.match(zoiaParser.Space)
                self.state = 166
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

            self.state = 167
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
        self.enterRule(localctx, 34, self.RULE_stdArgument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
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
        self.enterRule(localctx, 36, self.RULE_whitespace)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 171
                    _la = self._input.LA(1)
                    if not(_la==zoiaParser.Newline or _la==zoiaParser.Space):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 174
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
