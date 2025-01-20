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


    # Visit a parse tree produced by MiniGoParser#method_declared.
    def visitMethod_declared(self, ctx:MiniGoParser.Method_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_declared.
    def visitStruct_declared(self, ctx:MiniGoParser.Struct_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_declared.
    def visitInterface_declared(self, ctx:MiniGoParser.Interface_declaredContext):
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


    # Visit a parse tree produced by MiniGoParser#ignore.
    def visitIgnore(self, ctx:MiniGoParser.IgnoreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_statement.
    def visitList_statement(self, ctx:MiniGoParser.List_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declared_statement.
    def visitDeclared_statement(self, ctx:MiniGoParser.Declared_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_statement.
    def visitAssign_statement(self, ctx:MiniGoParser.Assign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignment_operator.
    def visitAssignment_operator(self, ctx:MiniGoParser.Assignment_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_statement.
    def visitIf_statement(self, ctx:MiniGoParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_elif.
    def visitList_elif(self, ctx:MiniGoParser.List_elifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_statement.
    def visitFor_statement(self, ctx:MiniGoParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#basic_for.
    def visitBasic_for(self, ctx:MiniGoParser.Basic_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#init_condition_update_for.
    def visitInit_condition_update_for(self, ctx:MiniGoParser.Init_condition_update_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#range_for.
    def visitRange_for(self, ctx:MiniGoParser.Range_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#break_statement.
    def visitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continue_statement.
    def visitContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#return_statement.
    def visitReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#call_statement.
    def visitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lbrace_code_block.
    def visitLbrace_code_block(self, ctx:MiniGoParser.Lbrace_code_blockContext):
        return self.visitChildren(ctx)



del MiniGoParser