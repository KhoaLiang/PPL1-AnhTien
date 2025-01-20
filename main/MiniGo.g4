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

//program: 'votien'+ EOF;
// ! ---------------- PASER DEADLINE PASS 9 TEST CASE 23:59 19/1 ----------------------- */
//program: ((CONST ID ASSIGN expression) | NEWLINE)+ EOF;
//TODO declared
program: NEWLINE* declared (declared | NEWLINE)* EOF;
//TODO Variables 5.1 pdf
declared:
	variables_declared
	| constants_declared
	| function_declared
	| method_declared
	| struct_declared
	| interface_declared;

// Variable declare
variables_declared: (implicit_var | keyword_var) SEMICOL; 
//TODO implicit_var, keyword_var
implicit_var: VAR ID ASSIGN expression;
keyword_var: VAR ( primitive_declaration |  array_declaration | interface_type) (ASSIGN expression)?;
//type of variable

primitive_type: INT | FLOAT | BOOLEAN | STRING;
primitive_declaration: ID primitive_type;
interface_type: ID STR ; //struct or interface
dimension_list: LBRACK INT_LIT RBRACK (LBRACK INT_LIT RBRACK)*;
array_declaration: dimension_list (primitive_type | ID); // array_declaration  view ID as the type of struct or interface

//Constant declare
constants_declared: CONST ID ASSIGN (expression | array_declaration expression) SEMICOL;

// function declare
function_declared: FUNC ID LPAREN (prameters_list)? RPAREN (primitive_type | ID | array_declaration)? LBRACE RBRACE; //(ignore? return_statement | ignore? block_statement | ignore);

// method declare
//(ID1 ID2) --> ID1 represent the name of the struct or interface instance, ID2 represent the name of the struct or interface for example: func (c Calculator) VoTien(x int) int {}
method_declared: FUNC LPAREN (ID ID) RPAREN ID LPAREN (prameters_list)? RPAREN (primitive_type | ID | array_declaration)? LBRACE RBRACE; //(ignore? return_statement | ignore? block_statement | ignore); 

// struct declare
struct_declared: TYPE ID STRUCT LBRACE ignore* ( prameter SEMICOL? (ignore)*)* RBRACE;
// struct declare
interface_declared: TYPE ID INTERFACE LBRACE ignore* ( ID LPAREN (prameters_list)? RPAREN (primitive_type | ID | array_declaration)? SEMICOL (ignore)*)* RBRACE;

//TODO prameters_list
prameters_list: prameter COMMA prameters_list | prameter; 
prameter: primitive_declaration | (ID array_declaration) | ID;
//TODO Literal 6.6 pdf
literal:
    INT_LIT
    | FLOAT_LIT
    | STRING_LIT
    | TRUE
    | FALSE
    | array_literal
    | struct_literal;

array_literal: LBRACE params RBRACE;
struct_literal: ID LBRACE list_elements RBRACE;



//TODO Expression 6 pdf
list_expression: params | ; // list này có thể rỗng
params: expression COMMA params | expression; //params thì không -> làm param của index trong mảng

list_elements: (ID COLON expression) (COMMA ID COLON expression)*;

expression: expression OR expression1 | expression1;
expression1: expression1 AND expression2 | expression2;
expression2: expression2 EQUAL expression3 | expression2 DIFF expression3 | expression2 LT expression3 | expression2 LTE expression3 | expression2 RT expression3 | expression2 RTE expression3 | expression3;
expression3: expression3 ADD expression4 | expression3 SUB expression4 | expression4;
expression4: expression4 MUL expression5 | expression4 DIV expression5 | expression4 MOD expression5 | expression5;
expression5: NOT expression5 | SUB expression5 | expression6;
expression6: expression6 (LPAREN list_expression RPAREN)? LBRACK (params) RBRACK | expression6 POINTTO expression7 | expression7;

// expression6: LBRACK expression6 RBRACK (LBRACK expression6 RBRACK)* type_of_array? | expression6 POINTTO expression7 | expression7;
expression7: LPAREN expression RPAREN | ID  | literal  | func_call;
func_call: ID LPAREN list_expression RPAREN;

// kí tự bỏ qua
ignore: NEWLINE+;

//TODO Statement 5 and 4 pdf
// list_statement: statement list_statement | statement;
// statement:
// 	(
// 		declared_statement
// 		| assign_statement
// 		| if_statement
// 		| for_statement
// 		| break_statement
// 		| continue_statement
// 		| call_statement
// 		| return_statement
// 	);

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

STR: 'str';

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
COLON: ':';
ASSIGNNIT: ':='; //(same as <-)

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
WS: [ \t\f\r]+ -> skip; // skip spaces, tabs, form feeds, and carriage returns
NEWLINE: '\r'? '\n';

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