import streamlit as st
from antlr4 import *
from OGCodeLexer import OGCodeLexer
from OGCodeParser import OGCodeParser
from OGCompiler import OGCompiler
from MyErrorListener import MyErrorListener
import matplotlib.pyplot as plt
import io


def compile_code(code):
    input_stream = InputStream(code)
    lexer = OGCodeLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = OGCodeParser(token_stream)

    parser.removeErrorListeners()
    parser.addErrorListener(MyErrorListener())
    tree = parser.program()

    compiler = OGCompiler()
    gcode = compiler.compile(tree)
    return gcode, compiler.drawing


st.set_page_config(page_title="OGCode IDE", layout="wide")

tabs = st.tabs(["OG-Code", "G-Code", "Podgląd"])

with tabs[0]:
    st.header("OG-Code Editor")
    ogcode = st.text_area("Wklej swój kod OG-Code tutaj:", height=400)
    
with tabs[1]:
    st.header("Wygenerowany G-code")
    if ogcode:
        try:
            gcode, drawing = compile_code(ogcode)
            st.text_area("G-code:", gcode, height=400)
        except Exception as e:
            st.error(f"Błąd kompilacji: {e}")
    else:
        st.info("Najpierw wprowadź OG-Code.")

with tabs[2]:
    st.header("Podgląd rysunku")
    if ogcode:
        try:
            gcode, drawing = compile_code(ogcode)
            if drawing:
                fig, ax = plt.subplots()
                for (x1, y1), (x2, y2) in drawing:
                    ax.plot([x1, x2], [y1, y2], color="black")
                ax.set_aspect("equal")
                ax.invert_yaxis()
                st.pyplot(fig)
            else:
                st.info("Brak danych do rysowania.")
        except Exception as e:
            st.error(f"Błąd podczas generowania rysunku: {e}")
    else:
        st.info("Najpierw wprowadź OG-Code.")

