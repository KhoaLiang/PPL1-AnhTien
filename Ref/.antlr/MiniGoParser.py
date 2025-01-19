# Generated from c:/Code/PPL/Ref/MiniGo.g4 by ANTLR 4.13.1
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
        4,1,61,220,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,1,0,1,0,1,0,4,0,
        42,8,0,11,0,12,0,43,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,55,8,
        1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,5,3,65,8,3,10,3,12,3,68,9,3,1,
        4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,5,7,85,
        8,7,10,7,12,7,88,9,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,98,8,8,
        10,8,12,8,101,9,8,1,9,1,9,1,9,1,9,1,9,1,9,5,9,109,8,9,10,9,12,9,
        112,9,9,1,10,1,10,1,10,1,10,1,10,1,10,5,10,120,8,10,10,10,12,10,
        123,9,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,5,11,146,8,11,
        10,11,12,11,149,9,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        5,12,160,8,12,10,12,12,12,163,9,12,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,5,13,177,8,13,10,13,12,13,180,9,13,
        1,14,1,14,1,14,1,14,1,14,3,14,187,8,14,1,15,1,15,1,15,1,15,1,15,
        1,15,3,15,195,8,15,1,15,1,15,1,15,5,15,200,8,15,10,15,12,15,203,
        9,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,213,8,16,1,17,
        1,17,1,17,1,17,1,17,1,17,0,6,18,20,22,24,26,30,18,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,0,1,2,0,7,7,9,12,233,0,41,1,0,0,
        0,2,54,1,0,0,0,4,56,1,0,0,0,6,58,1,0,0,0,8,69,1,0,0,0,10,72,1,0,
        0,0,12,76,1,0,0,0,14,81,1,0,0,0,16,89,1,0,0,0,18,102,1,0,0,0,20,
        113,1,0,0,0,22,124,1,0,0,0,24,150,1,0,0,0,26,164,1,0,0,0,28,186,
        1,0,0,0,30,194,1,0,0,0,32,212,1,0,0,0,34,214,1,0,0,0,36,37,5,13,
        0,0,37,38,5,51,0,0,38,39,5,35,0,0,39,42,3,18,9,0,40,42,5,56,0,0,
        41,36,1,0,0,0,41,40,1,0,0,0,42,43,1,0,0,0,43,41,1,0,0,0,43,44,1,
        0,0,0,44,45,1,0,0,0,45,46,5,0,0,1,46,1,1,0,0,0,47,55,5,52,0,0,48,
        55,5,53,0,0,49,55,5,54,0,0,50,55,5,19,0,0,51,55,5,20,0,0,52,55,3,
        10,5,0,53,55,3,12,6,0,54,47,1,0,0,0,54,48,1,0,0,0,54,49,1,0,0,0,
        54,50,1,0,0,0,54,51,1,0,0,0,54,52,1,0,0,0,54,53,1,0,0,0,55,3,1,0,
        0,0,56,57,7,0,0,0,57,5,1,0,0,0,58,59,5,47,0,0,59,60,5,52,0,0,60,
        66,5,48,0,0,61,62,5,47,0,0,62,63,5,52,0,0,63,65,5,48,0,0,64,61,1,
        0,0,0,65,68,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,7,1,0,0,0,68,
        66,1,0,0,0,69,70,3,6,3,0,70,71,3,4,2,0,71,9,1,0,0,0,72,73,5,45,0,
        0,73,74,3,14,7,0,74,75,5,46,0,0,75,11,1,0,0,0,76,77,5,51,0,0,77,
        78,5,45,0,0,78,79,3,16,8,0,79,80,5,46,0,0,80,13,1,0,0,0,81,86,3,
        18,9,0,82,83,5,49,0,0,83,85,3,18,9,0,84,82,1,0,0,0,85,88,1,0,0,0,
        86,84,1,0,0,0,86,87,1,0,0,0,87,15,1,0,0,0,88,86,1,0,0,0,89,90,5,
        51,0,0,90,91,5,42,0,0,91,92,3,18,9,0,92,99,1,0,0,0,93,94,5,49,0,
        0,94,95,5,51,0,0,95,96,5,42,0,0,96,98,3,18,9,0,97,93,1,0,0,0,98,
        101,1,0,0,0,99,97,1,0,0,0,99,100,1,0,0,0,100,17,1,0,0,0,101,99,1,
        0,0,0,102,103,6,9,-1,0,103,104,3,20,10,0,104,110,1,0,0,0,105,106,
        10,2,0,0,106,107,5,33,0,0,107,109,3,20,10,0,108,105,1,0,0,0,109,
        112,1,0,0,0,110,108,1,0,0,0,110,111,1,0,0,0,111,19,1,0,0,0,112,110,
        1,0,0,0,113,114,6,10,-1,0,114,115,3,22,11,0,115,121,1,0,0,0,116,
        117,10,2,0,0,117,118,5,32,0,0,118,120,3,22,11,0,119,116,1,0,0,0,
        120,123,1,0,0,0,121,119,1,0,0,0,121,122,1,0,0,0,122,21,1,0,0,0,123,
        121,1,0,0,0,124,125,6,11,-1,0,125,126,3,24,12,0,126,147,1,0,0,0,
        127,128,10,7,0,0,128,129,5,26,0,0,129,146,3,24,12,0,130,131,10,6,
        0,0,131,132,5,27,0,0,132,146,3,24,12,0,133,134,10,5,0,0,134,135,
        5,28,0,0,135,146,3,24,12,0,136,137,10,4,0,0,137,138,5,29,0,0,138,
        146,3,24,12,0,139,140,10,3,0,0,140,141,5,30,0,0,141,146,3,24,12,
        0,142,143,10,2,0,0,143,144,5,31,0,0,144,146,3,24,12,0,145,127,1,
        0,0,0,145,130,1,0,0,0,145,133,1,0,0,0,145,136,1,0,0,0,145,139,1,
        0,0,0,145,142,1,0,0,0,146,149,1,0,0,0,147,145,1,0,0,0,147,148,1,
        0,0,0,148,23,1,0,0,0,149,147,1,0,0,0,150,151,6,12,-1,0,151,152,3,
        26,13,0,152,161,1,0,0,0,153,154,10,3,0,0,154,155,5,21,0,0,155,160,
        3,26,13,0,156,157,10,2,0,0,157,158,5,22,0,0,158,160,3,26,13,0,159,
        153,1,0,0,0,159,156,1,0,0,0,160,163,1,0,0,0,161,159,1,0,0,0,161,
        162,1,0,0,0,162,25,1,0,0,0,163,161,1,0,0,0,164,165,6,13,-1,0,165,
        166,3,28,14,0,166,178,1,0,0,0,167,168,10,4,0,0,168,169,5,23,0,0,
        169,177,3,28,14,0,170,171,10,3,0,0,171,172,5,24,0,0,172,177,3,28,
        14,0,173,174,10,2,0,0,174,175,5,25,0,0,175,177,3,28,14,0,176,167,
        1,0,0,0,176,170,1,0,0,0,176,173,1,0,0,0,177,180,1,0,0,0,178,176,
        1,0,0,0,178,179,1,0,0,0,179,27,1,0,0,0,180,178,1,0,0,0,181,182,5,
        34,0,0,182,187,3,28,14,0,183,184,5,22,0,0,184,187,3,28,14,0,185,
        187,3,30,15,0,186,181,1,0,0,0,186,183,1,0,0,0,186,185,1,0,0,0,187,
        29,1,0,0,0,188,189,6,15,-1,0,189,190,5,47,0,0,190,191,3,30,15,0,
        191,192,5,48,0,0,192,195,1,0,0,0,193,195,3,32,16,0,194,188,1,0,0,
        0,194,193,1,0,0,0,195,201,1,0,0,0,196,197,10,2,0,0,197,198,5,41,
        0,0,198,200,3,32,16,0,199,196,1,0,0,0,200,203,1,0,0,0,201,199,1,
        0,0,0,201,202,1,0,0,0,202,31,1,0,0,0,203,201,1,0,0,0,204,205,5,43,
        0,0,205,206,3,18,9,0,206,207,5,44,0,0,207,213,1,0,0,0,208,213,5,
        51,0,0,209,213,3,2,1,0,210,213,3,34,17,0,211,213,1,0,0,0,212,204,
        1,0,0,0,212,208,1,0,0,0,212,209,1,0,0,0,212,210,1,0,0,0,212,211,
        1,0,0,0,213,33,1,0,0,0,214,215,5,51,0,0,215,216,5,43,0,0,216,217,
        3,14,7,0,217,218,5,44,0,0,218,35,1,0,0,0,18,41,43,54,66,86,99,110,
        121,145,147,159,161,176,178,186,194,201,212
    ]

class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'boolean'", "'const'", "'var'", 
                     "'continue'", "'break'", "'range'", "'nil'", "'true'", 
                     "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", 
                     "'!'", "'='", "'+='", "'-='", "'*='", "'/='", "'%='", 
                     "'.'", "':'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "','", "';'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                      "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
                      "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
                      "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "EQUAL", "DIFF", "LT", "LTE", "RT", "RTE", 
                      "AND", "OR", "NOT", "ASSIGN", "ASSIGNADD", "ASSIGNSUB", 
                      "ASSIGNMUL", "ASSIGNDIV", "ASSIGNMOD", "POINTTO", 
                      "COLON", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", 
                      "RBRACK", "COMMA", "SEMICOL", "ID", "INT_LIT", "FLOAT_LIT", 
                      "STRING_LIT", "WS", "NEWLINE", "COMMENT", "ML_COMMENT", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_literal = 1
    RULE_type_of_array = 2
    RULE_dimension_list = 3
    RULE_type_array = 4
    RULE_array_literal = 5
    RULE_struct_literal = 6
    RULE_list_expression = 7
    RULE_list_elements = 8
    RULE_expression = 9
    RULE_expression1 = 10
    RULE_expression2 = 11
    RULE_expression3 = 12
    RULE_expression4 = 13
    RULE_expression5 = 14
    RULE_expression6 = 15
    RULE_expression7 = 16
    RULE_func_call = 17

    ruleNames =  [ "program", "literal", "type_of_array", "dimension_list", 
                   "type_array", "array_literal", "struct_literal", "list_expression", 
                   "list_elements", "expression", "expression1", "expression2", 
                   "expression3", "expression4", "expression5", "expression6", 
                   "expression7", "func_call" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    FOR=3
    RETURN=4
    FUNC=5
    TYPE=6
    STRUCT=7
    INTERFACE=8
    STRING=9
    INT=10
    FLOAT=11
    BOOLEAN=12
    CONST=13
    VAR=14
    CONTINUE=15
    BREAK=16
    RANGE=17
    NIL=18
    TRUE=19
    FALSE=20
    ADD=21
    SUB=22
    MUL=23
    DIV=24
    MOD=25
    EQUAL=26
    DIFF=27
    LT=28
    LTE=29
    RT=30
    RTE=31
    AND=32
    OR=33
    NOT=34
    ASSIGN=35
    ASSIGNADD=36
    ASSIGNSUB=37
    ASSIGNMUL=38
    ASSIGNDIV=39
    ASSIGNMOD=40
    POINTTO=41
    COLON=42
    LPAREN=43
    RPAREN=44
    LBRACE=45
    RBRACE=46
    LBRACK=47
    RBRACK=48
    COMMA=49
    SEMICOL=50
    ID=51
    INT_LIT=52
    FLOAT_LIT=53
    STRING_LIT=54
    WS=55
    NEWLINE=56
    COMMENT=57
    ML_COMMENT=58
    ERROR_CHAR=59
    UNCLOSE_STRING=60
    ILLEGAL_ESCAPE=61

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def CONST(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.CONST)
            else:
                return self.getToken(MiniGoParser.CONST, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def ASSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ASSIGN)
            else:
                return self.getToken(MiniGoParser.ASSIGN, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 41
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [13]:
                    self.state = 36
                    self.match(MiniGoParser.CONST)
                    self.state = 37
                    self.match(MiniGoParser.ID)
                    self.state = 38
                    self.match(MiniGoParser.ASSIGN)
                    self.state = 39
                    self.expression(0)
                    pass
                elif token in [56]:
                    self.state = 40
                    self.match(MiniGoParser.NEWLINE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 43 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==13 or _la==56):
                    break

            self.state = 45
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_literal)
        try:
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.match(MiniGoParser.INT_LIT)
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 3)
                self.state = 49
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 4)
                self.state = 50
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 5)
                self.state = 51
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 6)
                self.state = 52
                self.array_literal()
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 7)
                self.state = 53
                self.struct_literal()
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


    class Type_of_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_type_of_array




    def type_of_array(self):

        localctx = MiniGoParser.Type_of_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_type_of_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7808) != 0)):
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


    class Dimension_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LBRACK)
            else:
                return self.getToken(MiniGoParser.LBRACK, i)

        def INT_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.INT_LIT)
            else:
                return self.getToken(MiniGoParser.INT_LIT, i)

        def RBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RBRACK)
            else:
                return self.getToken(MiniGoParser.RBRACK, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_dimension_list




    def dimension_list(self):

        localctx = MiniGoParser.Dimension_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_dimension_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(MiniGoParser.LBRACK)
            self.state = 59
            self.match(MiniGoParser.INT_LIT)
            self.state = 60
            self.match(MiniGoParser.RBRACK)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==47:
                self.state = 61
                self.match(MiniGoParser.LBRACK)
                self.state = 62
                self.match(MiniGoParser.INT_LIT)
                self.state = 63
                self.match(MiniGoParser.RBRACK)
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimension_list(self):
            return self.getTypedRuleContext(MiniGoParser.Dimension_listContext,0)


        def type_of_array(self):
            return self.getTypedRuleContext(MiniGoParser.Type_of_arrayContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_type_array




    def type_array(self):

        localctx = MiniGoParser.Type_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_type_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.dimension_list()
            self.state = 70
            self.type_of_array()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_literal




    def array_literal(self):

        localctx = MiniGoParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(MiniGoParser.LBRACE)
            self.state = 73
            self.list_expression()
            self.state = 74
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_elements(self):
            return self.getTypedRuleContext(MiniGoParser.List_elementsContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_struct_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(MiniGoParser.ID)
            self.state = 77
            self.match(MiniGoParser.LBRACE)
            self.state = 78
            self.list_elements()
            self.state = 79
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_list_expression




    def list_expression(self):

        localctx = MiniGoParser.List_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_list_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.expression(0)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==49:
                self.state = 82
                self.match(MiniGoParser.COMMA)
                self.state = 83
                self.expression(0)
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_elementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COLON)
            else:
                return self.getToken(MiniGoParser.COLON, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_list_elements




    def list_elements(self):

        localctx = MiniGoParser.List_elementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_list_elements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(MiniGoParser.ID)
            self.state = 90
            self.match(MiniGoParser.COLON)
            self.state = 91
            self.expression(0)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==49:
                self.state = 93
                self.match(MiniGoParser.COMMA)
                self.state = 94
                self.match(MiniGoParser.ID)
                self.state = 95
                self.match(MiniGoParser.COLON)
                self.state = 96
                self.expression(0)
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.expression1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 110
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 105
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 106
                    self.match(MiniGoParser.OR)
                    self.state = 107
                    self.expression1(0) 
                self.state = 112
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression2Context,0)


        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression1



    def expression1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expression1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 121
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 116
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 117
                    self.match(MiniGoParser.AND)
                    self.state = 118
                    self.expression2(0) 
                self.state = 123
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression2Context,0)


        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def DIFF(self):
            return self.getToken(MiniGoParser.DIFF, 0)

        def LT(self):
            return self.getToken(MiniGoParser.LT, 0)

        def LTE(self):
            return self.getToken(MiniGoParser.LTE, 0)

        def RT(self):
            return self.getToken(MiniGoParser.RT, 0)

        def RTE(self):
            return self.getToken(MiniGoParser.RTE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression2



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expression2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 147
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 145
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 127
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 128
                        self.match(MiniGoParser.EQUAL)
                        self.state = 129
                        self.expression3(0)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 130
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 131
                        self.match(MiniGoParser.DIFF)
                        self.state = 132
                        self.expression3(0)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 133
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 134
                        self.match(MiniGoParser.LT)
                        self.state = 135
                        self.expression3(0)
                        pass

                    elif la_ == 4:
                        localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 136
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 137
                        self.match(MiniGoParser.LTE)
                        self.state = 138
                        self.expression3(0)
                        pass

                    elif la_ == 5:
                        localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 139
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 140
                        self.match(MiniGoParser.RT)
                        self.state = 141
                        self.expression3(0)
                        pass

                    elif la_ == 6:
                        localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 142
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 143
                        self.match(MiniGoParser.RTE)
                        self.state = 144
                        self.expression3(0)
                        pass

             
                self.state = 149
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression3Context,0)


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression3



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expression3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 161
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 159
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                        self.state = 153
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 154
                        self.match(MiniGoParser.ADD)
                        self.state = 155
                        self.expression4(0)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                        self.state = 156
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 157
                        self.match(MiniGoParser.SUB)
                        self.state = 158
                        self.expression4(0)
                        pass

             
                self.state = 163
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression4Context,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression4



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expression4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 178
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 176
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                        self.state = 167
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 168
                        self.match(MiniGoParser.MUL)
                        self.state = 169
                        self.expression5()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                        self.state = 170
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 171
                        self.match(MiniGoParser.DIV)
                        self.state = 172
                        self.expression5()
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                        self.state = 173
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 174
                        self.match(MiniGoParser.MOD)
                        self.state = 175
                        self.expression5()
                        pass

             
                self.state = 180
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression5




    def expression5(self):

        localctx = MiniGoParser.Expression5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expression5)
        try:
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.match(MiniGoParser.NOT)
                self.state = 182
                self.expression5()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.match(MiniGoParser.SUB)
                self.state = 184
                self.expression5()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 185
                self.expression6(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def expression7(self):
            return self.getTypedRuleContext(MiniGoParser.Expression7Context,0)


        def POINTTO(self):
            return self.getToken(MiniGoParser.POINTTO, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression6



    def expression6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expression6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 189
                self.match(MiniGoParser.LBRACK)
                self.state = 190
                self.expression6(0)
                self.state = 191
                self.match(MiniGoParser.RBRACK)
                pass

            elif la_ == 2:
                self.state = 193
                self.expression7()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 201
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                    self.state = 196
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 197
                    self.match(MiniGoParser.POINTTO)
                    self.state = 198
                    self.expression7() 
                self.state = 203
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression7




    def expression7(self):

        localctx = MiniGoParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expression7)
        try:
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.match(MiniGoParser.LPAREN)
                self.state = 205
                self.expression(0)
                self.state = 206
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 209
                self.literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 210
                self.func_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call




    def func_call(self):

        localctx = MiniGoParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(MiniGoParser.ID)
            self.state = 215
            self.match(MiniGoParser.LPAREN)
            self.state = 216
            self.list_expression()
            self.state = 217
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.expression_sempred
        self._predicates[10] = self.expression1_sempred
        self._predicates[11] = self.expression2_sempred
        self._predicates[12] = self.expression3_sempred
        self._predicates[13] = self.expression4_sempred
        self._predicates[15] = self.expression6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression1_sempred(self, localctx:Expression1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 2)
         

    def expression6_sempred(self, localctx:Expression6Context, predIndex:int):
            if predIndex == 13:
                return self.precpred(self._ctx, 2)
         




