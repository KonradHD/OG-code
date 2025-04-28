from antlr4 import *
from OGCodeLexer import OGCodeLexer
from OGCodeParser import OGCodeParser

# Kolory CSS dla różnych tokenów
TOKEN_COLORS = {
    'BOOLEAN_TRUE': 'color: green;',
    'BOOLEAN_FALSE': 'color: red;',
    'NUMBER': 'color: blue;',
    'STRING': 'color: purple;',
    'IDENTIFIER': 'color: black;',
    'FUNCTION_KEYWORD': 'color: orange;',
    'LET_KEYWORD': 'color: orange;',
    'IF_KEYWORD': 'color: orange;',
    'ELSE_KEYWORD': 'color: orange;',
    'WHILE_KEYWORD': 'color: orange;',
    'RETURN_KEYWORD': 'color: orange;',
    'EQUAL_OPERATOR': 'color: purple;',
    'PLUS_OPERATOR': 'color: purple;',
    'MINUS_OPERATOR': 'color: purple;',
    'MULTIPLY_OPERATOR': 'color: purple;',
    'DIVIDE_OPERATOR': 'color: purple;',
    'MODULO_OPERATOR': 'color: purple;',
    'AND_KEYWORD': 'color: teal;',
    'OR_KEYWORD': 'color: teal;',
    'COMMA_SEPARATOR': 'color: gray;',
    'SEMICOLON_SEPARATOR': 'color: gray;',
    'LINE_COMMENT': 'color: gray;',
    'BLOCK_COMMENT': 'color: gray;',
}

def generate_colored_html(input_code):
    # Dodajemy <pre> do HTML, aby zachować białe znaki i nowe linie
    colored_code = "<pre>"
    
    # Przechodzimy po każdym znaku w kodzie wejściowym
    for char in input_code:
        # Jeśli napotkamy nową linię, zachowujemy ją
        if char == '\n':
            colored_code += '<br>'
            continue
        # Jeśli napotkamy spację, zachowujemy ją
        elif char == ' ':
            colored_code += '&nbsp;'  # Zamiana na non-breaking space
            continue

        # Teraz musimy sprawdzić tokeny, które będą kolorowane
        token_text = char
        token_type = None

        # Tokenizacja za pomocą lexer'a
        input_stream = InputStream(token_text)
        lexer = OGCodeLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        token_stream.fill()

        # Sprawdzamy typ tokenu
        for token in token_stream.tokens:
            token_type = token.type
        
        # Przypisujemy odpowiedni kolor na podstawie typu tokenu
        token_style = TOKEN_COLORS.get(OGCodeLexer.symbolicNames[token_type], None)
        if token_style:
            colored_code += f'<span style="{token_style}">{token_text}</span>'
        else:
            colored_code += token_text  # Jeśli brak koloru, dodajemy tekst bez zmian
    
    colored_code += "</pre>"

    # Cały wynik HTML
    return f'<html><body>{colored_code}</body></html>'

def main():
    with open("OG-code.example", "r") as program_file:
        input_code = program_file.read()

    colored_html = generate_colored_html(input_code)

    with open("colored_output.html", "w") as output_file:
        output_file.write(colored_html)

if __name__ == '__main__':
    main()
