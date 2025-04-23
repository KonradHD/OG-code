//Grammar 

program := funcDefinition


funcDefinition := FUNCTION_KEYWORD START_KEYWORD LEFT_PARENTHESIS parametersDefinition? RIGHT_PARENTHESIS LEFT_BRACE body returnStatement? LEFT_PARENTHESIS |
                  FUNCTION_KEYWORD IDENTIFIER LEFT_PARENTHESIS parametersDefinition? RIGHT_PARENTHESIS LEFT_BRACE body returnStatement? LEFT_PARENTHESIS funcDefinition

parametersDefinition := LET_KEYWORD IDENTIFIER (COMMA_SEPARATOR LET_KEYWORDS IDENTIFIER)*

returnStatement := RETURN_KEYWORD expression

body := loopStatement |
        commandBlock | 
        variableDefinition |
        expression | 
        ifStatement | 
        assignment | 
        incrementDecrementStatement | 
        commentStatement | 
        body body 

incrementDecrementStatement := IDENTIFIER (INCREMENT_OPERATOR | DECREMENT_OPERATOR)

ifStatement := IF_KEYWORD statement (ELSEIF_KEYWORD statement)* (ELSE_KEYWORD statement)?

statement := LEFT_PARENTHESIS condition RIGHT_PARENTHESIS LEFT_BRACES body RIGHT_BRACES

loopStatement := REPEAT_KEYWORD number LEFT_BRACE body RIGHT_BRACE | 
                  WHILE_KEYWORD statement

number := '[0-9]+(.[0-9])?[0-9]*'

variableDefinition := LET_KEYWORD IDENTIFIER (ASSIGNMENT_OPERATOR (expression | BOOLEAN_TRUE | BOOLEAN_FALSE))?

assignment := IDENTIFIER ASSIGNMENT_OPERATOR (expression | BOOLEAN_TRUE | BOOLEAN_FALSE)

expression := expression (PLUS_OPERATOR | MINUS_OPERATOR | MULTIPLY_OPERATOR | DIVIDE_OPERATOR | MODULO_OPERATOR) expression | 
              LEFT_PARENTHESIS expression RIGHT_PARENTHESIS | 
              number |
              IDENTIFIER

condition := expression (EQUAL_OPERATOR | UNEQUAL_OPERATOR | LESSER_OPERATOR | GREATER_OPERATOR | LESSER_OR_EQUAL_OPERATOR | GREATER_OR_EQUAL_OPERATOR) expression ((AND_KEYWORD | OR_KEYWORD) condition)*

commentStatement := COMMENT_LINE .* |
                    COMMENT_START_BLOCK .* COMMENT_END_BLOCK

commandBlock := FUCNTIONS_KEYWORDS LEFT_PARENTHESIS parameters? RIGHT_PARENTHESIS

parameters := assignment+
      

// Arithmetic operators 
ASSIGNMENT_OPERATOR : '=';
PLUS_OPERATOR : '+';
MINUS_OPERATOR : '-';
MULTIPLY_OPERATOR : '*';
DIVIDE_OPERATOR : '/';
MODULO_OPERATOR : '%';
INCREMENT_OPERATOR : '++';
DECREMENT_OPERATOR : '--';
EQUAL_OPERATOR : '==';
UNEQUAL_OPERATOR : '!=';
LESSER_OPERATOR : '<';
GREATER_OPERATOR : '>';
LESSER_OR_EQUAL_OPERATOR : '<=';
GREATER_OR_EQUAL_OPERATOR : '>=';

// Logic operators
AND_KEYWORD : 'and';
OR_KEYWORD : 'or';

// Logic constants
BOOLEAN_TRUE : 'True';
BOOLEAN_FALSE : 'False';

// Separators
COMMA_SEPARATOR : ',';

// Comments
COMMENT_LINE : '//';
COMMENT_START_BLOCK : '/*';
COMMENT_END_BLOCK : '*/';

// Brackets
LEFT_BRACKET : '[';
RIGHT_BRACKET : ']';
LEFT_PARENTHESIS : '(';
RIGHT_PARENTHESIS : ')';
LEFT_BRACE : '{';
RIGHT_BRACE : '}';

// Keywords 
FUNCTION_KEYWORD : 'function';
LET_KEYWORD : 'let';
REPEAT_KEYWORD : 'repeat';
WHILE_KEYWORD : 'while';
IF_KEYWORD : 'if';
ELSE_KEYWORD : 'else';
ELSEIF_KEYWORD : 'elseif';
RETURN_KEYWORD : 'return';
BREAK_KEYWORD : 'break';
START_KEYWORD : 'start';
FUNCTIONS_KEYWORDS : ['forward', 'move', 'turn', 'penUp', 'penDown', 'setSpeed', 'setPenTemp', 'circle', 'wait', 'cleanNozzle', 'ground', 'unit', 'autoLevel', 'setTableTemp', 'cooler', 'absolutePositioning', 'filledCircle',
'drawLetter'];
IDENTIFIER : '[A-Za-z_][A-Za-z_0-9]*';

forward(30, axis='X'/'Y'/'Z') - do przodu 30 mm - G0, G1
setPenTemp(344, wait=True) - M104 S200, M109 S200
setTableTemp() - M140 S60, M190 S60
move(x=30, y=43 z=45), przesuń się do xyz - G0, G1
turn() - skręca w prawo o x stopni - 
circle(R=30, X=0, Y=0) - rysuje okrąg o promieniu R i środku w X, Y - G3, G4
wait(300) - G4 
cleanNozzle() - usuwanie pozostałości atramentu z dyszy - G12
ground(XY/XZ/YZ) - wybieranie płaszczyzny w której operuje głowica - G17-19
unit("inches", "milimeters", "centimeters") - wybór jednostki - G20, G21
autoLevel(save=True) - uruchamia procedurę automatycznego poziomowania stołu, jeżeli true to zapisuje konfiguracje - G29
cooler(True) - włącza wentylator - M106, M107
absolutePositioning(True) - pozycje absolutne - G90, G91
filledCircle(R=30, X=0, Y=0) - rysuje wypełnione koło 
drawLetter(letter="M", L=100, W=50, X0=0, Y0=0) - rysuje literke M, X0, Y0 - pozycja środkowa, L - długość prostokąta, w którym literka będzie się mieścić, W - szerokość prostokąta 
