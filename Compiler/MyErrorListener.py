from antlr4.error.ErrorListener import ErrorListener

class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if "missing ';'" in msg:
            raise Exception(f"Missing ; near line {line}.")
        else:
            raise Exception(f"Błąd składni w linii {line}, kolumna {column}: {msg}")