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
        buf.write("\u0294\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\3\2\7\2h")
        buf.write("\n\2\f\2\16\2k\13\2\3\2\3\2\3\2\7\2p\n\2\f\2\16\2s\13")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3}\n\3\3\4\3\4\5")
        buf.write("\4\u0081\n\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\5\6\u008f\n\6\3\6\3\6\6\6\u0093\n\6\r\6\16\6\u0094")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u009d\n\6\5\6\u009f\n\6\5")
        buf.write("\6\u00a1\n\6\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\7\n\u00b1\n\n\f\n\16\n\u00b4\13\n\3\13")
        buf.write("\3\13\3\13\5\13\u00b9\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\5\f\u00c2\n\f\3\f\3\f\3\r\3\r\3\r\3\r\5\r\u00ca\n\r\3")
        buf.write("\r\3\r\3\r\3\r\5\r\u00d0\n\r\3\r\3\r\7\r\u00d4\n\r\f\r")
        buf.write("\16\r\u00d7\13\r\3\r\5\r\u00da\n\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00e7\n\16\3\16")
        buf.write("\3\16\3\16\3\16\5\16\u00ed\n\16\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\5\17\u00f7\n\17\3\17\3\17\3\17\5\17")
        buf.write("\u00fc\n\17\7\17\u00fe\n\17\f\17\16\17\u0101\13\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\5\20\u010a\n\20\3\20\3")
        buf.write("\20\3\20\5\20\u010f\n\20\3\20\3\20\3\20\3\20\5\20\u0115")
        buf.write("\n\20\3\20\5\20\u0118\n\20\3\20\5\20\u011b\n\20\7\20\u011d")
        buf.write("\n\20\f\20\16\20\u0120\13\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\5\21\u0129\n\21\3\22\3\22\3\22\3\22\5\22\u012f")
        buf.write("\n\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u0138\n")
        buf.write("\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\5\26\u0146\n\26\3\27\3\27\3\27\3\27\3\27\5")
        buf.write("\27\u014d\n\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\7\30\u0157\n\30\f\30\16\30\u015a\13\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\7\31\u0162\n\31\f\31\16\31\u0165\13\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\7\32\u016d\n\32\f\32\16")
        buf.write("\32\u0170\13\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\7\33\u0187\n\33\f\33\16\33\u018a\13\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\7\34\u0195\n")
        buf.write("\34\f\34\16\34\u0198\13\34\3\35\3\35\3\35\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\7\35\u01a6\n\35\f\35")
        buf.write("\16\35\u01a9\13\35\3\36\3\36\3\36\3\36\3\36\5\36\u01b0")
        buf.write("\n\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\7\37\u01bd\n\37\f\37\16\37\u01c0\13\37\3 \3 \3 ")
        buf.write("\3 \3 \3 \3 \5 \u01c9\n \3!\3!\3!\3!\3!\3\"\6\"\u01d1")
        buf.write("\n\"\r\"\16\"\u01d2\3#\3#\5#\u01d7\n#\3$\3$\3$\3$\5$\u01dd")
        buf.write("\n$\3%\3%\3%\3%\3%\3%\3%\3%\5%\u01e7\n%\3&\5&\u01ea\n")
        buf.write("&\3&\3&\5&\u01ee\n&\3&\5&\u01f1\n&\3\'\5\'\u01f4\n\'\3")
        buf.write("\'\3\'\5\'\u01f8\n\'\3\'\5\'\u01fb\n\'\3\'\3\'\3\'\7\'")
        buf.write("\u0200\n\'\f\'\16\'\u0203\13\'\3\'\3\'\3\'\3\'\5\'\u0209")
        buf.write("\n\'\3(\3(\3)\5)\u020e\n)\3)\3)\3)\3)\3)\3)\3)\3)\3)\5")
        buf.write(")\u0219\n)\3)\3)\3)\5)\u021e\n)\3*\5*\u0221\n*\3*\3*\3")
        buf.write("*\3*\3*\3*\3*\3*\3*\3*\3*\3*\5*\u022f\n*\3+\3+\3+\5+\u0234")
        buf.write("\n+\3,\5,\u0237\n,\3,\3,\3,\5,\u023c\n,\3,\3,\3-\5-\u0241")
        buf.write("\n-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u0250\n")
        buf.write("-\3-\3-\3.\5.\u0255\n.\3.\3.\3.\3.\3.\3.\3.\3.\5.\u025f")
        buf.write("\n.\3.\3.\3/\5/\u0264\n/\3/\3/\3/\5/\u0269\n/\3\60\5\60")
        buf.write("\u026c\n\60\3\60\3\60\3\60\5\60\u0271\n\60\3\61\5\61\u0274")
        buf.write("\n\61\3\61\3\61\5\61\u0278\n\61\3\61\5\61\u027b\n\61\3")
        buf.write("\61\5\61\u027e\n\61\3\62\5\62\u0281\n\62\3\62\3\62\3\62")
        buf.write("\5\62\u0286\n\62\3\63\3\63\7\63\u028a\n\63\f\63\16\63")
        buf.write("\u028d\13\63\3\63\5\63\u0290\n\63\3\63\3\63\3\63\2\b\60")
        buf.write("\62\64\668<\64\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bd\2\5\3\2")
        buf.write("\13\16\4\2\27\27\67\67\4\2&+..\2\u02d3\2i\3\2\2\2\4|\3")
        buf.write("\2\2\2\6\u0080\3\2\2\2\b\u0084\3\2\2\2\n\u0089\3\2\2\2")
        buf.write("\f\u00a2\3\2\2\2\16\u00a4\3\2\2\2\20\u00a7\3\2\2\2\22")
        buf.write("\u00aa\3\2\2\2\24\u00b5\3\2\2\2\26\u00ba\3\2\2\2\30\u00c5")
        buf.write("\3\2\2\2\32\u00dd\3\2\2\2\34\u00f1\3\2\2\2\36\u0104\3")
        buf.write("\2\2\2 \u0128\3\2\2\2\"\u012e\3\2\2\2$\u0137\3\2\2\2&")
        buf.write("\u0139\3\2\2\2(\u013e\3\2\2\2*\u0145\3\2\2\2,\u014c\3")
        buf.write("\2\2\2.\u014e\3\2\2\2\60\u015b\3\2\2\2\62\u0166\3\2\2")
        buf.write("\2\64\u0171\3\2\2\2\66\u018b\3\2\2\28\u0199\3\2\2\2:\u01af")
        buf.write("\3\2\2\2<\u01b1\3\2\2\2>\u01c8\3\2\2\2@\u01ca\3\2\2\2")
        buf.write("B\u01d0\3\2\2\2D\u01d4\3\2\2\2F\u01dc\3\2\2\2H\u01e6\3")
        buf.write("\2\2\2J\u01e9\3\2\2\2L\u01f3\3\2\2\2N\u020a\3\2\2\2P\u020d")
        buf.write("\3\2\2\2R\u022e\3\2\2\2T\u0233\3\2\2\2V\u0236\3\2\2\2")
        buf.write("X\u0240\3\2\2\2Z\u0254\3\2\2\2\\\u0263\3\2\2\2^\u026b")
        buf.write("\3\2\2\2`\u0273\3\2\2\2b\u0280\3\2\2\2d\u0287\3\2\2\2")
        buf.write("fh\7<\2\2gf\3\2\2\2hk\3\2\2\2ig\3\2\2\2ij\3\2\2\2jl\3")
        buf.write("\2\2\2ki\3\2\2\2lq\5\4\3\2mp\5\4\3\2np\7<\2\2om\3\2\2")
        buf.write("\2on\3\2\2\2ps\3\2\2\2qo\3\2\2\2qr\3\2\2\2rt\3\2\2\2s")
        buf.write("q\3\2\2\2tu\7\2\2\3u\3\3\2\2\2v}\5\6\4\2w}\5\26\f\2x}")
        buf.write("\5\30\r\2y}\5\32\16\2z}\5\34\17\2{}\5\36\20\2|v\3\2\2")
        buf.write("\2|w\3\2\2\2|x\3\2\2\2|y\3\2\2\2|z\3\2\2\2|{\3\2\2\2}")
        buf.write("\5\3\2\2\2~\u0081\5\b\5\2\177\u0081\5\n\6\2\u0080~\3\2")
        buf.write("\2\2\u0080\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0083")
        buf.write("\7\66\2\2\u0083\7\3\2\2\2\u0084\u0085\7\20\2\2\u0085\u0086")
        buf.write("\7\67\2\2\u0086\u0087\7&\2\2\u0087\u0088\5\60\31\2\u0088")
        buf.write("\t\3\2\2\2\u0089\u008e\7\20\2\2\u008a\u008f\5\16\b\2\u008b")
        buf.write("\u008c\7\67\2\2\u008c\u008f\5\24\13\2\u008d\u008f\5\20")
        buf.write("\t\2\u008e\u008a\3\2\2\2\u008e\u008b\3\2\2\2\u008e\u008d")
        buf.write("\3\2\2\2\u008f\u00a0\3\2\2\2\u0090\u009e\7&\2\2\u0091")
        buf.write("\u0093\5\60\31\2\u0092\u0091\3\2\2\2\u0093\u0094\3\2\2")
        buf.write("\2\u0094\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u009f")
        buf.write("\3\2\2\2\u0096\u009d\5&\24\2\u0097\u0098\7\67\2\2\u0098")
        buf.write("\u0099\7\61\2\2\u0099\u009a\5*\26\2\u009a\u009b\7\62\2")
        buf.write("\2\u009b\u009d\3\2\2\2\u009c\u0096\3\2\2\2\u009c\u0097")
        buf.write("\3\2\2\2\u009d\u009f\3\2\2\2\u009e\u0092\3\2\2\2\u009e")
        buf.write("\u009c\3\2\2\2\u009f\u00a1\3\2\2\2\u00a0\u0090\3\2\2\2")
        buf.write("\u00a0\u00a1\3\2\2\2\u00a1\13\3\2\2\2\u00a2\u00a3\t\2")
        buf.write("\2\2\u00a3\r\3\2\2\2\u00a4\u00a5\7\67\2\2\u00a5\u00a6")
        buf.write("\5\f\7\2\u00a6\17\3\2\2\2\u00a7\u00a8\7\67\2\2\u00a8\u00a9")
        buf.write("\t\3\2\2\u00a9\21\3\2\2\2\u00aa\u00ab\7\63\2\2\u00ab\u00ac")
        buf.write("\78\2\2\u00ac\u00b2\7\64\2\2\u00ad\u00ae\7\63\2\2\u00ae")
        buf.write("\u00af\78\2\2\u00af\u00b1\7\64\2\2\u00b0\u00ad\3\2\2\2")
        buf.write("\u00b1\u00b4\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b3\3")
        buf.write("\2\2\2\u00b3\23\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b5\u00b8")
        buf.write("\5\22\n\2\u00b6\u00b9\5\f\7\2\u00b7\u00b9\7\67\2\2\u00b8")
        buf.write("\u00b6\3\2\2\2\u00b8\u00b7\3\2\2\2\u00b9\25\3\2\2\2\u00ba")
        buf.write("\u00bb\7\17\2\2\u00bb\u00bc\7\67\2\2\u00bc\u00c1\7&\2")
        buf.write("\2\u00bd\u00c2\5\60\31\2\u00be\u00bf\5\24\13\2\u00bf\u00c0")
        buf.write("\5\60\31\2\u00c0\u00c2\3\2\2\2\u00c1\u00bd\3\2\2\2\u00c1")
        buf.write("\u00be\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c4\7\66\2")
        buf.write("\2\u00c4\27\3\2\2\2\u00c5\u00c6\7\7\2\2\u00c6\u00c7\7")
        buf.write("\67\2\2\u00c7\u00c9\7/\2\2\u00c8\u00ca\5 \21\2\u00c9\u00c8")
        buf.write("\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb")
        buf.write("\u00cf\7\60\2\2\u00cc\u00d0\5\f\7\2\u00cd\u00d0\7\67\2")
        buf.write("\2\u00ce\u00d0\5\24\13\2\u00cf\u00cc\3\2\2\2\u00cf\u00cd")
        buf.write("\3\2\2\2\u00cf\u00ce\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0")
        buf.write("\u00d1\3\2\2\2\u00d1\u00d5\7\61\2\2\u00d2\u00d4\5F$\2")
        buf.write("\u00d3\u00d2\3\2\2\2\u00d4\u00d7\3\2\2\2\u00d5\u00d3\3")
        buf.write("\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d9\3\2\2\2\u00d7\u00d5")
        buf.write("\3\2\2\2\u00d8\u00da\5D#\2\u00d9\u00d8\3\2\2\2\u00d9\u00da")
        buf.write("\3\2\2\2\u00da\u00db\3\2\2\2\u00db\u00dc\7\62\2\2\u00dc")
        buf.write("\31\3\2\2\2\u00dd\u00de\7\7\2\2\u00de\u00df\7/\2\2\u00df")
        buf.write("\u00e0\7\67\2\2\u00e0\u00e1\7\67\2\2\u00e1\u00e2\3\2\2")
        buf.write("\2\u00e2\u00e3\7\60\2\2\u00e3\u00e4\7\67\2\2\u00e4\u00e6")
        buf.write("\7/\2\2\u00e5\u00e7\5 \21\2\u00e6\u00e5\3\2\2\2\u00e6")
        buf.write("\u00e7\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00ec\7\60\2")
        buf.write("\2\u00e9\u00ed\5\f\7\2\u00ea\u00ed\7\67\2\2\u00eb\u00ed")
        buf.write("\5\24\13\2\u00ec\u00e9\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec")
        buf.write("\u00eb\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00ee\3\2\2\2")
        buf.write("\u00ee\u00ef\7\61\2\2\u00ef\u00f0\7\62\2\2\u00f0\33\3")
        buf.write("\2\2\2\u00f1\u00f2\7\b\2\2\u00f2\u00f3\7\67\2\2\u00f3")
        buf.write("\u00f4\7\t\2\2\u00f4\u00f6\7\61\2\2\u00f5\u00f7\5D#\2")
        buf.write("\u00f6\u00f5\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00ff\3")
        buf.write("\2\2\2\u00f8\u00f9\5\"\22\2\u00f9\u00fb\7\66\2\2\u00fa")
        buf.write("\u00fc\5D#\2\u00fb\u00fa\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc")
        buf.write("\u00fe\3\2\2\2\u00fd\u00f8\3\2\2\2\u00fe\u0101\3\2\2\2")
        buf.write("\u00ff\u00fd\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0102\3")
        buf.write("\2\2\2\u0101\u00ff\3\2\2\2\u0102\u0103\7\62\2\2\u0103")
        buf.write("\35\3\2\2\2\u0104\u0105\7\b\2\2\u0105\u0106\7\67\2\2\u0106")
        buf.write("\u0107\7\n\2\2\u0107\u0109\7\61\2\2\u0108\u010a\5D#\2")
        buf.write("\u0109\u0108\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u011e\3")
        buf.write("\2\2\2\u010b\u010c\7\67\2\2\u010c\u010e\7/\2\2\u010d\u010f")
        buf.write("\5 \21\2\u010e\u010d\3\2\2\2\u010e\u010f\3\2\2\2\u010f")
        buf.write("\u0110\3\2\2\2\u0110\u0114\7\60\2\2\u0111\u0115\5\f\7")
        buf.write("\2\u0112\u0115\7\67\2\2\u0113\u0115\5\24\13\2\u0114\u0111")
        buf.write("\3\2\2\2\u0114\u0112\3\2\2\2\u0114\u0113\3\2\2\2\u0114")
        buf.write("\u0115\3\2\2\2\u0115\u0117\3\2\2\2\u0116\u0118\7\66\2")
        buf.write("\2\u0117\u0116\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u011a")
        buf.write("\3\2\2\2\u0119\u011b\5D#\2\u011a\u0119\3\2\2\2\u011a\u011b")
        buf.write("\3\2\2\2\u011b\u011d\3\2\2\2\u011c\u010b\3\2\2\2\u011d")
        buf.write("\u0120\3\2\2\2\u011e\u011c\3\2\2\2\u011e\u011f\3\2\2\2")
        buf.write("\u011f\u0121\3\2\2\2\u0120\u011e\3\2\2\2\u0121\u0122\7")
        buf.write("\62\2\2\u0122\37\3\2\2\2\u0123\u0124\5\"\22\2\u0124\u0125")
        buf.write("\7\65\2\2\u0125\u0126\5 \21\2\u0126\u0129\3\2\2\2\u0127")
        buf.write("\u0129\5\"\22\2\u0128\u0123\3\2\2\2\u0128\u0127\3\2\2")
        buf.write("\2\u0129!\3\2\2\2\u012a\u012f\5\16\b\2\u012b\u012c\7\67")
        buf.write("\2\2\u012c\u012f\5\24\13\2\u012d\u012f\7\67\2\2\u012e")
        buf.write("\u012a\3\2\2\2\u012e\u012b\3\2\2\2\u012e\u012d\3\2\2\2")
        buf.write("\u012f#\3\2\2\2\u0130\u0138\78\2\2\u0131\u0138\79\2\2")
        buf.write("\u0132\u0138\7:\2\2\u0133\u0138\7\25\2\2\u0134\u0138\7")
        buf.write("\26\2\2\u0135\u0138\5&\24\2\u0136\u0138\5(\25\2\u0137")
        buf.write("\u0130\3\2\2\2\u0137\u0131\3\2\2\2\u0137\u0132\3\2\2\2")
        buf.write("\u0137\u0133\3\2\2\2\u0137\u0134\3\2\2\2\u0137\u0135\3")
        buf.write("\2\2\2\u0137\u0136\3\2\2\2\u0138%\3\2\2\2\u0139\u013a")
        buf.write("\5\24\13\2\u013a\u013b\7\61\2\2\u013b\u013c\5,\27\2\u013c")
        buf.write("\u013d\7\62\2\2\u013d\'\3\2\2\2\u013e\u013f\7\67\2\2\u013f")
        buf.write("\u0140\7\61\2\2\u0140\u0141\5.\30\2\u0141\u0142\7\62\2")
        buf.write("\2\u0142)\3\2\2\2\u0143\u0146\5,\27\2\u0144\u0146\3\2")
        buf.write("\2\2\u0145\u0143\3\2\2\2\u0145\u0144\3\2\2\2\u0146+\3")
        buf.write("\2\2\2\u0147\u0148\5\60\31\2\u0148\u0149\7\65\2\2\u0149")
        buf.write("\u014a\5,\27\2\u014a\u014d\3\2\2\2\u014b\u014d\5\60\31")
        buf.write("\2\u014c\u0147\3\2\2\2\u014c\u014b\3\2\2\2\u014d-\3\2")
        buf.write("\2\2\u014e\u014f\7\67\2\2\u014f\u0150\7-\2\2\u0150\u0151")
        buf.write("\5\60\31\2\u0151\u0158\3\2\2\2\u0152\u0153\7\65\2\2\u0153")
        buf.write("\u0154\7\67\2\2\u0154\u0155\7-\2\2\u0155\u0157\5\60\31")
        buf.write("\2\u0156\u0152\3\2\2\2\u0157\u015a\3\2\2\2\u0158\u0156")
        buf.write("\3\2\2\2\u0158\u0159\3\2\2\2\u0159/\3\2\2\2\u015a\u0158")
        buf.write("\3\2\2\2\u015b\u015c\b\31\1\2\u015c\u015d\5\62\32\2\u015d")
        buf.write("\u0163\3\2\2\2\u015e\u015f\f\4\2\2\u015f\u0160\7$\2\2")
        buf.write("\u0160\u0162\5\62\32\2\u0161\u015e\3\2\2\2\u0162\u0165")
        buf.write("\3\2\2\2\u0163\u0161\3\2\2\2\u0163\u0164\3\2\2\2\u0164")
        buf.write("\61\3\2\2\2\u0165\u0163\3\2\2\2\u0166\u0167\b\32\1\2\u0167")
        buf.write("\u0168\5\64\33\2\u0168\u016e\3\2\2\2\u0169\u016a\f\4\2")
        buf.write("\2\u016a\u016b\7#\2\2\u016b\u016d\5\64\33\2\u016c\u0169")
        buf.write("\3\2\2\2\u016d\u0170\3\2\2\2\u016e\u016c\3\2\2\2\u016e")
        buf.write("\u016f\3\2\2\2\u016f\63\3\2\2\2\u0170\u016e\3\2\2\2\u0171")
        buf.write("\u0172\b\33\1\2\u0172\u0173\5\66\34\2\u0173\u0188\3\2")
        buf.write("\2\2\u0174\u0175\f\t\2\2\u0175\u0176\7\35\2\2\u0176\u0187")
        buf.write("\5\66\34\2\u0177\u0178\f\b\2\2\u0178\u0179\7\36\2\2\u0179")
        buf.write("\u0187\5\66\34\2\u017a\u017b\f\7\2\2\u017b\u017c\7\37")
        buf.write("\2\2\u017c\u0187\5\66\34\2\u017d\u017e\f\6\2\2\u017e\u017f")
        buf.write("\7 \2\2\u017f\u0187\5\66\34\2\u0180\u0181\f\5\2\2\u0181")
        buf.write("\u0182\7!\2\2\u0182\u0187\5\66\34\2\u0183\u0184\f\4\2")
        buf.write("\2\u0184\u0185\7\"\2\2\u0185\u0187\5\66\34\2\u0186\u0174")
        buf.write("\3\2\2\2\u0186\u0177\3\2\2\2\u0186\u017a\3\2\2\2\u0186")
        buf.write("\u017d\3\2\2\2\u0186\u0180\3\2\2\2\u0186\u0183\3\2\2\2")
        buf.write("\u0187\u018a\3\2\2\2\u0188\u0186\3\2\2\2\u0188\u0189\3")
        buf.write("\2\2\2\u0189\65\3\2\2\2\u018a\u0188\3\2\2\2\u018b\u018c")
        buf.write("\b\34\1\2\u018c\u018d\58\35\2\u018d\u0196\3\2\2\2\u018e")
        buf.write("\u018f\f\5\2\2\u018f\u0190\7\30\2\2\u0190\u0195\58\35")
        buf.write("\2\u0191\u0192\f\4\2\2\u0192\u0193\7\31\2\2\u0193\u0195")
        buf.write("\58\35\2\u0194\u018e\3\2\2\2\u0194\u0191\3\2\2\2\u0195")
        buf.write("\u0198\3\2\2\2\u0196\u0194\3\2\2\2\u0196\u0197\3\2\2\2")
        buf.write("\u0197\67\3\2\2\2\u0198\u0196\3\2\2\2\u0199\u019a\b\35")
        buf.write("\1\2\u019a\u019b\5:\36\2\u019b\u01a7\3\2\2\2\u019c\u019d")
        buf.write("\f\6\2\2\u019d\u019e\7\32\2\2\u019e\u01a6\5:\36\2\u019f")
        buf.write("\u01a0\f\5\2\2\u01a0\u01a1\7\33\2\2\u01a1\u01a6\5:\36")
        buf.write("\2\u01a2\u01a3\f\4\2\2\u01a3\u01a4\7\34\2\2\u01a4\u01a6")
        buf.write("\5:\36\2\u01a5\u019c\3\2\2\2\u01a5\u019f\3\2\2\2\u01a5")
        buf.write("\u01a2\3\2\2\2\u01a6\u01a9\3\2\2\2\u01a7\u01a5\3\2\2\2")
        buf.write("\u01a7\u01a8\3\2\2\2\u01a89\3\2\2\2\u01a9\u01a7\3\2\2")
        buf.write("\2\u01aa\u01ab\7%\2\2\u01ab\u01b0\5:\36\2\u01ac\u01ad")
        buf.write("\7\31\2\2\u01ad\u01b0\5:\36\2\u01ae\u01b0\5<\37\2\u01af")
        buf.write("\u01aa\3\2\2\2\u01af\u01ac\3\2\2\2\u01af\u01ae\3\2\2\2")
        buf.write("\u01b0;\3\2\2\2\u01b1\u01b2\b\37\1\2\u01b2\u01b3\5> \2")
        buf.write("\u01b3\u01be\3\2\2\2\u01b4\u01b5\f\5\2\2\u01b5\u01b6\7")
        buf.write("\63\2\2\u01b6\u01b7\5\60\31\2\u01b7\u01b8\7\64\2\2\u01b8")
        buf.write("\u01bd\3\2\2\2\u01b9\u01ba\f\4\2\2\u01ba\u01bb\7,\2\2")
        buf.write("\u01bb\u01bd\5> \2\u01bc\u01b4\3\2\2\2\u01bc\u01b9\3\2")
        buf.write("\2\2\u01bd\u01c0\3\2\2\2\u01be\u01bc\3\2\2\2\u01be\u01bf")
        buf.write("\3\2\2\2\u01bf=\3\2\2\2\u01c0\u01be\3\2\2\2\u01c1\u01c2")
        buf.write("\7/\2\2\u01c2\u01c3\5\60\31\2\u01c3\u01c4\7\60\2\2\u01c4")
        buf.write("\u01c9\3\2\2\2\u01c5\u01c9\7\67\2\2\u01c6\u01c9\5$\23")
        buf.write("\2\u01c7\u01c9\5@!\2\u01c8\u01c1\3\2\2\2\u01c8\u01c5\3")
        buf.write("\2\2\2\u01c8\u01c6\3\2\2\2\u01c8\u01c7\3\2\2\2\u01c9?")
        buf.write("\3\2\2\2\u01ca\u01cb\7\67\2\2\u01cb\u01cc\7/\2\2\u01cc")
        buf.write("\u01cd\5*\26\2\u01cd\u01ce\7\60\2\2\u01ceA\3\2\2\2\u01cf")
        buf.write("\u01d1\7<\2\2\u01d0\u01cf\3\2\2\2\u01d1\u01d2\3\2\2\2")
        buf.write("\u01d2\u01d0\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3C\3\2\2")
        buf.write("\2\u01d4\u01d6\5B\"\2\u01d5\u01d7\5D#\2\u01d6\u01d5\3")
        buf.write("\2\2\2\u01d6\u01d7\3\2\2\2\u01d7E\3\2\2\2\u01d8\u01d9")
        buf.write("\5H%\2\u01d9\u01da\5F$\2\u01da\u01dd\3\2\2\2\u01db\u01dd")
        buf.write("\5H%\2\u01dc\u01d8\3\2\2\2\u01dc\u01db\3\2\2\2\u01ddG")
        buf.write("\3\2\2\2\u01de\u01e7\5J&\2\u01df\u01e7\5L\'\2\u01e0\u01e7")
        buf.write("\5P)\2\u01e1\u01e7\5T+\2\u01e2\u01e7\5\\/\2\u01e3\u01e7")
        buf.write("\5^\60\2\u01e4\u01e7\5`\61\2\u01e5\u01e7\5b\62\2\u01e6")
        buf.write("\u01de\3\2\2\2\u01e6\u01df\3\2\2\2\u01e6\u01e0\3\2\2\2")
        buf.write("\u01e6\u01e1\3\2\2\2\u01e6\u01e2\3\2\2\2\u01e6\u01e3\3")
        buf.write("\2\2\2\u01e6\u01e4\3\2\2\2\u01e6\u01e5\3\2\2\2\u01e7I")
        buf.write("\3\2\2\2\u01e8\u01ea\5D#\2\u01e9\u01e8\3\2\2\2\u01e9\u01ea")
        buf.write("\3\2\2\2\u01ea\u01ed\3\2\2\2\u01eb\u01ee\5\6\4\2\u01ec")
        buf.write("\u01ee\5\26\f\2\u01ed\u01eb\3\2\2\2\u01ed\u01ec\3\2\2")
        buf.write("\2\u01ee\u01f0\3\2\2\2\u01ef\u01f1\5D#\2\u01f0\u01ef\3")
        buf.write("\2\2\2\u01f0\u01f1\3\2\2\2\u01f1K\3\2\2\2\u01f2\u01f4")
        buf.write("\5D#\2\u01f3\u01f2\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4\u01f5")
        buf.write("\3\2\2\2\u01f5\u01f7\7\67\2\2\u01f6\u01f8\7,\2\2\u01f7")
        buf.write("\u01f6\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8\u01fa\3\2\2\2")
        buf.write("\u01f9\u01fb\7\67\2\2\u01fa\u01f9\3\2\2\2\u01fa\u01fb")
        buf.write("\3\2\2\2\u01fb\u0201\3\2\2\2\u01fc\u01fd\7\63\2\2\u01fd")
        buf.write("\u01fe\78\2\2\u01fe\u0200\7\64\2\2\u01ff\u01fc\3\2\2\2")
        buf.write("\u0200\u0203\3\2\2\2\u0201\u01ff\3\2\2\2\u0201\u0202\3")
        buf.write("\2\2\2\u0202\u0204\3\2\2\2\u0203\u0201\3\2\2\2\u0204\u0205")
        buf.write("\5N(\2\u0205\u0206\5\60\31\2\u0206\u0208\7\66\2\2\u0207")
        buf.write("\u0209\5D#\2\u0208\u0207\3\2\2\2\u0208\u0209\3\2\2\2\u0209")
        buf.write("M\3\2\2\2\u020a\u020b\t\4\2\2\u020bO\3\2\2\2\u020c\u020e")
        buf.write("\5D#\2\u020d\u020c\3\2\2\2\u020d\u020e\3\2\2\2\u020e\u020f")
        buf.write("\3\2\2\2\u020f\u0210\7\3\2\2\u0210\u0211\7/\2\2\u0211")
        buf.write("\u0212\5\60\31\2\u0212\u0213\7\60\2\2\u0213\u0214\5d\63")
        buf.write("\2\u0214\u021d\5R*\2\u0215\u0216\7\4\2\2\u0216\u0218\7")
        buf.write("\61\2\2\u0217\u0219\5D#\2\u0218\u0217\3\2\2\2\u0218\u0219")
        buf.write("\3\2\2\2\u0219\u021a\3\2\2\2\u021a\u021b\5H%\2\u021b\u021c")
        buf.write("\7\62\2\2\u021c\u021e\3\2\2\2\u021d\u0215\3\2\2\2\u021d")
        buf.write("\u021e\3\2\2\2\u021eQ\3\2\2\2\u021f\u0221\5D#\2\u0220")
        buf.write("\u021f\3\2\2\2\u0220\u0221\3\2\2\2\u0221\u0222\3\2\2\2")
        buf.write("\u0222\u0223\7\4\2\2\u0223\u0224\7\3\2\2\u0224\u0225\7")
        buf.write("/\2\2\u0225\u0226\5\60\31\2\u0226\u0227\7\60\2\2\u0227")
        buf.write("\u0228\7\61\2\2\u0228\u0229\5H%\2\u0229\u022a\7\62\2\2")
        buf.write("\u022a\u022b\3\2\2\2\u022b\u022c\5R*\2\u022c\u022f\3\2")
        buf.write("\2\2\u022d\u022f\3\2\2\2\u022e\u0220\3\2\2\2\u022e\u022d")
        buf.write("\3\2\2\2\u022fS\3\2\2\2\u0230\u0234\5V,\2\u0231\u0234")
        buf.write("\5X-\2\u0232\u0234\5Z.\2\u0233\u0230\3\2\2\2\u0233\u0231")
        buf.write("\3\2\2\2\u0233\u0232\3\2\2\2\u0234U\3\2\2\2\u0235\u0237")
        buf.write("\5D#\2\u0236\u0235\3\2\2\2\u0236\u0237\3\2\2\2\u0237\u0238")
        buf.write("\3\2\2\2\u0238\u0239\7\5\2\2\u0239\u023b\5\60\31\2\u023a")
        buf.write("\u023c\5D#\2\u023b\u023a\3\2\2\2\u023b\u023c\3\2\2\2\u023c")
        buf.write("\u023d\3\2\2\2\u023d\u023e\5d\63\2\u023eW\3\2\2\2\u023f")
        buf.write("\u0241\5D#\2\u0240\u023f\3\2\2\2\u0240\u0241\3\2\2\2\u0241")
        buf.write("\u0242\3\2\2\2\u0242\u0243\7\5\2\2\u0243\u0244\7\67\2")
        buf.write("\2\u0244\u0245\5N(\2\u0245\u0246\78\2\2\u0246\u0247\3")
        buf.write("\2\2\2\u0247\u0248\7\66\2\2\u0248\u0249\5\60\31\2\u0249")
        buf.write("\u024a\7\66\2\2\u024a\u024b\7\67\2\2\u024b\u024c\5N(\2")
        buf.write("\u024c\u024d\78\2\2\u024d\u024f\3\2\2\2\u024e\u0250\5")
        buf.write("D#\2\u024f\u024e\3\2\2\2\u024f\u0250\3\2\2\2\u0250\u0251")
        buf.write("\3\2\2\2\u0251\u0252\5d\63\2\u0252Y\3\2\2\2\u0253\u0255")
        buf.write("\5D#\2\u0254\u0253\3\2\2\2\u0254\u0255\3\2\2\2\u0255\u0256")
        buf.write("\3\2\2\2\u0256\u0257\7\5\2\2\u0257\u0258\7\67\2\2\u0258")
        buf.write("\u0259\7\65\2\2\u0259\u025a\7\67\2\2\u025a\u025b\7.\2")
        buf.write("\2\u025b\u025c\7\23\2\2\u025c\u025e\7\67\2\2\u025d\u025f")
        buf.write("\5D#\2\u025e\u025d\3\2\2\2\u025e\u025f\3\2\2\2\u025f\u0260")
        buf.write("\3\2\2\2\u0260\u0261\5d\63\2\u0261[\3\2\2\2\u0262\u0264")
        buf.write("\5D#\2\u0263\u0262\3\2\2\2\u0263\u0264\3\2\2\2\u0264\u0265")
        buf.write("\3\2\2\2\u0265\u0266\7\22\2\2\u0266\u0268\7\66\2\2\u0267")
        buf.write("\u0269\5D#\2\u0268\u0267\3\2\2\2\u0268\u0269\3\2\2\2\u0269")
        buf.write("]\3\2\2\2\u026a\u026c\5D#\2\u026b\u026a\3\2\2\2\u026b")
        buf.write("\u026c\3\2\2\2\u026c\u026d\3\2\2\2\u026d\u026e\7\21\2")
        buf.write("\2\u026e\u0270\7\66\2\2\u026f\u0271\5D#\2\u0270\u026f")
        buf.write("\3\2\2\2\u0270\u0271\3\2\2\2\u0271_\3\2\2\2\u0272\u0274")
        buf.write("\5D#\2\u0273\u0272\3\2\2\2\u0273\u0274\3\2\2\2\u0274\u0275")
        buf.write("\3\2\2\2\u0275\u0277\7\6\2\2\u0276\u0278\5\60\31\2\u0277")
        buf.write("\u0276\3\2\2\2\u0277\u0278\3\2\2\2\u0278\u027a\3\2\2\2")
        buf.write("\u0279\u027b\7\66\2\2\u027a\u0279\3\2\2\2\u027a\u027b")
        buf.write("\3\2\2\2\u027b\u027d\3\2\2\2\u027c\u027e\5D#\2\u027d\u027c")
        buf.write("\3\2\2\2\u027d\u027e\3\2\2\2\u027ea\3\2\2\2\u027f\u0281")
        buf.write("\5D#\2\u0280\u027f\3\2\2\2\u0280\u0281\3\2\2\2\u0281\u0282")
        buf.write("\3\2\2\2\u0282\u0283\5\60\31\2\u0283\u0285\7\66\2\2\u0284")
        buf.write("\u0286\5D#\2\u0285\u0284\3\2\2\2\u0285\u0286\3\2\2\2\u0286")
        buf.write("c\3\2\2\2\u0287\u028b\7\61\2\2\u0288\u028a\5H%\2\u0289")
        buf.write("\u0288\3\2\2\2\u028a\u028d\3\2\2\2\u028b\u0289\3\2\2\2")
        buf.write("\u028b\u028c\3\2\2\2\u028c\u028f\3\2\2\2\u028d\u028b\3")
        buf.write("\2\2\2\u028e\u0290\5D#\2\u028f\u028e\3\2\2\2\u028f\u0290")
        buf.write("\3\2\2\2\u0290\u0291\3\2\2\2\u0291\u0292\7\62\2\2\u0292")
        buf.write("e\3\2\2\2Tioq|\u0080\u008e\u0094\u009c\u009e\u00a0\u00b2")
        buf.write("\u00b8\u00c1\u00c9\u00cf\u00d5\u00d9\u00e6\u00ec\u00f6")
        buf.write("\u00fb\u00ff\u0109\u010e\u0114\u0117\u011a\u011e\u0128")
        buf.write("\u012e\u0137\u0145\u014c\u0158\u0163\u016e\u0186\u0188")
        buf.write("\u0194\u0196\u01a5\u01a7\u01af\u01bc\u01be\u01c8\u01d2")
        buf.write("\u01d6\u01dc\u01e6\u01e9\u01ed\u01f0\u01f3\u01f7\u01fa")
        buf.write("\u0201\u0208\u020d\u0218\u021d\u0220\u022e\u0233\u0236")
        buf.write("\u023b\u0240\u024f\u0254\u025e\u0263\u0268\u026b\u0270")
        buf.write("\u0273\u0277\u027a\u027d\u0280\u0285\u028b\u028f")
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
    RULE_ignore_recursive = 33
    RULE_list_statement = 34
    RULE_statement = 35
    RULE_declared_statement = 36
    RULE_assign_statement = 37
    RULE_assignment_operator = 38
    RULE_if_statement = 39
    RULE_list_elif = 40
    RULE_for_statement = 41
    RULE_basic_for = 42
    RULE_init_condition_update_for = 43
    RULE_range_for = 44
    RULE_break_statement = 45
    RULE_continue_statement = 46
    RULE_return_statement = 47
    RULE_call_statement = 48
    RULE_lbrace_code_block = 49

    ruleNames =  [ "program", "declared", "variables_declared", "implicit_var", 
                   "keyword_var", "primitive_type", "primitive_declaration", 
                   "interface_type", "dimension_list", "array_declaration", 
                   "constants_declared", "function_declared", "method_declared", 
                   "struct_declared", "interface_declared", "prameters_list", 
                   "prameter", "literal", "array_literal", "struct_literal", 
                   "list_expression", "params", "list_elements", "expression", 
                   "expression1", "expression2", "expression3", "expression4", 
                   "expression5", "expression6", "expression7", "func_call", 
                   "ignore", "ignore_recursive", "list_statement", "statement", 
                   "declared_statement", "assign_statement", "assignment_operator", 
                   "if_statement", "list_elif", "for_statement", "basic_for", 
                   "init_condition_update_for", "range_for", "break_statement", 
                   "continue_statement", "return_statement", "call_statement", 
                   "lbrace_code_block" ]

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
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NEWLINE:
                self.state = 100
                self.match(MiniGoParser.NEWLINE)
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 106
            self.declared()
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.NEWLINE))) != 0):
                self.state = 109
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR]:
                    self.state = 107
                    self.declared()
                    pass
                elif token in [MiniGoParser.NEWLINE]:
                    self.state = 108
                    self.match(MiniGoParser.NEWLINE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 114
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
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.variables_declared()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.constants_declared()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 118
                self.function_declared()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 119
                self.method_declared()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 120
                self.struct_declared()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 121
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
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 124
                self.implicit_var()
                pass

            elif la_ == 2:
                self.state = 125
                self.keyword_var()
                pass


            self.state = 128
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
            self.state = 130
            self.match(MiniGoParser.VAR)
            self.state = 131
            self.match(MiniGoParser.ID)
            self.state = 132
            self.match(MiniGoParser.ASSIGN)
            self.state = 133
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


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def array_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Array_declarationContext,0)


        def interface_type(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_typeContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


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
            self.state = 135
            self.match(MiniGoParser.VAR)
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 136
                self.primitive_declaration()
                pass

            elif la_ == 2:
                self.state = 137
                self.match(MiniGoParser.ID)
                self.state = 138
                self.array_declaration()
                pass

            elif la_ == 3:
                self.state = 139
                self.interface_type()
                pass


            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ASSIGN:
                self.state = 142
                self.match(MiniGoParser.ASSIGN)
                self.state = 156
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 144 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 143
                        self.expression(0)
                        self.state = 146 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0)):
                            break

                    pass

                elif la_ == 2:
                    self.state = 154
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.LBRACK]:
                        self.state = 148
                        self.array_literal()
                        pass
                    elif token in [MiniGoParser.ID]:
                        self.state = 149
                        self.match(MiniGoParser.ID)
                        self.state = 150
                        self.match(MiniGoParser.LBRACE)
                        self.state = 151
                        self.list_expression()
                        self.state = 152
                        self.match(MiniGoParser.RBRACE)
                        pass
                    else:
                        raise NoViableAltException(self)

                    pass




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
            self.state = 160
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
            self.state = 162
            self.match(MiniGoParser.ID)
            self.state = 163
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(MiniGoParser.ID)
            self.state = 166
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.STR or _la==MiniGoParser.ID):
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
            self.state = 168
            self.match(MiniGoParser.LBRACK)
            self.state = 169
            self.match(MiniGoParser.INT_LIT)
            self.state = 170
            self.match(MiniGoParser.RBRACK)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.LBRACK:
                self.state = 171
                self.match(MiniGoParser.LBRACK)
                self.state = 172
                self.match(MiniGoParser.INT_LIT)
                self.state = 173
                self.match(MiniGoParser.RBRACK)
                self.state = 178
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
            self.state = 179
            self.dimension_list()
            self.state = 182
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 180
                self.primitive_type()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 181
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
            self.state = 184
            self.match(MiniGoParser.CONST)
            self.state = 185
            self.match(MiniGoParser.ID)
            self.state = 186
            self.match(MiniGoParser.ASSIGN)
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 187
                self.expression(0)
                pass

            elif la_ == 2:
                self.state = 188
                self.array_declaration()
                self.state = 189
                self.expression(0)
                pass


            self.state = 193
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


        def list_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.List_statementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.List_statementContext,i)


        def ignore_recursive(self):
            return self.getTypedRuleContext(MiniGoParser.Ignore_recursiveContext,0)


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
            self.state = 195
            self.match(MiniGoParser.FUNC)
            self.state = 196
            self.match(MiniGoParser.ID)
            self.state = 197
            self.match(MiniGoParser.LPAREN)
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 198
                self.prameters_list()


            self.state = 201
            self.match(MiniGoParser.RPAREN)
            self.state = 205
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 202
                self.primitive_type()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 203
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.LBRACK]:
                self.state = 204
                self.array_declaration()
                pass
            elif token in [MiniGoParser.LBRACE]:
                pass
            else:
                pass
            self.state = 207
            self.match(MiniGoParser.LBRACE)
            self.state = 211
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 208
                    self.list_statement() 
                self.state = 213
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 214
                self.ignore_recursive()


            self.state = 217
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
            self.state = 219
            self.match(MiniGoParser.FUNC)
            self.state = 220
            self.match(MiniGoParser.LPAREN)

            self.state = 221
            self.match(MiniGoParser.ID)
            self.state = 222
            self.match(MiniGoParser.ID)
            self.state = 224
            self.match(MiniGoParser.RPAREN)
            self.state = 225
            self.match(MiniGoParser.ID)
            self.state = 226
            self.match(MiniGoParser.LPAREN)
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 227
                self.prameters_list()


            self.state = 230
            self.match(MiniGoParser.RPAREN)
            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 231
                self.primitive_type()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 232
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.LBRACK]:
                self.state = 233
                self.array_declaration()
                pass
            elif token in [MiniGoParser.LBRACE]:
                pass
            else:
                pass
            self.state = 236
            self.match(MiniGoParser.LBRACE)
            self.state = 237
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

        def ignore_recursive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Ignore_recursiveContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Ignore_recursiveContext,i)


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
            self.state = 239
            self.match(MiniGoParser.TYPE)
            self.state = 240
            self.match(MiniGoParser.ID)
            self.state = 241
            self.match(MiniGoParser.STRUCT)
            self.state = 242
            self.match(MiniGoParser.LBRACE)
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 243
                self.ignore_recursive()


            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.ID:
                self.state = 246
                self.prameter()
                self.state = 247
                self.match(MiniGoParser.SEMICOL)
                self.state = 249
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.NEWLINE:
                    self.state = 248
                    self.ignore_recursive()


                self.state = 255
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 256
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

        def ignore_recursive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Ignore_recursiveContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Ignore_recursiveContext,i)


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
            self.state = 258
            self.match(MiniGoParser.TYPE)
            self.state = 259
            self.match(MiniGoParser.ID)
            self.state = 260
            self.match(MiniGoParser.INTERFACE)
            self.state = 261
            self.match(MiniGoParser.LBRACE)
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 262
                self.ignore_recursive()


            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.ID:
                self.state = 265
                self.match(MiniGoParser.ID)
                self.state = 266
                self.match(MiniGoParser.LPAREN)
                self.state = 268
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ID:
                    self.state = 267
                    self.prameters_list()


                self.state = 270
                self.match(MiniGoParser.RPAREN)
                self.state = 274
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 271
                    self.primitive_type()

                elif la_ == 2:
                    self.state = 272
                    self.match(MiniGoParser.ID)

                elif la_ == 3:
                    self.state = 273
                    self.array_declaration()


                self.state = 277
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.SEMICOL:
                    self.state = 276
                    self.match(MiniGoParser.SEMICOL)


                self.state = 280
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.NEWLINE:
                    self.state = 279
                    self.ignore_recursive()


                self.state = 286
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 287
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
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                self.prameter()
                self.state = 290
                self.match(MiniGoParser.COMMA)
                self.state = 291
                self.prameters_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
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
            self.state = 300
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.primitive_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
                self.match(MiniGoParser.ID)
                self.state = 298
                self.array_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 299
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
            self.state = 309
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                self.match(MiniGoParser.INT_LIT)
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 304
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.TRUE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 305
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 306
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [MiniGoParser.LBRACK]:
                self.enterOuterAlt(localctx, 6)
                self.state = 307
                self.array_literal()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 7)
                self.state = 308
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

        def array_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Array_declarationContext,0)


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
            self.state = 311
            self.array_declaration()
            self.state = 312
            self.match(MiniGoParser.LBRACE)
            self.state = 313
            self.params()
            self.state = 314
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
            self.state = 316
            self.match(MiniGoParser.ID)
            self.state = 317
            self.match(MiniGoParser.LBRACE)
            self.state = 318
            self.list_elements()
            self.state = 319
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
            self.state = 323
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LPAREN, MiniGoParser.LBRACK, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 321
                self.params()
                pass
            elif token in [MiniGoParser.RPAREN, MiniGoParser.RBRACE]:
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
            self.state = 330
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self.expression(0)
                self.state = 326
                self.match(MiniGoParser.COMMA)
                self.state = 327
                self.params()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 329
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
            self.state = 332
            self.match(MiniGoParser.ID)
            self.state = 333
            self.match(MiniGoParser.COLON)
            self.state = 334
            self.expression(0)
            self.state = 342
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 336
                self.match(MiniGoParser.COMMA)
                self.state = 337
                self.match(MiniGoParser.ID)
                self.state = 338
                self.match(MiniGoParser.COLON)
                self.state = 339
                self.expression(0)
                self.state = 344
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
            self.state = 346
            self.expression1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 353
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 348
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 349
                    self.match(MiniGoParser.OR)
                    self.state = 350
                    self.expression1(0) 
                self.state = 355
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

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
            self.state = 357
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 364
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 359
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 360
                    self.match(MiniGoParser.AND)
                    self.state = 361
                    self.expression2(0) 
                self.state = 366
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

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
            self.state = 368
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 390
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 388
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 370
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 371
                        self.match(MiniGoParser.EQUAL)
                        self.state = 372
                        self.expression3(0)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 373
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 374
                        self.match(MiniGoParser.DIFF)
                        self.state = 375
                        self.expression3(0)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 376
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 377
                        self.match(MiniGoParser.LT)
                        self.state = 378
                        self.expression3(0)
                        pass

                    elif la_ == 4:
                        localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 379
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 380
                        self.match(MiniGoParser.LTE)
                        self.state = 381
                        self.expression3(0)
                        pass

                    elif la_ == 5:
                        localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 382
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 383
                        self.match(MiniGoParser.RT)
                        self.state = 384
                        self.expression3(0)
                        pass

                    elif la_ == 6:
                        localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 385
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 386
                        self.match(MiniGoParser.RTE)
                        self.state = 387
                        self.expression3(0)
                        pass

             
                self.state = 392
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

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
            self.state = 394
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 404
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 402
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                        self.state = 396
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 397
                        self.match(MiniGoParser.ADD)
                        self.state = 398
                        self.expression4(0)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                        self.state = 399
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 400
                        self.match(MiniGoParser.SUB)
                        self.state = 401
                        self.expression4(0)
                        pass

             
                self.state = 406
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

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
            self.state = 408
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 421
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 419
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                        self.state = 410
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 411
                        self.match(MiniGoParser.MUL)
                        self.state = 412
                        self.expression5()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                        self.state = 413
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 414
                        self.match(MiniGoParser.DIV)
                        self.state = 415
                        self.expression5()
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                        self.state = 416
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 417
                        self.match(MiniGoParser.MOD)
                        self.state = 418
                        self.expression5()
                        pass

             
                self.state = 423
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

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
            self.state = 429
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 424
                self.match(MiniGoParser.NOT)
                self.state = 425
                self.expression5()
                pass
            elif token in [MiniGoParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 426
                self.match(MiniGoParser.SUB)
                self.state = 427
                self.expression5()
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LPAREN, MiniGoParser.LBRACK, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 428
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

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.expression7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 444
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 442
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 434
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 435
                        self.match(MiniGoParser.LBRACK)
                        self.state = 436
                        self.expression(0)
                        self.state = 437
                        self.match(MiniGoParser.RBRACK)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 439
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 440
                        self.match(MiniGoParser.POINTTO)
                        self.state = 441
                        self.expression7()
                        pass

             
                self.state = 446
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

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
            self.state = 454
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 447
                self.match(MiniGoParser.LPAREN)
                self.state = 448
                self.expression(0)
                self.state = 449
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 451
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 452
                self.literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 453
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
            self.state = 456
            self.match(MiniGoParser.ID)
            self.state = 457
            self.match(MiniGoParser.LPAREN)
            self.state = 458
            self.list_expression()
            self.state = 459
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
            self.state = 462 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 461
                    self.match(MiniGoParser.NEWLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 464 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ignore_recursiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def ignore_recursive(self):
            return self.getTypedRuleContext(MiniGoParser.Ignore_recursiveContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_ignore_recursive

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgnore_recursive" ):
                return visitor.visitIgnore_recursive(self)
            else:
                return visitor.visitChildren(self)




    def ignore_recursive(self):

        localctx = MiniGoParser.Ignore_recursiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_ignore_recursive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self.ignore()
            self.state = 468
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.state = 467
                self.ignore_recursive()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_statement" ):
                return visitor.visitList_statement(self)
            else:
                return visitor.visitChildren(self)




    def list_statement(self):

        localctx = MiniGoParser.List_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_list_statement)
        try:
            self.state = 474
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 470
                self.statement()
                self.state = 471
                self.list_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 473
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declared_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Declared_statementContext,0)


        def assign_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(MiniGoParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(MiniGoParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Return_statementContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Call_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.state = 476
                self.declared_statement()
                pass

            elif la_ == 2:
                self.state = 477
                self.assign_statement()
                pass

            elif la_ == 3:
                self.state = 478
                self.if_statement()
                pass

            elif la_ == 4:
                self.state = 479
                self.for_statement()
                pass

            elif la_ == 5:
                self.state = 480
                self.break_statement()
                pass

            elif la_ == 6:
                self.state = 481
                self.continue_statement()
                pass

            elif la_ == 7:
                self.state = 482
                self.return_statement()
                pass

            elif la_ == 8:
                self.state = 483
                self.call_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declared_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variables_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Variables_declaredContext,0)


        def constants_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Constants_declaredContext,0)


        def ignore_recursive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Ignore_recursiveContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Ignore_recursiveContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declared_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclared_statement" ):
                return visitor.visitDeclared_statement(self)
            else:
                return visitor.visitChildren(self)




    def declared_statement(self):

        localctx = MiniGoParser.Declared_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_declared_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 486
                self.ignore_recursive()


            self.state = 491
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.VAR]:
                self.state = 489
                self.variables_declared()
                pass
            elif token in [MiniGoParser.CONST]:
                self.state = 490
                self.constants_declared()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 494
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.state = 493
                self.ignore_recursive()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_operatorContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def SEMICOL(self):
            return self.getToken(MiniGoParser.SEMICOL, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def ignore_recursive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Ignore_recursiveContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Ignore_recursiveContext,i)


        def POINTTO(self):
            return self.getToken(MiniGoParser.POINTTO, 0)

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
            return MiniGoParser.RULE_assign_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_statement" ):
                return visitor.visitAssign_statement(self)
            else:
                return visitor.visitChildren(self)




    def assign_statement(self):

        localctx = MiniGoParser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_assign_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 496
                self.ignore_recursive()


            self.state = 499
            self.match(MiniGoParser.ID)
            self.state = 501
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.POINTTO:
                self.state = 500
                self.match(MiniGoParser.POINTTO)


            self.state = 504
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 503
                self.match(MiniGoParser.ID)


            self.state = 511
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.LBRACK:
                self.state = 506
                self.match(MiniGoParser.LBRACK)
                self.state = 507
                self.match(MiniGoParser.INT_LIT)
                self.state = 508
                self.match(MiniGoParser.RBRACK)
                self.state = 513
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 514
            self.assignment_operator()
            self.state = 515
            self.expression(0)
            self.state = 516
            self.match(MiniGoParser.SEMICOL)
            self.state = 518
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.state = 517
                self.ignore_recursive()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def ASSIGNADD(self):
            return self.getToken(MiniGoParser.ASSIGNADD, 0)

        def ASSIGNSUB(self):
            return self.getToken(MiniGoParser.ASSIGNSUB, 0)

        def ASSIGNMUL(self):
            return self.getToken(MiniGoParser.ASSIGNMUL, 0)

        def ASSIGNDIV(self):
            return self.getToken(MiniGoParser.ASSIGNDIV, 0)

        def ASSIGNMOD(self):
            return self.getToken(MiniGoParser.ASSIGNMOD, 0)

        def ASSIGNNIT(self):
            return self.getToken(MiniGoParser.ASSIGNNIT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_operator" ):
                return visitor.visitAssignment_operator(self)
            else:
                return visitor.visitChildren(self)




    def assignment_operator(self):

        localctx = MiniGoParser.Assignment_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_assignment_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGN) | (1 << MiniGoParser.ASSIGNADD) | (1 << MiniGoParser.ASSIGNSUB) | (1 << MiniGoParser.ASSIGNMUL) | (1 << MiniGoParser.ASSIGNDIV) | (1 << MiniGoParser.ASSIGNMOD) | (1 << MiniGoParser.ASSIGNNIT))) != 0)):
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


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def list_elif(self):
            return self.getTypedRuleContext(MiniGoParser.List_elifContext,0)


        def lbrace_code_block(self):
            return self.getTypedRuleContext(MiniGoParser.Lbrace_code_blockContext,0)


        def ignore_recursive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Ignore_recursiveContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Ignore_recursiveContext,i)


        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = MiniGoParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 522
                self.ignore_recursive()


            self.state = 525
            self.match(MiniGoParser.IF)
            self.state = 526
            self.match(MiniGoParser.LPAREN)
            self.state = 527
            self.expression(0)
            self.state = 528
            self.match(MiniGoParser.RPAREN)

            self.state = 529
            self.lbrace_code_block()
            self.state = 530
            self.list_elif()
            self.state = 539
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 531
                self.match(MiniGoParser.ELSE)

                self.state = 532
                self.match(MiniGoParser.LBRACE)
                self.state = 534
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
                if la_ == 1:
                    self.state = 533
                    self.ignore_recursive()


                self.state = 536
                self.statement()
                self.state = 537
                self.match(MiniGoParser.RBRACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_elifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def list_elif(self):
            return self.getTypedRuleContext(MiniGoParser.List_elifContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def ignore_recursive(self):
            return self.getTypedRuleContext(MiniGoParser.Ignore_recursiveContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_elif

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_elif" ):
                return visitor.visitList_elif(self)
            else:
                return visitor.visitChildren(self)




    def list_elif(self):

        localctx = MiniGoParser.List_elifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_list_elif)
        self._la = 0 # Token type
        try:
            self.state = 556
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 542
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.NEWLINE:
                    self.state = 541
                    self.ignore_recursive()


                self.state = 544
                self.match(MiniGoParser.ELSE)
                self.state = 545
                self.match(MiniGoParser.IF)
                self.state = 546
                self.match(MiniGoParser.LPAREN)
                self.state = 547
                self.expression(0)
                self.state = 548
                self.match(MiniGoParser.RPAREN)

                self.state = 549
                self.match(MiniGoParser.LBRACE)
                self.state = 550
                self.statement()
                self.state = 551
                self.match(MiniGoParser.RBRACE)
                self.state = 553
                self.list_elif()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basic_for(self):
            return self.getTypedRuleContext(MiniGoParser.Basic_forContext,0)


        def init_condition_update_for(self):
            return self.getTypedRuleContext(MiniGoParser.Init_condition_update_forContext,0)


        def range_for(self):
            return self.getTypedRuleContext(MiniGoParser.Range_forContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = MiniGoParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_for_statement)
        try:
            self.state = 561
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 558
                self.basic_for()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 559
                self.init_condition_update_for()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 560
                self.range_for()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def lbrace_code_block(self):
            return self.getTypedRuleContext(MiniGoParser.Lbrace_code_blockContext,0)


        def ignore_recursive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Ignore_recursiveContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Ignore_recursiveContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_basic_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasic_for" ):
                return visitor.visitBasic_for(self)
            else:
                return visitor.visitChildren(self)




    def basic_for(self):

        localctx = MiniGoParser.Basic_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_basic_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 564
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 563
                self.ignore_recursive()


            self.state = 566
            self.match(MiniGoParser.FOR)
            self.state = 567
            self.expression(0)
            self.state = 569
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 568
                self.ignore_recursive()


            self.state = 571
            self.lbrace_code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_condition_update_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def SEMICOL(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOL)
            else:
                return self.getToken(MiniGoParser.SEMICOL, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def assignment_operator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Assignment_operatorContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Assignment_operatorContext,i)


        def INT_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.INT_LIT)
            else:
                return self.getToken(MiniGoParser.INT_LIT, i)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def lbrace_code_block(self):
            return self.getTypedRuleContext(MiniGoParser.Lbrace_code_blockContext,0)


        def ignore_recursive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Ignore_recursiveContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Ignore_recursiveContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_init_condition_update_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_condition_update_for" ):
                return visitor.visitInit_condition_update_for(self)
            else:
                return visitor.visitChildren(self)




    def init_condition_update_for(self):

        localctx = MiniGoParser.Init_condition_update_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_init_condition_update_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 574
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 573
                self.ignore_recursive()


            self.state = 576
            self.match(MiniGoParser.FOR)

            self.state = 577
            self.match(MiniGoParser.ID)
            self.state = 578
            self.assignment_operator()
            self.state = 579
            self.match(MiniGoParser.INT_LIT)
            self.state = 581
            self.match(MiniGoParser.SEMICOL)

            self.state = 582
            self.expression(0)
            self.state = 583
            self.match(MiniGoParser.SEMICOL)

            self.state = 584
            self.match(MiniGoParser.ID)
            self.state = 585
            self.assignment_operator()
            self.state = 586
            self.match(MiniGoParser.INT_LIT)
            self.state = 589
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 588
                self.ignore_recursive()


            self.state = 591
            self.lbrace_code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Range_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def ASSIGNNIT(self):
            return self.getToken(MiniGoParser.ASSIGNNIT, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def lbrace_code_block(self):
            return self.getTypedRuleContext(MiniGoParser.Lbrace_code_blockContext,0)


        def ignore_recursive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Ignore_recursiveContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Ignore_recursiveContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_range_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange_for" ):
                return visitor.visitRange_for(self)
            else:
                return visitor.visitChildren(self)




    def range_for(self):

        localctx = MiniGoParser.Range_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_range_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 594
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 593
                self.ignore_recursive()


            self.state = 596
            self.match(MiniGoParser.FOR)
            self.state = 597
            self.match(MiniGoParser.ID)
            self.state = 598
            self.match(MiniGoParser.COMMA)
            self.state = 599
            self.match(MiniGoParser.ID)
            self.state = 600
            self.match(MiniGoParser.ASSIGNNIT)
            self.state = 601
            self.match(MiniGoParser.RANGE)
            self.state = 602
            self.match(MiniGoParser.ID)
            self.state = 604
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 603
                self.ignore_recursive()


            self.state = 606
            self.lbrace_code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def SEMICOL(self):
            return self.getToken(MiniGoParser.SEMICOL, 0)

        def ignore_recursive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Ignore_recursiveContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Ignore_recursiveContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = MiniGoParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_break_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 609
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 608
                self.ignore_recursive()


            self.state = 611
            self.match(MiniGoParser.BREAK)
            self.state = 612
            self.match(MiniGoParser.SEMICOL)
            self.state = 614
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
            if la_ == 1:
                self.state = 613
                self.ignore_recursive()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def SEMICOL(self):
            return self.getToken(MiniGoParser.SEMICOL, 0)

        def ignore_recursive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Ignore_recursiveContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Ignore_recursiveContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = MiniGoParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_continue_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 617
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 616
                self.ignore_recursive()


            self.state = 619
            self.match(MiniGoParser.CONTINUE)
            self.state = 620
            self.match(MiniGoParser.SEMICOL)
            self.state = 622
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,73,self._ctx)
            if la_ == 1:
                self.state = 621
                self.ignore_recursive()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def ignore_recursive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Ignore_recursiveContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Ignore_recursiveContext,i)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def SEMICOL(self):
            return self.getToken(MiniGoParser.SEMICOL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = MiniGoParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 625
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 624
                self.ignore_recursive()


            self.state = 627
            self.match(MiniGoParser.RETURN)
            self.state = 629
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,75,self._ctx)
            if la_ == 1:
                self.state = 628
                self.expression(0)


            self.state = 632
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMICOL:
                self.state = 631
                self.match(MiniGoParser.SEMICOL)


            self.state = 635
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,77,self._ctx)
            if la_ == 1:
                self.state = 634
                self.ignore_recursive()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def SEMICOL(self):
            return self.getToken(MiniGoParser.SEMICOL, 0)

        def ignore_recursive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Ignore_recursiveContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Ignore_recursiveContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = MiniGoParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_call_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 638
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 637
                self.ignore_recursive()


            self.state = 640
            self.expression(0)
            self.state = 641
            self.match(MiniGoParser.SEMICOL)
            self.state = 643
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,79,self._ctx)
            if la_ == 1:
                self.state = 642
                self.ignore_recursive()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lbrace_code_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def ignore_recursive(self):
            return self.getTypedRuleContext(MiniGoParser.Ignore_recursiveContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_lbrace_code_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLbrace_code_block" ):
                return visitor.visitLbrace_code_block(self)
            else:
                return visitor.visitChildren(self)




    def lbrace_code_block(self):

        localctx = MiniGoParser.Lbrace_code_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_lbrace_code_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 645
            self.match(MiniGoParser.LBRACE)

            self.state = 649
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,80,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 646
                    self.statement() 
                self.state = 651
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,80,self._ctx)

            self.state = 653
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 652
                self.ignore_recursive()


            self.state = 655
            self.match(MiniGoParser.RBRACE)
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
         




