import random

def test(a,b,n):
    wynik = []
    while a!=b:
        c = a
        srednia = 0
        for j in range(n):
            d = 0
            tab1 = []
            tab2 = []
            for i in range(c):
                tab1.append(random.randint(1,100))
            for i in range(c):
                tab2.append(tab1[i])
            tab2.sort()
            while tab1!=tab2:
                random.shuffle(tab1)
                d = d + 1
            srednia = srednia + d
        wynik.append(srednia/n)
        a = a + 1
    return wynik

zakres1 = 3
zakres2 = 7
probka = 10000
wyniki = test(zakres1,zakres2,probka)

for i in range(len(wyniki)):

    print("Dla Listy "+str(zakres1)+" elementowej, sortowanie losowe wykonuje sie srednio w "+str(wyniki[i])+" probach")
    zakres1 = zakres1 + 1