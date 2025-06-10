from OGCodeParser import OGCodeParser
from OGCodeVisitor import OGCodeVisitor
from sympy import sympify
from CompilingHelper import Helper
from intersectionAnalyzer import intersectionAnalyzer


class OGCompiler(OGCodeVisitor):
    def __init__(self):
        self.output = [] 
        self.function_name = "" # currently compiling function
        self.other_functions = {} # function_name:  { "params": ["W", "H"], "body": ctx.body() }
        self.variables_values = {} # function_name : {var : value }
        self.isFunction_params = False
        self.function_params = {}
        self.pen_up = False
        self.helper = Helper(self)
        self.intersection_analyzer = intersectionAnalyzer()
        self.position = (110, 110, 0.2) # x, y, z - surface_number
        self.angle = 0  # W stopniach
        self.drawing = []


    def compile(self, tree):
        self.visit(tree)
        gcode_str = '\n'.join(self.output)
        print("compile zwraca gcode i rysunek")
        print(f"gcode:\n{gcode_str[:100]}...")  # pokaż pierwsze 100 znaków
        print(f"drawing: {self.drawing[:5]}")   # pokaż kilka elementów rysunku
        return gcode_str, self.drawing
    
    def visitProgram(self, ctx):
        self.visit(ctx.funcDefinition())


    def visitFuncDefinition(self, ctx):
        for function in ctx.otherFunction():
            self.visit(function)
        self.visit(ctx.startFunction())


    def visitStartFunction(self, ctx):
        self.function_name = "start"
        self.variables_values[self.function_name] = {}
        self.output.append("M201 X2500 Y2500 Z500 E5000")
        self.output.append("M203 X250 Y250 Z5 E40")
        self.output.append("M204 P2500 R500 T2500 ; sets acceleration (P, T) and retract acceleration (R)")
        self.output.append("M205 X10.00 Y10.00 Z0.40 E5.00 ; sets the jerk limits, mm/sec")
        self.output.append("M220 S100 ;Reset Feedrate")
        self.output.append("M221 S100 ;Reset Flowrate")
        self.output.append("M104 S220 ;Set final nozzle temp")
        self.output.append("M140 S55")
        self.output.append("M190 S55 ;Set and wait for bed temp to stabilize ")
        self.output.append("M109 S220")
        self.output.append("G28")# można coś dodać jeszcze 
        self.output.append("G92 E0 ;Reset Extruder")
        self.output.append("G1 F1000 ")
        self.output.append(f"; warstwa {(int)((self.position[2]/2)*10)}")
        self.output.append("G0 Z0.2 F600; move up")
        self.output.append("G0 X110 Y110 F3000;move to center")
        self.output.append("M83") # tryb przyrostowy ekstrudera
        for value in ctx.body():
            self.visit(value)
        self.output.append("; --- KONIEC ---")
        self.output.append("G1 E120.2 F1800 ; retract")
        self.output.append("G1 Z5 F600")
        self.output.append("G0 X0 Y0 F3000")
        self.output.append("M104 S0 ;Turn-off hotend") # wyłączenie grzałki ekstrudera
        self.output.append("M140 S0 ;Turn-off bed") # wyłączenie grzałki stołu grzewczego
        self.output.append("M106 S0 ;Turn-off fan ")
        self.output.append("M84 ;Disable all steppers") # zakończenie programu i reset parametrów


    def visitOtherFunction(self, ctx):
        self.function_name = ctx.IDENTIFIER().getText()
        self.variables_values[self.function_name] = {}
        self.other_functions[self.function_name] = {}
        params = []
        if ctx.parametersDefinition():
            params = self.visit(ctx.parametersDefinition())
        self.other_functions[self.function_name]["params"] = params
        self.other_functions[self.function_name]["body"] = []
        for value in ctx.body():
            self.other_functions[self.function_name]["body"].append(value)


    def visitParametersDefinition(self, ctx):
        params = []
        if ctx.IDENTIFIER():
            params = [id.getText() for id in ctx.IDENTIFIER()]
        return params


    def visitExpressionStatement(self, ctx):
        self.visit(ctx.expression())


    def visitExpression(self, ctx):
        if ctx.getChildCount() == 1:
            if ctx.NUMBER():
                return ctx.NUMBER().getText()
            if ctx.IDENTIFIER():
                var = ctx.IDENTIFIER().getText()
                return self.helper.getFloatValue(var)
            return "" 
        else:
            for i in range(ctx.getChildCount()):
                expr = ""
                for i in range(ctx.getChildCount()):
                    child = ctx.getChild(i)
                    text = child.getText()
                    # Rekurencyjnie odwiedzaj tylko te, które są expression
                    if child.getChildCount() > 0:
                        expr += str(self.visit(child))
                    else:
                        expr += text
            return expr


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
                value = self.variables_values[self.function_name].get(var)
                if value is None:
                    raise Exception(f"Variable {var} does not exist.")
            for _ in range(0, int(value)):
                for body in ctx.body():
                    self.visit(body)
        elif ctx.WHILE_KEYWORD():
            while self.visit(ctx.condition()):
                for value in ctx.body():
                    self.visit(value)   

    
    def visitCommandBlock(self, ctx):
        self.isFunction_params = True
        keyword = ""
        if ctx.FUNCTIONS_KEYWORDS():
            keyword = ctx.FUNCTIONS_KEYWORDS().getText()
            if ctx.parameters():
                self.visit(ctx.parameters())
            method = getattr(self.helper, keyword)
            method()

        if ctx.IDENTIFIER():
            keyword = ctx.IDENTIFIER().getText()
        # wywołanie zdefiniowanych funkcji
            if keyword in self.other_functions:
                previous_func_name = self.function_name
                if not ctx.parameters():
                    self.function_name = keyword
                    for line in self.other_functions[keyword]["body"]:
                        self.visit(line)
                else:
                    self.function_name = keyword
                    self.isFunction_params = False
                    self.visit(ctx.parameters()) # przypisanie wartości parametrów funkcji do self.function_params
                    self.isFunction_params = True
                    self.function_params.clear()
                    for line in self.other_functions[keyword]["body"]:
                        self.visit(line)
                self.function_name = previous_func_name
            else:
                raise Exception(f"Function {keyword} does not exist.")
        self.isFunction_params = False
        self.function_params.clear()


    def visitParameters(self, ctx):
        for assig in ctx.assignment():
            self.visit(assig)
    

    def visitAssignment(self, ctx):
        if ctx.expression():
            value = float(sympify(self.visit(ctx.expression())))
        if ctx.BOOLEAN_FALSE():
            value = "false"
        if ctx.BOOLEAN_TRUE():
            value = "true"
        if ctx.STRING():
            value = ctx.STRING().getText()
        if ctx.IDENTIFIER(1):
            name = ctx.IDENTIFIER(1).getText()
            value = self.variables_values[self.function_name].get(name)
            if value is None:
                raise Exception(f"Variable {name} does not exist.")
        variable = ctx.IDENTIFIER(0).getText()
        if self.isFunction_params:
            self.function_params[variable] = value
        else: 
            self.variables_values[self.function_name][variable] = value
                

    def visitVariableDefinition(self, ctx):
        if ctx.ASSIGNMENT_OPERATOR():
            if ctx.expression():
                value = float(sympify(self.visit(ctx.expression())))
            if ctx.BOOLEAN_FALSE():
                value = ctx.BOOLEAN_FALSE.getText()
            if ctx.BOOLEAN_TRUE():
                value = ctx.BOOLEAN_TRUE().getText()
            self.variables_values[self.function_name][ctx.IDENTIFIER().getText()] = value
        else:
            self.variables_values[self.function_name][ctx.IDENTIFIER().getText()] = None


    def visitIfStatement(self, ctx):
        if self.visit(ctx.condition()):
            for value in ctx.body():
                self.visit(value)
        elif ctx.elseIfStatement():
            for value in ctx.elseIfStatement():
                self.visit(value)
        elif ctx.elseStatement():
            self.visit(ctx.elseStatement())

    
    def visitElseIfStatement(self, ctx):
        if self.visit(ctx.condition()):
            for value in ctx.body():
                self.visit(value)


    def visitElseStatement(self, ctx):
        for value in ctx.body():
            self.visit(value)


    def visitIncrementDecrementStatement(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        value = self.helper.getFloatValue(var_name)
        if value is None:
            raise Exception(f"Variable {var_name} does not exist.")
        if ctx.INCREMENT_OPERATOR():
            value += 1
        if ctx.DECREMENT_OPERATOR():
            value -= 1
        self.variables_values[self.function_name][var_name] = value
        
        
    def visitCommentStatement(self, ctx):
        if ctx.LINE_COMMENT():
            self.output.append(f";{ctx.LINE_COMMENT().getText()[2:]}")
        if ctx.BLOCK_COMMENT():
            comment = ctx.BLOCK_COMMENT().getText()[2:-2]
            lines = comment.split("\n")
            for line in lines:
                self.output.append(f";{line.strip()}")
        

    def visitCondition(self, ctx):
        left = float(sympify(self.visit(ctx.expression(0))))
        right = float(sympify(self.visit(ctx.expression(1))))
        operator = ctx.getChild(1).getText()

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
            raise Exception(f"Unkown comparing operator: {operator}")
        
        left = self.helper.getFloatValue(left)
        right = self.helper.getFloatValue(right)
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
                raise Exception(f"Unknown logic operator: {logic_op}")
            i += 4  # Przejście do kolejnego operatora logicznego
        return result
    