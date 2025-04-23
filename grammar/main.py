from antlr4 import *
from OGCodeLexer import OGCodeLexer
from OGCodeParser import OGCodeParser


def main():
    with open("OG-code.example", "r") as program_file:
        input_code = program_file.read()
    input_stream = InputStream(input_code)

    lexer = OGCodeLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = OGCodeParser(token_stream)

    tree = parser.program()

    print(tree.toStringTree(recog=parser))


if __name__ == '__main__':
    main()
