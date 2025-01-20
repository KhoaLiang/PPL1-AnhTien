# Generated from main/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u01f4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3!\3\"")
        buf.write("\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(")
        buf.write("\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,\3-\3-\3-\3.\3.\3")
        buf.write("/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\3\66\3\66\7\66\u015b\n\66\f\66\16\66\u015e")
        buf.write("\13\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3")
        buf.write("\67\5\67\u016a\n\67\38\38\38\78\u016f\n8\f8\168\u0172")
        buf.write("\138\58\u0174\n8\39\39\39\69\u0179\n9\r9\169\u017a\3:")
        buf.write("\3:\3:\6:\u0180\n:\r:\16:\u0181\3;\3;\3;\6;\u0187\n;\r")
        buf.write(";\16;\u0188\3<\3<\3<\5<\u018e\n<\3<\3<\3=\3=\3>\6>\u0195")
        buf.write("\n>\r>\16>\u0196\3?\3?\5?\u019b\n?\3?\5?\u019e\n?\3@\3")
        buf.write("@\7@\u01a2\n@\f@\16@\u01a5\13@\3@\3@\3@\3A\3A\5A\u01ac")
        buf.write("\nA\3B\3B\3B\3C\3C\3C\3D\6D\u01b5\nD\rD\16D\u01b6\3D\3")
        buf.write("D\3E\5E\u01bc\nE\3E\3E\3F\3F\3F\3F\7F\u01c4\nF\fF\16F")
        buf.write("\u01c7\13F\3F\3F\3G\3G\3G\3G\3G\7G\u01d0\nG\fG\16G\u01d3")
        buf.write("\13G\3G\3G\3G\3G\3G\3H\3H\3H\3I\3I\7I\u01df\nI\fI\16I")
        buf.write("\u01e2\13I\3I\3I\3I\5I\u01e7\nI\3I\3I\3J\3J\7J\u01ed\n")
        buf.write("J\fJ\16J\u01f0\13J\3J\3J\3J\3\u01d1\2K\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60")
        buf.write("_\61a\62c\63e\64g\65i\66k\67m8o\2q\2s\2u\2w9y\2{\2}\2")
        buf.write("\177:\u0081\2\u0083\2\u0085\2\u0087;\u0089<\u008b=\u008d")
        buf.write(">\u008f?\u0091@\u0093A\3\2\23\5\2C\\aac|\6\2\62;C\\aa")
        buf.write("c|\3\2\63;\3\2\62;\4\2DDdd\3\2\62\63\4\2QQqq\3\2\629\4")
        buf.write("\2ZZzz\5\2\62;CHch\4\2GGgg\4\2--//\6\2\f\f\17\17$$^^\7")
        buf.write("\2$$^^ppttvv\5\2\13\13\16\17\"\"\4\2\f\f\17\17\3\3\f\f")
        buf.write("\2\u0200\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write("\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2")
        buf.write("?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2")
        buf.write("\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2")
        buf.write("\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2")
        buf.write("\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3")
        buf.write("\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2w")
        buf.write("\3\2\2\2\2\177\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2")
        buf.write("\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\3\u0095\3\2\2\2\5\u0098\3\2\2")
        buf.write("\2\7\u009d\3\2\2\2\t\u00a1\3\2\2\2\13\u00a8\3\2\2\2\r")
        buf.write("\u00ad\3\2\2\2\17\u00b2\3\2\2\2\21\u00b9\3\2\2\2\23\u00c3")
        buf.write("\3\2\2\2\25\u00ca\3\2\2\2\27\u00ce\3\2\2\2\31\u00d4\3")
        buf.write("\2\2\2\33\u00dc\3\2\2\2\35\u00e2\3\2\2\2\37\u00e6\3\2")
        buf.write("\2\2!\u00ef\3\2\2\2#\u00f5\3\2\2\2%\u00fb\3\2\2\2\'\u00ff")
        buf.write("\3\2\2\2)\u0104\3\2\2\2+\u010a\3\2\2\2-\u010e\3\2\2\2")
        buf.write("/\u0110\3\2\2\2\61\u0112\3\2\2\2\63\u0114\3\2\2\2\65\u0116")
        buf.write("\3\2\2\2\67\u0118\3\2\2\29\u011b\3\2\2\2;\u011e\3\2\2")
        buf.write("\2=\u0120\3\2\2\2?\u0123\3\2\2\2A\u0125\3\2\2\2C\u0128")
        buf.write("\3\2\2\2E\u012b\3\2\2\2G\u012e\3\2\2\2I\u0130\3\2\2\2")
        buf.write("K\u0132\3\2\2\2M\u0135\3\2\2\2O\u0138\3\2\2\2Q\u013b\3")
        buf.write("\2\2\2S\u013e\3\2\2\2U\u0141\3\2\2\2W\u0143\3\2\2\2Y\u0145")
        buf.write("\3\2\2\2[\u0148\3\2\2\2]\u014a\3\2\2\2_\u014c\3\2\2\2")
        buf.write("a\u014e\3\2\2\2c\u0150\3\2\2\2e\u0152\3\2\2\2g\u0154\3")
        buf.write("\2\2\2i\u0156\3\2\2\2k\u0158\3\2\2\2m\u0169\3\2\2\2o\u0173")
        buf.write("\3\2\2\2q\u0175\3\2\2\2s\u017c\3\2\2\2u\u0183\3\2\2\2")
        buf.write("w\u018a\3\2\2\2y\u0191\3\2\2\2{\u0194\3\2\2\2}\u019d\3")
        buf.write("\2\2\2\177\u019f\3\2\2\2\u0081\u01ab\3\2\2\2\u0083\u01ad")
        buf.write("\3\2\2\2\u0085\u01b0\3\2\2\2\u0087\u01b4\3\2\2\2\u0089")
        buf.write("\u01bb\3\2\2\2\u008b\u01bf\3\2\2\2\u008d\u01ca\3\2\2\2")
        buf.write("\u008f\u01d9\3\2\2\2\u0091\u01dc\3\2\2\2\u0093\u01ea\3")
        buf.write("\2\2\2\u0095\u0096\7k\2\2\u0096\u0097\7h\2\2\u0097\4\3")
        buf.write("\2\2\2\u0098\u0099\7g\2\2\u0099\u009a\7n\2\2\u009a\u009b")
        buf.write("\7u\2\2\u009b\u009c\7g\2\2\u009c\6\3\2\2\2\u009d\u009e")
        buf.write("\7h\2\2\u009e\u009f\7q\2\2\u009f\u00a0\7t\2\2\u00a0\b")
        buf.write("\3\2\2\2\u00a1\u00a2\7t\2\2\u00a2\u00a3\7g\2\2\u00a3\u00a4")
        buf.write("\7v\2\2\u00a4\u00a5\7w\2\2\u00a5\u00a6\7t\2\2\u00a6\u00a7")
        buf.write("\7p\2\2\u00a7\n\3\2\2\2\u00a8\u00a9\7h\2\2\u00a9\u00aa")
        buf.write("\7w\2\2\u00aa\u00ab\7p\2\2\u00ab\u00ac\7e\2\2\u00ac\f")
        buf.write("\3\2\2\2\u00ad\u00ae\7v\2\2\u00ae\u00af\7{\2\2\u00af\u00b0")
        buf.write("\7r\2\2\u00b0\u00b1\7g\2\2\u00b1\16\3\2\2\2\u00b2\u00b3")
        buf.write("\7u\2\2\u00b3\u00b4\7v\2\2\u00b4\u00b5\7t\2\2\u00b5\u00b6")
        buf.write("\7w\2\2\u00b6\u00b7\7e\2\2\u00b7\u00b8\7v\2\2\u00b8\20")
        buf.write("\3\2\2\2\u00b9\u00ba\7k\2\2\u00ba\u00bb\7p\2\2\u00bb\u00bc")
        buf.write("\7v\2\2\u00bc\u00bd\7g\2\2\u00bd\u00be\7t\2\2\u00be\u00bf")
        buf.write("\7h\2\2\u00bf\u00c0\7c\2\2\u00c0\u00c1\7e\2\2\u00c1\u00c2")
        buf.write("\7g\2\2\u00c2\22\3\2\2\2\u00c3\u00c4\7u\2\2\u00c4\u00c5")
        buf.write("\7v\2\2\u00c5\u00c6\7t\2\2\u00c6\u00c7\7k\2\2\u00c7\u00c8")
        buf.write("\7p\2\2\u00c8\u00c9\7i\2\2\u00c9\24\3\2\2\2\u00ca\u00cb")
        buf.write("\7k\2\2\u00cb\u00cc\7p\2\2\u00cc\u00cd\7v\2\2\u00cd\26")
        buf.write("\3\2\2\2\u00ce\u00cf\7h\2\2\u00cf\u00d0\7n\2\2\u00d0\u00d1")
        buf.write("\7q\2\2\u00d1\u00d2\7c\2\2\u00d2\u00d3\7v\2\2\u00d3\30")
        buf.write("\3\2\2\2\u00d4\u00d5\7d\2\2\u00d5\u00d6\7q\2\2\u00d6\u00d7")
        buf.write("\7q\2\2\u00d7\u00d8\7n\2\2\u00d8\u00d9\7g\2\2\u00d9\u00da")
        buf.write("\7c\2\2\u00da\u00db\7p\2\2\u00db\32\3\2\2\2\u00dc\u00dd")
        buf.write("\7e\2\2\u00dd\u00de\7q\2\2\u00de\u00df\7p\2\2\u00df\u00e0")
        buf.write("\7u\2\2\u00e0\u00e1\7v\2\2\u00e1\34\3\2\2\2\u00e2\u00e3")
        buf.write("\7x\2\2\u00e3\u00e4\7c\2\2\u00e4\u00e5\7t\2\2\u00e5\36")
        buf.write("\3\2\2\2\u00e6\u00e7\7e\2\2\u00e7\u00e8\7q\2\2\u00e8\u00e9")
        buf.write("\7p\2\2\u00e9\u00ea\7v\2\2\u00ea\u00eb\7k\2\2\u00eb\u00ec")
        buf.write("\7p\2\2\u00ec\u00ed\7w\2\2\u00ed\u00ee\7g\2\2\u00ee \3")
        buf.write("\2\2\2\u00ef\u00f0\7d\2\2\u00f0\u00f1\7t\2\2\u00f1\u00f2")
        buf.write("\7g\2\2\u00f2\u00f3\7c\2\2\u00f3\u00f4\7m\2\2\u00f4\"")
        buf.write("\3\2\2\2\u00f5\u00f6\7t\2\2\u00f6\u00f7\7c\2\2\u00f7\u00f8")
        buf.write("\7p\2\2\u00f8\u00f9\7i\2\2\u00f9\u00fa\7g\2\2\u00fa$\3")
        buf.write("\2\2\2\u00fb\u00fc\7p\2\2\u00fc\u00fd\7k\2\2\u00fd\u00fe")
        buf.write("\7n\2\2\u00fe&\3\2\2\2\u00ff\u0100\7v\2\2\u0100\u0101")
        buf.write("\7t\2\2\u0101\u0102\7w\2\2\u0102\u0103\7g\2\2\u0103(\3")
        buf.write("\2\2\2\u0104\u0105\7h\2\2\u0105\u0106\7c\2\2\u0106\u0107")
        buf.write("\7n\2\2\u0107\u0108\7u\2\2\u0108\u0109\7g\2\2\u0109*\3")
        buf.write("\2\2\2\u010a\u010b\7u\2\2\u010b\u010c\7v\2\2\u010c\u010d")
        buf.write("\7t\2\2\u010d,\3\2\2\2\u010e\u010f\7-\2\2\u010f.\3\2\2")
        buf.write("\2\u0110\u0111\7/\2\2\u0111\60\3\2\2\2\u0112\u0113\7,")
        buf.write("\2\2\u0113\62\3\2\2\2\u0114\u0115\7\61\2\2\u0115\64\3")
        buf.write("\2\2\2\u0116\u0117\7\'\2\2\u0117\66\3\2\2\2\u0118\u0119")
        buf.write("\7?\2\2\u0119\u011a\7?\2\2\u011a8\3\2\2\2\u011b\u011c")
        buf.write("\7#\2\2\u011c\u011d\7?\2\2\u011d:\3\2\2\2\u011e\u011f")
        buf.write("\7>\2\2\u011f<\3\2\2\2\u0120\u0121\7>\2\2\u0121\u0122")
        buf.write("\7?\2\2\u0122>\3\2\2\2\u0123\u0124\7@\2\2\u0124@\3\2\2")
        buf.write("\2\u0125\u0126\7@\2\2\u0126\u0127\7?\2\2\u0127B\3\2\2")
        buf.write("\2\u0128\u0129\7(\2\2\u0129\u012a\7(\2\2\u012aD\3\2\2")
        buf.write("\2\u012b\u012c\7~\2\2\u012c\u012d\7~\2\2\u012dF\3\2\2")
        buf.write("\2\u012e\u012f\7#\2\2\u012fH\3\2\2\2\u0130\u0131\7?\2")
        buf.write("\2\u0131J\3\2\2\2\u0132\u0133\7-\2\2\u0133\u0134\7?\2")
        buf.write("\2\u0134L\3\2\2\2\u0135\u0136\7/\2\2\u0136\u0137\7?\2")
        buf.write("\2\u0137N\3\2\2\2\u0138\u0139\7,\2\2\u0139\u013a\7?\2")
        buf.write("\2\u013aP\3\2\2\2\u013b\u013c\7\61\2\2\u013c\u013d\7?")
        buf.write("\2\2\u013dR\3\2\2\2\u013e\u013f\7\'\2\2\u013f\u0140\7")
        buf.write("?\2\2\u0140T\3\2\2\2\u0141\u0142\7\60\2\2\u0142V\3\2\2")
        buf.write("\2\u0143\u0144\7<\2\2\u0144X\3\2\2\2\u0145\u0146\7<\2")
        buf.write("\2\u0146\u0147\7?\2\2\u0147Z\3\2\2\2\u0148\u0149\7*\2")
        buf.write("\2\u0149\\\3\2\2\2\u014a\u014b\7+\2\2\u014b^\3\2\2\2\u014c")
        buf.write("\u014d\7}\2\2\u014d`\3\2\2\2\u014e\u014f\7\177\2\2\u014f")
        buf.write("b\3\2\2\2\u0150\u0151\7]\2\2\u0151d\3\2\2\2\u0152\u0153")
        buf.write("\7_\2\2\u0153f\3\2\2\2\u0154\u0155\7.\2\2\u0155h\3\2\2")
        buf.write("\2\u0156\u0157\7=\2\2\u0157j\3\2\2\2\u0158\u015c\t\2\2")
        buf.write("\2\u0159\u015b\t\3\2\2\u015a\u0159\3\2\2\2\u015b\u015e")
        buf.write("\3\2\2\2\u015c\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015d")
        buf.write("l\3\2\2\2\u015e\u015c\3\2\2\2\u015f\u016a\5o8\2\u0160")
        buf.write("\u0161\5q9\2\u0161\u0162\b\67\2\2\u0162\u016a\3\2\2\2")
        buf.write("\u0163\u0164\5s:\2\u0164\u0165\b\67\3\2\u0165\u016a\3")
        buf.write("\2\2\2\u0166\u0167\5u;\2\u0167\u0168\b\67\4\2\u0168\u016a")
        buf.write("\3\2\2\2\u0169\u015f\3\2\2\2\u0169\u0160\3\2\2\2\u0169")
        buf.write("\u0163\3\2\2\2\u0169\u0166\3\2\2\2\u016an\3\2\2\2\u016b")
        buf.write("\u0174\7\62\2\2\u016c\u0170\t\4\2\2\u016d\u016f\t\5\2")
        buf.write("\2\u016e\u016d\3\2\2\2\u016f\u0172\3\2\2\2\u0170\u016e")
        buf.write("\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u0174\3\2\2\2\u0172")
        buf.write("\u0170\3\2\2\2\u0173\u016b\3\2\2\2\u0173\u016c\3\2\2\2")
        buf.write("\u0174p\3\2\2\2\u0175\u0176\7\62\2\2\u0176\u0178\t\6\2")
        buf.write("\2\u0177\u0179\t\7\2\2\u0178\u0177\3\2\2\2\u0179\u017a")
        buf.write("\3\2\2\2\u017a\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017b")
        buf.write("r\3\2\2\2\u017c\u017d\7\62\2\2\u017d\u017f\t\b\2\2\u017e")
        buf.write("\u0180\t\t\2\2\u017f\u017e\3\2\2\2\u0180\u0181\3\2\2\2")
        buf.write("\u0181\u017f\3\2\2\2\u0181\u0182\3\2\2\2\u0182t\3\2\2")
        buf.write("\2\u0183\u0184\7\62\2\2\u0184\u0186\t\n\2\2\u0185\u0187")
        buf.write("\t\13\2\2\u0186\u0185\3\2\2\2\u0187\u0188\3\2\2\2\u0188")
        buf.write("\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189v\3\2\2\2\u018a")
        buf.write("\u018b\5{>\2\u018b\u018d\7\60\2\2\u018c\u018e\5{>\2\u018d")
        buf.write("\u018c\3\2\2\2\u018d\u018e\3\2\2\2\u018e\u018f\3\2\2\2")
        buf.write("\u018f\u0190\5}?\2\u0190x\3\2\2\2\u0191\u0192\t\5\2\2")
        buf.write("\u0192z\3\2\2\2\u0193\u0195\5y=\2\u0194\u0193\3\2\2\2")
        buf.write("\u0195\u0196\3\2\2\2\u0196\u0194\3\2\2\2\u0196\u0197\3")
        buf.write("\2\2\2\u0197|\3\2\2\2\u0198\u019a\t\f\2\2\u0199\u019b")
        buf.write("\t\r\2\2\u019a\u0199\3\2\2\2\u019a\u019b\3\2\2\2\u019b")
        buf.write("\u019c\3\2\2\2\u019c\u019e\5{>\2\u019d\u0198\3\2\2\2\u019d")
        buf.write("\u019e\3\2\2\2\u019e~\3\2\2\2\u019f\u01a3\7$\2\2\u01a0")
        buf.write("\u01a2\5\u0081A\2\u01a1\u01a0\3\2\2\2\u01a2\u01a5\3\2")
        buf.write("\2\2\u01a3\u01a1\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01a6")
        buf.write("\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a6\u01a7\7$\2\2\u01a7")
        buf.write("\u01a8\b@\5\2\u01a8\u0080\3\2\2\2\u01a9\u01ac\n\16\2\2")
        buf.write("\u01aa\u01ac\5\u0083B\2\u01ab\u01a9\3\2\2\2\u01ab\u01aa")
        buf.write("\3\2\2\2\u01ac\u0082\3\2\2\2\u01ad\u01ae\7^\2\2\u01ae")
        buf.write("\u01af\t\17\2\2\u01af\u0084\3\2\2\2\u01b0\u01b1\7^\2\2")
        buf.write("\u01b1\u01b2\n\17\2\2\u01b2\u0086\3\2\2\2\u01b3\u01b5")
        buf.write("\t\20\2\2\u01b4\u01b3\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6")
        buf.write("\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01b8\3\2\2\2")
        buf.write("\u01b8\u01b9\bD\6\2\u01b9\u0088\3\2\2\2\u01ba\u01bc\7")
        buf.write("\17\2\2\u01bb\u01ba\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc")
        buf.write("\u01bd\3\2\2\2\u01bd\u01be\7\f\2\2\u01be\u008a\3\2\2\2")
        buf.write("\u01bf\u01c0\7\61\2\2\u01c0\u01c1\7\61\2\2\u01c1\u01c5")
        buf.write("\3\2\2\2\u01c2\u01c4\n\21\2\2\u01c3\u01c2\3\2\2\2\u01c4")
        buf.write("\u01c7\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2")
        buf.write("\u01c6\u01c8\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c8\u01c9\b")
        buf.write("F\6\2\u01c9\u008c\3\2\2\2\u01ca\u01cb\7\61\2\2\u01cb\u01cc")
        buf.write("\7,\2\2\u01cc\u01d1\3\2\2\2\u01cd\u01d0\5\u008dG\2\u01ce")
        buf.write("\u01d0\13\2\2\2\u01cf\u01cd\3\2\2\2\u01cf\u01ce\3\2\2")
        buf.write("\2\u01d0\u01d3\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d1\u01cf")
        buf.write("\3\2\2\2\u01d2\u01d4\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d4")
        buf.write("\u01d5\7,\2\2\u01d5\u01d6\7\61\2\2\u01d6\u01d7\3\2\2\2")
        buf.write("\u01d7\u01d8\bG\6\2\u01d8\u008e\3\2\2\2\u01d9\u01da\13")
        buf.write("\2\2\2\u01da\u01db\bH\7\2\u01db\u0090\3\2\2\2\u01dc\u01e0")
        buf.write("\7$\2\2\u01dd\u01df\5\u0081A\2\u01de\u01dd\3\2\2\2\u01df")
        buf.write("\u01e2\3\2\2\2\u01e0\u01de\3\2\2\2\u01e0\u01e1\3\2\2\2")
        buf.write("\u01e1\u01e6\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e3\u01e4\7")
        buf.write("\17\2\2\u01e4\u01e7\7\f\2\2\u01e5\u01e7\t\22\2\2\u01e6")
        buf.write("\u01e3\3\2\2\2\u01e6\u01e5\3\2\2\2\u01e7\u01e8\3\2\2\2")
        buf.write("\u01e8\u01e9\bI\b\2\u01e9\u0092\3\2\2\2\u01ea\u01ee\7")
        buf.write("$\2\2\u01eb\u01ed\5\u0081A\2\u01ec\u01eb\3\2\2\2\u01ed")
        buf.write("\u01f0\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ee\u01ef\3\2\2\2")
        buf.write("\u01ef\u01f1\3\2\2\2\u01f0\u01ee\3\2\2\2\u01f1\u01f2\5")
        buf.write("\u0085C\2\u01f2\u01f3\bJ\t\2\u01f3\u0094\3\2\2\2\30\2")
        buf.write("\u015c\u0169\u0170\u0173\u017a\u0181\u0188\u018d\u0196")
        buf.write("\u019a\u019d\u01a3\u01ab\u01b6\u01bb\u01c5\u01cf\u01d1")
        buf.write("\u01e0\u01e6\u01ee\n\3\67\2\3\67\3\3\67\4\3@\5\b\2\2\3")
        buf.write("H\6\3I\7\3J\b")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    ELSE = 2
    FOR = 3
    RETURN = 4
    FUNC = 5
    TYPE = 6
    STRUCT = 7
    INTERFACE = 8
    STRING = 9
    INT = 10
    FLOAT = 11
    BOOLEAN = 12
    CONST = 13
    VAR = 14
    CONTINUE = 15
    BREAK = 16
    RANGE = 17
    NIL = 18
    TRUE = 19
    FALSE = 20
    STR = 21
    ADD = 22
    SUB = 23
    MUL = 24
    DIV = 25
    MOD = 26
    EQUAL = 27
    DIFF = 28
    LT = 29
    LTE = 30
    RT = 31
    RTE = 32
    AND = 33
    OR = 34
    NOT = 35
    ASSIGN = 36
    ASSIGNADD = 37
    ASSIGNSUB = 38
    ASSIGNMUL = 39
    ASSIGNDIV = 40
    ASSIGNMOD = 41
    POINTTO = 42
    COLON = 43
    ASSIGNNIT = 44
    LPAREN = 45
    RPAREN = 46
    LBRACE = 47
    RBRACE = 48
    LBRACK = 49
    RBRACK = 50
    COMMA = 51
    SEMICOL = 52
    ID = 53
    INT_LIT = 54
    FLOAT_LIT = 55
    STRING_LIT = 56
    WS = 57
    NEWLINE = 58
    COMMENT = 59
    ML_COMMENT = 60
    ERROR_CHAR = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'", "'str'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", 
            "'!'", "'='", "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", 
            "':'", "':='", "'('", "')'", "'{'", "'}'", "'['", "']'", "','", 
            "';'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
            "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "STR", "ADD", "SUB", 
            "MUL", "DIV", "MOD", "EQUAL", "DIFF", "LT", "LTE", "RT", "RTE", 
            "AND", "OR", "NOT", "ASSIGN", "ASSIGNADD", "ASSIGNSUB", "ASSIGNMUL", 
            "ASSIGNDIV", "ASSIGNMOD", "POINTTO", "COLON", "ASSIGNNIT", "LPAREN", 
            "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", "COMMA", "SEMICOL", 
            "ID", "INT_LIT", "FLOAT_LIT", "STRING_LIT", "WS", "NEWLINE", 
            "COMMENT", "ML_COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                  "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", 
                  "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", "FALSE", 
                  "STR", "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", "DIFF", 
                  "LT", "LTE", "RT", "RTE", "AND", "OR", "NOT", "ASSIGN", 
                  "ASSIGNADD", "ASSIGNSUB", "ASSIGNMUL", "ASSIGNDIV", "ASSIGNMOD", 
                  "POINTTO", "COLON", "ASSIGNNIT", "LPAREN", "RPAREN", "LBRACE", 
                  "RBRACE", "LBRACK", "RBRACK", "COMMA", "SEMICOL", "ID", 
                  "INT_LIT", "DEC_INT", "BIN_INT", "OCT_INT", "HEX_INT", 
                  "FLOAT_LIT", "DIGIT", "DIGITS", "OPT_EXP", "STRING_LIT", 
                  "STR_CHAR", "ESC_SEQ", "ESC_ILLEGAL", "WS", "NEWLINE", 
                  "COMMENT", "ML_COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[53] = self.INT_LIT_action 
            actions[62] = self.STRING_LIT_action 
            actions[70] = self.ERROR_CHAR_action 
            actions[71] = self.UNCLOSE_STRING_action 
            actions[72] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = str(int(self.text[2:], 2))
     

        if actionIndex == 1:
            self.text = str(int(self.text[2:], 8))
     

        if actionIndex == 2:
            self.text = str(int(self.text[2:], 16))
     

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                self.text = self.text[1:-1] 

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
                    raise UncloseString(self.text[1:-2])
                elif (self.text[-1] == '\n'):
                    raise UncloseString(self.text[1:-1])
                else:
                    raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

                raise IllegalEscape(self.text[1:])

     


