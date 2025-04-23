# Generated from OGCode.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .OGCodeParser import OGCodeParser
else:
    from OGCodeParser import OGCodeParser

# This class defines a complete listener for a parse tree produced by OGCodeParser.
class OGCodeListener(ParseTreeListener):

    # Enter a parse tree produced by OGCodeParser#program.
    def enterProgram(self, ctx:OGCodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by OGCodeParser#program.
    def exitProgram(self, ctx:OGCodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by OGCodeParser#funcDefinition.
    def enterFuncDefinition(self, ctx:OGCodeParser.FuncDefinitionContext):
        pass

    # Exit a parse tree produced by OGCodeParser#funcDefinition.
    def exitFuncDefinition(self, ctx:OGCodeParser.FuncDefinitionContext):
        pass


    # Enter a parse tree produced by OGCodeParser#parametersDefinition.
    def enterParametersDefinition(self, ctx:OGCodeParser.ParametersDefinitionContext):
        pass

    # Exit a parse tree produced by OGCodeParser#parametersDefinition.
    def exitParametersDefinition(self, ctx:OGCodeParser.ParametersDefinitionContext):
        pass


    # Enter a parse tree produced by OGCodeParser#returnStatement.
    def enterReturnStatement(self, ctx:OGCodeParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by OGCodeParser#returnStatement.
    def exitReturnStatement(self, ctx:OGCodeParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by OGCodeParser#body.
    def enterBody(self, ctx:OGCodeParser.BodyContext):
        pass

    # Exit a parse tree produced by OGCodeParser#body.
    def exitBody(self, ctx:OGCodeParser.BodyContext):
        pass


    # Enter a parse tree produced by OGCodeParser#incrementDecrementStatement.
    def enterIncrementDecrementStatement(self, ctx:OGCodeParser.IncrementDecrementStatementContext):
        pass

    # Exit a parse tree produced by OGCodeParser#incrementDecrementStatement.
    def exitIncrementDecrementStatement(self, ctx:OGCodeParser.IncrementDecrementStatementContext):
        pass


    # Enter a parse tree produced by OGCodeParser#ifStatement.
    def enterIfStatement(self, ctx:OGCodeParser.IfStatementContext):
        pass

    # Exit a parse tree produced by OGCodeParser#ifStatement.
    def exitIfStatement(self, ctx:OGCodeParser.IfStatementContext):
        pass


    # Enter a parse tree produced by OGCodeParser#statement.
    def enterStatement(self, ctx:OGCodeParser.StatementContext):
        pass

    # Exit a parse tree produced by OGCodeParser#statement.
    def exitStatement(self, ctx:OGCodeParser.StatementContext):
        pass


    # Enter a parse tree produced by OGCodeParser#loopStatement.
    def enterLoopStatement(self, ctx:OGCodeParser.LoopStatementContext):
        pass

    # Exit a parse tree produced by OGCodeParser#loopStatement.
    def exitLoopStatement(self, ctx:OGCodeParser.LoopStatementContext):
        pass


    # Enter a parse tree produced by OGCodeParser#number.
    def enterNumber(self, ctx:OGCodeParser.NumberContext):
        pass

    # Exit a parse tree produced by OGCodeParser#number.
    def exitNumber(self, ctx:OGCodeParser.NumberContext):
        pass


    # Enter a parse tree produced by OGCodeParser#variableDefinition.
    def enterVariableDefinition(self, ctx:OGCodeParser.VariableDefinitionContext):
        pass

    # Exit a parse tree produced by OGCodeParser#variableDefinition.
    def exitVariableDefinition(self, ctx:OGCodeParser.VariableDefinitionContext):
        pass


    # Enter a parse tree produced by OGCodeParser#assignment.
    def enterAssignment(self, ctx:OGCodeParser.AssignmentContext):
        pass

    # Exit a parse tree produced by OGCodeParser#assignment.
    def exitAssignment(self, ctx:OGCodeParser.AssignmentContext):
        pass


    # Enter a parse tree produced by OGCodeParser#expression.
    def enterExpression(self, ctx:OGCodeParser.ExpressionContext):
        pass

    # Exit a parse tree produced by OGCodeParser#expression.
    def exitExpression(self, ctx:OGCodeParser.ExpressionContext):
        pass


    # Enter a parse tree produced by OGCodeParser#condition.
    def enterCondition(self, ctx:OGCodeParser.ConditionContext):
        pass

    # Exit a parse tree produced by OGCodeParser#condition.
    def exitCondition(self, ctx:OGCodeParser.ConditionContext):
        pass


    # Enter a parse tree produced by OGCodeParser#commentStatement.
    def enterCommentStatement(self, ctx:OGCodeParser.CommentStatementContext):
        pass

    # Exit a parse tree produced by OGCodeParser#commentStatement.
    def exitCommentStatement(self, ctx:OGCodeParser.CommentStatementContext):
        pass


    # Enter a parse tree produced by OGCodeParser#commandBlock.
    def enterCommandBlock(self, ctx:OGCodeParser.CommandBlockContext):
        pass

    # Exit a parse tree produced by OGCodeParser#commandBlock.
    def exitCommandBlock(self, ctx:OGCodeParser.CommandBlockContext):
        pass


    # Enter a parse tree produced by OGCodeParser#parameters.
    def enterParameters(self, ctx:OGCodeParser.ParametersContext):
        pass

    # Exit a parse tree produced by OGCodeParser#parameters.
    def exitParameters(self, ctx:OGCodeParser.ParametersContext):
        pass



del OGCodeParser