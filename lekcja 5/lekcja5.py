x = "1"
y = "2"
y = x+y
print(y)


test1 = 'Giganci'
test2 = 'Programowania'
print(test1 + test2)


x = len("Giganci") + 2 * len("Programo" + "wania")
print(x)
x = 7 + 2 * (8 + 5)
print(x)

warunek = input('Podaj jakąś liczbę: ')

if int(warunek) > 10:
    print('Twoja liczba była większa niż 10.')
    pass
elif int(warunek) > 5:
    print('Twoja liczba była mniejsza od 10, ale większa niż 5.')
elif int(warunek) > 3:
    pass
elif int(warunek) > 2:
    pass
else:
    print("Twoja liczba była mniejsza niż 5.")
    pass
print('Do widzenia')

dzielna = int(input("Wprowadź dzielną: "))
dzielnik = int(input("Wprowadź dzielnik: "))

if dzielnik != 0:
    wynik = dzielna / dzielnik
    print(f"Wynik z dzielenia to: {wynik}")
    pass
else:
    print("Nie wolno dzielić przez zero!!!")
    pass


"""
ZADANIE 1.
Bierzesz udział w pierwszej fazie turnieju e-sportowego. O przejściu dalej decyduje
liczba wygranych meczów oraz zdobytych odznaczeń MVP (Most Valuable Player).
Aby przejść dalej należy zdobyć minimum 10 wygranych oraz mieć ich więcej niż
przegranych lub zdobyć 7 odznaczeń MVP.
Liczbę meczy wygranych, przegranych oraz liczbę odznaczeń MVP należy odczytać od
użytkownika na początku programu.
Jako wynik użytkownik powinien dostać informację: "Przechodzisz do drugiej rundy! Gratulacje!!"
lub "Niestety tym razem się nie udało :c"
"""
# Przykładowe rozwiązanie:
wygranych = int(input("Podaj liczbę wygranych: "))
przegranych = int(input("Podaj liczbę przegranych: "))
mvp = int(input("Podaj liczbę odznaczeń MVP: "))

if wygranych >= 10 and wygranych > przegranych or mvp >= 7:
    print("Gratuluję przejścia do kolejnej fazy turnieju")
    pass
else:
    print("Niestety nie udało Ci się przejść dalej")
    pass


"""
ZADANIE 2.
Napisz program, który informuje użytkownika o koszcie atrakcji turystycznej w
zależności od miesiąca. Program powinien zapytać o numer miesiąca, a następnie
powinien wyświetlić informację według poniższej zasady:
- w styczniu oraz lutym: $150
- w marcu i kwietniu: $199
- w maju oraz czerwcu: $249
- w lipcu, sierpniu oraz wrześniu: $299
- w październiku: $249
- w listopadzie oraz grudniu: $199
"""
# Przykładowe rozwiązanie
nr_miesiaca = int(input("Podaj numer miesiaca, ktory Cię interesuje: "))
if nr_miesiaca == 1 or nr_miesiaca == 2:
    print("Cena wynosi $150")
    pass
elif nr_miesiaca == 3 or nr_miesiaca == 4 or nr_miesiaca == 11 or nr_miesiaca == 12:
    print("Cena wynosi $199")
    pass
elif nr_miesiaca == 5 or nr_miesiaca == 6 or nr_miesiaca == 10:
    print("Cena wynosi $249")
    pass
elif nr_miesiaca == 7 or nr_miesiaca == 8 or nr_miesiaca == 9:
    print("Cena wynosi $299")
    pass
else:
    print("Wprowadź poprawny numer miesiąca")
    pass


# ZADANIE 3 - dokończyć kalkulator
print('Witaj w kalkulatorze! Jakiej opcji chcesz użyć?')
print('+ - dodawanie')
print('- - odejmowanie')
print('* - mnożenie')
print('/ - dzielenie')
dzialanie = input()
a = float(input("Wprowadź pierwszą liczbę:"))
b = float(input("Wprowadź drugą liczbę:"))

if dzialanie == '+':
    wynik = a + b
    pass
elif dzialanie == '-':
    wynik = a - b
    pass
elif dzialanie == '*':
    wynik = a * b
    pass
elif dzialanie == '/':
    if b == 0:
        print("Nie wolno dzielić przez zero!")
        wynik = "Error"
        pass
    else:
        wynik = a / b
        pass
    pass
else:
    print("Wprowadzono niepoprawny symbol")
    wynik = "Error"
pass


print(f'Wynik działania {a}{dzialanie}{b}={wynik}')