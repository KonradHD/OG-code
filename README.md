# OG-code – Edukacyjny Język do Generowania G-code

## Autorzy

**Martyna Gaj – margaj@student.agh.edu.pl**  
**Konrad Ćwięka – kcwieka@student.agh.edu.pl**

---

## 🎯 Cel projektu

**OG-code** to edukacyjny język programowania inspirowany językiem **Logo**, umożliwiający tworzenie prostych, wizualnych modeli za pomocą kodu, który następnie tłumaczony jest do **G-code** – języka sterującego drukarkami 3D. Projekt ma na celu:

- Nauczanie podstaw programowania i myślenia algorytmicznego.
- Pokazanie, jak programowanie może mieć fizyczne przełożenie w świecie rzeczywistym (druk 3D).
- Umożliwienie graficznej symulacji "rysowania" jak w Logo (turtle graphics).
- Zwiększenie atrakcyjności nauki przez interaktywność i natychmiastowy efekt działania kodu.

---

## ⚙️ Charakterystyka

- **Typ translatora**: *Kompilator* (OG-code → G-code)
- **Język implementacji**: *Python 3*
- **Parser i lexer**: generowane za pomocą **ANTLR4**
- **Dodatki**:
  - Graficzna wizualizacja działania kodu OG-code w czasie rzeczywistym (z wykorzystaniem `turtle`)
  - Kolorowanie składni w HTML
  - Prosty interfejs z trzema zakładkami:
    1. Edytor OG-code
    2. Wygenerowany G-code
    3. Wizualizacja rysunku

---

###  Sposób realizacji skanera/parsera

Planowane użycie generatorów parserów dla Pythona, np.:

- [`PLY`](https://www.dabeaz.com/ply/)
- [`Lark`](https://github.com/lark-parser/lark)

---

## 🔤 Gramatyka OG-code

Gramatyka została zapisana w pliku [`OGCode.g4`](grammar/OGCode.g4) i przetwarzana przez **ANTLR4**.

Obsługiwane konstrukcje to m.in.:

- Deklaracje funkcji (`function`)
- Zmienne i przypisania (`let`)
- Pętle `repeat`, `while`
- Instrukcje warunkowe `if`, `else`
- Operacje rysujące (`penDown`, `penUp`, `forward`, `turn`, `move`, `filledCircle`)
- Wartości liczbowe, logiczne i tekstowe
- Operatory matematyczne i logiczne

##  Opis tokenów

| Token       | Znaczenie                     |
|-------------|-------------------------------|
| `FORWARD`   | Ruch do przodu o zadaną wartość |
| `LEFT`      | Obrót w lewo (w stopniach)    |
| `RIGHT`     | Obrót w prawo (w stopniach)   |
| `PENUP`     | Podniesienie "rysika"         |
| `PENDOWN`   | Opuszczenie "rysika"          |
| `CIRCLE`    | Narysowanie okręgu o promieniu |
| `REPEAT`    | Powtórzenie bloku instrukcji  |
| `TO`        | Definicja procedury           |
| `END`       | Zakończenie procedury         |
| `ID`        | Identyfikator procedury       |
| `NUMBER`    | Wartość numeryczna (int)      |
| `[` `]`     | Początek i koniec bloku       |

---

## ✅ Przykładowy kod OG-code

```js
function start() {
    penDown();
    let bok = 40;
    repeat 4 {
        forward(bok);
        turn(90);
    }
    penUp();
}

## Jak zainstalować
plik requirement - to be announced
