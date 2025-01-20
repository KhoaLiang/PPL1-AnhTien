# Generated from c:/Code/PPL/main/MiniGo.g4 by ANTLR 4.13.1
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
        4,1,61,246,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,1,0,1,0,1,
        0,1,0,4,0,44,8,0,11,0,12,0,45,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,3,1,57,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,5,1,5,
        1,5,1,5,1,5,1,5,5,5,76,8,5,10,5,12,5,79,9,5,1,6,1,6,1,6,1,7,1,7,
        3,7,86,8,7,1,8,1,8,1,8,1,8,1,8,3,8,93,8,8,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,5,9,103,8,9,10,9,12,9,106,9,9,1,10,1,10,1,10,1,10,1,10,
        1,10,5,10,114,8,10,10,10,12,10,117,9,10,1,11,1,11,1,11,1,11,1,11,
        1,11,5,11,125,8,11,10,11,12,11,128,9,11,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,5,12,151,8,12,10,12,12,12,154,9,12,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,5,13,165,8,13,10,13,12,13,168,9,13,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,5,14,
        182,8,14,10,14,12,14,185,9,14,1,15,1,15,1,15,1,15,1,15,3,15,192,
        8,15,1,16,1,16,1,16,1,16,1,16,1,16,3,16,200,8,16,1,16,1,16,1,16,
        1,16,1,16,3,16,207,8,16,1,16,1,16,1,16,5,16,212,8,16,10,16,12,16,
        215,9,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,225,8,17,1,
        17,1,17,1,17,1,17,3,17,231,8,17,1,17,1,17,1,17,1,17,3,17,237,8,17,
        3,17,239,8,17,1,18,1,18,1,18,1,18,1,18,1,18,0,6,20,22,24,26,28,32,
        19,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,0,1,2,0,7,
        7,9,12,262,0,43,1,0,0,0,2,56,1,0,0,0,4,58,1,0,0,0,6,62,1,0,0,0,8,
        67,1,0,0,0,10,69,1,0,0,0,12,80,1,0,0,0,14,85,1,0,0,0,16,92,1,0,0,
        0,18,94,1,0,0,0,20,107,1,0,0,0,22,118,1,0,0,0,24,129,1,0,0,0,26,
        155,1,0,0,0,28,169,1,0,0,0,30,191,1,0,0,0,32,206,1,0,0,0,34,238,
        1,0,0,0,36,240,1,0,0,0,38,39,5,13,0,0,39,40,5,51,0,0,40,41,5,35,
        0,0,41,44,3,20,10,0,42,44,5,56,0,0,43,38,1,0,0,0,43,42,1,0,0,0,44,
        45,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,47,1,0,0,0,47,48,5,0,0,
        1,48,1,1,0,0,0,49,57,5,52,0,0,50,57,5,53,0,0,51,57,5,54,0,0,52,57,
        5,19,0,0,53,57,5,20,0,0,54,57,3,4,2,0,55,57,3,6,3,0,56,49,1,0,0,
        0,56,50,1,0,0,0,56,51,1,0,0,0,56,52,1,0,0,0,56,53,1,0,0,0,56,54,
        1,0,0,0,56,55,1,0,0,0,57,3,1,0,0,0,58,59,5,45,0,0,59,60,3,16,8,0,
        60,61,5,46,0,0,61,5,1,0,0,0,62,63,5,51,0,0,63,64,5,45,0,0,64,65,
        3,18,9,0,65,66,5,46,0,0,66,7,1,0,0,0,67,68,7,0,0,0,68,9,1,0,0,0,
        69,70,5,47,0,0,70,71,5,52,0,0,71,77,5,48,0,0,72,73,5,47,0,0,73,74,
        5,52,0,0,74,76,5,48,0,0,75,72,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,
        0,77,78,1,0,0,0,78,11,1,0,0,0,79,77,1,0,0,0,80,81,3,10,5,0,81,82,
        3,8,4,0,82,13,1,0,0,0,83,86,3,16,8,0,84,86,1,0,0,0,85,83,1,0,0,0,
        85,84,1,0,0,0,86,15,1,0,0,0,87,88,3,20,10,0,88,89,5,49,0,0,89,90,
        3,16,8,0,90,93,1,0,0,0,91,93,3,20,10,0,92,87,1,0,0,0,92,91,1,0,0,
        0,93,17,1,0,0,0,94,95,5,51,0,0,95,96,5,42,0,0,96,97,3,20,10,0,97,
        104,1,0,0,0,98,99,5,49,0,0,99,100,5,51,0,0,100,101,5,42,0,0,101,
        103,3,20,10,0,102,98,1,0,0,0,103,106,1,0,0,0,104,102,1,0,0,0,104,
        105,1,0,0,0,105,19,1,0,0,0,106,104,1,0,0,0,107,108,6,10,-1,0,108,
        109,3,22,11,0,109,115,1,0,0,0,110,111,10,2,0,0,111,112,5,33,0,0,
        112,114,3,22,11,0,113,110,1,0,0,0,114,117,1,0,0,0,115,113,1,0,0,
        0,115,116,1,0,0,0,116,21,1,0,0,0,117,115,1,0,0,0,118,119,6,11,-1,
        0,119,120,3,24,12,0,120,126,1,0,0,0,121,122,10,2,0,0,122,123,5,32,
        0,0,123,125,3,24,12,0,124,121,1,0,0,0,125,128,1,0,0,0,126,124,1,
        0,0,0,126,127,1,0,0,0,127,23,1,0,0,0,128,126,1,0,0,0,129,130,6,12,
        -1,0,130,131,3,26,13,0,131,152,1,0,0,0,132,133,10,7,0,0,133,134,
        5,26,0,0,134,151,3,26,13,0,135,136,10,6,0,0,136,137,5,27,0,0,137,
        151,3,26,13,0,138,139,10,5,0,0,139,140,5,28,0,0,140,151,3,26,13,
        0,141,142,10,4,0,0,142,143,5,29,0,0,143,151,3,26,13,0,144,145,10,
        3,0,0,145,146,5,30,0,0,146,151,3,26,13,0,147,148,10,2,0,0,148,149,
        5,31,0,0,149,151,3,26,13,0,150,132,1,0,0,0,150,135,1,0,0,0,150,138,
        1,0,0,0,150,141,1,0,0,0,150,144,1,0,0,0,150,147,1,0,0,0,151,154,
        1,0,0,0,152,150,1,0,0,0,152,153,1,0,0,0,153,25,1,0,0,0,154,152,1,
        0,0,0,155,156,6,13,-1,0,156,157,3,28,14,0,157,166,1,0,0,0,158,159,
        10,3,0,0,159,160,5,21,0,0,160,165,3,28,14,0,161,162,10,2,0,0,162,
        163,5,22,0,0,163,165,3,28,14,0,164,158,1,0,0,0,164,161,1,0,0,0,165,
        168,1,0,0,0,166,164,1,0,0,0,166,167,1,0,0,0,167,27,1,0,0,0,168,166,
        1,0,0,0,169,170,6,14,-1,0,170,171,3,30,15,0,171,183,1,0,0,0,172,
        173,10,4,0,0,173,174,5,23,0,0,174,182,3,30,15,0,175,176,10,3,0,0,
        176,177,5,24,0,0,177,182,3,30,15,0,178,179,10,2,0,0,179,180,5,25,
        0,0,180,182,3,30,15,0,181,172,1,0,0,0,181,175,1,0,0,0,181,178,1,
        0,0,0,182,185,1,0,0,0,183,181,1,0,0,0,183,184,1,0,0,0,184,29,1,0,
        0,0,185,183,1,0,0,0,186,187,5,34,0,0,187,192,3,30,15,0,188,189,5,
        22,0,0,189,192,3,30,15,0,190,192,3,32,16,0,191,186,1,0,0,0,191,188,
        1,0,0,0,191,190,1,0,0,0,192,31,1,0,0,0,193,194,6,16,-1,0,194,199,
        5,51,0,0,195,196,5,43,0,0,196,197,3,14,7,0,197,198,5,44,0,0,198,
        200,1,0,0,0,199,195,1,0,0,0,199,200,1,0,0,0,200,201,1,0,0,0,201,
        202,5,47,0,0,202,203,3,16,8,0,203,204,5,48,0,0,204,207,1,0,0,0,205,
        207,3,34,17,0,206,193,1,0,0,0,206,205,1,0,0,0,207,213,1,0,0,0,208,
        209,10,2,0,0,209,210,5,41,0,0,210,212,3,34,17,0,211,208,1,0,0,0,
        212,215,1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,214,33,1,0,0,0,215,
        213,1,0,0,0,216,217,5,43,0,0,217,218,3,20,10,0,218,219,5,44,0,0,
        219,239,1,0,0,0,220,224,5,51,0,0,221,222,5,47,0,0,222,223,5,52,0,
        0,223,225,5,48,0,0,224,221,1,0,0,0,224,225,1,0,0,0,225,239,1,0,0,
        0,226,230,3,2,1,0,227,228,5,47,0,0,228,229,5,52,0,0,229,231,5,48,
        0,0,230,227,1,0,0,0,230,231,1,0,0,0,231,239,1,0,0,0,232,236,3,36,
        18,0,233,234,5,47,0,0,234,235,5,52,0,0,235,237,5,48,0,0,236,233,
        1,0,0,0,236,237,1,0,0,0,237,239,1,0,0,0,238,216,1,0,0,0,238,220,
        1,0,0,0,238,226,1,0,0,0,238,232,1,0,0,0,239,35,1,0,0,0,240,241,5,
        51,0,0,241,242,5,43,0,0,242,243,3,14,7,0,243,244,5,44,0,0,244,37,
        1,0,0,0,23,43,45,56,77,85,92,104,115,126,150,152,164,166,181,183,
        191,199,206,213,224,230,236,238
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
    RULE_array_literal = 2
    RULE_struct_literal = 3
    RULE_type_of_array = 4
    RULE_dimension_list = 5
    RULE_type_array = 6
    RULE_list_expression = 7
    RULE_params = 8
    RULE_list_elements = 9
    RULE_expression = 10
    RULE_expression1 = 11
    RULE_expression2 = 12
    RULE_expression3 = 13
    RULE_expression4 = 14
    RULE_expression5 = 15
    RULE_expression6 = 16
    RULE_expression7 = 17
    RULE_func_call = 18

    ruleNames =  [ "program", "literal", "array_literal", "struct_literal", 
                   "type_of_array", "dimension_list", "type_array", "list_expression", 
                   "params", "list_elements", "expression", "expression1", 
                   "expression2", "expression3", "expression4", "expression5", 
                   "expression6", "expression7", "func_call" ]

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
            self.state = 43 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 43
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [13]:
                    self.state = 38
                    self.match(MiniGoParser.CONST)
                    self.state = 39
                    self.match(MiniGoParser.ID)
                    self.state = 40
                    self.match(MiniGoParser.ASSIGN)
                    self.state = 41
                    self.expression(0)
                    pass
                elif token in [56]:
                    self.state = 42
                    self.match(MiniGoParser.NEWLINE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 45 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==13 or _la==56):
                    break

            self.state = 47
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
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.match(MiniGoParser.INT_LIT)
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 3)
                self.state = 51
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 4)
                self.state = 52
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 5)
                self.state = 53
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 6)
                self.state = 54
                self.array_literal()
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 7)
                self.state = 55
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


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def params(self):
            return self.getTypedRuleContext(MiniGoParser.ParamsContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_literal




    def array_literal(self):

        localctx = MiniGoParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(MiniGoParser.LBRACE)
            self.state = 59
            self.params()
            self.state = 60
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
        self.enterRule(localctx, 6, self.RULE_struct_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(MiniGoParser.ID)
            self.state = 63
            self.match(MiniGoParser.LBRACE)
            self.state = 64
            self.list_elements()
            self.state = 65
            self.match(MiniGoParser.RBRACE)
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
        self.enterRule(localctx, 8, self.RULE_type_of_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
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
        self.enterRule(localctx, 10, self.RULE_dimension_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(MiniGoParser.LBRACK)
            self.state = 70
            self.match(MiniGoParser.INT_LIT)
            self.state = 71
            self.match(MiniGoParser.RBRACK)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==47:
                self.state = 72
                self.match(MiniGoParser.LBRACK)
                self.state = 73
                self.match(MiniGoParser.INT_LIT)
                self.state = 74
                self.match(MiniGoParser.RBRACK)
                self.state = 79
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
        self.enterRule(localctx, 12, self.RULE_type_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.dimension_list()
            self.state = 81
            self.type_of_array()
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

        def params(self):
            return self.getTypedRuleContext(MiniGoParser.ParamsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_expression




    def list_expression(self):

        localctx = MiniGoParser.List_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_list_expression)
        try:
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 20, 22, 34, 43, 45, 51, 52, 53, 54]:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.params()
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 2)

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


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def params(self):
            return self.getTypedRuleContext(MiniGoParser.ParamsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_params




    def params(self):

        localctx = MiniGoParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_params)
        try:
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.expression(0)
                self.state = 88
                self.match(MiniGoParser.COMMA)
                self.state = 89
                self.params()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.expression(0)
                pass


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
        self.enterRule(localctx, 18, self.RULE_list_elements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(MiniGoParser.ID)
            self.state = 95
            self.match(MiniGoParser.COLON)
            self.state = 96
            self.expression(0)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==49:
                self.state = 98
                self.match(MiniGoParser.COMMA)
                self.state = 99
                self.match(MiniGoParser.ID)
                self.state = 100
                self.match(MiniGoParser.COLON)
                self.state = 101
                self.expression(0)
                self.state = 106
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
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.expression1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 115
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 110
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 111
                    self.match(MiniGoParser.OR)
                    self.state = 112
                    self.expression1(0) 
                self.state = 117
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

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
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expression1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 126
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 121
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 122
                    self.match(MiniGoParser.AND)
                    self.state = 123
                    self.expression2(0) 
                self.state = 128
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expression2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 152
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 150
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 132
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 133
                        self.match(MiniGoParser.EQUAL)
                        self.state = 134
                        self.expression3(0)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 135
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 136
                        self.match(MiniGoParser.DIFF)
                        self.state = 137
                        self.expression3(0)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 138
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 139
                        self.match(MiniGoParser.LT)
                        self.state = 140
                        self.expression3(0)
                        pass

                    elif la_ == 4:
                        localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 141
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 142
                        self.match(MiniGoParser.LTE)
                        self.state = 143
                        self.expression3(0)
                        pass

                    elif la_ == 5:
                        localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 144
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 145
                        self.match(MiniGoParser.RT)
                        self.state = 146
                        self.expression3(0)
                        pass

                    elif la_ == 6:
                        localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 147
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 148
                        self.match(MiniGoParser.RTE)
                        self.state = 149
                        self.expression3(0)
                        pass

             
                self.state = 154
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expression3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 166
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 164
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                        self.state = 158
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 159
                        self.match(MiniGoParser.ADD)
                        self.state = 160
                        self.expression4(0)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                        self.state = 161
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 162
                        self.match(MiniGoParser.SUB)
                        self.state = 163
                        self.expression4(0)
                        pass

             
                self.state = 168
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expression4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 183
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 181
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                        self.state = 172
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 173
                        self.match(MiniGoParser.MUL)
                        self.state = 174
                        self.expression5()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                        self.state = 175
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 176
                        self.match(MiniGoParser.DIV)
                        self.state = 177
                        self.expression5()
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                        self.state = 178
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 179
                        self.match(MiniGoParser.MOD)
                        self.state = 180
                        self.expression5()
                        pass

             
                self.state = 185
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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
        self.enterRule(localctx, 30, self.RULE_expression5)
        try:
            self.state = 191
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.match(MiniGoParser.NOT)
                self.state = 187
                self.expression5()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.match(MiniGoParser.SUB)
                self.state = 189
                self.expression5()
                pass
            elif token in [19, 20, 43, 45, 51, 52, 53, 54]:
                self.enterOuterAlt(localctx, 3)
                self.state = 190
                self.expression6(0)
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


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def params(self):
            return self.getTypedRuleContext(MiniGoParser.ParamsContext,0)


        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def expression7(self):
            return self.getTypedRuleContext(MiniGoParser.Expression7Context,0)


        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def POINTTO(self):
            return self.getToken(MiniGoParser.POINTTO, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression6



    def expression6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expression6, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 194
                self.match(MiniGoParser.ID)
                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==43:
                    self.state = 195
                    self.match(MiniGoParser.LPAREN)
                    self.state = 196
                    self.list_expression()
                    self.state = 197
                    self.match(MiniGoParser.RPAREN)


                self.state = 201
                self.match(MiniGoParser.LBRACK)

                self.state = 202
                self.params()
                self.state = 203
                self.match(MiniGoParser.RBRACK)
                pass

            elif la_ == 2:
                self.state = 205
                self.expression7()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 213
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                    self.state = 208
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 209
                    self.match(MiniGoParser.POINTTO)
                    self.state = 210
                    self.expression7() 
                self.state = 215
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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

        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression7




    def expression7(self):

        localctx = MiniGoParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expression7)
        try:
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.match(MiniGoParser.LPAREN)
                self.state = 217
                self.expression(0)
                self.state = 218
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.match(MiniGoParser.ID)
                self.state = 224
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 221
                    self.match(MiniGoParser.LBRACK)
                    self.state = 222
                    self.match(MiniGoParser.INT_LIT)
                    self.state = 223
                    self.match(MiniGoParser.RBRACK)


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 226
                self.literal()
                self.state = 230
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                if la_ == 1:
                    self.state = 227
                    self.match(MiniGoParser.LBRACK)
                    self.state = 228
                    self.match(MiniGoParser.INT_LIT)
                    self.state = 229
                    self.match(MiniGoParser.RBRACK)


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 232
                self.func_call()
                self.state = 236
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    self.state = 233
                    self.match(MiniGoParser.LBRACK)
                    self.state = 234
                    self.match(MiniGoParser.INT_LIT)
                    self.state = 235
                    self.match(MiniGoParser.RBRACK)


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
        self.enterRule(localctx, 36, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(MiniGoParser.ID)
            self.state = 241
            self.match(MiniGoParser.LPAREN)
            self.state = 242
            self.list_expression()
            self.state = 243
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
        self._predicates[10] = self.expression_sempred
        self._predicates[11] = self.expression1_sempred
        self._predicates[12] = self.expression2_sempred
        self._predicates[13] = self.expression3_sempred
        self._predicates[14] = self.expression4_sempred
        self._predicates[16] = self.expression6_sempred
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
         




