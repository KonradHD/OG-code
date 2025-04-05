# 🐢 OG-code – Edukacyjny Język do Generowania G-code

**OG-code** to nowy, edukacyjny język programowania inspirowany klasycznym Logo (językiem z żółwiem), stworzony z myślą o uproszczeniu tworzenia modeli do druku 3D. Projekt powstaje w ramach kursu **"Teoria kompilacji i kompilatory"** i ma formę technologicznej ciekawostki/zabawki, która pozwala dzieciom rysować swoje dzieła w prostym języku programowania.

---

## 🎯 Cel projektu

Celem OG-code jest umożliwienie dzieciom (i nie tylko!) tworzenia modeli 3D za pomocą prostych komend, bez potrzeby znajomości zawiłości G-code. Chcemy ułatwić przejście od rysunku do druku 3D, jednocześnie wprowadzając użytkownika w świat programowania, algorytmiki i myślenia przestrzennego.

---

## 🧱 Technologie

- **Język implementacji:** Python
- **Zakres początkowy:** 2D (ruch po płaszczyźnie XY)
- **Docelowo:** rozszerzenie do 3D (ruch w osi Z jako wysokość rysunku)
- **Model działania:** Kompilacja bezpośrednio do G-code

---

## 🔤 Składnia języka

OG-code korzysta ze składni inspirowanej klasycznym Logo. Przykładowe komendy:

FORWARD 10 LEFT 90 FORWARD 20 PENUP FORWARD 5 PENDOWN CIRCLE 10 REPEAT 4 [ FORWARD 30 RIGHT 90 ] TO SQUARE REPEAT 4 [ FORWARD 20 RIGHT 90 ] END SQUARE


W przyszłości planowane są:
- **Pętle (REPEAT)**
- **Procedury (TO ... END)**
- **Zmienne i parametry (opcjonalnie)**

---

## 🧠 Jak to działa?

1. **Analiza leksykalna i składniowa:** kod OG-code jest analizowany i zamieniany na strukturę pośrednią.
2. **Generowanie G-code:** ze struktury pośredniej generowany jest gotowy kod do wydruku 3D.
3. **Podgląd (opcjonalny):** graficzna symulacja wydruku w 2D, pokazująca co zostanie narysowane.

---

## 🎨 Założenia projektowe

- Prostota: język ma być przystępny nawet dla dzieci.
- Minimalizm: tylko najważniejsze funkcje na początek.
- Przenośność: G-code generowany przez kompilator powinien działać na większości drukarek 3D.
- Rozszerzalność: łatwość dodawania nowych funkcji, w tym pracy w 3D (np. przez traktowanie rysunku 2D jako foremki z wysokością w osi Z).

---

## 📦 Przykład działania

Kod źródłowy:
REPEAT 4 [ FORWARD 50 RIGHT 90 ]


Wynik:

- Kwadrat o boku 50 mm.
- Wygenerowany G-code gotowy do druku (z kontrolą pozycji, włączeniem/wyłączeniem ekstrudera, itd.).
- Możliwość wizualizacji trasy rysowania w 2D.

---

## 🛠️ Status projektu

✅ Analiza pomysłu  
🚧 Tworzenie prototypu kompilatora w Pythonie  
🔜 Generowanie G-code  
🔜 Prosty podgląd graficzny  
🔜 Rozszerzenie do wymiaru Z

---

## 🤝 Autorzy

Projekt realizowany przez duet studentów w ramach kursu **Teoria kompilacji i kompilatory**.

- ✏️ Martyna Gaj
- ✏️ Konrad Ćwięka

---

## 🆓 Licencja

Projekt planujemy udostępnić jako open-source (MIT lub podobna licencja).

---

## 🌱 Plany na przyszłość

- Obsługa bardziej złożonej składni (np. zmienne, funkcje z parametrami)
- Generowanie trójwymiarowych brył przez "wytłaczanie" rysunku 2D
- Wersja online lub z GUI dla łatwiejszej obsługi




