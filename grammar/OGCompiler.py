from OGCodeParser import OGCodeParser
from OGCodeVisitor import OGCodeVisitor
from sympy import sympify
from CompilingHelper import Helper
from PIL import Image, ImageDraw

class OGCompiler(OGCodeVisitor):
    def __init__(self):
        self.output = []
        self.function_name = ""
        self.other_functions = {}
        self.variables_values = {}
        self.isFunction_params = False
        self.function_params = {}
        self.is_pen_up = False
        self.angle = 0
        self.helper = Helper(self)

        # Inicjalizacja obrazu
        self.image_size = (500, 500)
        self.image = Image.new("RGB", self.image_size, "white")
        self.draw = ImageDraw.Draw(self.image)

        # Pozycja startowa (środek obrazu)
        self.current_pos = (self.image_size[0] // 2, self.image_size[1] // 2)

    def compile(self, tree):
        self.visit(tree)
        return "\n".join(self.output)

    def visitProgram(self, ctx):
        self.visit(ctx.funcDefinition())

    def visitFuncDefinition(self, ctx):
        for function in ctx.otherFunction():
            self.visit(function)
        self.visit(ctx.startFunction())

    def visitStartFunction(self, ctx):
        self.function_name = "start"
        self.variables_values[self.function_name] = {}
        self.output.append("G28")
        for value in ctx.body():
            self.visit(value)
        self.output.append("M104 S0")
        self.output.append("M140 S0")
        self.output.append("M02")

    def visitCommandBlock(self, ctx):
        self.isFunction_params = True
        keyword = ""
        if ctx.FUNCTIONS_KEYWORDS():
            keyword = ctx.FUNCTIONS_KEYWORDS().getText()
            if ctx.parameters():
                self.visit(ctx.parameters())
            method = getattr(self.helper, keyword)
            method()

            # Własna obsługa niektórych poleceń rysujących
            if keyword == "FORWARD":
                distance = self.helper.getFloatValue("FORWARD")
                x, y = self.current_pos
                rad = self.angle * 3.14159 / 180
                dx = distance * math.cos(rad)
                dy = -distance * math.sin(rad)
                new_pos = (x + dx, y + dy)
                if not self.is_pen_up:
                    self.draw.line([self.current_pos, new_pos], fill="black", width=2)
                self.current_pos = new_pos

            elif keyword == "LEFT":
                angle = self.helper.getFloatValue("LEFT")
                self.angle = (self.angle + angle) % 360

            elif keyword == "RIGHT":
                angle = self.helper.getFloatValue("RIGHT")
                self.angle = (self.angle - angle) % 360

            elif keyword == "PENUP":
                self.is_pen_up = True

            elif keyword == "PENDOWN":
                self.is_pen_up = False

        elif ctx.IDENTIFIER():
            keyword = ctx.IDENTIFIER().getText()
            if keyword in self.other_functions:
                previous_func_name = self.function_name
                self.function_name = keyword
                if ctx.parameters():
                    self.isFunction_params = False
                    self.visit(ctx.parameters())
                    self.isFunction_params = True
                    self.function_params.clear()
                for line in self.other_functions[keyword]["body"]:
                    self.visit(line)
                self.function_name = previous_func_name

        self.isFunction_params = False
        self.function_params.clear()

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
        if self.isFunction_params:
            self.function_params[ctx.IDENTIFIER(0).getText()] = value
        else:
            self.variables_values[self.function_name][ctx.IDENTIFIER(0).getText()] = value
                

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
            raise Exception(f"Nieznany operator porównania: {operator}")
        
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
                raise Exception(f"Nieznany operator logiczny: {logic_op}")
            i += 4  # Przejście do kolejnego operatora logicznego
        return result
  