# OG-code – Edukacyjny Język do Generowania G-code

## Dane studentów

**Martyna Gaj - margaj@student.agh.edu.pl**  
**Konrad Ćwięka - kcwieka@student.agh.edu.pl**



---

## Założenia programu

###  Ogólne cele programu

OG-code to edukacyjny język programowania inspirowany Logo, który umożliwia tworzenie prostych modeli do druku 3D. Celem projektu jest ułatwienie dzieciom i początkującym wejścia w świat programowania, myślenia algorytmicznego i projektowania przestrzennego, bez potrzeby znajomości zawiłości G-code. Pozwala to na zaciekawienie dzieci programowaniem i ucieleśnienie ich zmagań z programem.

###  Rodzaj translatora

**Kompilator** – tłumaczący OG-code bezpośrednio na G-code.

###  Planowany wynik działania programu

- Kompilator języka OG-code do G-code
- Opcjonalnie: graficzna symulacja rysunku 2D (prewizualizacja ścieżki)
- Docelowo: wsparcie dla tworzenia modeli 3D przez wytłaczanie 2D

###  Planowany język implementacji

**Python**

###  Sposób realizacji skanera/parsera

Planowane użycie generatorów parserów dla Pythona, np.:

- [`PLY`](https://www.dabeaz.com/ply/)
- [`Lark`](https://github.com/lark-parser/lark)

---

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

##  Gramatyka języka (BNF)

[Gramatyka OG-code](Grammar.g4)

