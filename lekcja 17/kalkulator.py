zero = ["0", 'zero', 'zera', 'zerem']
jeden = ["1", 'jeden', 'jedynka', 'jedynkę']
dwa = ["2", 'dwa']

plus = ["+", "dodaj", "plus", 'dodać', 'dodac']

baza = [zero, jeden, dwa, plus]


def przetlumacz(slowo):
    for symbol in baza:
        for slowo_w_symbolu in symbol:
            if slowo == slowo_w_symbolu:
                return symbol[0]


def oblicz_z_tekstu(dzialanie):
    wynik = 0
    for znak in dzialanie:
        if znak.isdigit():
            pass
        else:
            pass
    pass
    return wynik


tekst = input("podaj tekst: ")  # wczytanie tekstu od użytkownika
dzialanie = ''

for slowo in tekst.split(' '):  # podzielenie go na kawałki
    dzialanie += przetlumacz(slowo)

print(dzialanie)
print(oblicz_z_tekstu(dzialanie))
