# Random-Sort-Stats 🎲📊

Program w Pythonie, który **symuluje „randomsort”** i liczy **średnią liczbę prób** potrzebnych do uzyskania posortowanej tablicy — w zależności od:
- rozmiaru tablicy,
- liczby powtórzeń (próbek) dla każdego rozmiaru. :contentReference[oaicite:2]{index=2}

> TL;DR: sprawdzasz empirycznie, jak „rośnie ból” przy sortowaniu losowym.

---

## ✨ Co to robi?

Dla kolejnych rozmiarów tablic `n` (od `zakres1` do `zakres2`) program:
1. generuje dane wejściowe,
2. uruchamia losowe podejście do sortowania (randomsort),
3. zlicza ile „prób” było potrzebnych, żeby tablica była posortowana,
4. powtarza to `probka` razy,
5. wypluwa statystyki (średnia / wyniki per rozmiar). :contentReference[oaicite:3]{index=3}

---

## ✅ Wymagania

- Python 3.x  
- (opcjonalnie) wirtualne środowisko `venv`

---

## 🚀 Szybki start

```bash
git clone https://github.com/indekplay/Random-Sort-Stats.git
cd Random-Sort-Stats
python Program1.py
