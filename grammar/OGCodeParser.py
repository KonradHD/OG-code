# Generated from OGCode.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,43,254,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,1,0,1,1,1,1,5,1,47,8,1,10,1,12,1,50,9,1,1,2,1,2,1,2,1,2,
        1,2,1,2,5,2,58,8,2,10,2,12,2,61,9,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,
        69,8,3,1,3,1,3,1,3,5,3,74,8,3,10,3,12,3,77,9,3,1,3,3,3,80,8,3,1,
        3,1,3,1,4,1,4,1,4,1,4,1,4,5,4,89,8,4,10,4,12,4,92,9,4,1,5,1,5,1,
        5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,111,
        8,6,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,5,8,122,8,8,10,8,12,8,125,
        9,8,1,8,1,8,5,8,129,8,8,10,8,12,8,132,9,8,1,8,3,8,135,8,8,1,9,1,
        9,1,9,1,9,1,9,1,9,5,9,143,8,9,10,9,12,9,146,9,9,1,9,1,9,1,10,1,10,
        1,10,5,10,153,8,10,10,10,12,10,156,9,10,1,10,1,10,1,11,1,11,1,11,
        1,11,5,11,164,8,11,10,11,12,11,167,9,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,5,11,176,8,11,10,11,12,11,179,9,11,1,11,1,11,3,11,183,
        8,11,1,12,1,12,1,12,1,12,1,12,1,12,3,12,191,8,12,3,12,193,8,12,1,
        13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,205,8,14,1,
        15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,217,8,16,1,
        16,1,16,1,16,5,16,222,8,16,10,16,12,16,225,9,16,1,17,1,17,1,17,1,
        17,1,17,5,17,232,8,17,10,17,12,17,235,9,17,1,18,1,18,1,19,1,19,1,
        19,3,19,242,8,19,1,19,1,19,1,20,1,20,1,20,5,20,249,8,20,10,20,12,
        20,252,9,20,1,20,0,1,32,21,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,40,0,6,1,0,7,8,1,0,40,41,1,0,2,6,1,0,9,14,1,0,
        15,16,1,0,21,22,266,0,42,1,0,0,0,2,44,1,0,0,0,4,51,1,0,0,0,6,64,
        1,0,0,0,8,83,1,0,0,0,10,93,1,0,0,0,12,110,1,0,0,0,14,112,1,0,0,0,
        16,115,1,0,0,0,18,136,1,0,0,0,20,149,1,0,0,0,22,182,1,0,0,0,24,184,
        1,0,0,0,26,194,1,0,0,0,28,197,1,0,0,0,30,206,1,0,0,0,32,216,1,0,
        0,0,34,226,1,0,0,0,36,236,1,0,0,0,38,238,1,0,0,0,40,245,1,0,0,0,
        42,43,3,2,1,0,43,1,1,0,0,0,44,48,3,4,2,0,45,47,3,6,3,0,46,45,1,0,
        0,0,47,50,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,3,1,0,0,0,50,48,
        1,0,0,0,51,52,5,29,0,0,52,53,5,38,0,0,53,54,5,25,0,0,54,55,5,26,
        0,0,55,59,5,27,0,0,56,58,3,12,6,0,57,56,1,0,0,0,58,61,1,0,0,0,59,
        57,1,0,0,0,59,60,1,0,0,0,60,62,1,0,0,0,61,59,1,0,0,0,62,63,5,28,
        0,0,63,5,1,0,0,0,64,65,5,29,0,0,65,66,5,40,0,0,66,68,5,25,0,0,67,
        69,3,8,4,0,68,67,1,0,0,0,68,69,1,0,0,0,69,70,1,0,0,0,70,71,5,26,
        0,0,71,75,5,27,0,0,72,74,3,12,6,0,73,72,1,0,0,0,74,77,1,0,0,0,75,
        73,1,0,0,0,75,76,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,78,80,3,10,
        5,0,79,78,1,0,0,0,79,80,1,0,0,0,80,81,1,0,0,0,81,82,5,28,0,0,82,
        7,1,0,0,0,83,84,5,30,0,0,84,90,5,40,0,0,85,86,5,19,0,0,86,87,5,30,
        0,0,87,89,5,40,0,0,88,85,1,0,0,0,89,92,1,0,0,0,90,88,1,0,0,0,90,
        91,1,0,0,0,91,9,1,0,0,0,92,90,1,0,0,0,93,94,5,36,0,0,94,95,3,30,
        15,0,95,11,1,0,0,0,96,111,3,22,11,0,97,98,3,38,19,0,98,99,5,20,0,
        0,99,111,1,0,0,0,100,101,3,24,12,0,101,102,5,20,0,0,102,111,1,0,
        0,0,103,111,3,30,15,0,104,111,3,16,8,0,105,111,3,26,13,0,106,107,
        3,14,7,0,107,108,5,20,0,0,108,111,1,0,0,0,109,111,3,36,18,0,110,
        96,1,0,0,0,110,97,1,0,0,0,110,100,1,0,0,0,110,103,1,0,0,0,110,104,
        1,0,0,0,110,105,1,0,0,0,110,106,1,0,0,0,110,109,1,0,0,0,111,13,1,
        0,0,0,112,113,5,40,0,0,113,114,7,0,0,0,114,15,1,0,0,0,115,116,5,
        33,0,0,116,117,5,25,0,0,117,118,3,34,17,0,118,119,5,26,0,0,119,123,
        5,27,0,0,120,122,3,12,6,0,121,120,1,0,0,0,122,125,1,0,0,0,123,121,
        1,0,0,0,123,124,1,0,0,0,124,126,1,0,0,0,125,123,1,0,0,0,126,130,
        5,28,0,0,127,129,3,18,9,0,128,127,1,0,0,0,129,132,1,0,0,0,130,128,
        1,0,0,0,130,131,1,0,0,0,131,134,1,0,0,0,132,130,1,0,0,0,133,135,
        3,20,10,0,134,133,1,0,0,0,134,135,1,0,0,0,135,17,1,0,0,0,136,137,
        5,35,0,0,137,138,5,25,0,0,138,139,3,34,17,0,139,140,5,26,0,0,140,
        144,5,27,0,0,141,143,3,12,6,0,142,141,1,0,0,0,143,146,1,0,0,0,144,
        142,1,0,0,0,144,145,1,0,0,0,145,147,1,0,0,0,146,144,1,0,0,0,147,
        148,5,28,0,0,148,19,1,0,0,0,149,150,5,34,0,0,150,154,5,27,0,0,151,
        153,3,12,6,0,152,151,1,0,0,0,153,156,1,0,0,0,154,152,1,0,0,0,154,
        155,1,0,0,0,155,157,1,0,0,0,156,154,1,0,0,0,157,158,5,28,0,0,158,
        21,1,0,0,0,159,160,5,31,0,0,160,161,7,1,0,0,161,165,5,27,0,0,162,
        164,3,12,6,0,163,162,1,0,0,0,164,167,1,0,0,0,165,163,1,0,0,0,165,
        166,1,0,0,0,166,168,1,0,0,0,167,165,1,0,0,0,168,183,5,28,0,0,169,
        170,5,32,0,0,170,171,5,25,0,0,171,172,3,34,17,0,172,173,5,26,0,0,
        173,177,5,27,0,0,174,176,3,12,6,0,175,174,1,0,0,0,176,179,1,0,0,
        0,177,175,1,0,0,0,177,178,1,0,0,0,178,180,1,0,0,0,179,177,1,0,0,
        0,180,181,5,28,0,0,181,183,1,0,0,0,182,159,1,0,0,0,182,169,1,0,0,
        0,183,23,1,0,0,0,184,185,5,30,0,0,185,192,5,40,0,0,186,190,5,1,0,
        0,187,191,3,32,16,0,188,191,5,17,0,0,189,191,5,18,0,0,190,187,1,
        0,0,0,190,188,1,0,0,0,190,189,1,0,0,0,191,193,1,0,0,0,192,186,1,
        0,0,0,192,193,1,0,0,0,193,25,1,0,0,0,194,195,3,28,14,0,195,196,5,
        20,0,0,196,27,1,0,0,0,197,198,5,40,0,0,198,204,5,1,0,0,199,205,3,
        32,16,0,200,205,5,17,0,0,201,205,5,18,0,0,202,205,5,43,0,0,203,205,
        5,40,0,0,204,199,1,0,0,0,204,200,1,0,0,0,204,201,1,0,0,0,204,202,
        1,0,0,0,204,203,1,0,0,0,205,29,1,0,0,0,206,207,3,32,16,0,207,208,
        5,20,0,0,208,31,1,0,0,0,209,210,6,16,-1,0,210,211,5,25,0,0,211,212,
        3,32,16,0,212,213,5,26,0,0,213,217,1,0,0,0,214,217,5,41,0,0,215,
        217,5,40,0,0,216,209,1,0,0,0,216,214,1,0,0,0,216,215,1,0,0,0,217,
        223,1,0,0,0,218,219,10,4,0,0,219,220,7,2,0,0,220,222,3,32,16,5,221,
        218,1,0,0,0,222,225,1,0,0,0,223,221,1,0,0,0,223,224,1,0,0,0,224,
        33,1,0,0,0,225,223,1,0,0,0,226,227,3,32,16,0,227,228,7,3,0,0,228,
        233,3,32,16,0,229,230,7,4,0,0,230,232,3,34,17,0,231,229,1,0,0,0,
        232,235,1,0,0,0,233,231,1,0,0,0,233,234,1,0,0,0,234,35,1,0,0,0,235,
        233,1,0,0,0,236,237,7,5,0,0,237,37,1,0,0,0,238,239,5,39,0,0,239,
        241,5,25,0,0,240,242,3,40,20,0,241,240,1,0,0,0,241,242,1,0,0,0,242,
        243,1,0,0,0,243,244,5,26,0,0,244,39,1,0,0,0,245,250,3,28,14,0,246,
        247,5,19,0,0,247,249,3,28,14,0,248,246,1,0,0,0,249,252,1,0,0,0,250,
        248,1,0,0,0,250,251,1,0,0,0,251,41,1,0,0,0,252,250,1,0,0,0,23,48,
        59,68,75,79,90,110,123,130,134,144,154,165,177,182,190,192,204,216,
        223,233,241,250
    ]

class OGCodeParser ( Parser ):

    grammarFileName = "OGCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'++'", "'--'", "'=='", "'!='", "'<'", "'>'", "'<='", 
                     "'>='", "'and'", "'or'", "'true'", "'false'", "','", 
                     "';'", "<INVALID>", "<INVALID>", "'['", "']'", "'('", 
                     "')'", "'{'", "'}'", "'function'", "'let'", "'repeat'", 
                     "'while'", "'if'", "'else'", "'elseif'", "'return'", 
                     "'break'", "'start'" ]

    symbolicNames = [ "<INVALID>", "ASSIGNMENT_OPERATOR", "PLUS_OPERATOR", 
                      "MINUS_OPERATOR", "MULTIPLY_OPERATOR", "DIVIDE_OPERATOR", 
                      "MODULO_OPERATOR", "INCREMENT_OPERATOR", "DECREMENT_OPERATOR", 
                      "EQUAL_OPERATOR", "UNEQUAL_OPERATOR", "LESSER_OPERATOR", 
                      "GREATER_OPERATOR", "LESSER_OR_EQUAL_OPERATOR", "GREATER_OR_EQUAL_OPERATOR", 
                      "AND_KEYWORD", "OR_KEYWORD", "BOOLEAN_TRUE", "BOOLEAN_FALSE", 
                      "COMMA_SEPARATOR", "SEMICOLON_SEPARATOR", "LINE_COMMENT", 
                      "BLOCK_COMMENT", "LEFT_BRACKET", "RIGHT_BRACKET", 
                      "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", "LEFT_BRACE", 
                      "RIGHT_BRACE", "FUNCTION_KEYWORD", "LET_KEYWORD", 
                      "REPEAT_KEYWORD", "WHILE_KEYWORD", "IF_KEYWORD", "ELSE_KEYWORD", 
                      "ELSEIF_KEYWORD", "RETURN_KEYWORD", "BREAK_KEYWORD", 
                      "START_KEYWORD", "FUNCTIONS_KEYWORDS", "IDENTIFIER", 
                      "NUMBER", "WS", "STRING" ]

    RULE_program = 0
    RULE_funcDefinition = 1
    RULE_startFunction = 2
    RULE_otherFunction = 3
    RULE_parametersDefinition = 4
    RULE_returnStatement = 5
    RULE_body = 6
    RULE_incrementDecrementStatement = 7
    RULE_ifStatement = 8
    RULE_elseIfStatement = 9
    RULE_elseStatement = 10
    RULE_loopStatement = 11
    RULE_variableDefinition = 12
    RULE_assignmentStatement = 13
    RULE_assignment = 14
    RULE_expressionStatement = 15
    RULE_expression = 16
    RULE_condition = 17
    RULE_commentStatement = 18
    RULE_commandBlock = 19
    RULE_parameters = 20

    ruleNames =  [ "program", "funcDefinition", "startFunction", "otherFunction", 
                   "parametersDefinition", "returnStatement", "body", "incrementDecrementStatement", 
                   "ifStatement", "elseIfStatement", "elseStatement", "loopStatement", 
                   "variableDefinition", "assignmentStatement", "assignment", 
                   "expressionStatement", "expression", "condition", "commentStatement", 
                   "commandBlock", "parameters" ]

    EOF = Token.EOF
    ASSIGNMENT_OPERATOR=1
    PLUS_OPERATOR=2
    MINUS_OPERATOR=3
    MULTIPLY_OPERATOR=4
    DIVIDE_OPERATOR=5
    MODULO_OPERATOR=6
    INCREMENT_OPERATOR=7
    DECREMENT_OPERATOR=8
    EQUAL_OPERATOR=9
    UNEQUAL_OPERATOR=10
    LESSER_OPERATOR=11
    GREATER_OPERATOR=12
    LESSER_OR_EQUAL_OPERATOR=13
    GREATER_OR_EQUAL_OPERATOR=14
    AND_KEYWORD=15
    OR_KEYWORD=16
    BOOLEAN_TRUE=17
    BOOLEAN_FALSE=18
    COMMA_SEPARATOR=19
    SEMICOLON_SEPARATOR=20
    LINE_COMMENT=21
    BLOCK_COMMENT=22
    LEFT_BRACKET=23
    RIGHT_BRACKET=24
    LEFT_PARENTHESIS=25
    RIGHT_PARENTHESIS=26
    LEFT_BRACE=27
    RIGHT_BRACE=28
    FUNCTION_KEYWORD=29
    LET_KEYWORD=30
    REPEAT_KEYWORD=31
    WHILE_KEYWORD=32
    IF_KEYWORD=33
    ELSE_KEYWORD=34
    ELSEIF_KEYWORD=35
    RETURN_KEYWORD=36
    BREAK_KEYWORD=37
    START_KEYWORD=38
    FUNCTIONS_KEYWORDS=39
    IDENTIFIER=40
    NUMBER=41
    WS=42
    STRING=43

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcDefinition(self):
            return self.getTypedRuleContext(OGCodeParser.FuncDefinitionContext,0)


        def getRuleIndex(self):
            return OGCodeParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = OGCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.funcDefinition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def startFunction(self):
            return self.getTypedRuleContext(OGCodeParser.StartFunctionContext,0)


        def otherFunction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OGCodeParser.OtherFunctionContext)
            else:
                return self.getTypedRuleContext(OGCodeParser.OtherFunctionContext,i)


        def getRuleIndex(self):
            return OGCodeParser.RULE_funcDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDefinition" ):
                listener.enterFuncDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDefinition" ):
                listener.exitFuncDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDefinition" ):
                return visitor.visitFuncDefinition(self)
            else:
                return visitor.visitChildren(self)




    def funcDefinition(self):

        localctx = OGCodeParser.FuncDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_funcDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.startFunction()
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 45
                self.otherFunction()
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StartFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION_KEYWORD(self):
            return self.getToken(OGCodeParser.FUNCTION_KEYWORD, 0)

        def START_KEYWORD(self):
            return self.getToken(OGCodeParser.START_KEYWORD, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(OGCodeParser.LEFT_PARENTHESIS, 0)

        def RIGHT_PARENTHESIS(self):
            return self.getToken(OGCodeParser.RIGHT_PARENTHESIS, 0)

        def LEFT_BRACE(self):
            return self.getToken(OGCodeParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(OGCodeParser.RIGHT_BRACE, 0)

        def body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OGCodeParser.BodyContext)
            else:
                return self.getTypedRuleContext(OGCodeParser.BodyContext,i)


        def getRuleIndex(self):
            return OGCodeParser.RULE_startFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStartFunction" ):
                listener.enterStartFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStartFunction" ):
                listener.exitStartFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStartFunction" ):
                return visitor.visitStartFunction(self)
            else:
                return visitor.visitChildren(self)




    def startFunction(self):

        localctx = OGCodeParser.StartFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_startFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(OGCodeParser.FUNCTION_KEYWORD)
            self.state = 52
            self.match(OGCodeParser.START_KEYWORD)
            self.state = 53
            self.match(OGCodeParser.LEFT_PARENTHESIS)
            self.state = 54
            self.match(OGCodeParser.RIGHT_PARENTHESIS)
            self.state = 55
            self.match(OGCodeParser.LEFT_BRACE)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3864436670464) != 0):
                self.state = 56
                self.body()
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 62
            self.match(OGCodeParser.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OtherFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION_KEYWORD(self):
            return self.getToken(OGCodeParser.FUNCTION_KEYWORD, 0)

        def IDENTIFIER(self):
            return self.getToken(OGCodeParser.IDENTIFIER, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(OGCodeParser.LEFT_PARENTHESIS, 0)

        def RIGHT_PARENTHESIS(self):
            return self.getToken(OGCodeParser.RIGHT_PARENTHESIS, 0)

        def LEFT_BRACE(self):
            return self.getToken(OGCodeParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(OGCodeParser.RIGHT_BRACE, 0)

        def parametersDefinition(self):
            return self.getTypedRuleContext(OGCodeParser.ParametersDefinitionContext,0)


        def body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OGCodeParser.BodyContext)
            else:
                return self.getTypedRuleContext(OGCodeParser.BodyContext,i)


        def returnStatement(self):
            return self.getTypedRuleContext(OGCodeParser.ReturnStatementContext,0)


        def getRuleIndex(self):
            return OGCodeParser.RULE_otherFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOtherFunction" ):
                listener.enterOtherFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOtherFunction" ):
                listener.exitOtherFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOtherFunction" ):
                return visitor.visitOtherFunction(self)
            else:
                return visitor.visitChildren(self)




    def otherFunction(self):

        localctx = OGCodeParser.OtherFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_otherFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(OGCodeParser.FUNCTION_KEYWORD)
            self.state = 65
            self.match(OGCodeParser.IDENTIFIER)
            self.state = 66
            self.match(OGCodeParser.LEFT_PARENTHESIS)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 67
                self.parametersDefinition()


            self.state = 70
            self.match(OGCodeParser.RIGHT_PARENTHESIS)
            self.state = 71
            self.match(OGCodeParser.LEFT_BRACE)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3864436670464) != 0):
                self.state = 72
                self.body()
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 78
                self.returnStatement()


            self.state = 81
            self.match(OGCodeParser.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET_KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(OGCodeParser.LET_KEYWORD)
            else:
                return self.getToken(OGCodeParser.LET_KEYWORD, i)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(OGCodeParser.IDENTIFIER)
            else:
                return self.getToken(OGCodeParser.IDENTIFIER, i)

        def COMMA_SEPARATOR(self, i:int=None):
            if i is None:
                return self.getTokens(OGCodeParser.COMMA_SEPARATOR)
            else:
                return self.getToken(OGCodeParser.COMMA_SEPARATOR, i)

        def getRuleIndex(self):
            return OGCodeParser.RULE_parametersDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametersDefinition" ):
                listener.enterParametersDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametersDefinition" ):
                listener.exitParametersDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametersDefinition" ):
                return visitor.visitParametersDefinition(self)
            else:
                return visitor.visitChildren(self)




    def parametersDefinition(self):

        localctx = OGCodeParser.ParametersDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_parametersDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(OGCodeParser.LET_KEYWORD)
            self.state = 84
            self.match(OGCodeParser.IDENTIFIER)
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 85
                self.match(OGCodeParser.COMMA_SEPARATOR)
                self.state = 86
                self.match(OGCodeParser.LET_KEYWORD)
                self.state = 87
                self.match(OGCodeParser.IDENTIFIER)
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN_KEYWORD(self):
            return self.getToken(OGCodeParser.RETURN_KEYWORD, 0)

        def expressionStatement(self):
            return self.getTypedRuleContext(OGCodeParser.ExpressionStatementContext,0)


        def getRuleIndex(self):
            return OGCodeParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = OGCodeParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(OGCodeParser.RETURN_KEYWORD)
            self.state = 94
            self.expressionStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def loopStatement(self):
            return self.getTypedRuleContext(OGCodeParser.LoopStatementContext,0)


        def commandBlock(self):
            return self.getTypedRuleContext(OGCodeParser.CommandBlockContext,0)


        def SEMICOLON_SEPARATOR(self):
            return self.getToken(OGCodeParser.SEMICOLON_SEPARATOR, 0)

        def variableDefinition(self):
            return self.getTypedRuleContext(OGCodeParser.VariableDefinitionContext,0)


        def expressionStatement(self):
            return self.getTypedRuleContext(OGCodeParser.ExpressionStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(OGCodeParser.IfStatementContext,0)


        def assignmentStatement(self):
            return self.getTypedRuleContext(OGCodeParser.AssignmentStatementContext,0)


        def incrementDecrementStatement(self):
            return self.getTypedRuleContext(OGCodeParser.IncrementDecrementStatementContext,0)


        def commentStatement(self):
            return self.getTypedRuleContext(OGCodeParser.CommentStatementContext,0)


        def getRuleIndex(self):
            return OGCodeParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = OGCodeParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_body)
        try:
            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.loopStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                self.commandBlock()
                self.state = 98
                self.match(OGCodeParser.SEMICOLON_SEPARATOR)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 100
                self.variableDefinition()
                self.state = 101
                self.match(OGCodeParser.SEMICOLON_SEPARATOR)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 103
                self.expressionStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 104
                self.ifStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 105
                self.assignmentStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 106
                self.incrementDecrementStatement()
                self.state = 107
                self.match(OGCodeParser.SEMICOLON_SEPARATOR)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 109
                self.commentStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncrementDecrementStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(OGCodeParser.IDENTIFIER, 0)

        def INCREMENT_OPERATOR(self):
            return self.getToken(OGCodeParser.INCREMENT_OPERATOR, 0)

        def DECREMENT_OPERATOR(self):
            return self.getToken(OGCodeParser.DECREMENT_OPERATOR, 0)

        def getRuleIndex(self):
            return OGCodeParser.RULE_incrementDecrementStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncrementDecrementStatement" ):
                listener.enterIncrementDecrementStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncrementDecrementStatement" ):
                listener.exitIncrementDecrementStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIncrementDecrementStatement" ):
                return visitor.visitIncrementDecrementStatement(self)
            else:
                return visitor.visitChildren(self)




    def incrementDecrementStatement(self):

        localctx = OGCodeParser.IncrementDecrementStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_incrementDecrementStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(OGCodeParser.IDENTIFIER)
            self.state = 113
            _la = self._input.LA(1)
            if not(_la==7 or _la==8):
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


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF_KEYWORD(self):
            return self.getToken(OGCodeParser.IF_KEYWORD, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(OGCodeParser.LEFT_PARENTHESIS, 0)

        def condition(self):
            return self.getTypedRuleContext(OGCodeParser.ConditionContext,0)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(OGCodeParser.RIGHT_PARENTHESIS, 0)

        def LEFT_BRACE(self):
            return self.getToken(OGCodeParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(OGCodeParser.RIGHT_BRACE, 0)

        def body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OGCodeParser.BodyContext)
            else:
                return self.getTypedRuleContext(OGCodeParser.BodyContext,i)


        def elseIfStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OGCodeParser.ElseIfStatementContext)
            else:
                return self.getTypedRuleContext(OGCodeParser.ElseIfStatementContext,i)


        def elseStatement(self):
            return self.getTypedRuleContext(OGCodeParser.ElseStatementContext,0)


        def getRuleIndex(self):
            return OGCodeParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = OGCodeParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(OGCodeParser.IF_KEYWORD)
            self.state = 116
            self.match(OGCodeParser.LEFT_PARENTHESIS)
            self.state = 117
            self.condition()
            self.state = 118
            self.match(OGCodeParser.RIGHT_PARENTHESIS)
            self.state = 119
            self.match(OGCodeParser.LEFT_BRACE)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3864436670464) != 0):
                self.state = 120
                self.body()
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 126
            self.match(OGCodeParser.RIGHT_BRACE)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 127
                self.elseIfStatement()
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 133
                self.elseStatement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseIfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF_KEYWORD(self):
            return self.getToken(OGCodeParser.ELSEIF_KEYWORD, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(OGCodeParser.LEFT_PARENTHESIS, 0)

        def condition(self):
            return self.getTypedRuleContext(OGCodeParser.ConditionContext,0)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(OGCodeParser.RIGHT_PARENTHESIS, 0)

        def LEFT_BRACE(self):
            return self.getToken(OGCodeParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(OGCodeParser.RIGHT_BRACE, 0)

        def body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OGCodeParser.BodyContext)
            else:
                return self.getTypedRuleContext(OGCodeParser.BodyContext,i)


        def getRuleIndex(self):
            return OGCodeParser.RULE_elseIfStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseIfStatement" ):
                listener.enterElseIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseIfStatement" ):
                listener.exitElseIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseIfStatement" ):
                return visitor.visitElseIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def elseIfStatement(self):

        localctx = OGCodeParser.ElseIfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_elseIfStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(OGCodeParser.ELSEIF_KEYWORD)
            self.state = 137
            self.match(OGCodeParser.LEFT_PARENTHESIS)
            self.state = 138
            self.condition()
            self.state = 139
            self.match(OGCodeParser.RIGHT_PARENTHESIS)
            self.state = 140
            self.match(OGCodeParser.LEFT_BRACE)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3864436670464) != 0):
                self.state = 141
                self.body()
                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 147
            self.match(OGCodeParser.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE_KEYWORD(self):
            return self.getToken(OGCodeParser.ELSE_KEYWORD, 0)

        def LEFT_BRACE(self):
            return self.getToken(OGCodeParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(OGCodeParser.RIGHT_BRACE, 0)

        def body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OGCodeParser.BodyContext)
            else:
                return self.getTypedRuleContext(OGCodeParser.BodyContext,i)


        def getRuleIndex(self):
            return OGCodeParser.RULE_elseStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseStatement" ):
                listener.enterElseStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseStatement" ):
                listener.exitElseStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseStatement" ):
                return visitor.visitElseStatement(self)
            else:
                return visitor.visitChildren(self)




    def elseStatement(self):

        localctx = OGCodeParser.ElseStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_elseStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(OGCodeParser.ELSE_KEYWORD)
            self.state = 150
            self.match(OGCodeParser.LEFT_BRACE)
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3864436670464) != 0):
                self.state = 151
                self.body()
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 157
            self.match(OGCodeParser.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REPEAT_KEYWORD(self):
            return self.getToken(OGCodeParser.REPEAT_KEYWORD, 0)

        def LEFT_BRACE(self):
            return self.getToken(OGCodeParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(OGCodeParser.RIGHT_BRACE, 0)

        def NUMBER(self):
            return self.getToken(OGCodeParser.NUMBER, 0)

        def IDENTIFIER(self):
            return self.getToken(OGCodeParser.IDENTIFIER, 0)

        def body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OGCodeParser.BodyContext)
            else:
                return self.getTypedRuleContext(OGCodeParser.BodyContext,i)


        def WHILE_KEYWORD(self):
            return self.getToken(OGCodeParser.WHILE_KEYWORD, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(OGCodeParser.LEFT_PARENTHESIS, 0)

        def condition(self):
            return self.getTypedRuleContext(OGCodeParser.ConditionContext,0)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(OGCodeParser.RIGHT_PARENTHESIS, 0)

        def getRuleIndex(self):
            return OGCodeParser.RULE_loopStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopStatement" ):
                listener.enterLoopStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopStatement" ):
                listener.exitLoopStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopStatement" ):
                return visitor.visitLoopStatement(self)
            else:
                return visitor.visitChildren(self)




    def loopStatement(self):

        localctx = OGCodeParser.LoopStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_loopStatement)
        self._la = 0 # Token type
        try:
            self.state = 182
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.match(OGCodeParser.REPEAT_KEYWORD)
                self.state = 160
                _la = self._input.LA(1)
                if not(_la==40 or _la==41):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 161
                self.match(OGCodeParser.LEFT_BRACE)
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3864436670464) != 0):
                    self.state = 162
                    self.body()
                    self.state = 167
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 168
                self.match(OGCodeParser.RIGHT_BRACE)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.match(OGCodeParser.WHILE_KEYWORD)
                self.state = 170
                self.match(OGCodeParser.LEFT_PARENTHESIS)
                self.state = 171
                self.condition()
                self.state = 172
                self.match(OGCodeParser.RIGHT_PARENTHESIS)
                self.state = 173
                self.match(OGCodeParser.LEFT_BRACE)
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3864436670464) != 0):
                    self.state = 174
                    self.body()
                    self.state = 179
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 180
                self.match(OGCodeParser.RIGHT_BRACE)
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


    class VariableDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET_KEYWORD(self):
            return self.getToken(OGCodeParser.LET_KEYWORD, 0)

        def IDENTIFIER(self):
            return self.getToken(OGCodeParser.IDENTIFIER, 0)

        def ASSIGNMENT_OPERATOR(self):
            return self.getToken(OGCodeParser.ASSIGNMENT_OPERATOR, 0)

        def expression(self):
            return self.getTypedRuleContext(OGCodeParser.ExpressionContext,0)


        def BOOLEAN_TRUE(self):
            return self.getToken(OGCodeParser.BOOLEAN_TRUE, 0)

        def BOOLEAN_FALSE(self):
            return self.getToken(OGCodeParser.BOOLEAN_FALSE, 0)

        def getRuleIndex(self):
            return OGCodeParser.RULE_variableDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDefinition" ):
                listener.enterVariableDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDefinition" ):
                listener.exitVariableDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDefinition" ):
                return visitor.visitVariableDefinition(self)
            else:
                return visitor.visitChildren(self)




    def variableDefinition(self):

        localctx = OGCodeParser.VariableDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_variableDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(OGCodeParser.LET_KEYWORD)
            self.state = 185
            self.match(OGCodeParser.IDENTIFIER)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 186
                self.match(OGCodeParser.ASSIGNMENT_OPERATOR)
                self.state = 190
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [25, 40, 41]:
                    self.state = 187
                    self.expression(0)
                    pass
                elif token in [17]:
                    self.state = 188
                    self.match(OGCodeParser.BOOLEAN_TRUE)
                    pass
                elif token in [18]:
                    self.state = 189
                    self.match(OGCodeParser.BOOLEAN_FALSE)
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


    class AssignmentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(OGCodeParser.AssignmentContext,0)


        def SEMICOLON_SEPARATOR(self):
            return self.getToken(OGCodeParser.SEMICOLON_SEPARATOR, 0)

        def getRuleIndex(self):
            return OGCodeParser.RULE_assignmentStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentStatement" ):
                listener.enterAssignmentStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentStatement" ):
                listener.exitAssignmentStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentStatement" ):
                return visitor.visitAssignmentStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignmentStatement(self):

        localctx = OGCodeParser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.assignment()
            self.state = 195
            self.match(OGCodeParser.SEMICOLON_SEPARATOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(OGCodeParser.IDENTIFIER)
            else:
                return self.getToken(OGCodeParser.IDENTIFIER, i)

        def ASSIGNMENT_OPERATOR(self):
            return self.getToken(OGCodeParser.ASSIGNMENT_OPERATOR, 0)

        def expression(self):
            return self.getTypedRuleContext(OGCodeParser.ExpressionContext,0)


        def BOOLEAN_TRUE(self):
            return self.getToken(OGCodeParser.BOOLEAN_TRUE, 0)

        def BOOLEAN_FALSE(self):
            return self.getToken(OGCodeParser.BOOLEAN_FALSE, 0)

        def STRING(self):
            return self.getToken(OGCodeParser.STRING, 0)

        def getRuleIndex(self):
            return OGCodeParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = OGCodeParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(OGCodeParser.IDENTIFIER)
            self.state = 198
            self.match(OGCodeParser.ASSIGNMENT_OPERATOR)
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 199
                self.expression(0)
                pass

            elif la_ == 2:
                self.state = 200
                self.match(OGCodeParser.BOOLEAN_TRUE)
                pass

            elif la_ == 3:
                self.state = 201
                self.match(OGCodeParser.BOOLEAN_FALSE)
                pass

            elif la_ == 4:
                self.state = 202
                self.match(OGCodeParser.STRING)
                pass

            elif la_ == 5:
                self.state = 203
                self.match(OGCodeParser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(OGCodeParser.ExpressionContext,0)


        def SEMICOLON_SEPARATOR(self):
            return self.getToken(OGCodeParser.SEMICOLON_SEPARATOR, 0)

        def getRuleIndex(self):
            return OGCodeParser.RULE_expressionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatement" ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatement" ):
                listener.exitExpressionStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionStatement" ):
                return visitor.visitExpressionStatement(self)
            else:
                return visitor.visitChildren(self)




    def expressionStatement(self):

        localctx = OGCodeParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.expression(0)
            self.state = 207
            self.match(OGCodeParser.SEMICOLON_SEPARATOR)
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

        def LEFT_PARENTHESIS(self):
            return self.getToken(OGCodeParser.LEFT_PARENTHESIS, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OGCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OGCodeParser.ExpressionContext,i)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(OGCodeParser.RIGHT_PARENTHESIS, 0)

        def NUMBER(self):
            return self.getToken(OGCodeParser.NUMBER, 0)

        def IDENTIFIER(self):
            return self.getToken(OGCodeParser.IDENTIFIER, 0)

        def PLUS_OPERATOR(self):
            return self.getToken(OGCodeParser.PLUS_OPERATOR, 0)

        def MINUS_OPERATOR(self):
            return self.getToken(OGCodeParser.MINUS_OPERATOR, 0)

        def MULTIPLY_OPERATOR(self):
            return self.getToken(OGCodeParser.MULTIPLY_OPERATOR, 0)

        def DIVIDE_OPERATOR(self):
            return self.getToken(OGCodeParser.DIVIDE_OPERATOR, 0)

        def MODULO_OPERATOR(self):
            return self.getToken(OGCodeParser.MODULO_OPERATOR, 0)

        def getRuleIndex(self):
            return OGCodeParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OGCodeParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.state = 210
                self.match(OGCodeParser.LEFT_PARENTHESIS)
                self.state = 211
                self.expression(0)
                self.state = 212
                self.match(OGCodeParser.RIGHT_PARENTHESIS)
                pass
            elif token in [41]:
                self.state = 214
                self.match(OGCodeParser.NUMBER)
                pass
            elif token in [40]:
                self.state = 215
                self.match(OGCodeParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 223
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OGCodeParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 218
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 219
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 124) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 220
                    self.expression(5) 
                self.state = 225
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OGCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OGCodeParser.ExpressionContext,i)


        def EQUAL_OPERATOR(self):
            return self.getToken(OGCodeParser.EQUAL_OPERATOR, 0)

        def UNEQUAL_OPERATOR(self):
            return self.getToken(OGCodeParser.UNEQUAL_OPERATOR, 0)

        def LESSER_OPERATOR(self):
            return self.getToken(OGCodeParser.LESSER_OPERATOR, 0)

        def GREATER_OPERATOR(self):
            return self.getToken(OGCodeParser.GREATER_OPERATOR, 0)

        def LESSER_OR_EQUAL_OPERATOR(self):
            return self.getToken(OGCodeParser.LESSER_OR_EQUAL_OPERATOR, 0)

        def GREATER_OR_EQUAL_OPERATOR(self):
            return self.getToken(OGCodeParser.GREATER_OR_EQUAL_OPERATOR, 0)

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OGCodeParser.ConditionContext)
            else:
                return self.getTypedRuleContext(OGCodeParser.ConditionContext,i)


        def AND_KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(OGCodeParser.AND_KEYWORD)
            else:
                return self.getToken(OGCodeParser.AND_KEYWORD, i)

        def OR_KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(OGCodeParser.OR_KEYWORD)
            else:
                return self.getToken(OGCodeParser.OR_KEYWORD, i)

        def getRuleIndex(self):
            return OGCodeParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = OGCodeParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.expression(0)
            self.state = 227
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32256) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 228
            self.expression(0)
            self.state = 233
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 229
                    _la = self._input.LA(1)
                    if not(_la==15 or _la==16):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 230
                    self.condition() 
                self.state = 235
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LINE_COMMENT(self):
            return self.getToken(OGCodeParser.LINE_COMMENT, 0)

        def BLOCK_COMMENT(self):
            return self.getToken(OGCodeParser.BLOCK_COMMENT, 0)

        def getRuleIndex(self):
            return OGCodeParser.RULE_commentStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommentStatement" ):
                listener.enterCommentStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommentStatement" ):
                listener.exitCommentStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommentStatement" ):
                return visitor.visitCommentStatement(self)
            else:
                return visitor.visitChildren(self)




    def commentStatement(self):

        localctx = OGCodeParser.CommentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_commentStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            _la = self._input.LA(1)
            if not(_la==21 or _la==22):
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


    class CommandBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTIONS_KEYWORDS(self):
            return self.getToken(OGCodeParser.FUNCTIONS_KEYWORDS, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(OGCodeParser.LEFT_PARENTHESIS, 0)

        def RIGHT_PARENTHESIS(self):
            return self.getToken(OGCodeParser.RIGHT_PARENTHESIS, 0)

        def parameters(self):
            return self.getTypedRuleContext(OGCodeParser.ParametersContext,0)


        def getRuleIndex(self):
            return OGCodeParser.RULE_commandBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommandBlock" ):
                listener.enterCommandBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommandBlock" ):
                listener.exitCommandBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommandBlock" ):
                return visitor.visitCommandBlock(self)
            else:
                return visitor.visitChildren(self)




    def commandBlock(self):

        localctx = OGCodeParser.CommandBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_commandBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(OGCodeParser.FUNCTIONS_KEYWORDS)
            self.state = 239
            self.match(OGCodeParser.LEFT_PARENTHESIS)
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40:
                self.state = 240
                self.parameters()


            self.state = 243
            self.match(OGCodeParser.RIGHT_PARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OGCodeParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(OGCodeParser.AssignmentContext,i)


        def COMMA_SEPARATOR(self, i:int=None):
            if i is None:
                return self.getTokens(OGCodeParser.COMMA_SEPARATOR)
            else:
                return self.getToken(OGCodeParser.COMMA_SEPARATOR, i)

        def getRuleIndex(self):
            return OGCodeParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameters" ):
                return visitor.visitParameters(self)
            else:
                return visitor.visitChildren(self)




    def parameters(self):

        localctx = OGCodeParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.assignment()
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 246
                self.match(OGCodeParser.COMMA_SEPARATOR)
                self.state = 247
                self.assignment()
                self.state = 252
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self._predicates[16] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         




