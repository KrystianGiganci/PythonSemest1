# wprowadzone_haslo = input("Podaj hasło: ")
# poprawnosc_hasla = "Maslo" == wprowadzone_haslo
# if poprawnosc_hasla:
#     print("Udało Ci się zalogować!")
#     pass
# else:
#     print("Podano błędne hasło!")
#     pass

# a = 20
# b = 15
# c = 1
# z = 70

# if a == 20 or b < 10 and c > -5 and ... or 20 < z < 120:
#     print("Udało się spełnić wszystkie warunki")
#     pass

# wczytane_slowo = input('Wpisz przykładowe słowo: ')
# czy_zawiera_a = 'a' in wczytane_slowo
# if czy_zawiera_a:
#      print('Wpisano ciąg znaków zawierający literę a')
# else:
#      print('Wpisano ciąg znaków niezawierający litery a')

# imie = 'Krystian'
# test = 'a' in imie
# print(test)

"""
Standardowe logowanie: login, hasło. Program zapyta użytkownika najpierw o login,
a potem o hasło. Następnie porówna je z zapisanym loginem i hasłem w kodzie.

Drugie polecenie: rozszerzmy nasze zadanie o logowanie dwuetapowe. Po wpisaniu poprawnego loginu oraz hasła
program powinien poprosić użytkownika o podanie PINu potwierdzającego.
"""
"""
# import getpass
login =  "ToJestMójLogin"
haslo =  "ToJestMojeHaslo"
PIN =  "3516"  # pomimo tego ze jest to liczba to powinien być to string
               # w celu uniknięcia błędnego działania gdy pierwszą cyfrą PINu będzie 0

wpisany_login =  input("Podaj login: ")
wpisane_haslo =  input("Podaj hasło: ")
# wpisane_haslo =  getpass.getpass("Podaj hasło: ") # wersja z "utajnionym" wpisywaniem hasła

if wpisany_login == login and wpisane_haslo == haslo:
    print("Podano prawidłowy login oraz hasło!")
    wpisany_PIN = input("Teraz należy podać PIN.")
    if wpisany_PIN == PIN:
        print("Udało się zalogować!")
        pass
    pass
else:
    print("Podano błędne dane")
    pass
"""

# przykładowa zagnieżdżona instrukcja warunkowa:
# if warunek1:
#     if warunek2:
#         if warunek3:
#             pass
#         pass
#     pass

"""
Napisz program, który wczyta od użytkownika długości 3 boków trójkąta,
a następnie "odpowie" na następujące pytania:
0. Sprawdzić czy da się utworzyć taki trójkąt.
Można użyć funkcji exit() do przerwania programu.
1. Jaki jest najkrótszy i najdłuższy bok?
2. Jaki jest jego obwód?
3. Jaki jest to rodzaj trójkąta: równoboczny, równoramienny albo różnoboczny?
4. Jaki jest to rodzaj trójkąta: prostokątny, rozwartokątny czy ostrokątny?
Podpowiedź: przydatny może być wzór Pitagorasa.
"""

a = float(input("Podaj długość boku a: "))
b = float(input("Podaj długość boku b: "))
c = float(input("Podaj długość boku c: "))

# Potwierdzenie dla użytkownika
print(f"Podano boki: a = {a}, b = {b} oraz c = {c}")

# Zadanie 1.
najkrotszy_bok = min(a, b, c)
najdluzszy_bok = max(a, b, c)
print(f"Najkrótszy bok: {najkrotszy_bok}, najdłuższy bok: {najdluzszy_bok}")

# Zadanie 2.
obwod = a + b + c
print(f"Obwod tego trójkąta wynosi {obwod}")

# Zadanie 0.
sredni_bok = obwod - najkrotszy_bok - najdluzszy_bok
if najdluzszy_bok >= sredni_bok + najkrotszy_bok or a <= 0 or b <= 0 or c <= 0:
    print("Błąd! Podane boki nie mogą utworzyć trójkąta.")

# Zadanie 3.
if a == b == c:     # Sprawdzamy czy wszystkie boki są równe
    print("Jest to trójkąt równoboczny.")
    pass
elif a != b != c and a != c:   # Sprawdzamy czy wszystkie boki są różne
    print("Jest to trójkąt różnoboczny.")
else:               # W innym wypadku jest to trójkąt równoramienny
    print("Jest to trójkąt równoramienny.")

# Zadanie 4. - zadanie domowe
