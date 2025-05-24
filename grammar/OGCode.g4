grammar OGCode;

program : funcDefinition;

funcDefinition : otherFunction* startFunction;

startFunction : FUNCTION_KEYWORD START_KEYWORD LEFT_PARENTHESIS RIGHT_PARENTHESIS LEFT_BRACE body* RIGHT_BRACE;

otherFunction : FUNCTION_KEYWORD IDENTIFIER LEFT_PARENTHESIS parametersDefinition? RIGHT_PARENTHESIS LEFT_BRACE body* RIGHT_BRACE;

parametersDefinition : LET_KEYWORD IDENTIFIER (COMMA_SEPARATOR LET_KEYWORD IDENTIFIER)*;

body : loopStatement |
        commandBlock SEMICOLON_SEPARATOR | 
        variableDefinition SEMICOLON_SEPARATOR |
        expressionStatement | 
        ifStatement | 
        assignmentStatement | 
        incrementDecrementStatement SEMICOLON_SEPARATOR | 
        commentStatement;

incrementDecrementStatement : IDENTIFIER (INCREMENT_OPERATOR | DECREMENT_OPERATOR);

ifStatement : IF_KEYWORD LEFT_PARENTHESIS condition RIGHT_PARENTHESIS LEFT_BRACE body* RIGHT_BRACE (elseIfStatement)* (elseStatement)?;

elseIfStatement : ELSEIF_KEYWORD LEFT_PARENTHESIS condition RIGHT_PARENTHESIS LEFT_BRACE body* RIGHT_BRACE;

elseStatement : ELSE_KEYWORD LEFT_BRACE body* RIGHT_BRACE;

loopStatement : REPEAT_KEYWORD (NUMBER | IDENTIFIER) LEFT_BRACE body* RIGHT_BRACE | 
                  WHILE_KEYWORD LEFT_PARENTHESIS condition RIGHT_PARENTHESIS LEFT_BRACE body* RIGHT_BRACE;

variableDefinition : LET_KEYWORD IDENTIFIER (ASSIGNMENT_OPERATOR (expression | BOOLEAN_TRUE | BOOLEAN_FALSE))?;

assignmentStatement : assignment SEMICOLON_SEPARATOR;

assignment : IDENTIFIER ASSIGNMENT_OPERATOR (expression | BOOLEAN_TRUE | BOOLEAN_FALSE | STRING | IDENTIFIER);

expressionStatement : expression SEMICOLON_SEPARATOR;

expression : expression (MULTIPLY_OPERATOR | DIVIDE_OPERATOR | MODULO_OPERATOR) expression |
            expression (PLUS_OPERATOR | MINUS_OPERATOR) expression |
            LEFT_PARENTHESIS expression RIGHT_PARENTHESIS | 
            NUMBER |
            IDENTIFIER | 
            MINUS_OPERATOR expression;


condition : expression (EQUAL_OPERATOR | UNEQUAL_OPERATOR | LESSER_OPERATOR | GREATER_OPERATOR | LESSER_OR_EQUAL_OPERATOR | GREATER_OR_EQUAL_OPERATOR) expression ((AND_KEYWORD | OR_KEYWORD) condition)*;

commentStatement : LINE_COMMENT | BLOCK_COMMENT;

commandBlock : (FUNCTIONS_KEYWORDS | IDENTIFIER) LEFT_PARENTHESIS parameters? RIGHT_PARENTHESIS;

parameters : assignment (COMMA_SEPARATOR assignment)*;
      

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
BOOLEAN_TRUE : 'true';
BOOLEAN_FALSE : 'false';

// Separators
COMMA_SEPARATOR : ',';
SEMICOLON_SEPARATOR : ';';

// Comments
LINE_COMMENT : '//' ~[\r\n]*;
BLOCK_COMMENT : '/*' .*? '*/';

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
START_KEYWORD : 'start';
FUNCTIONS_KEYWORDS : 'forward' | 'move' | 'turn' | 'penUp' | 'penDown' | 'setPenTemp'
    | 'circle' | 'wait' | 'cleanNozzle' | 'ground' | 'unit' | 'autoLevel' | 'setAngle'
    | 'setTableTemp' | 'cooler' | 'absolutePositioning' | 'filledCircle' | 'drawLetter' 
    | 'moveVertically' | 'square' | 'nextSurface';

// Helpers
IDENTIFIER : [A-Za-z_][A-Za-z_0-9]*;
NUMBER : '-'?[0-9]+ ('.' [0-9]+)?;
WS : [ \t\r\n]+ -> skip ; // Ignoruj białe znaki
STRING : '\'' (~[\n'\r])* '\'';
