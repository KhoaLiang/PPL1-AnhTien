# Generated from main/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declared.
    def visitDeclared(self, ctx:MiniGoParser.DeclaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#variables_declared.
    def visitVariables_declared(self, ctx:MiniGoParser.Variables_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#implicit_var.
    def visitImplicit_var(self, ctx:MiniGoParser.Implicit_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#keyword_var.
    def visitKeyword_var(self, ctx:MiniGoParser.Keyword_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primitive_type.
    def visitPrimitive_type(self, ctx:MiniGoParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primitive_declaration.
    def visitPrimitive_declaration(self, ctx:MiniGoParser.Primitive_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_type.
    def visitInterface_type(self, ctx:MiniGoParser.Interface_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dimension_list.
    def visitDimension_list(self, ctx:MiniGoParser.Dimension_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_declaration.
    def visitArray_declaration(self, ctx:MiniGoParser.Array_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#constants_declared.
    def visitConstants_declared(self, ctx:MiniGoParser.Constants_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#function_declared.
    def visitFunction_declared(self, ctx:MiniGoParser.Function_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#prameters_list.
    def visitPrameters_list(self, ctx:MiniGoParser.Prameters_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#prameter.
    def visitPrameter(self, ctx:MiniGoParser.PrameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_literal.
    def visitArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_literal.
    def visitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_expression.
    def visitList_expression(self, ctx:MiniGoParser.List_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#params.
    def visitParams(self, ctx:MiniGoParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_elements.
    def visitList_elements(self, ctx:MiniGoParser.List_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression.
    def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression1.
    def visitExpression1(self, ctx:MiniGoParser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression2.
    def visitExpression2(self, ctx:MiniGoParser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression3.
    def visitExpression3(self, ctx:MiniGoParser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression4.
    def visitExpression4(self, ctx:MiniGoParser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression5.
    def visitExpression5(self, ctx:MiniGoParser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression6.
    def visitExpression6(self, ctx:MiniGoParser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression7.
    def visitExpression7(self, ctx:MiniGoParser.Expression7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_call.
    def visitFunc_call(self, ctx:MiniGoParser.Func_callContext):
        return self.visitChildren(ctx)



del MiniGoParser