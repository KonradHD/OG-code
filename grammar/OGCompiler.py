from OGCodeParser import OGCodeParser
from OGCodeVisitor import OGCodeVisitor
import math

class OGCompiler(OGCodeVisitor):
    def __init__(self):
        self.output = []
        self.func_names_and_params = {} # "return" - value to będzie wartość zwraca przez funkcje
        self.variables_values = {}
        self.isFunction_params = False
        self.function_params = {}
        self.is_pen_up = False
        self.angle = 0


    def compile(self, tree):
        self.visit(tree)
        return "\n".join(self.output)

    
    def visitProgram(self, ctx):
        self.visit(ctx.funcDefinition())


    def visitFuncDefinition(self, ctx):
        self.visit(ctx.startFunction())
        for function in ctx.otherFunction():
            self.visit(function)


    def visitStartFunction(self, ctx):
        self.output.append("G28")# można coś dodać jeszcze 
        for value in ctx.body():
            self.visit(value)
        self.output.append("M104 S0") # wyłączenie grzałki ekstrudera
        self.output.append("M140 S0") # wyłączenie grzałki stołu grzewczego
        self.output.append("M02") # zakończenie programu i reset parametrów
        self.variables_values.clear()


    def visitOtherFunction(self, ctx):
        function_name = ctx.IDENTIFIER().getText()
        if ctx.parametersDefinition():
            params = self.visit(ctx.parametersDefinition())
        self.func_names_and_params[function_name] = params
        for param in params:
            self.variables_values[param] = None
        for value in ctx.body():
            self.visit(value)
        if ctx.returnStatement():
            self.visit(ctx.returnStatement())
        self.output.append("}")
        self.variables_values.clear()


    def visitParametersDefinition(self, ctx):
        params = [id for id in ctx.IDENTIFIER()]
        return params
    

    def visitReturnStatement(self, ctx):
        expression = self.visit(ctx.expressionStatement())
        self.func_names_and_params["return"] = expression


    def visitExpressionStatement(self, ctx):
        self.visit(ctx.expression())


    def visitExpression(self, ctx):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.getChild(0))
            operator = ctx.getChild(1).getText()
            right = self.visit(ctx.getChild(2))
            return f"({left} {operator} {right})"
        elif ctx.getChildCount() == 1:
            return ctx.getChild(0).getText()
        else:
            # Obsługa innych przypadków, np. wyrażeń w nawiasach
            return self.visitChildren(ctx)
            # nwm czy to git 



    def visitBody(self, ctx):
        if ctx.loopStatement():
            self.visit(ctx.loopStatement())
        if ctx.commandBlock():
            self.visit(ctx.commandBlock())
        if ctx.variableDefinition():
            self.visit(ctx.variableDefinition())
        if ctx.expressionStatement():
            self.visit(ctx.expressionStatement())
        if ctx.ifStatement():
            self.visit(ctx.ifStatement())
        if ctx.assignmentStatement():
            self.visit(ctx.assignmentStatement())
        if ctx.incrementDecrementStatement():
            self.visit(ctx.incrementDecrementStatement())
        if ctx.commentStatement():
            self.visit(ctx.commentStatement())


    def visitAssignmentStatement(self, ctx):
        self.visit(ctx.assignment())
    

    def visitLoopStatement(self, ctx):
        if ctx.REPEAT_KEYWORD():
            if ctx.NUMBER():
                value = ctx.NUMBER().getText()
            else:
                var = ctx.IDENTIFIER().getText()
                value = self.variables_values.get(var)
            for _ in range(0, int(value)):
                for value in ctx.body():
                    self.visit(value)
        elif ctx.WHILE_KEYWORD():
            while self.visit(ctx.condition()):
                for value in ctx.body():
                    self.visit(value)   

    
    def visitCommandBlock(self, ctx):
        self.isFunction_params = True
        keyword = ctx.FUNCTIONS_KEYWORDS().getText()
        print(self.variables_values)
        if ctx.parameters():
            self.visit(ctx.parameters())
            if keyword == "setAngle":
                self.angle = self.getFloatValue("angle")
            if keyword == "forward":
                print(self.function_params)
                axis = self.getXYZValue("axis")
                length = self.getFloatValue("L")
                if axis is None:
                    angle_rad = math.radians(self.angle)
                    x = math.cos(angle_rad)*length 
                    y = math.sin(angle_rad)*length
                    self.output.append(f"G1 X{x} Y{y}" if self.is_pen_up else f"G0 X{x} Y{y} F1000")
                else:
                    self.output.append("G91") # włączenie pozycjonowania względnego
                    self.output.append(f"G1 {axis}{length}" if self.is_pen_up else f"G0 {axis}{length} F1000")
                    self.output.append("G90") # włączenie pozycjonowania bezwzględnego
            if keyword == "setPenTemp":
                temp = self.getFloatValue("T")
                self.output.append(f"M104 S{temp}" if not self.getBoolValue("wait") else f"M109 S{temp}")
            if keyword == "ground":
                surface = self.getXYZValue("surface")
                if surface == "XY":
                    self.output.append("G17")
                elif surface == "XZ":
                    self.output.append("G18")
                elif surface == "YZ":
                    self.output.append("G19")
            if keyword == "autoLevel":
                self.output.append("G29")
                if self.getBoolValue("save"):
                    self.output.append("M500")
            if keyword == "turn":
                angle = self.getFloatValue("angle")
                self.angle = (angle + self.angle)%360
            if keyword == "move":
                x = self.getFloatValue("X")
                y = self.getFloatValue("Y")
                self.output.append(f"G1 X{x} Y{y}" if self.is_pen_up else f"G0 X{x} Y{y} F1000")
        else:
            if keyword == "penDown":
                self.is_pen_up = False
                self.output.append("G1 Z5 F300") # przestań rysować
            if keyword == "penUp":
                self.is_pen_up = True
                self.output.append("G1 Z0 F300") # rysuj
        self.isFunction_params = False
        self.function_params.clear()


    def getFloatValue(self, variable):
        try: 
            return float(variable)
        except:
            if self.isFunction_params:
                value = self.function_params.get(variable)
            else:
                value = self.variables_values.get(variable)
            try:
                float(value)
            except:
                if self.variables_values.get(value):
                    value = self.variables_values.get(value)
            return float(value)


    def getXYZValue(self, variable):
        axis = self.function_params.get(variable)
        if axis is None:
            return None
        if axis.find("'") != -1:
            axis = axis.replace("'", "")
            if axis not in ("X", "Y", "Z", "XY", "YZ", "XZ"):
                return None
            return axis
        if self.variables_values.get(axis):
            axis = self.variables_values.get(axis)
        return axis
    

    def getBoolValue(self, variable):
        value = self.function_params.get(variable)
        if value in ("true", "false"):
            return value == "true"
        if self.variables_values.get(value):
            new_value = self.variables_values.get(value)
            if new_value in ("true", "false"):
                return new_value == "true"
        return None
    

    def visitParameters(self, ctx):
        for assig in ctx.assignment():
            self.visit(assig)
    

    def visitAssignment(self, ctx):
        if ctx.expression():
            value = self.visit(ctx.expression())
        if ctx.BOOLEAN_FALSE():
            value = "false"
        if ctx.BOOLEAN_TRUE():
            value = "true"
        if ctx.STRING():
            value = ctx.STRING().getText()
        if ctx.IDENTIFIER(1):
            name = ctx.IDENTIFIER(1).getText()
            value = self.variables_values.get(name)
        if self.isFunction_params:
            self.function_params[ctx.IDENTIFIER(0).getText()] = value
        else:
            self.variables_values[ctx.IDENTIFIER(0).getText()] = value
                

    def visitVariableDefinition(self, ctx):
        if ctx.ASSIGNMENT_OPERATOR():
            if ctx.expression():
                value = self.visit(ctx.expression())
            if ctx.BOOLEAN_FALSE():
                value = ctx.BOOLEAN_FALSE.getText()
            if ctx.BOOLEAN_TRUE():
                value = ctx.BOOLEAN_TRUE().getText()
            self.variables_values[ctx.IDENTIFIER().getText()] = value
        else:
            self.variables_values[ctx.IDENTIFIER().getText()] = None


    def visitIfStatement(self, ctx):
        if self.visit(ctx.condition()):
            for value in ctx.body():
                self.visit(value)
        elif ctx.elseIfStatement():
            for value in ctx.elseIfStatement():
                self.visit(value)
        elif ctx.elseStatement():
            self.visit(ctx.elseStatement)

    
    def visitElseIfStatement(self, ctx):
        if self.visit(ctx.condition()):
            for value in ctx.body():
                self.visit(value)


    def visitElseStatement(self, ctx):
        for value in ctx.body():
            self.visit(value)


    def visitIncrementDecrementStatement(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        value = self.getFloatValue(var_name)
        if ctx.INCREMENT_OPERATOR():
            value += 1
        if ctx.DECREMENT_OPERATOR():
            value -= 1

        self.variables_values[var_name] = value
        
        
    def visitCommentStatement(self, ctx):
        if ctx.LINE_COMMENT():
            self.output.append(f";{ctx.LINE_COMMENT().getText()[2:]}")
        if ctx.BLOCK_COMMENT():
            comment = ctx.BLOCK_COMMENT().getText()[2:-2]
            lines = comment.split("\n")
            for line in lines:
                self.output.append(f";{line.strip()}")
        

    def visitCondition(self, ctx):
        # Ocena lewej strony wyrażenia
        left = self.visit(ctx.expression(0))
        print(left)
        # Ocena prawej strony wyrażenia
        right = self.visit(ctx.expression(1))
        print(right)
        # Pobranie operatora porównania
        operator = ctx.getChild(1).getText()
        print(operator)

        # Mapowanie operatorów na funkcje porównujące
        operators = {
            '==': lambda a, b: a == b,
            '!=': lambda a, b: a != b,
            '<': lambda a, b: a < b,
            '>': lambda a, b: a > b,
            '<=': lambda a, b: a <= b,
            '>=': lambda a, b: a >= b,
        }

        # Sprawdzenie, czy operator jest obsługiwany
        if operator not in operators:
            raise Exception(f"Nieznany operator porównania: {operator}")
        
        left = self.getFloatValue(left)
        print(left)
        right = self.getFloatValue(right)
        print(right)
        # Ocena podstawowego warunku
        result = operators[operator](left, right)

        # Obsługa złożonych warunków logicznych (AND, OR)
        i = 3  # Indeks pierwszego operatora logicznego
        while i < ctx.getChildCount():
            logic_op = ctx.getChild(i).getText().lower()
            next_condition = self.visit(ctx.condition(i // 4))
            if logic_op == 'and':
                result = result and next_condition
            elif logic_op == 'or':
                result = result or next_condition
            else:
                raise Exception(f"Nieznany operator logiczny: {logic_op}")
            i += 4  # Przejście do kolejnego operatora logicznego
        print(result)
        return result


        
