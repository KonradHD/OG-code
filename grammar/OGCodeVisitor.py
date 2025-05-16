# Generated from OGCode.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .OGCodeParser import OGCodeParser
else:
    from OGCodeParser import OGCodeParser

# This class defines a complete generic visitor for a parse tree produced by OGCodeParser.

class OGCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by OGCodeParser#program.
    def visitProgram(self, ctx:OGCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGCodeParser#funcDefinition.
    def visitFuncDefinition(self, ctx:OGCodeParser.FuncDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGCodeParser#startFunction.
    def visitStartFunction(self, ctx:OGCodeParser.StartFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGCodeParser#otherFunction.
    def visitOtherFunction(self, ctx:OGCodeParser.OtherFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGCodeParser#parametersDefinition.
    def visitParametersDefinition(self, ctx:OGCodeParser.ParametersDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGCodeParser#body.
    def visitBody(self, ctx:OGCodeParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGCodeParser#incrementDecrementStatement.
    def visitIncrementDecrementStatement(self, ctx:OGCodeParser.IncrementDecrementStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGCodeParser#ifStatement.
    def visitIfStatement(self, ctx:OGCodeParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGCodeParser#elseIfStatement.
    def visitElseIfStatement(self, ctx:OGCodeParser.ElseIfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGCodeParser#elseStatement.
    def visitElseStatement(self, ctx:OGCodeParser.ElseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGCodeParser#loopStatement.
    def visitLoopStatement(self, ctx:OGCodeParser.LoopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGCodeParser#variableDefinition.
    def visitVariableDefinition(self, ctx:OGCodeParser.VariableDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGCodeParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:OGCodeParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGCodeParser#assignment.
    def visitAssignment(self, ctx:OGCodeParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGCodeParser#expressionStatement.
    def visitExpressionStatement(self, ctx:OGCodeParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGCodeParser#expression.
    def visitExpression(self, ctx:OGCodeParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGCodeParser#condition.
    def visitCondition(self, ctx:OGCodeParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGCodeParser#commentStatement.
    def visitCommentStatement(self, ctx:OGCodeParser.CommentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGCodeParser#commandBlock.
    def visitCommandBlock(self, ctx:OGCodeParser.CommandBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGCodeParser#parameters.
    def visitParameters(self, ctx:OGCodeParser.ParametersContext):
        return self.visitChildren(ctx)



del OGCodeParser