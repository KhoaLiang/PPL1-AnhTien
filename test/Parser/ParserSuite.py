"""
 * Initial code for Assignment 1, 2
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 07.01.2025
"""

import unittest
from TestUtils import TestParser
import inspect

class ParserSuite(unittest.TestCase):
    def test_001(self):
        """Literal"""
        self.assertTrue(TestParser.test("const LAKhoa = 1;","successful", inspect.stack()[0].function))

    def test_002(self):
        """Literal"""
        self.assertTrue(TestParser.test("const LAKhoa = true;","successful", inspect.stack()[0].function))

    def test_003(self):
        """Literal"""
        self.assertTrue(TestParser.test("const LAKhoa = [5][0]string{1, \"string\"};","successful", inspect.stack()[0].function))

    def test_004(self):
        """Literal"""
        self.assertTrue(TestParser.test("const LAKhoa = [1.]ID{1, 3};","Error on line 1 col 16: 1.", inspect.stack()[0].function))

    def test_005(self):
        """Literal"""
        self.assertTrue(TestParser.test("const LAKhoa = Person{name: \"Alice\", age: 30};","successful", inspect.stack()[0].function))

    def test_006(self):
        """expression"""
        self.assertTrue(TestParser.test("const LAKhoa = 1 || 2 && c + 3 / 2 - -1;","successful", inspect.stack()[0].function))

    def test_007(self):
        """expression"""
        self.assertTrue(TestParser.test("const LAKhoa = 1[2] + foo()[2] + ID[2].b.b;","successful", inspect.stack()[0].function))

    def test_008(self):
        """expression"""
        self.assertTrue(TestParser.test("const LAKhoa = ca.foo(132) + b.c[2];","successful", inspect.stack()[0].function))

    def test_009(self):
        """expression"""
        self.assertTrue(TestParser.test("const LAKhoa = a.a.foo();","successful", inspect.stack()[0].function))

    def test_010(self):
        """declared variables"""
        self.assertTrue(TestParser.test("""
            var x int = foo() + 3 / 4;
            var y = "Hello" / 4;   
            var z str;
        ""","successful", inspect.stack()[0].function))

    def test_011(self):
        """declared constants"""
        self.assertTrue(TestParser.test("""
            const LAKhoa = a.b() + 2;
        ""","successful", inspect.stack()[0].function))

    def test_012(self):
        """declared function"""
        self.assertTrue(TestParser.test("""
            func LAKhoa(x int, y int) int {}
            func LAKhoa1() [2][3] ID {}         
            func LAKhoa2() {}                                       
        ""","successful", inspect.stack()[0].function))

    def test_013(self):
        """declared method"""
        self.assertTrue(TestParser.test("""
            func (c Calculator) LAKhoa(x int) int {}  
            func (c Calculator) LAKhoa() ID {}      
            func (c Calculator) LAKhoa(x int, y [2]LAKhoa) {}                                                      
        ""","successful", inspect.stack()[0].function))

    def test_014(self):
        """declared struct"""
        self.assertTrue(TestParser.test("""
            type LAKhoa struct {
                LAKhoa string ;
                LAKhoa [1][3]LAKhoa ;                     
            }
            type LAKhoa struct {}                                                                       
        ""","successful", inspect.stack()[0].function))

    def test_015(self):
        """declared struct"""
        self.assertTrue(TestParser.test("""
            type LAKhoa struct {
                LAKhoa string ;
                LAKhoa [1][3]LAKhoa ;                     
            }
            type LAKhoa struct {}                                                                       
        ""","successful", inspect.stack()[0].function))

    def test_016(self):
        """declared Interface"""
        self.assertTrue(TestParser.test("""
            type Calculator interface {
                                        
                Add(x, y int) int;
                Subtract(a, b float, c int) [3]ID;
                Reset()
                                        
                SayHello(name string);
                                        
            }
            type LAKhoa interface {}                                                                       
        ""","successful", inspect.stack()[0].function))

    def test_017(self):
        """declared_statement"""
        self.assertTrue(TestParser.test("""    
            func LAKhoa() {
                var x int = foo() + 3 / 4;
                var y = "Hello" / 4;   
                var z str;
                                        
                const LAKhoa = a.b() + 2;
            }                                       
        ""","successful", inspect.stack()[0].function))


    def test_018(self):
        """assign_statement"""
        self.assertTrue(TestParser.test("""    
            func LAKhoa() {
                x  := foo() + 3 / 4;
                x.c[2][4] := 1 + 2;                       
            }                                       
        ""","successful", inspect.stack()[0].function))

    def test_019(self):
        """if_statement"""
        self.assertTrue(TestParser.test("""    
            func LAKhoa() {
                if (x > 10) {} 
                if (x > 10) {
                  
                } else if (x == 10) {
                    var z str;
                } else {
                    var z ID;
                }
            }
        ""","successful", inspect.stack()[0].function))

    def test_020(self):
        """for_statement"""
        self.assertTrue(TestParser.test("""    
            func LAKhoa() {
                for i < 10 {}
                for i := 0; i < 10; i += 1 {}
                for index, value := range array {}
            }
        ""","successful", inspect.stack()[0].function))


    def test_021(self):
        """break and continue, return, Call  statement"""
        self.assertTrue(TestParser.test("""    
            func LAKhoa() {                           
                for i < 10 {break;}
                break;
                continue;
                return 1;
                return
                foo(2 + x, 4 / y); m.goo();                        
             }
                                        
        ""","successful", inspect.stack()[0].function))
    def test_022(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z LAKhoa = [true]int{1};                         
        ""","Error on line 2 col 28: true", inspect.stack()[0].function))
    def test_023(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z LAKhoa = [2]int{1;                         
        ""","Error on line 2 col 35: ;", inspect.stack()[0].function))
    def test_024(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z LAKhoa = [2]int{};                         
        ""","Error on line 2 col 34: }", inspect.stack()[0].function))
    def test_025(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z LAKhoa = ID {};                         
        ""","successful", inspect.stack()[0].function))
    def test_026(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z LAKhoa = a >= 2 <= "string" > a[2][3] < ID{A: 2} >= [2]S{2};                         
        ""","successful", inspect.stack()[0].function))
    def test_027(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z LAKhoa = a[2][3][a + 2];                         
        ""","successful", inspect.stack()[0].function))
    def test_028(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z LAKhoa = a[2, 3];                         
        ""","Error on line 2 col 30: ,", inspect.stack()[0].function))
    def test_029(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            var a [2][3]int = 2 + 3 / 4;
        ""","successful", inspect.stack()[0].function))
    def test_030(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            func Add(a) [2]id {}
""","Error on line 2 col 22: )", inspect.stack()[0].function))
    def test_031(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            type Calculator struct {
                                        
                value int;
                a [2]int; a [2]ID;
                c Calculator                    
            }
""","successful", inspect.stack()[0].function))
    def test_032(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            type Calculator struct {
                c Calculator
                c Cal a int;         
            }
""","Error on line 4 col 22: a", inspect.stack()[0].function))
    def test_033(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            type Calculator interface {
                Add(x int,c,d ID); Add()
        }
""","successful", inspect.stack()[0].function))
    def test_034(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            type Calculator interface {}
            type Person struct{};
""","successful", inspect.stack()[0].function))
    def test_035(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            type Calculator interface {};
""","successful", inspect.stack()[0].function))
    def test_036(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func (c c) Add(x, c int) {}
""","Error on line 2 col 28: ,", inspect.stack()[0].function))
    def test_037(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
                                        
            func (c c) Add(x int) {}
                                        
            func Add(x int) {} var c int;
                                        
            var c int; type Calculator struct{} type Calculator struct{} var c int;
""","Error on line 7 col 48: type", inspect.stack()[0].function))
    def test_038(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        const a = a[2].b
                                        var a = a[2].b; var a = "s";           
                                    }""","successful", inspect.stack()[0].function))
    def test_039(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        a += 2;
                                        a -= a[2].b();
                                        a /= 2
                                        a *= 2
                                        a %= 2;       
                                    }""","successful", inspect.stack()[0].function))
    def test_040(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        a[2].b := 2;       
                                    }""","successful", inspect.stack()[0].function))
    def test_041(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        a.c[2].e[3].k += 2;       
                                    }""","successful", inspect.stack()[0].function))
    def test_042(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        a.foo() += 2;       
                                    }""","Error on line 3 col 48: +=", inspect.stack()[0].function))
    def test_043(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        2 + 2 += 2;       
                                    }""","Error on line 3 col 40: 2", inspect.stack()[0].function))
    def test_044(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                       a[2+3&&2] += foo().b[2];       
                                    }""","successful", inspect.stack()[0].function))
    def test_045(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        if (x.foo().b[2]) {
                                            a := 2;
                                        } else if (a && b) {

                                        } else {
                                            a := 2;
                                        }   
                                    }""","successful", inspect.stack()[0].function))
    def test_046(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        if (x.foo().b[2]) 
                                        {
                                            if (){}
                                        } 
                                    }""","Error on line 5 col 48: )", inspect.stack()[0].function))
    def test_047(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        if (x.foo().b[2]) 
                                        {
                                            if (1){} else {}

                                        } else if(2)
                                        {
                                        }
                                    }""","successful", inspect.stack()[0].function))
    def test_048(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        if (x.foo().b[2]) 
                                        {
                                        } else if(1)
                                        {
                                        }else if(1)
                                        {
                                        }else if(2)
                                        {
                                        }else 
                                        {
                                        }
                                    }""","successful", inspect.stack()[0].function))
    def test_049(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for var i = 0; i < 10; i += 1 {
                                            // loop body
                                        }
                                    }""","successful", inspect.stack()[0].function))
    # I probly have to separate this test case, implicit var specifically initialized for the for loop
    def test_050(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for var i [2]int = 0; foo().a.b(); i[3] := 1 {
                                            // loop body
                                        }
                                    }""","successful", inspect.stack()[0].function))
    def test_051(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for index, value := range arr[2] {
                                        }
                                    }""","successful", inspect.stack()[0].function))
    def test_052(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        break;
                                        continue
                                        break; continue; break
                                    }""","successful", inspect.stack()[0].function))
    def test_053(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        a[2][3].foo(2 + 3, a {a:2})
                                    }""","successful", inspect.stack()[0].function))
    def test_054(self):
        """Literal"""
        self.assertTrue(TestParser.test("const x = 3.14;","successful", inspect.stack()[0].function))

    def test_055(self):
        """Literal"""
        self.assertTrue(TestParser.test("const y = \"Hello, World!\";","successful", inspect.stack()[0].function))

    def test_056(self):
        """Literal"""
        self.assertTrue(TestParser.test("const z = true;","successful", inspect.stack()[0].function))

    def test_057(self):
        """Expression"""
        self.assertTrue(TestParser.test("const a = 5 + 3 * 2;","successful", inspect.stack()[0].function))

    def test_058(self):
        """Expression"""
        self.assertTrue(TestParser.test("const b = (1 + 2) * (3 - 4);","successful", inspect.stack()[0].function))

    def test_059(self):
        """Expression"""
        self.assertTrue(TestParser.test("const c = a && b || !c;","successful", inspect.stack()[0].function))

    def test_060(self):
        """Declared"""
        self.assertTrue(TestParser.test("var x int = 10;","successful", inspect.stack()[0].function))

    def test_061(self):
        """Declared"""
        self.assertTrue(TestParser.test("var y string = \"test\";","successful", inspect.stack()[0].function))

    def test_062(self):
        """Declared"""
        self.assertTrue(TestParser.test("var z bool = false;","successful", inspect.stack()[0].function))

    def test_063(self):
        """Struct"""
        self.assertTrue(TestParser.test("""
            type Person struct {
                name string;
                age int;
            }
        ""","successful", inspect.stack()[0].function))

    def test_064(self):
        """Struct"""
        self.assertTrue(TestParser.test("""
            type Point struct {
                x, y float;
            }
        ""","successful", inspect.stack()[0].function))
    def test_065(self):
        """Variable Declaration with Implicit Variable"""
        self.assertTrue(TestParser.test("var x = 10;","successful", inspect.stack()[0].function))

    def test_066(self):
        """Variable Declaration with Keyword Variable"""
        self.assertTrue(TestParser.test("var y int = 20;","successful", inspect.stack()[0].function))

    def test_067(self):
        """Constant Declaration"""
        self.assertTrue(TestParser.test("const z = 30;","successful", inspect.stack()[0].function))

    def test_068(self):
        """Function Declaration with Parameters"""
        self.assertTrue(TestParser.test("func add(a int, b int) int { return a + b; }","successful", inspect.stack()[0].function))

    def test_069(self):
        """Function Declaration without Parameters"""
        self.assertTrue(TestParser.test("func greet() string { return \"Hello\"; }","successful", inspect.stack()[0].function))

    def test_070(self):
        """Struct Declaration with Fields"""
        self.assertTrue(TestParser.test("""
            type Car struct {
                make string;
                model string;
                year int;
            }
        ""","successful", inspect.stack()[0].function))

    def test_071(self):
        """Struct Declaration without Fields"""
        self.assertTrue(TestParser.test("""type Empty struct {}
                                        ""","successful", inspect.stack()[0].function))

    def test_072(self):
        """Interface Declaration with Methods"""
        self.assertTrue(TestParser.test("""
            type Shape interface {
                area() float;
                perimeter() float;
            }
        ""","successful", inspect.stack()[0].function))

    def test_073(self):
        """Interface Declaration without Methods"""
        self.assertTrue(TestParser.test("type EmptyInterface interface {};","successful", inspect.stack()[0].function))
    
    def test_074(self):
        """Interface Declaration without Methods"""
        self.assertTrue(TestParser.test("""type EmptyInterface interface {}
                                        ""","successful", inspect.stack()[0].function))
    def test_075(self):
        """Function with Variable Declaration"""
        self.assertTrue(TestParser.test("""
            func test() {
                var x int = 10;
            }
        """, "successful", inspect.stack()[0].function))

    def test_076(self):
        """Function with Constant Declaration"""
        self.assertTrue(TestParser.test("""
            func test() {
                const y = 20;
            }
        """, "successful", inspect.stack()[0].function))

    def test_077(self):
        """Function with Assignment Statement"""
        self.assertTrue(TestParser.test("""
            func test() {
                x = 30;
            }
        """, "successful", inspect.stack()[0].function))

    def test_078(self):
        """Function with If Statement"""
        self.assertTrue(TestParser.test("""
            func test() {
                if (x > 10) {
                    x = 20;
                }
            }
        """, "successful", inspect.stack()[0].function))

    def test_079(self):
        """Function with For Statement"""
        self.assertTrue(TestParser.test("""
            func test() {
                for var i = 0; i < 10; i = i + 1 {
                    x = x + i;
                }
            }
        """, "successful", inspect.stack()[0].function))

    def test_080(self):
        """Function with Break Statement"""
        self.assertTrue(TestParser.test("""
            func test() {
                for var i = 0; i < 10; i = i + 1 {
                    if (i == 5) {
                        break;
                    }
                }
            }
        """, "successful", inspect.stack()[0].function))

    def test_081(self):
        """Function with Continue Statement"""
        self.assertTrue(TestParser.test("""
            func test() {
                for var i = 0; i < 10; i = i + 1 {
                    if (i % 2 == 0) {
                        continue;
                    }
                    x = x + i;
                }
            }
        """, "successful", inspect.stack()[0].function))

    def test_082(self):
        """Function with Return Statement"""
        self.assertTrue(TestParser.test("""
            func test() {
                return x;
            }
        """, "successful", inspect.stack()[0].function))

    def test_083(self):
        """Function with Function Call"""
        self.assertTrue(TestParser.test("""
            func test() {
                foo();
            }
        """, "successful", inspect.stack()[0].function))

    def test_084(self):
        """Function with Method Call"""
        self.assertTrue(TestParser.test("""
            func test() {
                obj.method();
            }
        """, "successful", inspect.stack()[0].function))

    def test_085(self):
        """Function with Nested If Statement"""
        self.assertTrue(TestParser.test("""
            func test() {
                if (x > 10) {
                    if (y < 20) {
                        x = 30;
                    }
                }
            }
        """, "successful", inspect.stack()[0].function))

    def test_086(self):
        """Function with Nested For Statement"""
        self.assertTrue(TestParser.test("""
            func test() {
                for var i = 0; i < 10; i = i + 1 {
                    for var j = 0; j < 5; j = j + 1 {
                        x = x + i + j;
                    }
                }
            }
        """, "successful", inspect.stack()[0].function))

    def test_087(self):
        """Function with If-Else Statement"""
        self.assertTrue(TestParser.test("""
            func test() {
                if (x > 10) {
                    x = 20;
                } else {
                    x = 30;
                }
            }
        """, "successful", inspect.stack()[0].function))

    def test_088(self):
        """Function with If-Else If-Else Statement"""
        self.assertTrue(TestParser.test("""
            func test() {
                if (x > 10) {
                    x = 20;
                } else if (x < 5) {
                    x = 30;
                } else {
                    x = 40;
                }
            }
        """, "successful", inspect.stack()[0].function))

    def test_089(self):
        """Function with Multiple Statements"""
        self.assertTrue(TestParser.test("""
            func test() {
                var x int = 10;
                const y = 20;
                x = x + y;
                return x;
            }
        """, "successful", inspect.stack()[0].function))

    def test_090(self):
        """Function with Complex Statements"""
        self.assertTrue(TestParser.test("""
            func test() {
                var x int = 10;
                const y = 20;
                if (x > y) {
                    x = x - y;
                } else {
                    x = x + y;
                }
                for var i = 0; i < 10; i = i + 1 {
                    x = x + i;
                }
                return x;
            }
        """, "successful", inspect.stack()[0].function))
    def test_091(self):
        """Constant Declaration with Integer"""
        self.assertTrue(TestParser.test("const x = 10;","successful", inspect.stack()[0].function))

    def test_092(self):
        """Constant Declaration with Float"""
        self.assertTrue(TestParser.test("const y = 20.5;","successful", inspect.stack()[0].function))

    def test_093(self):
        """Constant Declaration with String"""
        self.assertTrue(TestParser.test("const z = \"Hello\";","successful", inspect.stack()[0].function))

    def test_094(self):
        """Constant Declaration with Boolean"""
        self.assertTrue(TestParser.test("const flag = true;","successful", inspect.stack()[0].function))

    def test_095(self):
        """Array Declaration with Primitive Type"""
        self.assertTrue(TestParser.test("var arr [5]int;","successful", inspect.stack()[0].function))

    def test_096(self):
        """Array Declaration with Struct Type"""
        self.assertTrue(TestParser.test("var arr [5]Person;","successful", inspect.stack()[0].function))

    def test_097(self):
        """Array Declaration with Initialization"""
        self.assertTrue(TestParser.test("var arr [3]int = [3]int{1, 2, 3};","successful", inspect.stack()[0].function))

    def test_098(self):
        """Array Declaration with Initialization"""
        self.assertTrue(TestParser.test("var arr [3]string = [3]string{1, 2, 3};","successful", inspect.stack()[0].function))

    def test_099(self):
        """Array Declaration with Multiple Dimensions"""
        self.assertTrue(TestParser.test("var arr [2][3]int;","successful", inspect.stack()[0].function))
    def test_100(self):
        """Array Declaration with Multiple Dimensions"""
        self.assertTrue(TestParser.test("var arr [2][3]AnhKhoa;","successful", inspect.stack()[0].function))