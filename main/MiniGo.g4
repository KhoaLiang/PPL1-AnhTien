grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language = Python3;
}

program: 'votien'+ EOF;
// ! ---------------- PASER DEADLINE PASS 13 TEST CASE 23:59 19/1 ----------------------- */
// program: ((CONST ID ASSIGN expression) | NEWLINE)+ EOF;

// //TODO Literal 6.6 pdf
// literal:
// 	INT_LIT
// 	| FLOAT_LIT
// 	| STRING_LIT
// 	| TRUE
// 	| FALSE
// 	| array_literal
// 	| struct_literal;

// // TODO 5.2 Expressions 6 pdf
// list_expression: expression COMMA list_expression | expression;
// expression: expression OR expression1 | expression1;

//! ---------------- PASER ----------------------- */


// ! ---------------- LEXER DEADLINE PASS 13 TEST CASE 23:59 16/1 ----------------------- */

//TODO Keywords 3.3.2 pdf
IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN: 'return';
FUNC: 'func'; 
TYPE: 'type';
STRUCT: 'struct';
INTERFACE: 'interface';
STRING: 'string';
INT: 'int';
FLOAT: 'float';
BOOLEAN: 'boolean';
CONST: 'const';
VAR: 'var';
CONTINUE: 'continue';
BREAK: 'break';
RANGE: 'range';
NIL: 'nil';
TRUE: 'true';
FALSE: 'false';

//TODO Operators 3.3.3 pdf
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQUAL: '==';
DIFF: '!=';
LT: '<';
LTE: '<=';
RT: '>';
RTE: '>=';
AND: '&&';
OR: '||';
NOT: '!';
ASSIGN: '=';
ASSIGNADD: '+=';
ASSIGNSUB: '-=';
ASSIGNMUL: '*=';
ASSIGNDIV: '/=';
ASSIGNMOD: '%=';
POINTTO: '.';

//TODO Separators 3.3.4 pdf
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
LBRACK: '[';
RBRACK: ']';
COMMA: ',';
SEMICOL: ';';

//TODO Identifiers 3.3.1 pdf
ID: [a-zA-Z_][a-zA-Z0-9_]*;

//TODO Literals 3.3.5 pdf
// INT_LIT: [0-9];
// //INTERGER LITERAL
// DEC_INT: '0' | [1-9] [0-9]*;
// BIN_INT: '0' [bB] [01]+ {
//     self.text = str(int(self.text[2:], 2))
// };
// OCT_INT: '0' [oO] [0-7]+{
//     self.text = str(int(self.text[2:], 8))
// };
// HEX_INT: '0' [xX] [0-9a-fA-F]+{
//     self.text = str(int(self.text[2:], 16))
// };

INT_LIT: 
    DEC_INT | 
    BIN_INT {self.text = str(int(self.text[2:], 2))} | 
    OCT_INT {self.text = str(int(self.text[2:], 8))} | 
    HEX_INT {self.text = str(int(self.text[2:], 16))};

fragment DEC_INT: '0' | [1-9] [0-9]*;
fragment BIN_INT: '0' [bB] [01]+;
fragment OCT_INT: '0' [oO] [0-7]+;
fragment HEX_INT: '0' [xX] [0-9a-fA-F]+;

//FLOAT LITERAL
FLOAT_LIT: DIGITS '.' (DIGITS)? OPT_EXP;
fragment DIGIT: [0-9];
fragment DIGITS: DIGIT+;
fragment OPT_EXP: ([Ee] [+-]? DIGITS)?;

//STRING LITERAL
STRING_LIT: '"' STR_CHAR* '"' {
    self.text = self.text[1:-1] 
};
fragment STR_CHAR: ~[\r\n\\"] | ESC_SEQ;
fragment ESC_SEQ: '\\' [ntr"\\];
fragment ESC_ILLEGAL: '\\' ~[ntr"\\];


//TODO skip 3.1 and 3.2 pdf
WS: [ \t\f\r\n]+ -> skip; // skip spaces, tabs 
NEWLINE: '\r'? '\n' -> skip; // skip newline
//SINGLE LINE COMMENT
COMMENT: '//' ~[\r\n]* -> skip;

//MULTI LINE COMMENT
ML_COMMENT: '/*' (ML_COMMENT | .)*? '*/' -> skip;

//TODO ERROR pdf BTL1 + lexererr.py
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' STR_CHAR* ('\r\n' | '\n' | EOF) {
    if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
        raise UncloseString(self.text[1:-2])
    elif (self.text[-1] == '\n'):
        raise UncloseString(self.text[1:-1])
    else:
        raise UncloseString(self.text[1:])
};

ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL {
    raise IllegalEscape(self.text[1:])
};

//! ---------------- LEXER ----------------------- */