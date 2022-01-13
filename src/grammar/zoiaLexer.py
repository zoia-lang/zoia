# Generated from grammar/zoia.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("J\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\7\2 \n\2\f\2\16\2#\13\2\3\2\3\2\3\3\3\3")
        buf.write("\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\5\13@\n\13\3")
        buf.write("\f\3\f\3\r\3\r\3\16\6\16G\n\16\r\16\16\16H\2\2\17\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\3\2\5\4\2\f\f\17\17\n\2\"\"\u00a2\u00a2\u1682\u1682")
        buf.write("\u2002\u200c\u202a\u202b\u2031\u2031\u2061\u2061\u3002")
        buf.write("\u3002\23\2\f\f\17\17\"\"%%,,==??BB]_~~\u00a2\u00a2\u1682")
        buf.write("\u1682\u2002\u200c\u202a\u202b\u2031\u2031\u2061\u2061")
        buf.write("\u3002\u3002\2L\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\3\35\3\2\2\2\5&\3\2\2\2\7(\3\2\2\2")
        buf.write("\t*\3\2\2\2\13,\3\2\2\2\r.\3\2\2\2\17\60\3\2\2\2\21\62")
        buf.write("\3\2\2\2\23\64\3\2\2\2\25?\3\2\2\2\27A\3\2\2\2\31C\3\2")
        buf.write("\2\2\33F\3\2\2\2\35!\7%\2\2\36 \n\2\2\2\37\36\3\2\2\2")
        buf.write(" #\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"$\3\2\2\2#!\3\2\2\2")
        buf.write("$%\b\2\2\2%\4\3\2\2\2&\'\7,\2\2\'\6\3\2\2\2()\7B\2\2)")
        buf.write("\b\3\2\2\2*+\7^\2\2+\n\3\2\2\2,-\7~\2\2-\f\3\2\2\2./\7")
        buf.write("_\2\2/\16\3\2\2\2\60\61\7]\2\2\61\20\3\2\2\2\62\63\7?")
        buf.write("\2\2\63\22\3\2\2\2\64\65\7^\2\2\65\66\7j\2\2\66\67\7g")
        buf.write("\2\2\678\7c\2\289\7f\2\29:\7g\2\2:;\7t\2\2;\24\3\2\2\2")
        buf.write("<=\7\17\2\2=@\7\f\2\2>@\t\2\2\2?<\3\2\2\2?>\3\2\2\2@\26")
        buf.write("\3\2\2\2AB\7=\2\2B\30\3\2\2\2CD\t\3\2\2D\32\3\2\2\2EG")
        buf.write("\n\4\2\2FE\3\2\2\2GH\3\2\2\2HF\3\2\2\2HI\3\2\2\2I\34\3")
        buf.write("\2\2\2\6\2!?H\3\b\2\2")
        return buf.getvalue()


class zoiaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT = 1
    Asterisk = 2
    At = 3
    Backslash = 4
    Bar = 5
    BracketsClose = 6
    BracketsOpen = 7
    Equals = 8
    Header = 9
    Newline = 10
    Semicolon = 11
    Space = 12
    Word = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'*'", "'@'", "'\\'", "'|'", "']'", "'['", "'='", "'\\header'",
            "';'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "Asterisk", "At", "Backslash", "Bar", "BracketsClose",
            "BracketsOpen", "Equals", "Header", "Newline", "Semicolon",
            "Space", "Word" ]

    ruleNames = [ "COMMENT", "Asterisk", "At", "Backslash", "Bar", "BracketsClose",
                  "BracketsOpen", "Equals", "Header", "Newline", "Semicolon",
                  "Space", "Word" ]

    grammarFileName = "zoia.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None
