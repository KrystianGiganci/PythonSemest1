import random

"""
ZADANIE 6.
Napisz program, który zapyta użytkownika o liczbę, a następnie wypisze na
ekranie tyle wyników z rzutu kością sześcienną.
Rzut kością sześcienną to wynik z losowania liczby od 1 do 6 (włącznie).
"""
# liczba_rzutow = int(input("Liczba rzutów kością: "))
# for i in range(liczba_rzutow):          # [0, 1, 2,..., liczba_rzutów-1]
#     print(random.randint(1, 6))

"""
ZADANIE 7
Napisz funkcję, która przyjmuje 2 argumenty:
- tekst, typu str
- n, typu int
a zwraca nowy napis, który powstaje poprzez połączenie text n razy.
"""


def laczenie_slow(tekst: str, n: int) -> str:
    nowy_tekst = tekst * n
    return nowy_tekst


# Wykorzystaj kod ponizej do testowania:
t1 = laczenie_slow("Slowo", 3)
print(f"Czy 'SlowoSlowoSlowo' zgadza się z wynikiem funkcji? Wynik funkcji: '{t1}'")

t2 = laczenie_slow("Aa", 5)
print(f"Czy 'AaAaAaAaAa' zgadza się z wynikiem funkcji? Wynik funkcji: '{t2}'")

t3 = laczenie_slow("Onomatopeja", 0)
print(f"Czy '' zgadza się z wynikiem funkcji? Wynik funkcji: '{t3}'")

t4 = laczenie_slow("Kilka spacji", 2)
print(f"Czy 'Kilka spacjiKilka spacji' zgadza się z wynikiem funkcji? Wynik funkcji: '{t4}'")

"""
ZADANIE 8.
Przygotuj funkcję, która otrzymuje jeden argument: n - liczbę elementów.
Funkcja ma zwrócić listę n - losowych elementów od 0 do 100
Wywołaj ją kilka razy, aby sprawdzić, czy za każdym razem zwraca różne wartości
"""


"""
ZADANIE 9.
Napisz program aplikacji graficznej, która co 3 sekundy zmienia kolor tła. Nowy
kolor tła powinien być losowany.
Podpowiedź:
Pamiętaj o wykorzystaniu liczby klatek do wykrycia kiedy mijają kolejne 3 sekundy
Pamiętaj o budowaniu koloru RGB:
RGB składa się z trzech kolorów, każdy może przyjąć wartość od 0 do 255 (włącznie)
RGB = [R, G, B] możesz przechowywać to jako listę
"""


"""
ZADANIE 10.
Dodaj do poprzedniego zadania wykrywanie naciśnięcia klawisza 'b'.
Jeśli taki klawisz zostanie naciśnięty kolor tła powinien zmienić się
na czarny, a po puszczeniu klawisza kolor:
a) powinien zostać na nowo wylosowany - wersja podstawowa
b) powinien wrócić poprzedni kolor - wersja rozszerzona
"""
