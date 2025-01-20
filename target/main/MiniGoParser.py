# Generated from main/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A")
        buf.write("\u01ac\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\3\2\7\2F\n\2\f\2\16\2I")
        buf.write("\13\2\3\2\3\2\3\2\7\2N\n\2\f\2\16\2Q\13\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\5\3[\n\3\3\4\3\4\5\4_\n\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\5\6l\n\6\3\6\3\6")
        buf.write("\5\6p\n\6\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\7\n\u0080\n\n\f\n\16\n\u0083\13\n\3\13\3")
        buf.write("\13\3\13\5\13\u0088\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5")
        buf.write("\f\u0091\n\f\3\f\3\f\3\r\3\r\3\r\3\r\5\r\u0099\n\r\3\r")
        buf.write("\3\r\3\r\3\r\5\r\u009f\n\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00ad\n\16\3\16\3")
        buf.write("\16\3\16\3\16\5\16\u00b3\n\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\7\17\u00bd\n\17\f\17\16\17\u00c0\13\17")
        buf.write("\3\17\3\17\3\17\7\17\u00c5\n\17\f\17\16\17\u00c8\13\17")
        buf.write("\7\17\u00ca\n\17\f\17\16\17\u00cd\13\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\7\20\u00d6\n\20\f\20\16\20\u00d9")
        buf.write("\13\20\3\20\3\20\3\20\5\20\u00de\n\20\3\20\3\20\3\20\3")
        buf.write("\20\5\20\u00e4\n\20\3\20\5\20\u00e7\n\20\3\20\7\20\u00ea")
        buf.write("\n\20\f\20\16\20\u00ed\13\20\7\20\u00ef\n\20\f\20\16\20")
        buf.write("\u00f2\13\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\5\21\u00fb")
        buf.write("\n\21\3\22\3\22\3\22\3\22\5\22\u0101\n\22\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\5\23\u010a\n\23\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\5\26\u0117\n")
        buf.write("\26\3\27\3\27\3\27\3\27\3\27\5\27\u011e\n\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\7\30\u0128\n\30\f\30\16")
        buf.write("\30\u012b\13\30\3\31\3\31\3\31\3\31\3\31\3\31\7\31\u0133")
        buf.write("\n\31\f\31\16\31\u0136\13\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\7\32\u013e\n\32\f\32\16\32\u0141\13\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\7\33\u0158\n")
        buf.write("\33\f\33\16\33\u015b\13\33\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\7\34\u0166\n\34\f\34\16\34\u0169\13")
        buf.write("\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\7\35\u0177\n\35\f\35\16\35\u017a\13\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\5\36\u0181\n\36\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\5\37\u018b\n\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\7\37\u0194\n\37\f\37\16\37\u0197")
        buf.write("\13\37\3 \3 \3 \3 \3 \3 \3 \5 \u01a0\n \3!\3!\3!\3!\3")
        buf.write("!\3\"\6\"\u01a8\n\"\r\"\16\"\u01a9\3\"\2\b\60\62\64\66")
        buf.write("8<#\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>@B\2\3\3\2\13\16\2\u01ce\2G\3\2\2\2\4Z\3")
        buf.write("\2\2\2\6^\3\2\2\2\bb\3\2\2\2\ng\3\2\2\2\fq\3\2\2\2\16")
        buf.write("s\3\2\2\2\20v\3\2\2\2\22y\3\2\2\2\24\u0084\3\2\2\2\26")
        buf.write("\u0089\3\2\2\2\30\u0094\3\2\2\2\32\u00a3\3\2\2\2\34\u00b7")
        buf.write("\3\2\2\2\36\u00d0\3\2\2\2 \u00fa\3\2\2\2\"\u0100\3\2\2")
        buf.write("\2$\u0109\3\2\2\2&\u010b\3\2\2\2(\u010f\3\2\2\2*\u0116")
        buf.write("\3\2\2\2,\u011d\3\2\2\2.\u011f\3\2\2\2\60\u012c\3\2\2")
        buf.write("\2\62\u0137\3\2\2\2\64\u0142\3\2\2\2\66\u015c\3\2\2\2")
        buf.write("8\u016a\3\2\2\2:\u0180\3\2\2\2<\u0182\3\2\2\2>\u019f\3")
        buf.write("\2\2\2@\u01a1\3\2\2\2B\u01a7\3\2\2\2DF\7<\2\2ED\3\2\2")
        buf.write("\2FI\3\2\2\2GE\3\2\2\2GH\3\2\2\2HJ\3\2\2\2IG\3\2\2\2J")
        buf.write("O\5\4\3\2KN\5\4\3\2LN\7<\2\2MK\3\2\2\2ML\3\2\2\2NQ\3\2")
        buf.write("\2\2OM\3\2\2\2OP\3\2\2\2PR\3\2\2\2QO\3\2\2\2RS\7\2\2\3")
        buf.write("S\3\3\2\2\2T[\5\6\4\2U[\5\26\f\2V[\5\30\r\2W[\5\32\16")
        buf.write("\2X[\5\34\17\2Y[\5\36\20\2ZT\3\2\2\2ZU\3\2\2\2ZV\3\2\2")
        buf.write("\2ZW\3\2\2\2ZX\3\2\2\2ZY\3\2\2\2[\5\3\2\2\2\\_\5\b\5\2")
        buf.write("]_\5\n\6\2^\\\3\2\2\2^]\3\2\2\2_`\3\2\2\2`a\7\66\2\2a")
        buf.write("\7\3\2\2\2bc\7\20\2\2cd\7\67\2\2de\7&\2\2ef\5\60\31\2")
        buf.write("f\t\3\2\2\2gk\7\20\2\2hl\5\16\b\2il\5\24\13\2jl\5\20\t")
        buf.write("\2kh\3\2\2\2ki\3\2\2\2kj\3\2\2\2lo\3\2\2\2mn\7&\2\2np")
        buf.write("\5\60\31\2om\3\2\2\2op\3\2\2\2p\13\3\2\2\2qr\t\2\2\2r")
        buf.write("\r\3\2\2\2st\7\67\2\2tu\5\f\7\2u\17\3\2\2\2vw\7\67\2\2")
        buf.write("wx\7\27\2\2x\21\3\2\2\2yz\7\63\2\2z{\78\2\2{\u0081\7\64")
        buf.write("\2\2|}\7\63\2\2}~\78\2\2~\u0080\7\64\2\2\177|\3\2\2\2")
        buf.write("\u0080\u0083\3\2\2\2\u0081\177\3\2\2\2\u0081\u0082\3\2")
        buf.write("\2\2\u0082\23\3\2\2\2\u0083\u0081\3\2\2\2\u0084\u0087")
        buf.write("\5\22\n\2\u0085\u0088\5\f\7\2\u0086\u0088\7\67\2\2\u0087")
        buf.write("\u0085\3\2\2\2\u0087\u0086\3\2\2\2\u0088\25\3\2\2\2\u0089")
        buf.write("\u008a\7\17\2\2\u008a\u008b\7\67\2\2\u008b\u0090\7&\2")
        buf.write("\2\u008c\u0091\5\60\31\2\u008d\u008e\5\24\13\2\u008e\u008f")
        buf.write("\5\60\31\2\u008f\u0091\3\2\2\2\u0090\u008c\3\2\2\2\u0090")
        buf.write("\u008d\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0093\7\66\2")
        buf.write("\2\u0093\27\3\2\2\2\u0094\u0095\7\7\2\2\u0095\u0096\7")
        buf.write("\67\2\2\u0096\u0098\7/\2\2\u0097\u0099\5 \21\2\u0098\u0097")
        buf.write("\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009a\3\2\2\2\u009a")
        buf.write("\u009e\7\60\2\2\u009b\u009f\5\f\7\2\u009c\u009f\7\67\2")
        buf.write("\2\u009d\u009f\5\24\13\2\u009e\u009b\3\2\2\2\u009e\u009c")
        buf.write("\3\2\2\2\u009e\u009d\3\2\2\2\u009e\u009f\3\2\2\2\u009f")
        buf.write("\u00a0\3\2\2\2\u00a0\u00a1\7\61\2\2\u00a1\u00a2\7\62\2")
        buf.write("\2\u00a2\31\3\2\2\2\u00a3\u00a4\7\7\2\2\u00a4\u00a5\7")
        buf.write("/\2\2\u00a5\u00a6\7\67\2\2\u00a6\u00a7\7\67\2\2\u00a7")
        buf.write("\u00a8\3\2\2\2\u00a8\u00a9\7\60\2\2\u00a9\u00aa\7\67\2")
        buf.write("\2\u00aa\u00ac\7/\2\2\u00ab\u00ad\5 \21\2\u00ac\u00ab")
        buf.write("\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae")
        buf.write("\u00b2\7\60\2\2\u00af\u00b3\5\f\7\2\u00b0\u00b3\7\67\2")
        buf.write("\2\u00b1\u00b3\5\24\13\2\u00b2\u00af\3\2\2\2\u00b2\u00b0")
        buf.write("\3\2\2\2\u00b2\u00b1\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3")
        buf.write("\u00b4\3\2\2\2\u00b4\u00b5\7\61\2\2\u00b5\u00b6\7\62\2")
        buf.write("\2\u00b6\33\3\2\2\2\u00b7\u00b8\7\b\2\2\u00b8\u00b9\7")
        buf.write("\67\2\2\u00b9\u00ba\7\t\2\2\u00ba\u00be\7\61\2\2\u00bb")
        buf.write("\u00bd\5B\"\2\u00bc\u00bb\3\2\2\2\u00bd\u00c0\3\2\2\2")
        buf.write("\u00be\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00cb\3")
        buf.write("\2\2\2\u00c0\u00be\3\2\2\2\u00c1\u00c2\5\"\22\2\u00c2")
        buf.write("\u00c6\7\66\2\2\u00c3\u00c5\5B\"\2\u00c4\u00c3\3\2\2\2")
        buf.write("\u00c5\u00c8\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c7\3")
        buf.write("\2\2\2\u00c7\u00ca\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c9\u00c1")
        buf.write("\3\2\2\2\u00ca\u00cd\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cb")
        buf.write("\u00cc\3\2\2\2\u00cc\u00ce\3\2\2\2\u00cd\u00cb\3\2\2\2")
        buf.write("\u00ce\u00cf\7\62\2\2\u00cf\35\3\2\2\2\u00d0\u00d1\7\b")
        buf.write("\2\2\u00d1\u00d2\7\67\2\2\u00d2\u00d3\7\n\2\2\u00d3\u00d7")
        buf.write("\7\61\2\2\u00d4\u00d6\5B\"\2\u00d5\u00d4\3\2\2\2\u00d6")
        buf.write("\u00d9\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2")
        buf.write("\u00d8\u00f0\3\2\2\2\u00d9\u00d7\3\2\2\2\u00da\u00db\7")
        buf.write("\67\2\2\u00db\u00dd\7/\2\2\u00dc\u00de\5 \21\2\u00dd\u00dc")
        buf.write("\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00df\3\2\2\2\u00df")
        buf.write("\u00e3\7\60\2\2\u00e0\u00e4\5\f\7\2\u00e1\u00e4\7\67\2")
        buf.write("\2\u00e2\u00e4\5\24\13\2\u00e3\u00e0\3\2\2\2\u00e3\u00e1")
        buf.write("\3\2\2\2\u00e3\u00e2\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4")
        buf.write("\u00e6\3\2\2\2\u00e5\u00e7\7\66\2\2\u00e6\u00e5\3\2\2")
        buf.write("\2\u00e6\u00e7\3\2\2\2\u00e7\u00eb\3\2\2\2\u00e8\u00ea")
        buf.write("\5B\"\2\u00e9\u00e8\3\2\2\2\u00ea\u00ed\3\2\2\2\u00eb")
        buf.write("\u00e9\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\u00ef\3\2\2\2")
        buf.write("\u00ed\u00eb\3\2\2\2\u00ee\u00da\3\2\2\2\u00ef\u00f2\3")
        buf.write("\2\2\2\u00f0\u00ee\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\u00f3")
        buf.write("\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f3\u00f4\7\62\2\2\u00f4")
        buf.write("\37\3\2\2\2\u00f5\u00f6\5\"\22\2\u00f6\u00f7\7\65\2\2")
        buf.write("\u00f7\u00f8\5 \21\2\u00f8\u00fb\3\2\2\2\u00f9\u00fb\5")
        buf.write("\"\22\2\u00fa\u00f5\3\2\2\2\u00fa\u00f9\3\2\2\2\u00fb")
        buf.write("!\3\2\2\2\u00fc\u0101\5\16\b\2\u00fd\u00fe\7\67\2\2\u00fe")
        buf.write("\u0101\5\24\13\2\u00ff\u0101\7\67\2\2\u0100\u00fc\3\2")
        buf.write("\2\2\u0100\u00fd\3\2\2\2\u0100\u00ff\3\2\2\2\u0101#\3")
        buf.write("\2\2\2\u0102\u010a\78\2\2\u0103\u010a\79\2\2\u0104\u010a")
        buf.write("\7:\2\2\u0105\u010a\7\25\2\2\u0106\u010a\7\26\2\2\u0107")
        buf.write("\u010a\5&\24\2\u0108\u010a\5(\25\2\u0109\u0102\3\2\2\2")
        buf.write("\u0109\u0103\3\2\2\2\u0109\u0104\3\2\2\2\u0109\u0105\3")
        buf.write("\2\2\2\u0109\u0106\3\2\2\2\u0109\u0107\3\2\2\2\u0109\u0108")
        buf.write("\3\2\2\2\u010a%\3\2\2\2\u010b\u010c\7\61\2\2\u010c\u010d")
        buf.write("\5,\27\2\u010d\u010e\7\62\2\2\u010e\'\3\2\2\2\u010f\u0110")
        buf.write("\7\67\2\2\u0110\u0111\7\61\2\2\u0111\u0112\5.\30\2\u0112")
        buf.write("\u0113\7\62\2\2\u0113)\3\2\2\2\u0114\u0117\5,\27\2\u0115")
        buf.write("\u0117\3\2\2\2\u0116\u0114\3\2\2\2\u0116\u0115\3\2\2\2")
        buf.write("\u0117+\3\2\2\2\u0118\u0119\5\60\31\2\u0119\u011a\7\65")
        buf.write("\2\2\u011a\u011b\5,\27\2\u011b\u011e\3\2\2\2\u011c\u011e")
        buf.write("\5\60\31\2\u011d\u0118\3\2\2\2\u011d\u011c\3\2\2\2\u011e")
        buf.write("-\3\2\2\2\u011f\u0120\7\67\2\2\u0120\u0121\7-\2\2\u0121")
        buf.write("\u0122\5\60\31\2\u0122\u0129\3\2\2\2\u0123\u0124\7\65")
        buf.write("\2\2\u0124\u0125\7\67\2\2\u0125\u0126\7-\2\2\u0126\u0128")
        buf.write("\5\60\31\2\u0127\u0123\3\2\2\2\u0128\u012b\3\2\2\2\u0129")
        buf.write("\u0127\3\2\2\2\u0129\u012a\3\2\2\2\u012a/\3\2\2\2\u012b")
        buf.write("\u0129\3\2\2\2\u012c\u012d\b\31\1\2\u012d\u012e\5\62\32")
        buf.write("\2\u012e\u0134\3\2\2\2\u012f\u0130\f\4\2\2\u0130\u0131")
        buf.write("\7$\2\2\u0131\u0133\5\62\32\2\u0132\u012f\3\2\2\2\u0133")
        buf.write("\u0136\3\2\2\2\u0134\u0132\3\2\2\2\u0134\u0135\3\2\2\2")
        buf.write("\u0135\61\3\2\2\2\u0136\u0134\3\2\2\2\u0137\u0138\b\32")
        buf.write("\1\2\u0138\u0139\5\64\33\2\u0139\u013f\3\2\2\2\u013a\u013b")
        buf.write("\f\4\2\2\u013b\u013c\7#\2\2\u013c\u013e\5\64\33\2\u013d")
        buf.write("\u013a\3\2\2\2\u013e\u0141\3\2\2\2\u013f\u013d\3\2\2\2")
        buf.write("\u013f\u0140\3\2\2\2\u0140\63\3\2\2\2\u0141\u013f\3\2")
        buf.write("\2\2\u0142\u0143\b\33\1\2\u0143\u0144\5\66\34\2\u0144")
        buf.write("\u0159\3\2\2\2\u0145\u0146\f\t\2\2\u0146\u0147\7\35\2")
        buf.write("\2\u0147\u0158\5\66\34\2\u0148\u0149\f\b\2\2\u0149\u014a")
        buf.write("\7\36\2\2\u014a\u0158\5\66\34\2\u014b\u014c\f\7\2\2\u014c")
        buf.write("\u014d\7\37\2\2\u014d\u0158\5\66\34\2\u014e\u014f\f\6")
        buf.write("\2\2\u014f\u0150\7 \2\2\u0150\u0158\5\66\34\2\u0151\u0152")
        buf.write("\f\5\2\2\u0152\u0153\7!\2\2\u0153\u0158\5\66\34\2\u0154")
        buf.write("\u0155\f\4\2\2\u0155\u0156\7\"\2\2\u0156\u0158\5\66\34")
        buf.write("\2\u0157\u0145\3\2\2\2\u0157\u0148\3\2\2\2\u0157\u014b")
        buf.write("\3\2\2\2\u0157\u014e\3\2\2\2\u0157\u0151\3\2\2\2\u0157")
        buf.write("\u0154\3\2\2\2\u0158\u015b\3\2\2\2\u0159\u0157\3\2\2\2")
        buf.write("\u0159\u015a\3\2\2\2\u015a\65\3\2\2\2\u015b\u0159\3\2")
        buf.write("\2\2\u015c\u015d\b\34\1\2\u015d\u015e\58\35\2\u015e\u0167")
        buf.write("\3\2\2\2\u015f\u0160\f\5\2\2\u0160\u0161\7\30\2\2\u0161")
        buf.write("\u0166\58\35\2\u0162\u0163\f\4\2\2\u0163\u0164\7\31\2")
        buf.write("\2\u0164\u0166\58\35\2\u0165\u015f\3\2\2\2\u0165\u0162")
        buf.write("\3\2\2\2\u0166\u0169\3\2\2\2\u0167\u0165\3\2\2\2\u0167")
        buf.write("\u0168\3\2\2\2\u0168\67\3\2\2\2\u0169\u0167\3\2\2\2\u016a")
        buf.write("\u016b\b\35\1\2\u016b\u016c\5:\36\2\u016c\u0178\3\2\2")
        buf.write("\2\u016d\u016e\f\6\2\2\u016e\u016f\7\32\2\2\u016f\u0177")
        buf.write("\5:\36\2\u0170\u0171\f\5\2\2\u0171\u0172\7\33\2\2\u0172")
        buf.write("\u0177\5:\36\2\u0173\u0174\f\4\2\2\u0174\u0175\7\34\2")
        buf.write("\2\u0175\u0177\5:\36\2\u0176\u016d\3\2\2\2\u0176\u0170")
        buf.write("\3\2\2\2\u0176\u0173\3\2\2\2\u0177\u017a\3\2\2\2\u0178")
        buf.write("\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u01799\3\2\2\2\u017a")
        buf.write("\u0178\3\2\2\2\u017b\u017c\7%\2\2\u017c\u0181\5:\36\2")
        buf.write("\u017d\u017e\7\31\2\2\u017e\u0181\5:\36\2\u017f\u0181")
        buf.write("\5<\37\2\u0180\u017b\3\2\2\2\u0180\u017d\3\2\2\2\u0180")
        buf.write("\u017f\3\2\2\2\u0181;\3\2\2\2\u0182\u0183\b\37\1\2\u0183")
        buf.write("\u0184\5> \2\u0184\u0195\3\2\2\2\u0185\u018a\f\5\2\2\u0186")
        buf.write("\u0187\7/\2\2\u0187\u0188\5*\26\2\u0188\u0189\7\60\2\2")
        buf.write("\u0189\u018b\3\2\2\2\u018a\u0186\3\2\2\2\u018a\u018b\3")
        buf.write("\2\2\2\u018b\u018c\3\2\2\2\u018c\u018d\7\63\2\2\u018d")
        buf.write("\u018e\5,\27\2\u018e\u018f\7\64\2\2\u018f\u0194\3\2\2")
        buf.write("\2\u0190\u0191\f\4\2\2\u0191\u0192\7,\2\2\u0192\u0194")
        buf.write("\5> \2\u0193\u0185\3\2\2\2\u0193\u0190\3\2\2\2\u0194\u0197")
        buf.write("\3\2\2\2\u0195\u0193\3\2\2\2\u0195\u0196\3\2\2\2\u0196")
        buf.write("=\3\2\2\2\u0197\u0195\3\2\2\2\u0198\u0199\7/\2\2\u0199")
        buf.write("\u019a\5\60\31\2\u019a\u019b\7\60\2\2\u019b\u01a0\3\2")
        buf.write("\2\2\u019c\u01a0\7\67\2\2\u019d\u01a0\5$\23\2\u019e\u01a0")
        buf.write("\5@!\2\u019f\u0198\3\2\2\2\u019f\u019c\3\2\2\2\u019f\u019d")
        buf.write("\3\2\2\2\u019f\u019e\3\2\2\2\u01a0?\3\2\2\2\u01a1\u01a2")
        buf.write("\7\67\2\2\u01a2\u01a3\7/\2\2\u01a3\u01a4\5*\26\2\u01a4")
        buf.write("\u01a5\7\60\2\2\u01a5A\3\2\2\2\u01a6\u01a8\7<\2\2\u01a7")
        buf.write("\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01a7\3\2\2\2")
        buf.write("\u01a9\u01aa\3\2\2\2\u01aaC\3\2\2\2-GMOZ^ko\u0081\u0087")
        buf.write("\u0090\u0098\u009e\u00ac\u00b2\u00be\u00c6\u00cb\u00d7")
        buf.write("\u00dd\u00e3\u00e6\u00eb\u00f0\u00fa\u0100\u0109\u0116")
        buf.write("\u011d\u0129\u0134\u013f\u0157\u0159\u0165\u0167\u0176")
        buf.write("\u0178\u0180\u018a\u0193\u0195\u019f\u01a9")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'boolean'", "'const'", "'var'", 
                     "'continue'", "'break'", "'range'", "'nil'", "'true'", 
                     "'false'", "'str'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", 
                     "'||'", "'!'", "'='", "'+='", "'-='", "'*='", "'/='", 
                     "'%='", "'.'", "':'", "':='", "'('", "')'", "'{'", 
                     "'}'", "'['", "']'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                      "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
                      "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
                      "NIL", "TRUE", "FALSE", "STR", "ADD", "SUB", "MUL", 
                      "DIV", "MOD", "EQUAL", "DIFF", "LT", "LTE", "RT", 
                      "RTE", "AND", "OR", "NOT", "ASSIGN", "ASSIGNADD", 
                      "ASSIGNSUB", "ASSIGNMUL", "ASSIGNDIV", "ASSIGNMOD", 
                      "POINTTO", "COLON", "ASSIGNNIT", "LPAREN", "RPAREN", 
                      "LBRACE", "RBRACE", "LBRACK", "RBRACK", "COMMA", "SEMICOL", 
                      "ID", "INT_LIT", "FLOAT_LIT", "STRING_LIT", "WS", 
                      "NEWLINE", "COMMENT", "ML_COMMENT", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_declared = 1
    RULE_variables_declared = 2
    RULE_implicit_var = 3
    RULE_keyword_var = 4
    RULE_primitive_type = 5
    RULE_primitive_declaration = 6
    RULE_interface_type = 7
    RULE_dimension_list = 8
    RULE_array_declaration = 9
    RULE_constants_declared = 10
    RULE_function_declared = 11
    RULE_method_declared = 12
    RULE_struct_declared = 13
    RULE_interface_declared = 14
    RULE_prameters_list = 15
    RULE_prameter = 16
    RULE_literal = 17
    RULE_array_literal = 18
    RULE_struct_literal = 19
    RULE_list_expression = 20
    RULE_params = 21
    RULE_list_elements = 22
    RULE_expression = 23
    RULE_expression1 = 24
    RULE_expression2 = 25
    RULE_expression3 = 26
    RULE_expression4 = 27
    RULE_expression5 = 28
    RULE_expression6 = 29
    RULE_expression7 = 30
    RULE_func_call = 31
    RULE_ignore = 32

    ruleNames =  [ "program", "declared", "variables_declared", "implicit_var", 
                   "keyword_var", "primitive_type", "primitive_declaration", 
                   "interface_type", "dimension_list", "array_declaration", 
                   "constants_declared", "function_declared", "method_declared", 
                   "struct_declared", "interface_declared", "prameters_list", 
                   "prameter", "literal", "array_literal", "struct_literal", 
                   "list_expression", "params", "list_elements", "expression", 
                   "expression1", "expression2", "expression3", "expression4", 
                   "expression5", "expression6", "expression7", "func_call", 
                   "ignore" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    FOR=3
    RETURN=4
    FUNC=5
    TYPE=6
    STRUCT=7
    INTERFACE=8
    STRING=9
    INT=10
    FLOAT=11
    BOOLEAN=12
    CONST=13
    VAR=14
    CONTINUE=15
    BREAK=16
    RANGE=17
    NIL=18
    TRUE=19
    FALSE=20
    STR=21
    ADD=22
    SUB=23
    MUL=24
    DIV=25
    MOD=26
    EQUAL=27
    DIFF=28
    LT=29
    LTE=30
    RT=31
    RTE=32
    AND=33
    OR=34
    NOT=35
    ASSIGN=36
    ASSIGNADD=37
    ASSIGNSUB=38
    ASSIGNMUL=39
    ASSIGNDIV=40
    ASSIGNMOD=41
    POINTTO=42
    COLON=43
    ASSIGNNIT=44
    LPAREN=45
    RPAREN=46
    LBRACE=47
    RBRACE=48
    LBRACK=49
    RBRACK=50
    COMMA=51
    SEMICOL=52
    ID=53
    INT_LIT=54
    FLOAT_LIT=55
    STRING_LIT=56
    WS=57
    NEWLINE=58
    COMMENT=59
    ML_COMMENT=60
    ERROR_CHAR=61
    UNCLOSE_STRING=62
    ILLEGAL_ESCAPE=63

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declared(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclaredContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclaredContext,i)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NEWLINE:
                self.state = 66
                self.match(MiniGoParser.NEWLINE)
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
            self.declared()
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.NEWLINE))) != 0):
                self.state = 75
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR]:
                    self.state = 73
                    self.declared()
                    pass
                elif token in [MiniGoParser.NEWLINE]:
                    self.state = 74
                    self.match(MiniGoParser.NEWLINE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 80
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variables_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Variables_declaredContext,0)


        def constants_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Constants_declaredContext,0)


        def function_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Function_declaredContext,0)


        def method_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declaredContext,0)


        def struct_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declaredContext,0)


        def interface_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declaredContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclared" ):
                return visitor.visitDeclared(self)
            else:
                return visitor.visitChildren(self)




    def declared(self):

        localctx = MiniGoParser.DeclaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declared)
        try:
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.variables_declared()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.constants_declared()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 84
                self.function_declared()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 85
                self.method_declared()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 86
                self.struct_declared()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 87
                self.interface_declared()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variables_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOL(self):
            return self.getToken(MiniGoParser.SEMICOL, 0)

        def implicit_var(self):
            return self.getTypedRuleContext(MiniGoParser.Implicit_varContext,0)


        def keyword_var(self):
            return self.getTypedRuleContext(MiniGoParser.Keyword_varContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_variables_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariables_declared" ):
                return visitor.visitVariables_declared(self)
            else:
                return visitor.visitChildren(self)




    def variables_declared(self):

        localctx = MiniGoParser.Variables_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variables_declared)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 90
                self.implicit_var()
                pass

            elif la_ == 2:
                self.state = 91
                self.keyword_var()
                pass


            self.state = 94
            self.match(MiniGoParser.SEMICOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implicit_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_implicit_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_var" ):
                return visitor.visitImplicit_var(self)
            else:
                return visitor.visitChildren(self)




    def implicit_var(self):

        localctx = MiniGoParser.Implicit_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_implicit_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(MiniGoParser.VAR)
            self.state = 97
            self.match(MiniGoParser.ID)
            self.state = 98
            self.match(MiniGoParser.ASSIGN)
            self.state = 99
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Keyword_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def primitive_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_declarationContext,0)


        def array_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Array_declarationContext,0)


        def interface_type(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_typeContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_keyword_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyword_var" ):
                return visitor.visitKeyword_var(self)
            else:
                return visitor.visitChildren(self)




    def keyword_var(self):

        localctx = MiniGoParser.Keyword_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_keyword_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(MiniGoParser.VAR)
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 102
                self.primitive_declaration()
                pass

            elif la_ == 2:
                self.state = 103
                self.array_declaration()
                pass

            elif la_ == 3:
                self.state = 104
                self.interface_type()
                pass


            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ASSIGN:
                self.state = 107
                self.match(MiniGoParser.ASSIGN)
                self.state = 108
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = MiniGoParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_primitive_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_declaration" ):
                return visitor.visitPrimitive_declaration(self)
            else:
                return visitor.visitChildren(self)




    def primitive_declaration(self):

        localctx = MiniGoParser.Primitive_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_primitive_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(MiniGoParser.ID)
            self.state = 114
            self.primitive_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STR(self):
            return self.getToken(MiniGoParser.STR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_type" ):
                return visitor.visitInterface_type(self)
            else:
                return visitor.visitChildren(self)




    def interface_type(self):

        localctx = MiniGoParser.Interface_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_interface_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(MiniGoParser.ID)
            self.state = 117
            self.match(MiniGoParser.STR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dimension_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LBRACK)
            else:
                return self.getToken(MiniGoParser.LBRACK, i)

        def INT_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.INT_LIT)
            else:
                return self.getToken(MiniGoParser.INT_LIT, i)

        def RBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RBRACK)
            else:
                return self.getToken(MiniGoParser.RBRACK, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_dimension_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension_list" ):
                return visitor.visitDimension_list(self)
            else:
                return visitor.visitChildren(self)




    def dimension_list(self):

        localctx = MiniGoParser.Dimension_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_dimension_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(MiniGoParser.LBRACK)
            self.state = 120
            self.match(MiniGoParser.INT_LIT)
            self.state = 121
            self.match(MiniGoParser.RBRACK)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.LBRACK:
                self.state = 122
                self.match(MiniGoParser.LBRACK)
                self.state = 123
                self.match(MiniGoParser.INT_LIT)
                self.state = 124
                self.match(MiniGoParser.RBRACK)
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimension_list(self):
            return self.getTypedRuleContext(MiniGoParser.Dimension_listContext,0)


        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_declaration" ):
                return visitor.visitArray_declaration(self)
            else:
                return visitor.visitChildren(self)




    def array_declaration(self):

        localctx = MiniGoParser.Array_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_array_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.dimension_list()
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 131
                self.primitive_type()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 132
                self.match(MiniGoParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constants_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def SEMICOL(self):
            return self.getToken(MiniGoParser.SEMICOL, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def array_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Array_declarationContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_constants_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstants_declared" ):
                return visitor.visitConstants_declared(self)
            else:
                return visitor.visitChildren(self)




    def constants_declared(self):

        localctx = MiniGoParser.Constants_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_constants_declared)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(MiniGoParser.CONST)
            self.state = 136
            self.match(MiniGoParser.ID)
            self.state = 137
            self.match(MiniGoParser.ASSIGN)
            self.state = 142
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LPAREN, MiniGoParser.LBRACE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.state = 138
                self.expression(0)
                pass
            elif token in [MiniGoParser.LBRACK]:
                self.state = 139
                self.array_declaration()
                self.state = 140
                self.expression(0)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 144
            self.match(MiniGoParser.SEMICOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def prameters_list(self):
            return self.getTypedRuleContext(MiniGoParser.Prameters_listContext,0)


        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def array_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Array_declarationContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_function_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declared" ):
                return visitor.visitFunction_declared(self)
            else:
                return visitor.visitChildren(self)




    def function_declared(self):

        localctx = MiniGoParser.Function_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_function_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(MiniGoParser.FUNC)
            self.state = 147
            self.match(MiniGoParser.ID)
            self.state = 148
            self.match(MiniGoParser.LPAREN)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 149
                self.prameters_list()


            self.state = 152
            self.match(MiniGoParser.RPAREN)
            self.state = 156
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 153
                self.primitive_type()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 154
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.LBRACK]:
                self.state = 155
                self.array_declaration()
                pass
            elif token in [MiniGoParser.LBRACE]:
                pass
            else:
                pass
            self.state = 158
            self.match(MiniGoParser.LBRACE)
            self.state = 159
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LPAREN)
            else:
                return self.getToken(MiniGoParser.LPAREN, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RPAREN)
            else:
                return self.getToken(MiniGoParser.RPAREN, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def prameters_list(self):
            return self.getTypedRuleContext(MiniGoParser.Prameters_listContext,0)


        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def array_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Array_declarationContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_declared" ):
                return visitor.visitMethod_declared(self)
            else:
                return visitor.visitChildren(self)




    def method_declared(self):

        localctx = MiniGoParser.Method_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_method_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(MiniGoParser.FUNC)
            self.state = 162
            self.match(MiniGoParser.LPAREN)

            self.state = 163
            self.match(MiniGoParser.ID)
            self.state = 164
            self.match(MiniGoParser.ID)
            self.state = 166
            self.match(MiniGoParser.RPAREN)
            self.state = 167
            self.match(MiniGoParser.ID)
            self.state = 168
            self.match(MiniGoParser.LPAREN)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 169
                self.prameters_list()


            self.state = 172
            self.match(MiniGoParser.RPAREN)
            self.state = 176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 173
                self.primitive_type()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 174
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.LBRACK]:
                self.state = 175
                self.array_declaration()
                pass
            elif token in [MiniGoParser.LBRACE]:
                pass
            else:
                pass
            self.state = 178
            self.match(MiniGoParser.LBRACE)
            self.state = 179
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.IgnoreContext,i)


        def prameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.PrameterContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.PrameterContext,i)


        def SEMICOL(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOL)
            else:
                return self.getToken(MiniGoParser.SEMICOL, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_declared" ):
                return visitor.visitStruct_declared(self)
            else:
                return visitor.visitChildren(self)




    def struct_declared(self):

        localctx = MiniGoParser.Struct_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_struct_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(MiniGoParser.TYPE)
            self.state = 182
            self.match(MiniGoParser.ID)
            self.state = 183
            self.match(MiniGoParser.STRUCT)
            self.state = 184
            self.match(MiniGoParser.LBRACE)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NEWLINE:
                self.state = 185
                self.ignore()
                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.ID:
                self.state = 191
                self.prameter()
                self.state = 192
                self.match(MiniGoParser.SEMICOL)
                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.NEWLINE:
                    self.state = 193
                    self.ignore()
                    self.state = 198
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 204
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.IgnoreContext,i)


        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LPAREN)
            else:
                return self.getToken(MiniGoParser.LPAREN, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RPAREN)
            else:
                return self.getToken(MiniGoParser.RPAREN, i)

        def prameters_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Prameters_listContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Prameters_listContext,i)


        def primitive_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Primitive_typeContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,i)


        def array_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Array_declarationContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Array_declarationContext,i)


        def SEMICOL(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOL)
            else:
                return self.getToken(MiniGoParser.SEMICOL, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_declared" ):
                return visitor.visitInterface_declared(self)
            else:
                return visitor.visitChildren(self)




    def interface_declared(self):

        localctx = MiniGoParser.Interface_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_interface_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(MiniGoParser.TYPE)
            self.state = 207
            self.match(MiniGoParser.ID)
            self.state = 208
            self.match(MiniGoParser.INTERFACE)
            self.state = 209
            self.match(MiniGoParser.LBRACE)
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NEWLINE:
                self.state = 210
                self.ignore()
                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.ID:
                self.state = 216
                self.match(MiniGoParser.ID)
                self.state = 217
                self.match(MiniGoParser.LPAREN)
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ID:
                    self.state = 218
                    self.prameters_list()


                self.state = 221
                self.match(MiniGoParser.RPAREN)
                self.state = 225
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 222
                    self.primitive_type()

                elif la_ == 2:
                    self.state = 223
                    self.match(MiniGoParser.ID)

                elif la_ == 3:
                    self.state = 224
                    self.array_declaration()


                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.SEMICOL:
                    self.state = 227
                    self.match(MiniGoParser.SEMICOL)


                self.state = 233
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.NEWLINE:
                    self.state = 230
                    self.ignore()
                    self.state = 235
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 241
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prameters_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prameter(self):
            return self.getTypedRuleContext(MiniGoParser.PrameterContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def prameters_list(self):
            return self.getTypedRuleContext(MiniGoParser.Prameters_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_prameters_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrameters_list" ):
                return visitor.visitPrameters_list(self)
            else:
                return visitor.visitChildren(self)




    def prameters_list(self):

        localctx = MiniGoParser.Prameters_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_prameters_list)
        try:
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.prameter()
                self.state = 244
                self.match(MiniGoParser.COMMA)
                self.state = 245
                self.prameters_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.prameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_declarationContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def array_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Array_declarationContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_prameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrameter" ):
                return visitor.visitPrameter(self)
            else:
                return visitor.visitChildren(self)




    def prameter(self):

        localctx = MiniGoParser.PrameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_prameter)
        try:
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.primitive_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                self.match(MiniGoParser.ID)
                self.state = 252
                self.array_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 253
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_literal)
        try:
            self.state = 263
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.match(MiniGoParser.INT_LIT)
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 258
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.TRUE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 259
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 260
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [MiniGoParser.LBRACE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 261
                self.array_literal()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 7)
                self.state = 262
                self.struct_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def params(self):
            return self.getTypedRuleContext(MiniGoParser.ParamsContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = MiniGoParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(MiniGoParser.LBRACE)
            self.state = 266
            self.params()
            self.state = 267
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_elements(self):
            return self.getTypedRuleContext(MiniGoParser.List_elementsContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal" ):
                return visitor.visitStruct_literal(self)
            else:
                return visitor.visitChildren(self)




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_struct_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(MiniGoParser.ID)
            self.state = 270
            self.match(MiniGoParser.LBRACE)
            self.state = 271
            self.list_elements()
            self.state = 272
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def params(self):
            return self.getTypedRuleContext(MiniGoParser.ParamsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expression" ):
                return visitor.visitList_expression(self)
            else:
                return visitor.visitChildren(self)




    def list_expression(self):

        localctx = MiniGoParser.List_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_list_expression)
        try:
            self.state = 276
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LPAREN, MiniGoParser.LBRACE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                self.params()
                pass
            elif token in [MiniGoParser.RPAREN]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def params(self):
            return self.getTypedRuleContext(MiniGoParser.ParamsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = MiniGoParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_params)
        try:
            self.state = 283
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.expression(0)
                self.state = 279
                self.match(MiniGoParser.COMMA)
                self.state = 280
                self.params()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_elementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COLON)
            else:
                return self.getToken(MiniGoParser.COLON, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_list_elements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_elements" ):
                return visitor.visitList_elements(self)
            else:
                return visitor.visitChildren(self)




    def list_elements(self):

        localctx = MiniGoParser.List_elementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_list_elements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(MiniGoParser.ID)
            self.state = 286
            self.match(MiniGoParser.COLON)
            self.state = 287
            self.expression(0)
            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 289
                self.match(MiniGoParser.COMMA)
                self.state = 290
                self.match(MiniGoParser.ID)
                self.state = 291
                self.match(MiniGoParser.COLON)
                self.state = 292
                self.expression(0)
                self.state = 297
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.expression1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 306
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 301
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 302
                    self.match(MiniGoParser.OR)
                    self.state = 303
                    self.expression1(0) 
                self.state = 308
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression2Context,0)


        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)



    def expression1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expression1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 317
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 312
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 313
                    self.match(MiniGoParser.AND)
                    self.state = 314
                    self.expression2(0) 
                self.state = 319
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression2Context,0)


        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def DIFF(self):
            return self.getToken(MiniGoParser.DIFF, 0)

        def LT(self):
            return self.getToken(MiniGoParser.LT, 0)

        def LTE(self):
            return self.getToken(MiniGoParser.LTE, 0)

        def RT(self):
            return self.getToken(MiniGoParser.RT, 0)

        def RTE(self):
            return self.getToken(MiniGoParser.RTE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression2" ):
                return visitor.visitExpression2(self)
            else:
                return visitor.visitChildren(self)



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_expression2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 343
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 341
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 323
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 324
                        self.match(MiniGoParser.EQUAL)
                        self.state = 325
                        self.expression3(0)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 326
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 327
                        self.match(MiniGoParser.DIFF)
                        self.state = 328
                        self.expression3(0)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 329
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 330
                        self.match(MiniGoParser.LT)
                        self.state = 331
                        self.expression3(0)
                        pass

                    elif la_ == 4:
                        localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 332
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 333
                        self.match(MiniGoParser.LTE)
                        self.state = 334
                        self.expression3(0)
                        pass

                    elif la_ == 5:
                        localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 335
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 336
                        self.match(MiniGoParser.RT)
                        self.state = 337
                        self.expression3(0)
                        pass

                    elif la_ == 6:
                        localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 338
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 339
                        self.match(MiniGoParser.RTE)
                        self.state = 340
                        self.expression3(0)
                        pass

             
                self.state = 345
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression3Context,0)


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression3" ):
                return visitor.visitExpression3(self)
            else:
                return visitor.visitChildren(self)



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_expression3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 357
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 355
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                        self.state = 349
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 350
                        self.match(MiniGoParser.ADD)
                        self.state = 351
                        self.expression4(0)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                        self.state = 352
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 353
                        self.match(MiniGoParser.SUB)
                        self.state = 354
                        self.expression4(0)
                        pass

             
                self.state = 359
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression4Context,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression4" ):
                return visitor.visitExpression4(self)
            else:
                return visitor.visitChildren(self)



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_expression4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 374
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 372
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                        self.state = 363
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 364
                        self.match(MiniGoParser.MUL)
                        self.state = 365
                        self.expression5()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                        self.state = 366
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 367
                        self.match(MiniGoParser.DIV)
                        self.state = 368
                        self.expression5()
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                        self.state = 369
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 370
                        self.match(MiniGoParser.MOD)
                        self.state = 371
                        self.expression5()
                        pass

             
                self.state = 376
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)




    def expression5(self):

        localctx = MiniGoParser.Expression5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expression5)
        try:
            self.state = 382
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 377
                self.match(MiniGoParser.NOT)
                self.state = 378
                self.expression5()
                pass
            elif token in [MiniGoParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 379
                self.match(MiniGoParser.SUB)
                self.state = 380
                self.expression5()
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LPAREN, MiniGoParser.LBRACE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 381
                self.expression6(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression7(self):
            return self.getTypedRuleContext(MiniGoParser.Expression7Context,0)


        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def params(self):
            return self.getTypedRuleContext(MiniGoParser.ParamsContext,0)


        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def POINTTO(self):
            return self.getToken(MiniGoParser.POINTTO, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression6" ):
                return visitor.visitExpression6(self)
            else:
                return visitor.visitChildren(self)



    def expression6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_expression6, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.expression7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 403
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 401
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 387
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 392
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==MiniGoParser.LPAREN:
                            self.state = 388
                            self.match(MiniGoParser.LPAREN)
                            self.state = 389
                            self.list_expression()
                            self.state = 390
                            self.match(MiniGoParser.RPAREN)


                        self.state = 394
                        self.match(MiniGoParser.LBRACK)

                        self.state = 395
                        self.params()
                        self.state = 396
                        self.match(MiniGoParser.RBRACK)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 398
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 399
                        self.match(MiniGoParser.POINTTO)
                        self.state = 400
                        self.expression7()
                        pass

             
                self.state = 405
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression7" ):
                return visitor.visitExpression7(self)
            else:
                return visitor.visitChildren(self)




    def expression7(self):

        localctx = MiniGoParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_expression7)
        try:
            self.state = 413
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 406
                self.match(MiniGoParser.LPAREN)
                self.state = 407
                self.expression(0)
                self.state = 408
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 410
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 411
                self.literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 412
                self.func_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = MiniGoParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.match(MiniGoParser.ID)
            self.state = 416
            self.match(MiniGoParser.LPAREN)
            self.state = 417
            self.list_expression()
            self.state = 418
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IgnoreContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_ignore

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgnore" ):
                return visitor.visitIgnore(self)
            else:
                return visitor.visitChildren(self)




    def ignore(self):

        localctx = MiniGoParser.IgnoreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_ignore)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 420
                    self.match(MiniGoParser.NEWLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 423 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[23] = self.expression_sempred
        self._predicates[24] = self.expression1_sempred
        self._predicates[25] = self.expression2_sempred
        self._predicates[26] = self.expression3_sempred
        self._predicates[27] = self.expression4_sempred
        self._predicates[29] = self.expression6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression1_sempred(self, localctx:Expression1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 2)
         

    def expression6_sempred(self, localctx:Expression6Context, predIndex:int):
            if predIndex == 13:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 2)
         




