# Podpowiedź - aby włączać/wyłączać poszczególne etapy
# możemy w następujący sposób użyć skrótu klawiszowego Ctrl + /
# 1. Zaznaczamy fragment tekstu, który chcemy zakomentować/odkomentować
# 2. Wciskamy Ctrl + /
# 3. Gotowe, pracować dalej!


"""
ZADANIE 1.
Utwórz trzy zmienne, do których wpisz wartość 3 jako odpowiedni typ:
- x_int - jako liczba całkowita
- x_float - jako liczba z przecinkiem
- x_str - jako napis
"""

x_int = 3
x_float = 3.0
x_str = "3"


# Odkomentuj poniższe dwie linijki, aby sprawdzić czy zadanie zostało zrobione prawidłowo.
# wynik = type(x_int) == int and type(x_float) == float and type(x_str) == str
# print("Brawo! Zadanie zaliczone!") if wynik else print("Coś nie zadziałało, spróbuj ponownie")
"""
ZADANIE 2.
Utwórz zmienną napis_liczba, która przechowuje wartość "290".
Następnie utwórz zmienną x i użyj konwersji z typu str na typ int,
aby zmienna x przechowywała to co napis_liczba, ale jako typ liczby całkowitej.
"""

napis_liczba = "290"
x = int(napis_liczba)


"""
ZADANIE 3.
Utwórz 3 zmienne:
- pole_trojkata
- podstawa_trojkata
- wysokosc_trojkata
Do podstawa_trojkata oraz wysokosc_trojkata powinny trafić wartości odczytane z
konsoli (od użytkownika).
Oblicz pole takiego trójkąta i zapisz wynik w zmiennej pole_trojkata
Wyświetl wynik jako komunikat:

Pole trójkąta o podstawie XX oraz wysokości XX wynosi XX.

(W miejsce XX powinny pojawić się odpowiednie wartości liczbowe)
"""

podstawa_trojkata = float(input("Podstawa: "))
wysokosc_trojkata = float(input("Wysokość: "))
pole_trojkata = podstawa_trojkata * wysokosc_trojkata / 2
print(f"Pole trójkąta o podstawie {podstawa_trojkata} i wysokości {wysokosc_trojkata} wynosi {pole_trojkata}.")

"""
ZADANIE 4.
Zapytaj użytkownika o jego wiek i na tej podstawie wyświetla w konsoli jeden z
komunikatów:
- Jesteś pełnoletni/a.
- Nie jesteś jeszcze pełnoletni/a. Brakuje Ci XX lat do 18 roku życia.
Zamiast XX powinna pojawić się odpowiednia wartość liczbowa.
"""
wiek = int(input("Podaj swój wiek: "))
if wiek >= 18:
    print("Jesteś pełnoletni/a")
else:
    brakuje = 18 - wiek
    print(f"Nie jesteś jeszcze pełnoletni/a. Brakuje Ci {brakuje} lat do 18 roku życia.")

"""
ZADANIE 5.
Cena atrakcji turystycznej zależy od miesiąca. Napisz program, który zapyta
użytkownika o liczbę biletów oraz miesiąc, w którym chce odwiedzić park
rozrywki i na tej podstawie obliczy koszt transakcji.
Koszt biletu w danym miesiącu (miesiąc jako numer -> koszt biletu):
- 1 -> 50 zł
- 2 -> 50 zł
- 3 -> 100 zł
- 4 -> 100 zł
- 5 -> 200 zł
- 6 -> 200 zł
- 7 -> 250 zł
- 8 -> 200 zł
- 9 -> 200 zł
- 10 -> 100 zł
- 11 -> 100 zł
- 12 -> 50 zł
Wyświetl komunikat:
"Cena biletów: XX zł"
(XX to wartość liczbowa)

Na przykład:
Gdy użytkownik poda miesiąc = 3 oraz liczbę_biletów = 4
otrzymujemy wynik: "Cena biletów to 400 zł".

Lecz jeśli wprowadzono niepoprawny numer miesiąc
program powinien wyświetlić informację:
"Wprowadzono niepoprawny numer miesiąca. Spróbuj ponownie"
"""
