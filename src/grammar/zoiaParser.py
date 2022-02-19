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
        buf.write("\u00b7\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\3\2\7\2+\n\2\f\2\16\2.\13\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\4\5\4\67\n\4\3\4\3\4\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\6\5A\n\5\r\5\16\5B\3\6\3\6\3\6\6\6H\n\6\r\6\16")
        buf.write("\6I\3\7\3\7\3\7\3\7\3\7\3\7\5\7R\n\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\7\7Z\n\7\f\7\16\7]\13\7\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\f\5\ft\n\f\3\f\3\f\5\fx\n\f\3\r\3\r\5\r|\n\r\3")
        buf.write("\16\3\16\3\16\5\16\u0081\n\16\3\17\3\17\3\17\5\17\u0086")
        buf.write("\n\17\3\17\5\17\u0089\n\17\3\20\3\20\5\20\u008d\n\20\3")
        buf.write("\20\3\20\3\20\5\20\u0092\n\20\3\20\7\20\u0095\n\20\f\20")
        buf.write("\16\20\u0098\13\20\3\20\5\20\u009b\n\20\3\20\5\20\u009e")
        buf.write("\n\20\3\20\3\20\3\21\3\21\5\21\u00a4\n\21\3\22\3\22\5")
        buf.write("\22\u00a8\n\22\3\22\3\22\5\22\u00ac\n\22\3\22\3\22\3\23")
        buf.write("\3\23\3\24\6\24\u00b3\n\24\r\24\16\24\u00b4\3\24\3\u0096")
        buf.write("\2\25\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&\2\4")
        buf.write("\3\2\16\17\4\2\f\f\16\16\2\u00c8\2(\3\2\2\2\4\61\3\2\2")
        buf.write("\2\6\66\3\2\2\2\b@\3\2\2\2\nG\3\2\2\2\fQ\3\2\2\2\16^\3")
        buf.write("\2\2\2\20f\3\2\2\2\22l\3\2\2\2\24p\3\2\2\2\26s\3\2\2\2")
        buf.write("\30y\3\2\2\2\32}\3\2\2\2\34\u0082\3\2\2\2\36\u008a\3\2")
        buf.write("\2\2 \u00a3\3\2\2\2\"\u00a5\3\2\2\2$\u00af\3\2\2\2&\u00b2")
        buf.write("\3\2\2\2(,\5\4\3\2)+\5\6\4\2*)\3\2\2\2+.\3\2\2\2,*\3\2")
        buf.write("\2\2,-\3\2\2\2-/\3\2\2\2.,\3\2\2\2/\60\7\2\2\3\60\3\3")
        buf.write("\2\2\2\61\62\7\13\2\2\62\63\5\36\20\2\63\64\7\f\2\2\64")
        buf.write("\5\3\2\2\2\65\67\5\b\5\2\66\65\3\2\2\2\66\67\3\2\2\2\67")
        buf.write("8\3\2\2\289\7\f\2\29\7\3\2\2\2:A\5\24\13\2;A\5\32\16\2")
        buf.write("<A\5\34\17\2=A\5\22\n\2>A\5\20\t\2?A\5\16\b\2@:\3\2\2")
        buf.write("\2@;\3\2\2\2@<\3\2\2\2@=\3\2\2\2@>\3\2\2\2@?\3\2\2\2A")
        buf.write("B\3\2\2\2B@\3\2\2\2BC\3\2\2\2C\t\3\2\2\2DH\5\26\f\2EH")
        buf.write("\5\32\16\2FH\5\34\17\2GD\3\2\2\2GE\3\2\2\2GF\3\2\2\2H")
        buf.write("I\3\2\2\2IG\3\2\2\2IJ\3\2\2\2J\13\3\2\2\2KR\5\30\r\2L")
        buf.write("R\5\32\16\2MR\5\34\17\2NR\5\22\n\2OR\5\20\t\2PR\5\16\b")
        buf.write("\2QK\3\2\2\2QL\3\2\2\2QM\3\2\2\2QN\3\2\2\2QO\3\2\2\2Q")
        buf.write("P\3\2\2\2R[\3\2\2\2SZ\5\24\13\2TZ\5\32\16\2UZ\5\34\17")
        buf.write("\2VZ\5\22\n\2WZ\5\20\t\2XZ\5\16\b\2YS\3\2\2\2YT\3\2\2")
        buf.write("\2YU\3\2\2\2YV\3\2\2\2YW\3\2\2\2YX\3\2\2\2Z]\3\2\2\2[")
        buf.write("Y\3\2\2\2[\\\3\2\2\2\\\r\3\2\2\2][\3\2\2\2^_\7\4\2\2_")
        buf.write("`\7\4\2\2`a\7\4\2\2ab\5\n\6\2bc\7\4\2\2cd\7\4\2\2de\7")
        buf.write("\4\2\2e\17\3\2\2\2fg\7\4\2\2gh\7\4\2\2hi\5\n\6\2ij\7\4")
        buf.write("\2\2jk\7\4\2\2k\21\3\2\2\2lm\7\4\2\2mn\5\n\6\2no\7\4\2")
        buf.write("\2o\23\3\2\2\2pq\t\2\2\2q\25\3\2\2\2rt\7\16\2\2sr\3\2")
        buf.write("\2\2st\3\2\2\2tu\3\2\2\2uw\7\17\2\2vx\7\16\2\2wv\3\2\2")
        buf.write("\2wx\3\2\2\2x\27\3\2\2\2y{\7\17\2\2z|\7\16\2\2{z\3\2\2")
        buf.write("\2{|\3\2\2\2|\31\3\2\2\2}~\7\5\2\2~\u0080\7\17\2\2\177")
        buf.write("\u0081\7\7\2\2\u0080\177\3\2\2\2\u0080\u0081\3\2\2\2\u0081")
        buf.write("\33\3\2\2\2\u0082\u0083\7\6\2\2\u0083\u0085\7\17\2\2\u0084")
        buf.write("\u0086\5\36\20\2\u0085\u0084\3\2\2\2\u0085\u0086\3\2\2")
        buf.write("\2\u0086\u0088\3\2\2\2\u0087\u0089\7\7\2\2\u0088\u0087")
        buf.write("\3\2\2\2\u0088\u0089\3\2\2\2\u0089\35\3\2\2\2\u008a\u008c")
        buf.write("\7\t\2\2\u008b\u008d\5&\24\2\u008c\u008b\3\2\2\2\u008c")
        buf.write("\u008d\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u0096\5 \21\2")
        buf.write("\u008f\u0091\7\r\2\2\u0090\u0092\5&\24\2\u0091\u0090\3")
        buf.write("\2\2\2\u0091\u0092\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0095")
        buf.write("\5 \21\2\u0094\u008f\3\2\2\2\u0095\u0098\3\2\2\2\u0096")
        buf.write("\u0097\3\2\2\2\u0096\u0094\3\2\2\2\u0097\u009a\3\2\2\2")
        buf.write("\u0098\u0096\3\2\2\2\u0099\u009b\7\r\2\2\u009a\u0099\3")
        buf.write("\2\2\2\u009a\u009b\3\2\2\2\u009b\u009d\3\2\2\2\u009c\u009e")
        buf.write("\5&\24\2\u009d\u009c\3\2\2\2\u009d\u009e\3\2\2\2\u009e")
        buf.write("\u009f\3\2\2\2\u009f\u00a0\7\b\2\2\u00a0\37\3\2\2\2\u00a1")
        buf.write("\u00a4\5\"\22\2\u00a2\u00a4\5$\23\2\u00a3\u00a1\3\2\2")
        buf.write("\2\u00a3\u00a2\3\2\2\2\u00a4!\3\2\2\2\u00a5\u00a7\7\17")
        buf.write("\2\2\u00a6\u00a8\7\16\2\2\u00a7\u00a6\3\2\2\2\u00a7\u00a8")
        buf.write("\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00ab\7\n\2\2\u00aa")
        buf.write("\u00ac\7\16\2\2\u00ab\u00aa\3\2\2\2\u00ab\u00ac\3\2\2")
        buf.write("\2\u00ac\u00ad\3\2\2\2\u00ad\u00ae\5\f\7\2\u00ae#\3\2")
        buf.write("\2\2\u00af\u00b0\5\f\7\2\u00b0%\3\2\2\2\u00b1\u00b3\t")
        buf.write("\3\2\2\u00b2\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b2")
        buf.write("\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\'\3\2\2\2\32,\66@B")
        buf.write("GIQY[sw{\u0080\u0085\u0088\u008c\u0091\u0096\u009a\u009d")
        buf.write("\u00a3\u00a7\u00ab\u00b4")
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
        self.enterRule(localctx, 26, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(zoiaParser.Backslash)
            self.state = 129
            self.match(zoiaParser.Word)
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
