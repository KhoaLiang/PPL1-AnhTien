grammar VoTien;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

//! -------------------------- Lexical structure ----------------------- // TODO KeyWord
//TODO KeyWord

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

//!  -------------------------- end Lexical structure ------------------- //

// //! --------------------------  parser structure ----------------------- //

// declared
program: (ID | ERROR_STRING*) EOF;


// //! -------------------------- end  parser structure ----------------------- //