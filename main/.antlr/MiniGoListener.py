# Generated from h:/Projects/PPL1-AnhTien/main/MiniGo.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete listener for a parse tree produced by MiniGoParser.
class MiniGoListener(ParseTreeListener):

    # Enter a parse tree produced by MiniGoParser#program.
    def enterProgram(self, ctx:MiniGoParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniGoParser#program.
    def exitProgram(self, ctx:MiniGoParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniGoParser#declared.
    def enterDeclared(self, ctx:MiniGoParser.DeclaredContext):
        pass

    # Exit a parse tree produced by MiniGoParser#declared.
    def exitDeclared(self, ctx:MiniGoParser.DeclaredContext):
        pass


    # Enter a parse tree produced by MiniGoParser#variables_declared.
    def enterVariables_declared(self, ctx:MiniGoParser.Variables_declaredContext):
        pass

    # Exit a parse tree produced by MiniGoParser#variables_declared.
    def exitVariables_declared(self, ctx:MiniGoParser.Variables_declaredContext):
        pass


    # Enter a parse tree produced by MiniGoParser#implicit_var.
    def enterImplicit_var(self, ctx:MiniGoParser.Implicit_varContext):
        pass

    # Exit a parse tree produced by MiniGoParser#implicit_var.
    def exitImplicit_var(self, ctx:MiniGoParser.Implicit_varContext):
        pass


    # Enter a parse tree produced by MiniGoParser#keyword_var.
    def enterKeyword_var(self, ctx:MiniGoParser.Keyword_varContext):
        pass

    # Exit a parse tree produced by MiniGoParser#keyword_var.
    def exitKeyword_var(self, ctx:MiniGoParser.Keyword_varContext):
        pass


    # Enter a parse tree produced by MiniGoParser#primitive_type.
    def enterPrimitive_type(self, ctx:MiniGoParser.Primitive_typeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#primitive_type.
    def exitPrimitive_type(self, ctx:MiniGoParser.Primitive_typeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#primitive_declaration.
    def enterPrimitive_declaration(self, ctx:MiniGoParser.Primitive_declarationContext):
        pass

    # Exit a parse tree produced by MiniGoParser#primitive_declaration.
    def exitPrimitive_declaration(self, ctx:MiniGoParser.Primitive_declarationContext):
        pass


    # Enter a parse tree produced by MiniGoParser#interface_type.
    def enterInterface_type(self, ctx:MiniGoParser.Interface_typeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#interface_type.
    def exitInterface_type(self, ctx:MiniGoParser.Interface_typeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#dimension_list.
    def enterDimension_list(self, ctx:MiniGoParser.Dimension_listContext):
        pass

    # Exit a parse tree produced by MiniGoParser#dimension_list.
    def exitDimension_list(self, ctx:MiniGoParser.Dimension_listContext):
        pass


    # Enter a parse tree produced by MiniGoParser#array_declaration.
    def enterArray_declaration(self, ctx:MiniGoParser.Array_declarationContext):
        pass

    # Exit a parse tree produced by MiniGoParser#array_declaration.
    def exitArray_declaration(self, ctx:MiniGoParser.Array_declarationContext):
        pass


    # Enter a parse tree produced by MiniGoParser#constants_declared.
    def enterConstants_declared(self, ctx:MiniGoParser.Constants_declaredContext):
        pass

    # Exit a parse tree produced by MiniGoParser#constants_declared.
    def exitConstants_declared(self, ctx:MiniGoParser.Constants_declaredContext):
        pass


    # Enter a parse tree produced by MiniGoParser#function_declared.
    def enterFunction_declared(self, ctx:MiniGoParser.Function_declaredContext):
        pass

    # Exit a parse tree produced by MiniGoParser#function_declared.
    def exitFunction_declared(self, ctx:MiniGoParser.Function_declaredContext):
        pass


    # Enter a parse tree produced by MiniGoParser#method_declared.
    def enterMethod_declared(self, ctx:MiniGoParser.Method_declaredContext):
        pass

    # Exit a parse tree produced by MiniGoParser#method_declared.
    def exitMethod_declared(self, ctx:MiniGoParser.Method_declaredContext):
        pass


    # Enter a parse tree produced by MiniGoParser#struct_declared.
    def enterStruct_declared(self, ctx:MiniGoParser.Struct_declaredContext):
        pass

    # Exit a parse tree produced by MiniGoParser#struct_declared.
    def exitStruct_declared(self, ctx:MiniGoParser.Struct_declaredContext):
        pass


    # Enter a parse tree produced by MiniGoParser#struct_declared_content.
    def enterStruct_declared_content(self, ctx:MiniGoParser.Struct_declared_contentContext):
        pass

    # Exit a parse tree produced by MiniGoParser#struct_declared_content.
    def exitStruct_declared_content(self, ctx:MiniGoParser.Struct_declared_contentContext):
        pass


    # Enter a parse tree produced by MiniGoParser#interface_declared.
    def enterInterface_declared(self, ctx:MiniGoParser.Interface_declaredContext):
        pass

    # Exit a parse tree produced by MiniGoParser#interface_declared.
    def exitInterface_declared(self, ctx:MiniGoParser.Interface_declaredContext):
        pass


    # Enter a parse tree produced by MiniGoParser#prameters_list.
    def enterPrameters_list(self, ctx:MiniGoParser.Prameters_listContext):
        pass

    # Exit a parse tree produced by MiniGoParser#prameters_list.
    def exitPrameters_list(self, ctx:MiniGoParser.Prameters_listContext):
        pass


    # Enter a parse tree produced by MiniGoParser#prameter.
    def enterPrameter(self, ctx:MiniGoParser.PrameterContext):
        pass

    # Exit a parse tree produced by MiniGoParser#prameter.
    def exitPrameter(self, ctx:MiniGoParser.PrameterContext):
        pass


    # Enter a parse tree produced by MiniGoParser#prameters_list_method.
    def enterPrameters_list_method(self, ctx:MiniGoParser.Prameters_list_methodContext):
        pass

    # Exit a parse tree produced by MiniGoParser#prameters_list_method.
    def exitPrameters_list_method(self, ctx:MiniGoParser.Prameters_list_methodContext):
        pass


    # Enter a parse tree produced by MiniGoParser#prameter_method.
    def enterPrameter_method(self, ctx:MiniGoParser.Prameter_methodContext):
        pass

    # Exit a parse tree produced by MiniGoParser#prameter_method.
    def exitPrameter_method(self, ctx:MiniGoParser.Prameter_methodContext):
        pass


    # Enter a parse tree produced by MiniGoParser#valid_endline.
    def enterValid_endline(self, ctx:MiniGoParser.Valid_endlineContext):
        pass

    # Exit a parse tree produced by MiniGoParser#valid_endline.
    def exitValid_endline(self, ctx:MiniGoParser.Valid_endlineContext):
        pass


    # Enter a parse tree produced by MiniGoParser#literal.
    def enterLiteral(self, ctx:MiniGoParser.LiteralContext):
        pass

    # Exit a parse tree produced by MiniGoParser#literal.
    def exitLiteral(self, ctx:MiniGoParser.LiteralContext):
        pass


    # Enter a parse tree produced by MiniGoParser#array_literal.
    def enterArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        pass

    # Exit a parse tree produced by MiniGoParser#array_literal.
    def exitArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        pass


    # Enter a parse tree produced by MiniGoParser#struct_literal.
    def enterStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        pass

    # Exit a parse tree produced by MiniGoParser#struct_literal.
    def exitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        pass


    # Enter a parse tree produced by MiniGoParser#list_expression.
    def enterList_expression(self, ctx:MiniGoParser.List_expressionContext):
        pass

    # Exit a parse tree produced by MiniGoParser#list_expression.
    def exitList_expression(self, ctx:MiniGoParser.List_expressionContext):
        pass


    # Enter a parse tree produced by MiniGoParser#params.
    def enterParams(self, ctx:MiniGoParser.ParamsContext):
        pass

    # Exit a parse tree produced by MiniGoParser#params.
    def exitParams(self, ctx:MiniGoParser.ParamsContext):
        pass


    # Enter a parse tree produced by MiniGoParser#list_elements.
    def enterList_elements(self, ctx:MiniGoParser.List_elementsContext):
        pass

    # Exit a parse tree produced by MiniGoParser#list_elements.
    def exitList_elements(self, ctx:MiniGoParser.List_elementsContext):
        pass


    # Enter a parse tree produced by MiniGoParser#expression.
    def enterExpression(self, ctx:MiniGoParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MiniGoParser#expression.
    def exitExpression(self, ctx:MiniGoParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MiniGoParser#expression1.
    def enterExpression1(self, ctx:MiniGoParser.Expression1Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expression1.
    def exitExpression1(self, ctx:MiniGoParser.Expression1Context):
        pass


    # Enter a parse tree produced by MiniGoParser#expression2.
    def enterExpression2(self, ctx:MiniGoParser.Expression2Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expression2.
    def exitExpression2(self, ctx:MiniGoParser.Expression2Context):
        pass


    # Enter a parse tree produced by MiniGoParser#expression3.
    def enterExpression3(self, ctx:MiniGoParser.Expression3Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expression3.
    def exitExpression3(self, ctx:MiniGoParser.Expression3Context):
        pass


    # Enter a parse tree produced by MiniGoParser#expression4.
    def enterExpression4(self, ctx:MiniGoParser.Expression4Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expression4.
    def exitExpression4(self, ctx:MiniGoParser.Expression4Context):
        pass


    # Enter a parse tree produced by MiniGoParser#expression5.
    def enterExpression5(self, ctx:MiniGoParser.Expression5Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expression5.
    def exitExpression5(self, ctx:MiniGoParser.Expression5Context):
        pass


    # Enter a parse tree produced by MiniGoParser#expression6.
    def enterExpression6(self, ctx:MiniGoParser.Expression6Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expression6.
    def exitExpression6(self, ctx:MiniGoParser.Expression6Context):
        pass


    # Enter a parse tree produced by MiniGoParser#expression7.
    def enterExpression7(self, ctx:MiniGoParser.Expression7Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expression7.
    def exitExpression7(self, ctx:MiniGoParser.Expression7Context):
        pass


    # Enter a parse tree produced by MiniGoParser#func_call.
    def enterFunc_call(self, ctx:MiniGoParser.Func_callContext):
        pass

    # Exit a parse tree produced by MiniGoParser#func_call.
    def exitFunc_call(self, ctx:MiniGoParser.Func_callContext):
        pass


    # Enter a parse tree produced by MiniGoParser#ignore.
    def enterIgnore(self, ctx:MiniGoParser.IgnoreContext):
        pass

    # Exit a parse tree produced by MiniGoParser#ignore.
    def exitIgnore(self, ctx:MiniGoParser.IgnoreContext):
        pass


    # Enter a parse tree produced by MiniGoParser#ignore_recursive.
    def enterIgnore_recursive(self, ctx:MiniGoParser.Ignore_recursiveContext):
        pass

    # Exit a parse tree produced by MiniGoParser#ignore_recursive.
    def exitIgnore_recursive(self, ctx:MiniGoParser.Ignore_recursiveContext):
        pass


    # Enter a parse tree produced by MiniGoParser#list_statement.
    def enterList_statement(self, ctx:MiniGoParser.List_statementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#list_statement.
    def exitList_statement(self, ctx:MiniGoParser.List_statementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#statement.
    def enterStatement(self, ctx:MiniGoParser.StatementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#statement.
    def exitStatement(self, ctx:MiniGoParser.StatementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#declared_statement.
    def enterDeclared_statement(self, ctx:MiniGoParser.Declared_statementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#declared_statement.
    def exitDeclared_statement(self, ctx:MiniGoParser.Declared_statementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#assign_statement.
    def enterAssign_statement(self, ctx:MiniGoParser.Assign_statementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#assign_statement.
    def exitAssign_statement(self, ctx:MiniGoParser.Assign_statementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#assignment_operator.
    def enterAssignment_operator(self, ctx:MiniGoParser.Assignment_operatorContext):
        pass

    # Exit a parse tree produced by MiniGoParser#assignment_operator.
    def exitAssignment_operator(self, ctx:MiniGoParser.Assignment_operatorContext):
        pass


    # Enter a parse tree produced by MiniGoParser#member_access.
    def enterMember_access(self, ctx:MiniGoParser.Member_accessContext):
        pass

    # Exit a parse tree produced by MiniGoParser#member_access.
    def exitMember_access(self, ctx:MiniGoParser.Member_accessContext):
        pass


    # Enter a parse tree produced by MiniGoParser#if_statement.
    def enterIf_statement(self, ctx:MiniGoParser.If_statementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#if_statement.
    def exitIf_statement(self, ctx:MiniGoParser.If_statementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#list_elif.
    def enterList_elif(self, ctx:MiniGoParser.List_elifContext):
        pass

    # Exit a parse tree produced by MiniGoParser#list_elif.
    def exitList_elif(self, ctx:MiniGoParser.List_elifContext):
        pass


    # Enter a parse tree produced by MiniGoParser#for_statement.
    def enterFor_statement(self, ctx:MiniGoParser.For_statementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#for_statement.
    def exitFor_statement(self, ctx:MiniGoParser.For_statementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#basic_for.
    def enterBasic_for(self, ctx:MiniGoParser.Basic_forContext):
        pass

    # Exit a parse tree produced by MiniGoParser#basic_for.
    def exitBasic_for(self, ctx:MiniGoParser.Basic_forContext):
        pass


    # Enter a parse tree produced by MiniGoParser#init_condition_update_for.
    def enterInit_condition_update_for(self, ctx:MiniGoParser.Init_condition_update_forContext):
        pass

    # Exit a parse tree produced by MiniGoParser#init_condition_update_for.
    def exitInit_condition_update_for(self, ctx:MiniGoParser.Init_condition_update_forContext):
        pass


    # Enter a parse tree produced by MiniGoParser#range_for.
    def enterRange_for(self, ctx:MiniGoParser.Range_forContext):
        pass

    # Exit a parse tree produced by MiniGoParser#range_for.
    def exitRange_for(self, ctx:MiniGoParser.Range_forContext):
        pass


    # Enter a parse tree produced by MiniGoParser#implicit_var_for.
    def enterImplicit_var_for(self, ctx:MiniGoParser.Implicit_var_forContext):
        pass

    # Exit a parse tree produced by MiniGoParser#implicit_var_for.
    def exitImplicit_var_for(self, ctx:MiniGoParser.Implicit_var_forContext):
        pass


    # Enter a parse tree produced by MiniGoParser#assign_statement_for.
    def enterAssign_statement_for(self, ctx:MiniGoParser.Assign_statement_forContext):
        pass

    # Exit a parse tree produced by MiniGoParser#assign_statement_for.
    def exitAssign_statement_for(self, ctx:MiniGoParser.Assign_statement_forContext):
        pass


    # Enter a parse tree produced by MiniGoParser#break_statement.
    def enterBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#break_statement.
    def exitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#continue_statement.
    def enterContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#continue_statement.
    def exitContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#return_statement.
    def enterReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#return_statement.
    def exitReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#call_statement.
    def enterCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#call_statement.
    def exitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#method_call.
    def enterMethod_call(self, ctx:MiniGoParser.Method_callContext):
        pass

    # Exit a parse tree produced by MiniGoParser#method_call.
    def exitMethod_call(self, ctx:MiniGoParser.Method_callContext):
        pass


    # Enter a parse tree produced by MiniGoParser#lbrace_code_block.
    def enterLbrace_code_block(self, ctx:MiniGoParser.Lbrace_code_blockContext):
        pass

    # Exit a parse tree produced by MiniGoParser#lbrace_code_block.
    def exitLbrace_code_block(self, ctx:MiniGoParser.Lbrace_code_blockContext):
        pass



del MiniGoParser