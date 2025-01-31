import sys
import os
import unittest
import inspect

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    
    def test_001(self):
        """Keywords"""
        self.assertTrue(TestLexer.test("if","if,<EOF>", inspect.stack()[0].function))

    def test_002(self):
        """Operators"""
        self.assertTrue(TestLexer.test("+","+,<EOF>", inspect.stack()[0].function))
        
    def test_003(self):
        """Separators"""
        self.assertTrue(TestLexer.test("[]","[,],<EOF>", inspect.stack()[0].function))
        
    def test_004(self):
        """Identifiers"""
        self.assertTrue(TestLexer.test("_ANHKHOA","_ANHKHOA,<EOF>", inspect.stack()[0].function))
        
    def test_005(self):
        """Literals INT"""
        self.assertTrue(TestLexer.test("12","12,<EOF>", inspect.stack()[0].function))
        
    def test_006(self):
        """Literals INT 16*1 + 1 = 17"""
        self.assertTrue(TestLexer.test("0x11","17,<EOF>", inspect.stack()[0].function))
    
    def test_007(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.test("12.e-8","12.e-8,<EOF>", inspect.stack()[0].function))
    
    def test_008(self):
        """Literals String"""
        self.assertTrue(TestLexer.test(""" "ANHKHOA \\r" ""","ANHKHOA \\r,<EOF>", inspect.stack()[0].function))
        
    def test_009(self):
        """COMMENTS"""
        self.assertTrue(TestLexer.test("// ANHKHOA","<EOF>", inspect.stack()[0].function))

    def test_010(self):
        """COMMENTS"""
        self.assertTrue(TestLexer.test("/* VO /* /*TIEN*/ */ SHIBA","SHIBA,<EOF>", inspect.stack()[0].function))

    def test_011(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.test("^","ErrorToken ^", inspect.stack()[0].function))

    def test_012(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.test(""" "ANHKHOA\n" ""","Unclosed string: ANHKHOA", inspect.stack()[0].function))
    
    def test_013(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.test(""" "ANHKHOA\\f" ""","Illegal escape in string: ANHKHOA\\f", inspect.stack()[0].function))

    def test_014(self):
        """NEWLINE"""
        self.assertTrue(TestLexer.test(""" 
            const a = 2;
""","\n,const,a,=,2,;,\n,<EOF>", inspect.stack()[0].function))

    def test_015(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.test("0452.", "0,452.,<EOF>", inspect.stack()[0].function))

    def test_016(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.test("010.010e-020", "0,10.010e-0,20,<EOF>", inspect.stack()[0].function))

    def test_017(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.test("00.1e2", "0,0.1e2,<EOF>", inspect.stack()[0].function))

    def test_018(self):
        """Expressions"""
        self.assertTrue(TestLexer.test("""    
            var z ANHKHOA = a[2, 3];                         
        ""","\n,var,z,ANHKHOA,=,a,[,2,,,3,],;,\n,<EOF>", inspect.stack()[0].function))

    def test_019(self):
        """Declared"""
        self.assertTrue(TestLexer.test("""    
            type Calculator struct {
                value int;
                a [2]int; a [2]ID;
                c Calculator                    
            }
""","\n,type,Calculator,struct,{,\n,value,int,;,\n,a,[,2,],int,;,a,[,2,],ID,;,\n,c,Calculator,\n,},\n,<EOF>", inspect.stack()[0].function))

    def test_020(self):
        """Keywords"""
        self.assertTrue(TestLexer.test("else","else,<EOF>", inspect.stack()[0].function))

    def test_021(self):
        """Keywords"""
        self.assertTrue(TestLexer.test("for","for,<EOF>", inspect.stack()[0].function))

    def test_022(self):
        """Keywords"""
        self.assertTrue(TestLexer.test("return","return,<EOF>", inspect.stack()[0].function))

    def test_023(self):
        """Keywords"""
        self.assertTrue(TestLexer.test("func","func,<EOF>", inspect.stack()[0].function))

    def test_024(self):
        """Keywords"""
        self.assertTrue(TestLexer.test("type","type,<EOF>", inspect.stack()[0].function))

    def test_025(self):
        """Keywords"""
        self.assertTrue(TestLexer.test("struct","struct,<EOF>", inspect.stack()[0].function))

    def test_026(self):
        """Keywords"""
        self.assertTrue(TestLexer.test("interface","interface,<EOF>", inspect.stack()[0].function))

    def test_027(self):
        """Keywords"""
        self.assertTrue(TestLexer.test("string","string,<EOF>", inspect.stack()[0].function))

    def test_028(self):
        """Keywords"""
        self.assertTrue(TestLexer.test("int","int,<EOF>", inspect.stack()[0].function))

    def test_029(self):
        """Keywords"""
        self.assertTrue(TestLexer.test("float","float,<EOF>", inspect.stack()[0].function))

    def test_030(self):
        """Keywords"""
        self.assertTrue(TestLexer.test("boolean","boolean,<EOF>", inspect.stack()[0].function))

    def test_031(self):
        """Keywords"""
        self.assertTrue(TestLexer.test("const","const,<EOF>", inspect.stack()[0].function))

    def test_032(self):
        """Keywords"""
        self.assertTrue(TestLexer.test("var","var,<EOF>", inspect.stack()[0].function))

    def test_033(self):
        """Keywords"""
        self.assertTrue(TestLexer.test("continue","continue,<EOF>", inspect.stack()[0].function))

    def test_034(self):
        """Keywords"""
        self.assertTrue(TestLexer.test("break","break,<EOF>", inspect.stack()[0].function))

    def test_035(self):
        """Keywords"""
        self.assertTrue(TestLexer.test("range","range,<EOF>", inspect.stack()[0].function))

    def test_036(self):
        """Keywords"""
        self.assertTrue(TestLexer.test("nil","nil,<EOF>", inspect.stack()[0].function))

    def test_037(self):
        """Keywords"""
        self.assertTrue(TestLexer.test("true","true,<EOF>", inspect.stack()[0].function))

    def test_038(self):
        """Keywords"""
        self.assertTrue(TestLexer.test("false","false,<EOF>", inspect.stack()[0].function))

    def test_039(self):
        """Operators"""
        self.assertTrue(TestLexer.test("-","-,<EOF>", inspect.stack()[0].function))

    def test_040(self):
        """Operators"""
        self.assertTrue(TestLexer.test("*","*,<EOF>", inspect.stack()[0].function))

    def test_041(self):
        """Operators"""
        self.assertTrue(TestLexer.test("/","/,<EOF>", inspect.stack()[0].function))

    def test_042(self):
        """Operators"""
        self.assertTrue(TestLexer.test("%","%,<EOF>", inspect.stack()[0].function))

    def test_043(self):
        """Operators"""
        self.assertTrue(TestLexer.test("==","==,<EOF>", inspect.stack()[0].function))

    def test_044(self):
        """Operators"""
        self.assertTrue(TestLexer.test("!=","!=,<EOF>", inspect.stack()[0].function))

    def test_045(self):
        """Operators"""
        self.assertTrue(TestLexer.test("<","<,<EOF>", inspect.stack()[0].function))

    def test_046(self):
        """Operators"""
        self.assertTrue(TestLexer.test("<=","<=,<EOF>", inspect.stack()[0].function))

    def test_047(self):
        """Operators"""
        self.assertTrue(TestLexer.test(">",">,<EOF>", inspect.stack()[0].function))

    def test_048(self):
        """Operators"""
        self.assertTrue(TestLexer.test(">=",">=,<EOF>", inspect.stack()[0].function))

    def test_049(self):
        """Operators"""
        self.assertTrue(TestLexer.test("&&","&&,<EOF>", inspect.stack()[0].function))

    def test_050(self):
        """Operators"""
        self.assertTrue(TestLexer.test("||","||,<EOF>", inspect.stack()[0].function))

    def test_051(self):
        """Operators"""
        self.assertTrue(TestLexer.test("!","!,<EOF>", inspect.stack()[0].function))

    def test_052(self):
        """Operators"""
        self.assertTrue(TestLexer.test("=","=,<EOF>", inspect.stack()[0].function))

    def test_053(self):
        """Operators"""
        self.assertTrue(TestLexer.test("+=","+=,<EOF>", inspect.stack()[0].function))

    def test_054(self):
        """Operators"""
        self.assertTrue(TestLexer.test("-=","-=,<EOF>", inspect.stack()[0].function))

    def test_055(self):
        """Operators"""
        self.assertTrue(TestLexer.test("*=","*=,<EOF>", inspect.stack()[0].function))

    def test_056(self):
        """Operators"""
        self.assertTrue(TestLexer.test("/=","/=,<EOF>", inspect.stack()[0].function))

    def test_057(self):
        """Operators"""
        self.assertTrue(TestLexer.test("%=","%=,<EOF>", inspect.stack()[0].function))

    def test_058(self):
        """Operators"""
        self.assertTrue(TestLexer.test(".",".,<EOF>", inspect.stack()[0].function))

    def test_059(self):
        """Operators"""
        self.assertTrue(TestLexer.test(":=",":=,<EOF>", inspect.stack()[0].function))

    def test_060(self):
        """Separators"""
        self.assertTrue(TestLexer.test("(", "(,<EOF>", inspect.stack()[0].function))

    def test_061(self):
        """Separators"""
        self.assertTrue(TestLexer.test(")", "),<EOF>", inspect.stack()[0].function))

    def test_062(self):
        """Separators"""
        self.assertTrue(TestLexer.test("{", "{,<EOF>", inspect.stack()[0].function))

    def test_063(self):
        """Separators"""
        self.assertTrue(TestLexer.test("}", "},<EOF>", inspect.stack()[0].function))

    def test_064(self):
        """Separators"""
        self.assertTrue(TestLexer.test("[", "[,<EOF>", inspect.stack()[0].function))

    def test_065(self):
        """Separators"""
        self.assertTrue(TestLexer.test("]", "],<EOF>", inspect.stack()[0].function))

    def test_066(self):
        """Separators"""
        self.assertTrue(TestLexer.test(",", ",,<EOF>", inspect.stack()[0].function))

    def test_067(self):
        """Separators"""
        self.assertTrue(TestLexer.test(";", ";,<EOF>", inspect.stack()[0].function))

    def test_068(self):
        """Identifiers"""
        self.assertTrue(TestLexer.test("a", "a,<EOF>", inspect.stack()[0].function))

    def test_069(self):
        """Identifiers"""
        self.assertTrue(TestLexer.test("A", "A,<EOF>", inspect.stack()[0].function))

    def test_070(self):
        """Identifiers"""
        self.assertTrue(TestLexer.test("a1", "a1,<EOF>", inspect.stack()[0].function))

    def test_071(self):
        """Identifiers"""
        self.assertTrue(TestLexer.test("A1", "A1,<EOF>", inspect.stack()[0].function))

    def test_072(self):
        """Identifiers"""
        self.assertTrue(TestLexer.test("_a", "_a,<EOF>", inspect.stack()[0].function))

    def test_073(self):
        """Identifiers"""
        self.assertTrue(TestLexer.test("_A", "_A,<EOF>", inspect.stack()[0].function))

    def test_074(self):
        """Identifiers"""
        self.assertTrue(TestLexer.test("a_", "a_,<EOF>", inspect.stack()[0].function))

    def test_075(self):
        """Identifiers"""
        self.assertTrue(TestLexer.test("A_", "A_,<EOF>", inspect.stack()[0].function))

    def test_076(self):
        """Identifiers"""
        self.assertTrue(TestLexer.test("a1_", "a1_,<EOF>", inspect.stack()[0].function))

    def test_077(self):
        """Identifiers"""
        self.assertTrue(TestLexer.test("A1_", "A1_,<EOF>", inspect.stack()[0].function))

    def test_078(self):
        """Literals INT"""
        self.assertTrue(TestLexer.test("0", "0,<EOF>", inspect.stack()[0].function))

    def test_079(self):
        """Literals INT"""
        self.assertTrue(TestLexer.test("123", "123,<EOF>", inspect.stack()[0].function))

    def test_080(self):
        """Literals INT"""
        self.assertTrue(TestLexer.test("0b101", "5,<EOF>", inspect.stack()[0].function))

    def test_081(self):
        """Literals INT"""
        self.assertTrue(TestLexer.test("0o17", "15,<EOF>", inspect.stack()[0].function))

    def test_082(self):
        """Literals INT"""
        self.assertTrue(TestLexer.test("0x1F", "31,<EOF>", inspect.stack()[0].function))

    def test_083(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.test("0.1", "0.1,<EOF>", inspect.stack()[0].function))

    def test_084(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.test("1.0", "1.0,<EOF>", inspect.stack()[0].function))
        
    def test_085(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.test("1.2567", "1.2567,<EOF>", inspect.stack()[0].function))

    def test_086(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.test("23232.23237", "23232.23237,<EOF>", inspect.stack()[0].function))


    def test_087(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.test("1.0e-2", "1.0e-2,<EOF>", inspect.stack()[0].function))

    def test_088(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.test("0.1e2", "0.1e2,<EOF>", inspect.stack()[0].function))
    def test_089(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.test("00.1e2", "0,0.1e2,<EOF>", inspect.stack()[0].function))

    def test_090(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.test("1.0e+2", "1.0e+2,<EOF>", inspect.stack()[0].function))

    def test_091(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.test("1.0e-75", "1.0e-75,<EOF>", inspect.stack()[0].function))
    
    def test_092(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.test("45.0e-2", "45.0e-2,<EOF>", inspect.stack()[0].function))
    
    def test_093(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.test("1.0e-2", "1.0e-2,<EOF>", inspect.stack()[0].function))

    def test_094(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.test("0.1e-2", "0.1e-2,<EOF>", inspect.stack()[0].function))

    def test_095(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.test("0.1e-11", "0.1e-11,<EOF>", inspect.stack()[0].function))

    def test_096(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.test("1.0e2", "1.0e2,<EOF>", inspect.stack()[0].function))

    def test_097(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.test("0.1e+2", "0.1e+2,<EOF>", inspect.stack()[0].function))

    def test_098(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.test("0.1e+8", "0.1e+8,<EOF>", inspect.stack()[0].function))

    def test_099(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.test("1.0e+2", "1.0e+2,<EOF>", inspect.stack()[0].function))

    def test_100(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.test("0.1e+2", "0.1e+2,<EOF>", inspect.stack()[0].function))