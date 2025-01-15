# Generated from main/VoTien.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\4")
        buf.write("\27\b\1\4\2\t\2\4\3\t\3\3\2\3\2\3\2\7\2\13\n\2\f\2\16")
        buf.write("\2\16\13\2\3\3\7\3\21\n\3\f\3\16\3\24\13\3\3\3\3\3\2\2")
        buf.write("\4\3\3\5\4\3\2\2\2\30\2\3\3\2\2\2\2\5\3\2\2\2\3\7\3\2")
        buf.write("\2\2\5\22\3\2\2\2\7\f\13\2\2\2\b\t\13\2\2\2\t\13\13\2")
        buf.write("\2\2\n\b\3\2\2\2\13\16\3\2\2\2\f\n\3\2\2\2\f\r\3\2\2\2")
        buf.write("\r\4\3\2\2\2\16\f\3\2\2\2\17\21\13\2\2\2\20\17\3\2\2\2")
        buf.write("\21\24\3\2\2\2\22\20\3\2\2\2\22\23\3\2\2\2\23\25\3\2\2")
        buf.write("\2\24\22\3\2\2\2\25\26\b\3\2\2\26\6\3\2\2\2\5\2\f\22\3")
        buf.write("\3\3\2")
        return buf.getvalue()


class VoTienLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    ERROR_STRING = 2

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "ID", "ERROR_STRING" ]

    ruleNames = [ "ID", "ERROR_STRING" ]

    grammarFileName = "VoTien.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[1] = self.ERROR_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


