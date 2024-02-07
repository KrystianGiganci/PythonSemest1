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


tekst = input("podaj tekst: ")  # wczytanie tekstu od użytkownika
dzialanie = ''

for slowo in tekst.split(' '):  # podzielenie go na kawałki
    dzialanie += przetlumacz(slowo)

print(dzialanie)
