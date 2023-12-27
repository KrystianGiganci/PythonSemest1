"""
Napisz funkcję, która otrzymuje liczbę całkowitą (int) a zwraca sumę jej cyfr.
Przyklad dla liczby 345 otrzymujemy 3+4+5=12, czyli zwraca 12.
"""


def suma_cyfr(liczba):
    suma = 0
    for numer in str(liczba):
        suma += int(numer)
    print(f'Suma Cyfr Liczby {liczba} to {suma}')


suma_cyfr(999)
suma_cyfr(555)
suma_cyfr(127)