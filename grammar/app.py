import streamlit as st
from antlr4 import *
from OGCodeLexer import OGCodeLexer
from OGCodeParser import OGCodeParser
from OGCompiler import OGCompiler
import MyErrorListener

def compile_code(code):
    input_stream = InputStream(code)
    lexer = OGCodeLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = OGCodeParser(token_stream)

    parser.removeErrorListeners()
    parser.addErrorListener(MyErrorListener())
    tree = parser.program()

    compiler = OGCompiler()
    return compiler.compile(tree)

st.set_page_config(page_title="OGCode IDE", layout="wide")

tabs = st.tabs(["OG-Code", "G-Code", "Podgląd"])

with tabs[0]:
    st.header("OG-Code Editor")
    ogcode = st.text_area("Wklej swój kod OG-Code tutaj:", height=400)
    
with tabs[1]:
    st.header("Wygenerowany G-code")
    if ogcode:
        try:
            gcode = compile_code(ogcode)
            st.text_area("G-code:", gcode, height=400)
        except Exception as e:
            st.error(f"Błąd kompilacji: {e}")
    else:
        st.info("Najpierw wprowadź OG-Code.")

with tabs[2]:
    st.header("Podgląd rysunku")
    st.info("Tutaj może być w przyszłości podgląd rysunku z G-code (np. SVG lub obrazek).")
