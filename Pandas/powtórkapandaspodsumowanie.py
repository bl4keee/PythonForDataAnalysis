# -*- coding: utf-8 -*-
"""PowtórkaPandasPodsumowanie.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vK0vswlKaSGXE10iXYGUl6gVrVIlNPwM

**Zadanie 1. Zaimportuj plik gospodarstwa.rda.**
"""

import pandas as pd
import numpy as np

dane = pd.read_excel(io = "gospodarstwa.xlsx")
dane.head()

"""**Zadanie 2. Utwórz zbiór, w którym są gospodarstwa ze wsi.**"""

dane.loc[dane["klm"] == 6]
## alternatywa 1 = dane.loc[dane.klm == 6]
## alternatywa 2 = dane.query("klm == 6")

"""**Zadanie 3. Utwórz zbiór, w którym są gospodarstwa o dochodach > 2000 zł.**"""

dane.loc[dane.dochg > 2000]
dane.dochg.describe()
## alternatywa 1 = dane.query("klm == 6 & dochg > 2000")

"""**Zadanie 4. Utwórz zbiór, który zawiera gospodarstwa z województwa wielkopolskiego oraz które zamieszkują wieś i mają dochody powyżej 3000 zł.**"""

dane.query("woj == 30 & klm == 6 & dochg > 3000")

"""**Zadanie 5. Wyświetl informacje o gospodarstwach z województwa dolnośląskiego
i mazowieckiego z miast powyżej 500 tys. mieszkańców.**
"""

wynik2 = dane.loc[dane.woj.isin([2, 14]) & (dane.klm == 1)]
print(wynik2.shape)
## alternatywa 1 = wynik1 = loc[(dane.woj == 2) | (dane.woj == 14) (dane.klm == 1)] coś nie działa, idk

"""**Zadanie 6. Losowo wybierz zbiór 30% gospodarstw domowych.**"""

## wszystko z losowaniem czy prawdopodobieństwem - numpy
np.random.seed(123) ## seed pozwala na porównywalność i odtwarzalność wyników
ncases = dane.shape[0] ## wyświetla ilość wierszy
sample = round(0.3 * ncases) ## zaokrągla do wartości całkowitych
print(ncases, sample) 
rows = np.random.randint(low = 0, high = ncases, size = sample)
dane.iloc[rows] ## iloc, gdyż wybieramy z listy liczb całkowitych

"""**Zadanie 7. Losowo wybierz 100 gospodarstw.**"""

np.random.seed(123)
dane.iloc[np.random.randint(low = 0, high = ncases, size = 100)]

"""**Zadanie 8. Wybierz gospodarstwa domowe z wierszy 10–15.**"""

dane.iloc[10:16]

"""**Zadanie 9. Wybierz gospodarstwa domowe z danymi tylko dla kolumny woj i wydg
ale w odniesieniu jedynie dla gospodarstw z województwa wielkopolskiego.**
"""

dane.loc[dane.woj == 30, ["woj", "wydg"]]

"""**Zadanie 10. Wybierz wszystkie gospodarstwa, których dochód jest z przedziału
3000–4000 i zostaw tylko tą zmienną w zbiorze.**
"""

dane.query("dochg > 3000 & dochg < 4000")
## nie skończyłem

"""**Zadanie 11. Wybierz wszystkie kolumny od klm do zut włącznie.**"""

dane[dane.columns[0:4]]

"""**Zadanie 12. Wybierz wszystkie kolumny, które zaczynają się na literę d.**"""

dane.columns.str.startswith("d") ## zwraca True i False w tablicy

flag = dane.columns.str.startswith("d")
dane[dane.columns[flag]] ## wyświetla wszystkie kolumny, które zaczynają się na literę "D"

"""**Zadanie 13. Wybierz wszystkie kolumny, które kończą sie na oj.**"""

flag2 = dane.columns.str.endswith("oj")
dane[dane.columns[flag2]]

"""**Zadanie 14. Utwórz nową zmienną roznica=dochg-wydg. Pozostaw w zbiorze zmienne
dochg, wydg i roznica**
"""

dane["roznica"] = dane["dochg"] - dane["wydg"]
## alternatywa 1 = dane["roznica"] = dane.dochg - dane.wydg
dane[["dochg", "wydg", "roznica"]].head()

"""**Zadanie 15. Utwórz nowe zmienne x=ln(dochg) oraz y=ln(wydg). Pamiętaj, że ln
liczymy dla dodatnich wartości.**
"""

dane["x"] = np.log(dane.dochg)
dane["y"] = np.log(dane.wydg)
dane.x.describe()
## printuje błąd = występuje dzielenie przez zero

"""**Zadanie 16. Dokonaj zamiany nazwy zmiennych dochg na dochod oraz wydg na
wydatki.**
"""

print(dane.head()) ## przed zmianą 

dane = dane.rename(columns = {"dochg" : "dochod", "wydg" : "wydatki"})

print(dane.head()) ## po zmianie

"""**Zadanie 17. Oblicz ile było gospodarstw domowych ze względu na poszczególne
warianty zmiennej klm.**
"""

dane.groupby("klm").count() ## printuje wszystkie kolumny ale z danymi tylko do takiej ilości ile jest wariantów w klm czyli 6 
dane.groupby("klm").klm.count() ## printuje ile jest wariantów w klm czyli 6

dane.groupby("klm").dochod.mean() ## średni dochód w klm

dane.groupby(["klm", "d21"]).dochod.mean() ## średni dochód w klm + d21 (czy użytkuje grunt)

dane.groupby("klm")["dochod", "wydatki"].mean() ## printuje dochod i wydatki względem klm (liczby wariantów w klm czyli 6)

"""**Zadanie 18. Oblicz ile było gospodarstw domowych w poszczególnych województwach.**"""

dane.groupby("woj").count()
## nie wiem