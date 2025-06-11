from antlr4 import *
from OGCodeLexer import OGCodeLexer
from OGCodeParser import OGCodeParser
from OGCompiler import OGCompiler
from MyErrorListener import MyErrorListener


def create_parser_from_input(input_stream):
    lexer = OGCodeLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = OGCodeParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(MyErrorListener())
    return parser


def print_tree(node, indent=0):
    node_text = node.getText() if hasattr(node, 'getText') else ""
    print("  " * indent + f"{type(node).__name__}: {node_text}")
    for i in range(node.getChildCount()):
        print_tree(node.getChild(i), indent + 1)


def compile_to_GCode(input_path, output_path):
    OG_content = FileStream(input_path, encoding="utf-8")
    parser = create_parser_from_input(OG_content)
    tree = parser.program()
    compiler = OGCompiler()
    g_code, drawing_data = compiler.compile(tree)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(g_code)


def main():
    with open("../examples/circles_example.txt", "r", encoding="utf-8") as program_file:
        input_code = program_file.read()

    input_stream = InputStream(input_code)
    parser = create_parser_from_input(input_stream)

    tree = parser.program()
    print_tree(tree)

    compile_to_GCode("../examples/circles_example.txt", "G-code.gcode")


if __name__ == '__main__':
    main()
