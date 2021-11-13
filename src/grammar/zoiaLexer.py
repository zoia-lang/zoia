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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("C\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\7\n\64\n\n\f\n")
        buf.write("\16\n\67\13\n\3\n\3\n\3\13\3\13\3\13\5\13>\n\13\3\f\3")
        buf.write("\f\3\r\3\r\2\2\16\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\3\2\4\4\2\f\f\17\17\n\2\"\"\u00a2")
        buf.write("\u00a2\u1682\u1682\u2002\u200c\u202a\u202b\u2031\u2031")
        buf.write("\u2061\u2061\u3002\u3002\3\13\2\2\2!\2#\2\u00a1\2\u00a3")
        buf.write("\2\u1681\2\u1683\2\u2001\2\u200d\2\u2029\2\u202c\2\u2030")
        buf.write("\2\u2032\2\u2060\2\u2062\2\u3001\2\u3003\2\1\22D\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3\33\3\2\2\2\5")
        buf.write("#\3\2\2\2\7%\3\2\2\2\t\'\3\2\2\2\13)\3\2\2\2\r+\3\2\2")
        buf.write("\2\17-\3\2\2\2\21/\3\2\2\2\23\61\3\2\2\2\25=\3\2\2\2\27")
        buf.write("?\3\2\2\2\31A\3\2\2\2\33\34\7^\2\2\34\35\7j\2\2\35\36")
        buf.write("\7g\2\2\36\37\7c\2\2\37 \7f\2\2 !\7g\2\2!\"\7t\2\2\"\4")
        buf.write("\3\2\2\2#$\7B\2\2$\6\3\2\2\2%&\7^\2\2&\b\3\2\2\2\'(\7")
        buf.write("~\2\2(\n\3\2\2\2)*\7]\2\2*\f\3\2\2\2+,\7=\2\2,\16\3\2")
        buf.write("\2\2-.\7_\2\2.\20\3\2\2\2/\60\7?\2\2\60\22\3\2\2\2\61")
        buf.write("\65\7%\2\2\62\64\n\2\2\2\63\62\3\2\2\2\64\67\3\2\2\2\65")
        buf.write("\63\3\2\2\2\65\66\3\2\2\2\668\3\2\2\2\67\65\3\2\2\289")
        buf.write("\b\n\2\29\24\3\2\2\2:;\7\17\2\2;>\7\f\2\2<>\t\2\2\2=:")
        buf.write("\3\2\2\2=<\3\2\2\2>\26\3\2\2\2?@\t\3\2\2@\30\3\2\2\2A")
        buf.write("B\t\4\2\2B\32\3\2\2\2\5\2\65=\3\b\2\2")
        return buf.getvalue()


class zoiaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    COMMENT = 9
    Newline = 10
    Space = 11
    Char = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\\header'", "'@'", "'\\'", "'|'", "'['", "';'", "']'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "Newline", "Space", "Char" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6",
                  "T__7", "COMMENT", "Newline", "Space", "Char" ]

    grammarFileName = "zoia.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None
