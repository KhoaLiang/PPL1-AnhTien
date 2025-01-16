//! --------------------------  START LEXER structure ----------------------- //
// TODO KeyWord
TRUE: 'true';
FALSE: 'false';
NUMBER: 'number';
BOOL: 'bool';
STRING: 'string'; 
RETURN: 'return';
VAR: 'var'; 
DYNAMIC: 'dynamic';
FUNC: 'func'; 
FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONTINUE: 'continue'; 
IF: 'if'; 
ELSE: 'else'; 
ELIF: 'elif'; 
BEGIN: 'begin';
END: 'end'; 
NOT: 'not'; 
AND: 'and'; 
OR: 'or';


// TODO Operators
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQUAL: '=';
NOT_EQUAL: '!=';
LT: '<';
GT: '>';
LE: '<=';
GE: '>=';
STR_EQ: '==';
STR_CONCAT: '...';
ASSIGNINIT: '<-';

// TODO Separators
LSB: '[';
RSB: ']';
LP: '(';
RP: ')';
CM: ',';

// TODO Identifiers
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// TODO Literal 
NUMBER_LIT: DIGITS OPT_FRAC OPT_EXP;
fragment DIGIT: [0-9];
fragment DIGITS: DIGIT+;
fragment OPT_FRAC: ('.' DIGIT*)?;
fragment OPT_EXP: ([Ee] [+-]? DIGITS)?;

STRING_LIT: '"' STR_CHAR* '"' {
    self.text = self.text[1:-1] };
fragment STR_CHAR: ~[\r\n\\"] | ESC_SEQ;
fragment ESC_SEQ: '\\' [bfrnt'\\] | '\'"';
fragment ESC_ILLEGAL: [\r] | '\\' ~[bfrnt'\\];

// TODO NEWLINE COMMENTS WS
NEWLINE: [\n]; // 
COMMENTS: '##' ~[\n\r]* -> skip; // Comments
WS : [ \f\b\t\r]+ -> skip ; // skip spaces, tabs

// TODO ERROR
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


//!  -------------------------- END LEXER structure ------------------- //