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
        self.assertTrue(TestParser.test("const Votien = 1;","successful", inspect.stack()[0].function))

    def test_002(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = true;","successful", inspect.stack()[0].function))

    def test_003(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = [5][0]string{1, \"string\"};","successful", inspect.stack()[0].function))

    def test_004(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = [1.]ID{1, 3};","Error on line 1 col 16: 1.", inspect.stack()[0].function))

    def test_005(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = Person{name: \"Alice\", age: 30};","successful", inspect.stack()[0].function))

    def test_006(self):
        """expression"""
        self.assertTrue(TestParser.test("const Votien = 1 || 2 && c + 3 / 2 - -1;","successful", inspect.stack()[0].function))

    def test_007(self):
        """expression"""
        self.assertTrue(TestParser.test("const Votien = 1[2] + foo()[2] + ID[2].b.b;","successful", inspect.stack()[0].function))

    def test_008(self):
        """expression"""
        self.assertTrue(TestParser.test("const Votien = ca.foo(132) + b.c[2];","successful", inspect.stack()[0].function))

    def test_009(self):
        """expression"""
        self.assertTrue(TestParser.test("const Votien = a.a.foo();","successful", inspect.stack()[0].function))

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
            const VoTien = a.b() + 2;
        ""","successful", inspect.stack()[0].function))

    def test_012(self):
        """declared function"""
        self.assertTrue(TestParser.test("""
            func VoTien(x int, y int) int {}
            func VoTien1() [2][3] ID {}         
            func VoTien2() {}                                       
        ""","successful", inspect.stack()[0].function))

    def test_013(self):
        """declared method"""
        self.assertTrue(TestParser.test("""
            func (c Calculator) VoTien(x int) int {}  
            func (c Calculator) VoTien() ID {}      
            func (c Calculator) VoTien(x int, y [2]VoTien) {}                                                      
        ""","successful", inspect.stack()[0].function))

    def test_014(self):
        """declared struct"""
        self.assertTrue(TestParser.test("""
            type VoTien struct {
                VoTien string ;
                VoTien [1][3]VoTien ;                     
            }
            type VoTien struct {}                                                                       
        ""","successful", inspect.stack()[0].function))

    def test_015(self):
        """declared struct"""
        self.assertTrue(TestParser.test("""
            type VoTien struct {
                VoTien string ;
                VoTien [1][3]VoTien ;                     
            }
            type VoTien struct {}                                                                       
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
            type VoTien interface {}                                                                       
        ""","successful", inspect.stack()[0].function))

    def test_017(self):
        """declared_statement"""
        self.assertTrue(TestParser.test("""    
            func VoTien() {
                var x int = foo() + 3 / 4;
                var y = "Hello" / 4;   
                var z str;
                                        
                const VoTien = a.b() + 2;
            }                                       
        ""","successful", inspect.stack()[0].function))


    def test_018(self):
        """assign_statement"""
        self.assertTrue(TestParser.test("""    
            func VoTien() {
                x  := foo() + 3 / 4;
                x.c[2][4] := 1 + 2;                       
            }                                       
        ""","successful", inspect.stack()[0].function))

    def test_019(self):
        """if_statement"""
        self.assertTrue(TestParser.test("""    
            func VoTien() {
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
            func VoTien() {
                for i < 10 {}
                for i := 0; i < 10; i += 1 {}
                for index, value := range array {}
            }
        ""","successful", inspect.stack()[0].function))


    def test_021(self):
        """break and continue, return, Call  statement"""
        self.assertTrue(TestParser.test("""    
            func VoTien() {                           
                for i < 10 {break;}
                break;
                continue;
                return 1;
                return
                foo(2 + x, 4 / y); m.goo();                        
             }
                                        
        ""","successful", inspect.stack()[0].function))
    def test_025(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = [true]int{1};                         
        ""","Error on line 2 col 28: true", inspect.stack()[0].function))
    def test_028(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = [2]int{1;                         
        ""","Error on line 2 col 35: ;", inspect.stack()[0].function))
    def test_030(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = [2]int{};                         
        ""","Error on line 2 col 34: }", inspect.stack()[0].function))
    def test_031(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = ID {};                         
        ""","successful", inspect.stack()[0].function))
    def test_037(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = a >= 2 <= "string" > a[2][3] < ID{A: 2} >= [2]S{2};                         
        ""","successful", inspect.stack()[0].function))
    def test_041(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = a[2][3][a + 2];                         
        ""","successful", inspect.stack()[0].function))
    def test_042(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = a[2, 3];                         
        ""","Error on line 2 col 30: ,", inspect.stack()[0].function))
    def test_058(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            var a [2][3]int = 2 + 3 / 4;
        ""","successful", inspect.stack()[0].function))
    def test_071(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            func Add(a) [2]id {}
""","Error on line 2 col 22: )", inspect.stack()[0].function))
    def test_077(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            type Calculator struct {
                                        
                value int;
                a [2]int; a [2]ID;
                c Calculator                    
            }
""","successful", inspect.stack()[0].function))
    def test_078(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            type Calculator struct {
                c Calculator
                c Cal a int;         
            }
""","Error on line 4 col 22: a", inspect.stack()[0].function))
    def test_084(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            type Calculator interface {
                Add(x int,c,d ID); Add()
        }
""","successful", inspect.stack()[0].function))
    def test_086(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            type Calculator interface {}
            type Person struct{};
""","successful", inspect.stack()[0].function))
    def test_087(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            type Calculator interface {};
""","successful", inspect.stack()[0].function))
    def test_091(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func (c c) Add(x, c int) {}
""","Error on line 2 col 28: ,", inspect.stack()[0].function))
    def test_095(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
                                        
            func (c c) Add(x int) {}
                                        
            func Add(x int) {} var c int;
                                        
            var c int; type Calculator struct{} type Calculator struct{} var c int;
""","Error on line 7 col 48: type", inspect.stack()[0].function))
    def test_105(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        const a = a[2].b
                                        var a = a[2].b; var a = "s";           
                                    }""","successful", inspect.stack()[0].function))
    def test_107(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        a += 2;
                                        a -= a[2].b();
                                        a /= 2
                                        a *= 2
                                        a %= 2;       
                                    }""","successful", inspect.stack()[0].function))
    def test_108(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        a[2].b := 2;       
                                    }""","successful", inspect.stack()[0].function))
    def test_109(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        a.c[2].e[3].k += 2;       
                                    }""","successful", inspect.stack()[0].function))
    def test_110(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        a.foo() += 2;       
                                    }""","Error on line 3 col 48: +=", inspect.stack()[0].function))