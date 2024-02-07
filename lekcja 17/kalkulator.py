zero = ["0", 'zero', 'zera', 'zerem']
jeden = ["1", 'jeden', 'jedynka', 'jedynkę']
dwa = ["2", 'dwa']

plus = ["+", "dodaj", "plus", 'dodać', 'dodac']

baza = [zero, jeden, plus]


def przetlumacz(slowo):
    wynik = ''
    # TODO
    return wynik


tekst = input("podaj tekst: ")  # wczytanie tekstu od użytkownika
dzialanie = ''

for slowo in tekst.split(' '):  # podzielenie go na kawałki
    dzialanie += przetlumacz(slowo)

print(dzialanie)
