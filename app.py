import streamlit as st
from streamlit_ace import st_ace
from antlr4 import *
from grammar.OGCodeLexer import OGCodeLexer
from grammar.OGCodeParser import OGCodeParser
from Compiler.OGCompiler import OGCompiler
from Compiler.MyErrorListener import MyErrorListener
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
    result = compiler.compile(tree)
    if isinstance(result, tuple) and len(result) == 2:
        return result
    elif isinstance(result, str):
        # Domniemaj, że brak rysunku
        return result, []
    else:
        raise ValueError(f"Nieoczekiwany zwrot z compile(): {result}")


st.set_page_config(page_title="OGCode IDE", layout="wide")

tabs = st.tabs(["OG-Code", "G-Code", "Podgląd"])

ogcode = ""
with tabs[0]:
    st.header("OG-Code Editor")
    ogcode = st_ace(
        language='python',  # nie ma 'ogcode' więc wybierz najbardziej zbliżony język, np. python lub plain_text
        theme='monokai',
        keybinding='vscode',
        font_size=14,
        tab_size=4,
        show_gutter=True,
        show_print_margin=False,
        wrap=True,
        auto_update=True,
        placeholder="Wklej lub wpisz kod OG-Code tutaj...",
        height=400,
        key="ogcode_ace"
    )
gcode, drawing = None, None
if ogcode:
    try:
        gcode, drawing = compile_code(ogcode)
    except Exception as e:
        st.error(f"Błąd kompilacji: {e}")

with tabs[1]:
    st.header("Wygenerowany G-code")
    if gcode:
        st.text_area("G-code:", gcode, height=400)
    else:
        st.info("Najpierw wprowadź poprawny OG-Code.")

with tabs[2]:
    st.header("Podgląd rysunku")
    if drawing:
        fig, ax = plt.subplots(figsize=(4, 4), dpi=80)
        all_x, all_y = [], []
        scale = 0.05


        for item in drawing:
            if (isinstance(item, tuple) and len(item) == 2 and
                isinstance(item[0], tuple) and len(item[0]) == 2 and
                isinstance(item[1], tuple) and len(item[1]) == 2):
                (x1, y1), (x2, y2) = item
                x1 *= scale
                y1 *= scale
                x2 *= scale
                y2 *= scale
                ax.plot([x1, x2], [y1, y2], color="black")
            else:
                st.write(f"Pominięto element o nieoczekiwanym formacie: {item}")

        # Ustawienie granic osi na podstawie danych
        if all_x and all_y:
            min_x, max_x = min(all_x), max(all_x)
            min_y, max_y = min(all_y), max(all_y)

            margin_x = (max_x - min_x) * 0.1
            margin_y = (max_y - min_y) * 0.1

            ax.set_xlim(min_x - margin_x, max_x + margin_x)
            ax.set_ylim(min_y - margin_y, max_y + margin_y)

        ax.set_aspect("equal")
        ax.invert_yaxis()
        ax.axis('off')

        st.pyplot(fig)
    else:
        st.info("Brak danych do rysowania lub niepoprawny kod.")
