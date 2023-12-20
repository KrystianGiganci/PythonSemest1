# zagnieżdżone pętle for

for a in range(1, 11):  # pierwsza pętla odpowiadająca za ilość wierszy
    line = ""  # inicjujemy zmienną tekstową do której będziemy "doklejać" kolejne wyniki
    for b in range(1, 11):  # druga pętla odpowiadająca za ilość kolumn
        line += str(a*b).center(4) + "|"  # doklejamy kolejne wyniki do naszej linijki
        pass
    print(line)  # wypisujemy całą linijkę na ekran
    pass
