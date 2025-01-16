grammar VoTien;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

//! -------------------------- Lexical structure ----------------------- // TODO KeyWord
//TODO KeyWord
T: 'T';
CONTINUE: 'continue';
F: 'F';
IF: 'if'; 
ELSE: 'else';
FOR: 'for';
BOOL: 'bool';
NUMBER: 'number';
RETURN: 'return';
STRING: 'string';
FUNC: 'func'; 
ENDFUNC: 'endfunc';
CALL: 'call';

//TODO Operators

//TODO Separators

// TODO Identifiers
ID: (.)((.)(.))*;

//TODO Literal

//TODO SKIP

// TODO ERROR
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: 
ILLIGAL ESCAPE:

//exercise

//!  -------------------------- end Lexical structure ------------------- //

// //! --------------------------  parser structure ----------------------- //

// declared
program: (ID | ERROR_STRING*) EOF;


// //! -------------------------- end  parser structure ----------------------- //