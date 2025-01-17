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
        buf.write("\u01df\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"")
        buf.write("\3\"\3#\3#\3#\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3")
        buf.write("(\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60")
        buf.write("\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\7\64\u0151")
        buf.write("\n\64\f\64\16\64\u0154\13\64\3\65\3\65\3\65\7\65\u0159")
        buf.write("\n\65\f\65\16\65\u015c\13\65\5\65\u015e\n\65\3\66\3\66")
        buf.write("\3\66\6\66\u0163\n\66\r\66\16\66\u0164\3\66\3\66\3\67")
        buf.write("\3\67\3\67\6\67\u016c\n\67\r\67\16\67\u016d\3\67\3\67")
        buf.write("\38\38\38\68\u0175\n8\r8\168\u0176\38\38\39\39\39\59\u017e")
        buf.write("\n9\39\39\3:\3:\3;\6;\u0185\n;\r;\16;\u0186\3<\3<\5<\u018b")
        buf.write("\n<\3<\5<\u018e\n<\3=\3=\7=\u0192\n=\f=\16=\u0195\13=")
        buf.write("\3=\3=\3=\3>\3>\5>\u019c\n>\3?\3?\3?\3@\3@\3@\3A\6A\u01a5")
        buf.write("\nA\rA\16A\u01a6\3A\3A\3B\3B\3B\3B\7B\u01af\nB\fB\16B")
        buf.write("\u01b2\13B\3B\3B\3C\3C\3C\3C\3C\7C\u01bb\nC\fC\16C\u01be")
        buf.write("\13C\3C\3C\3C\3C\3C\3D\3D\3D\3E\3E\7E\u01ca\nE\fE\16E")
        buf.write("\u01cd\13E\3E\3E\3E\5E\u01d2\nE\3E\3E\3F\3F\7F\u01d8\n")
        buf.write("F\fF\16F\u01db\13F\3F\3F\3F\3\u01bc\2G\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60")
        buf.write("_\61a\62c\63e\64g\65i\66k\67m8o9q:s\2u\2w\2y;{\2}\2\177")
        buf.write("\2\u0081<\u0083=\u0085>\u0087?\u0089@\u008bA\3\2\23\5")
        buf.write("\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3\2\62;\4\2DDdd\3\2\62")
        buf.write("\63\4\2QQqq\3\2\629\4\2ZZzz\5\2\62;CHch\4\2GGgg\4\2--")
        buf.write("//\6\2\f\f\17\17$$^^\7\2$$^^ppttvv\5\2\13\f\16\17\"\"")
        buf.write("\4\2\f\f\17\17\3\3\f\f\2\u01eb\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3")
        buf.write("\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write("\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write("\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2")
        buf.write("O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2")
        buf.write("\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2")
        buf.write("\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2")
        buf.write("\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2y\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\3\u008d\3\2\2\2\5\u0094")
        buf.write("\3\2\2\2\7\u0097\3\2\2\2\t\u009c\3\2\2\2\13\u00a0\3\2")
        buf.write("\2\2\r\u00a7\3\2\2\2\17\u00ac\3\2\2\2\21\u00b1\3\2\2\2")
        buf.write("\23\u00b8\3\2\2\2\25\u00c2\3\2\2\2\27\u00c9\3\2\2\2\31")
        buf.write("\u00cd\3\2\2\2\33\u00d3\3\2\2\2\35\u00db\3\2\2\2\37\u00e1")
        buf.write("\3\2\2\2!\u00e5\3\2\2\2#\u00ee\3\2\2\2%\u00f4\3\2\2\2")
        buf.write("\'\u00fa\3\2\2\2)\u00fe\3\2\2\2+\u0103\3\2\2\2-\u0109")
        buf.write("\3\2\2\2/\u010b\3\2\2\2\61\u010d\3\2\2\2\63\u010f\3\2")
        buf.write("\2\2\65\u0111\3\2\2\2\67\u0113\3\2\2\29\u0116\3\2\2\2")
        buf.write(";\u0119\3\2\2\2=\u011b\3\2\2\2?\u011e\3\2\2\2A\u0120\3")
        buf.write("\2\2\2C\u0123\3\2\2\2E\u0126\3\2\2\2G\u0129\3\2\2\2I\u012b")
        buf.write("\3\2\2\2K\u012d\3\2\2\2M\u0130\3\2\2\2O\u0133\3\2\2\2")
        buf.write("Q\u0136\3\2\2\2S\u0139\3\2\2\2U\u013c\3\2\2\2W\u013e\3")
        buf.write("\2\2\2Y\u0140\3\2\2\2[\u0142\3\2\2\2]\u0144\3\2\2\2_\u0146")
        buf.write("\3\2\2\2a\u0148\3\2\2\2c\u014a\3\2\2\2e\u014c\3\2\2\2")
        buf.write("g\u014e\3\2\2\2i\u015d\3\2\2\2k\u015f\3\2\2\2m\u0168\3")
        buf.write("\2\2\2o\u0171\3\2\2\2q\u017a\3\2\2\2s\u0181\3\2\2\2u\u0184")
        buf.write("\3\2\2\2w\u018d\3\2\2\2y\u018f\3\2\2\2{\u019b\3\2\2\2")
        buf.write("}\u019d\3\2\2\2\177\u01a0\3\2\2\2\u0081\u01a4\3\2\2\2")
        buf.write("\u0083\u01aa\3\2\2\2\u0085\u01b5\3\2\2\2\u0087\u01c4\3")
        buf.write("\2\2\2\u0089\u01c7\3\2\2\2\u008b\u01d5\3\2\2\2\u008d\u008e")
        buf.write("\7x\2\2\u008e\u008f\7q\2\2\u008f\u0090\7v\2\2\u0090\u0091")
        buf.write("\7k\2\2\u0091\u0092\7g\2\2\u0092\u0093\7p\2\2\u0093\4")
        buf.write("\3\2\2\2\u0094\u0095\7k\2\2\u0095\u0096\7h\2\2\u0096\6")
        buf.write("\3\2\2\2\u0097\u0098\7g\2\2\u0098\u0099\7n\2\2\u0099\u009a")
        buf.write("\7u\2\2\u009a\u009b\7g\2\2\u009b\b\3\2\2\2\u009c\u009d")
        buf.write("\7h\2\2\u009d\u009e\7q\2\2\u009e\u009f\7t\2\2\u009f\n")
        buf.write("\3\2\2\2\u00a0\u00a1\7t\2\2\u00a1\u00a2\7g\2\2\u00a2\u00a3")
        buf.write("\7v\2\2\u00a3\u00a4\7w\2\2\u00a4\u00a5\7t\2\2\u00a5\u00a6")
        buf.write("\7p\2\2\u00a6\f\3\2\2\2\u00a7\u00a8\7h\2\2\u00a8\u00a9")
        buf.write("\7w\2\2\u00a9\u00aa\7p\2\2\u00aa\u00ab\7e\2\2\u00ab\16")
        buf.write("\3\2\2\2\u00ac\u00ad\7v\2\2\u00ad\u00ae\7{\2\2\u00ae\u00af")
        buf.write("\7r\2\2\u00af\u00b0\7g\2\2\u00b0\20\3\2\2\2\u00b1\u00b2")
        buf.write("\7u\2\2\u00b2\u00b3\7v\2\2\u00b3\u00b4\7t\2\2\u00b4\u00b5")
        buf.write("\7w\2\2\u00b5\u00b6\7e\2\2\u00b6\u00b7\7v\2\2\u00b7\22")
        buf.write("\3\2\2\2\u00b8\u00b9\7k\2\2\u00b9\u00ba\7p\2\2\u00ba\u00bb")
        buf.write("\7v\2\2\u00bb\u00bc\7g\2\2\u00bc\u00bd\7t\2\2\u00bd\u00be")
        buf.write("\7h\2\2\u00be\u00bf\7c\2\2\u00bf\u00c0\7e\2\2\u00c0\u00c1")
        buf.write("\7g\2\2\u00c1\24\3\2\2\2\u00c2\u00c3\7u\2\2\u00c3\u00c4")
        buf.write("\7v\2\2\u00c4\u00c5\7t\2\2\u00c5\u00c6\7k\2\2\u00c6\u00c7")
        buf.write("\7p\2\2\u00c7\u00c8\7i\2\2\u00c8\26\3\2\2\2\u00c9\u00ca")
        buf.write("\7k\2\2\u00ca\u00cb\7p\2\2\u00cb\u00cc\7v\2\2\u00cc\30")
        buf.write("\3\2\2\2\u00cd\u00ce\7h\2\2\u00ce\u00cf\7n\2\2\u00cf\u00d0")
        buf.write("\7q\2\2\u00d0\u00d1\7c\2\2\u00d1\u00d2\7v\2\2\u00d2\32")
        buf.write("\3\2\2\2\u00d3\u00d4\7d\2\2\u00d4\u00d5\7q\2\2\u00d5\u00d6")
        buf.write("\7q\2\2\u00d6\u00d7\7n\2\2\u00d7\u00d8\7g\2\2\u00d8\u00d9")
        buf.write("\7c\2\2\u00d9\u00da\7p\2\2\u00da\34\3\2\2\2\u00db\u00dc")
        buf.write("\7e\2\2\u00dc\u00dd\7q\2\2\u00dd\u00de\7p\2\2\u00de\u00df")
        buf.write("\7u\2\2\u00df\u00e0\7v\2\2\u00e0\36\3\2\2\2\u00e1\u00e2")
        buf.write("\7x\2\2\u00e2\u00e3\7c\2\2\u00e3\u00e4\7t\2\2\u00e4 \3")
        buf.write("\2\2\2\u00e5\u00e6\7e\2\2\u00e6\u00e7\7q\2\2\u00e7\u00e8")
        buf.write("\7p\2\2\u00e8\u00e9\7v\2\2\u00e9\u00ea\7k\2\2\u00ea\u00eb")
        buf.write("\7p\2\2\u00eb\u00ec\7w\2\2\u00ec\u00ed\7g\2\2\u00ed\"")
        buf.write("\3\2\2\2\u00ee\u00ef\7d\2\2\u00ef\u00f0\7t\2\2\u00f0\u00f1")
        buf.write("\7g\2\2\u00f1\u00f2\7c\2\2\u00f2\u00f3\7m\2\2\u00f3$\3")
        buf.write("\2\2\2\u00f4\u00f5\7t\2\2\u00f5\u00f6\7c\2\2\u00f6\u00f7")
        buf.write("\7p\2\2\u00f7\u00f8\7i\2\2\u00f8\u00f9\7g\2\2\u00f9&\3")
        buf.write("\2\2\2\u00fa\u00fb\7p\2\2\u00fb\u00fc\7k\2\2\u00fc\u00fd")
        buf.write("\7n\2\2\u00fd(\3\2\2\2\u00fe\u00ff\7v\2\2\u00ff\u0100")
        buf.write("\7t\2\2\u0100\u0101\7w\2\2\u0101\u0102\7g\2\2\u0102*\3")
        buf.write("\2\2\2\u0103\u0104\7h\2\2\u0104\u0105\7c\2\2\u0105\u0106")
        buf.write("\7n\2\2\u0106\u0107\7u\2\2\u0107\u0108\7g\2\2\u0108,\3")
        buf.write("\2\2\2\u0109\u010a\7-\2\2\u010a.\3\2\2\2\u010b\u010c\7")
        buf.write("/\2\2\u010c\60\3\2\2\2\u010d\u010e\7,\2\2\u010e\62\3\2")
        buf.write("\2\2\u010f\u0110\7\61\2\2\u0110\64\3\2\2\2\u0111\u0112")
        buf.write("\7\'\2\2\u0112\66\3\2\2\2\u0113\u0114\7?\2\2\u0114\u0115")
        buf.write("\7?\2\2\u01158\3\2\2\2\u0116\u0117\7#\2\2\u0117\u0118")
        buf.write("\7?\2\2\u0118:\3\2\2\2\u0119\u011a\7>\2\2\u011a<\3\2\2")
        buf.write("\2\u011b\u011c\7>\2\2\u011c\u011d\7?\2\2\u011d>\3\2\2")
        buf.write("\2\u011e\u011f\7@\2\2\u011f@\3\2\2\2\u0120\u0121\7@\2")
        buf.write("\2\u0121\u0122\7?\2\2\u0122B\3\2\2\2\u0123\u0124\7(\2")
        buf.write("\2\u0124\u0125\7(\2\2\u0125D\3\2\2\2\u0126\u0127\7~\2")
        buf.write("\2\u0127\u0128\7~\2\2\u0128F\3\2\2\2\u0129\u012a\7#\2")
        buf.write("\2\u012aH\3\2\2\2\u012b\u012c\7?\2\2\u012cJ\3\2\2\2\u012d")
        buf.write("\u012e\7-\2\2\u012e\u012f\7?\2\2\u012fL\3\2\2\2\u0130")
        buf.write("\u0131\7/\2\2\u0131\u0132\7?\2\2\u0132N\3\2\2\2\u0133")
        buf.write("\u0134\7,\2\2\u0134\u0135\7?\2\2\u0135P\3\2\2\2\u0136")
        buf.write("\u0137\7\61\2\2\u0137\u0138\7?\2\2\u0138R\3\2\2\2\u0139")
        buf.write("\u013a\7\'\2\2\u013a\u013b\7?\2\2\u013bT\3\2\2\2\u013c")
        buf.write("\u013d\7\60\2\2\u013dV\3\2\2\2\u013e\u013f\7*\2\2\u013f")
        buf.write("X\3\2\2\2\u0140\u0141\7+\2\2\u0141Z\3\2\2\2\u0142\u0143")
        buf.write("\7}\2\2\u0143\\\3\2\2\2\u0144\u0145\7\177\2\2\u0145^\3")
        buf.write("\2\2\2\u0146\u0147\7]\2\2\u0147`\3\2\2\2\u0148\u0149\7")
        buf.write("_\2\2\u0149b\3\2\2\2\u014a\u014b\7.\2\2\u014bd\3\2\2\2")
        buf.write("\u014c\u014d\7=\2\2\u014df\3\2\2\2\u014e\u0152\t\2\2\2")
        buf.write("\u014f\u0151\t\3\2\2\u0150\u014f\3\2\2\2\u0151\u0154\3")
        buf.write("\2\2\2\u0152\u0150\3\2\2\2\u0152\u0153\3\2\2\2\u0153h")
        buf.write("\3\2\2\2\u0154\u0152\3\2\2\2\u0155\u015e\7\62\2\2\u0156")
        buf.write("\u015a\t\4\2\2\u0157\u0159\t\5\2\2\u0158\u0157\3\2\2\2")
        buf.write("\u0159\u015c\3\2\2\2\u015a\u0158\3\2\2\2\u015a\u015b\3")
        buf.write("\2\2\2\u015b\u015e\3\2\2\2\u015c\u015a\3\2\2\2\u015d\u0155")
        buf.write("\3\2\2\2\u015d\u0156\3\2\2\2\u015ej\3\2\2\2\u015f\u0160")
        buf.write("\7\62\2\2\u0160\u0162\t\6\2\2\u0161\u0163\t\7\2\2\u0162")
        buf.write("\u0161\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0162\3\2\2\2")
        buf.write("\u0164\u0165\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0167\b")
        buf.write("\66\2\2\u0167l\3\2\2\2\u0168\u0169\7\62\2\2\u0169\u016b")
        buf.write("\t\b\2\2\u016a\u016c\t\t\2\2\u016b\u016a\3\2\2\2\u016c")
        buf.write("\u016d\3\2\2\2\u016d\u016b\3\2\2\2\u016d\u016e\3\2\2\2")
        buf.write("\u016e\u016f\3\2\2\2\u016f\u0170\b\67\3\2\u0170n\3\2\2")
        buf.write("\2\u0171\u0172\7\62\2\2\u0172\u0174\t\n\2\2\u0173\u0175")
        buf.write("\t\13\2\2\u0174\u0173\3\2\2\2\u0175\u0176\3\2\2\2\u0176")
        buf.write("\u0174\3\2\2\2\u0176\u0177\3\2\2\2\u0177\u0178\3\2\2\2")
        buf.write("\u0178\u0179\b8\4\2\u0179p\3\2\2\2\u017a\u017b\5u;\2\u017b")
        buf.write("\u017d\7\60\2\2\u017c\u017e\5u;\2\u017d\u017c\3\2\2\2")
        buf.write("\u017d\u017e\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0180\5")
        buf.write("w<\2\u0180r\3\2\2\2\u0181\u0182\t\5\2\2\u0182t\3\2\2\2")
        buf.write("\u0183\u0185\5s:\2\u0184\u0183\3\2\2\2\u0185\u0186\3\2")
        buf.write("\2\2\u0186\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187v\3")
        buf.write("\2\2\2\u0188\u018a\t\f\2\2\u0189\u018b\t\r\2\2\u018a\u0189")
        buf.write("\3\2\2\2\u018a\u018b\3\2\2\2\u018b\u018c\3\2\2\2\u018c")
        buf.write("\u018e\5u;\2\u018d\u0188\3\2\2\2\u018d\u018e\3\2\2\2\u018e")
        buf.write("x\3\2\2\2\u018f\u0193\7$\2\2\u0190\u0192\5{>\2\u0191\u0190")
        buf.write("\3\2\2\2\u0192\u0195\3\2\2\2\u0193\u0191\3\2\2\2\u0193")
        buf.write("\u0194\3\2\2\2\u0194\u0196\3\2\2\2\u0195\u0193\3\2\2\2")
        buf.write("\u0196\u0197\7$\2\2\u0197\u0198\b=\5\2\u0198z\3\2\2\2")
        buf.write("\u0199\u019c\n\16\2\2\u019a\u019c\5}?\2\u019b\u0199\3")
        buf.write("\2\2\2\u019b\u019a\3\2\2\2\u019c|\3\2\2\2\u019d\u019e")
        buf.write("\7^\2\2\u019e\u019f\t\17\2\2\u019f~\3\2\2\2\u01a0\u01a1")
        buf.write("\7^\2\2\u01a1\u01a2\n\17\2\2\u01a2\u0080\3\2\2\2\u01a3")
        buf.write("\u01a5\t\20\2\2\u01a4\u01a3\3\2\2\2\u01a5\u01a6\3\2\2")
        buf.write("\2\u01a6\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01a8")
        buf.write("\3\2\2\2\u01a8\u01a9\bA\6\2\u01a9\u0082\3\2\2\2\u01aa")
        buf.write("\u01ab\7\61\2\2\u01ab\u01ac\7\61\2\2\u01ac\u01b0\3\2\2")
        buf.write("\2\u01ad\u01af\n\21\2\2\u01ae\u01ad\3\2\2\2\u01af\u01b2")
        buf.write("\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1")
        buf.write("\u01b3\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b3\u01b4\bB\6\2")
        buf.write("\u01b4\u0084\3\2\2\2\u01b5\u01b6\7\61\2\2\u01b6\u01b7")
        buf.write("\7,\2\2\u01b7\u01bc\3\2\2\2\u01b8\u01bb\5\u0085C\2\u01b9")
        buf.write("\u01bb\13\2\2\2\u01ba\u01b8\3\2\2\2\u01ba\u01b9\3\2\2")
        buf.write("\2\u01bb\u01be\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bc\u01ba")
        buf.write("\3\2\2\2\u01bd\u01bf\3\2\2\2\u01be\u01bc\3\2\2\2\u01bf")
        buf.write("\u01c0\7,\2\2\u01c0\u01c1\7\61\2\2\u01c1\u01c2\3\2\2\2")
        buf.write("\u01c2\u01c3\bC\6\2\u01c3\u0086\3\2\2\2\u01c4\u01c5\13")
        buf.write("\2\2\2\u01c5\u01c6\bD\7\2\u01c6\u0088\3\2\2\2\u01c7\u01cb")
        buf.write("\7$\2\2\u01c8\u01ca\5{>\2\u01c9\u01c8\3\2\2\2\u01ca\u01cd")
        buf.write("\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc")
        buf.write("\u01d1\3\2\2\2\u01cd\u01cb\3\2\2\2\u01ce\u01cf\7\17\2")
        buf.write("\2\u01cf\u01d2\7\f\2\2\u01d0\u01d2\t\22\2\2\u01d1\u01ce")
        buf.write("\3\2\2\2\u01d1\u01d0\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3")
        buf.write("\u01d4\bE\b\2\u01d4\u008a\3\2\2\2\u01d5\u01d9\7$\2\2\u01d6")
        buf.write("\u01d8\5{>\2\u01d7\u01d6\3\2\2\2\u01d8\u01db\3\2\2\2\u01d9")
        buf.write("\u01d7\3\2\2\2\u01d9\u01da\3\2\2\2\u01da\u01dc\3\2\2\2")
        buf.write("\u01db\u01d9\3\2\2\2\u01dc\u01dd\5\177@\2\u01dd\u01de")
        buf.write("\bF\t\2\u01de\u008c\3\2\2\2\26\2\u0152\u015a\u015d\u0164")
        buf.write("\u016d\u0176\u017d\u0186\u018a\u018d\u0193\u019b\u01a6")
        buf.write("\u01b0\u01ba\u01bc\u01cb\u01d1\u01d9\n\3\66\2\3\67\3\3")
        buf.write("8\4\3=\5\b\2\2\3D\6\3E\7\3F\b")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    IF = 2
    ELSE = 3
    FOR = 4
    RETURN = 5
    FUNC = 6
    TYPE = 7
    STRUCT = 8
    INTERFACE = 9
    STRING = 10
    INT = 11
    FLOAT = 12
    BOOLEAN = 13
    CONST = 14
    VAR = 15
    CONTINUE = 16
    BREAK = 17
    RANGE = 18
    NIL = 19
    TRUE = 20
    FALSE = 21
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
    LPAREN = 43
    RPAREN = 44
    LBRACE = 45
    RBRACE = 46
    LBRACK = 47
    RBRACK = 48
    COMMA = 49
    SEMICOL = 50
    ID = 51
    DEC_INT = 52
    BIN_INT = 53
    OCT_INT = 54
    HEX_INT = 55
    FLOAT_LIT = 56
    STRING_LIT = 57
    WS = 58
    COMMENT = 59
    ML_COMMENT = 60
    ERROR_CHAR = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'votien'", "'if'", "'else'", "'for'", "'return'", "'func'", 
            "'type'", "'struct'", "'interface'", "'string'", "'int'", "'float'", 
            "'boolean'", "'const'", "'var'", "'continue'", "'break'", "'range'", 
            "'nil'", "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", 
            "'!'", "'='", "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", 
            "'('", "')'", "'{'", "'}'", "'['", "']'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
            "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", 
            "DIV", "MOD", "EQUAL", "DIFF", "LT", "LTE", "RT", "RTE", "AND", 
            "OR", "NOT", "ASSIGN", "ASSIGNADD", "ASSIGNSUB", "ASSIGNMUL", 
            "ASSIGNDIV", "ASSIGNMOD", "POINTTO", "LPAREN", "RPAREN", "LBRACE", 
            "RBRACE", "LBRACK", "RBRACK", "COMMA", "SEMICOL", "ID", "DEC_INT", 
            "BIN_INT", "OCT_INT", "HEX_INT", "FLOAT_LIT", "STRING_LIT", 
            "WS", "COMMENT", "ML_COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", 
                  "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
                  "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", 
                  "FALSE", "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", "DIFF", 
                  "LT", "LTE", "RT", "RTE", "AND", "OR", "NOT", "ASSIGN", 
                  "ASSIGNADD", "ASSIGNSUB", "ASSIGNMUL", "ASSIGNDIV", "ASSIGNMOD", 
                  "POINTTO", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", 
                  "RBRACK", "COMMA", "SEMICOL", "ID", "DEC_INT", "BIN_INT", 
                  "OCT_INT", "HEX_INT", "FLOAT_LIT", "DIGIT", "DIGITS", 
                  "OPT_EXP", "STRING_LIT", "STR_CHAR", "ESC_SEQ", "ESC_ILLEGAL", 
                  "WS", "COMMENT", "ML_COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", 
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
            actions[52] = self.BIN_INT_action 
            actions[53] = self.OCT_INT_action 
            actions[54] = self.HEX_INT_action 
            actions[59] = self.STRING_LIT_action 
            actions[66] = self.ERROR_CHAR_action 
            actions[67] = self.UNCLOSE_STRING_action 
            actions[68] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def BIN_INT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                self.text = str(int(self.text[2:], 2))

     

    def OCT_INT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                self.text = str(int(self.text[2:], 8))

     

    def HEX_INT_action(self, localctx:RuleContext , actionIndex:int):
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

     


