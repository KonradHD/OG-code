from antlr4 import *
from OGCodeLexer import OGCodeLexer
from OGCodeParser import OGCodeParser


def print_tree(node, indent=0):
    node_text = node.getText() if hasattr(node, 'getText') else ""
    print("  " * indent + f"{type(node).__name__}: {node_text}")
    for i in range(node.getChildCount()):
        print_tree(node.getChild(i), indent + 1)


def main():
    with open("OG-code.example", "r") as program_file:
        input_code = program_file.read()
    input_stream = InputStream(input_code)

    lexer = OGCodeLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = OGCodeParser(token_stream)

    tree = parser.program()
    print_tree(tree)


if __name__ == '__main__':
    main()
