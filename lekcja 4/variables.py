liczba = 3   # przypisujemy do zmiennej liczba wartość trzy

liczba == 3  # sprawdzamy czy zmienna 'liczba' jest równa trzy
liczba != 3  # sprawdzamy czy zmienna 'liczba' jest różna od liczby trzy


print("Czy możesz skorzystać z rollercoastera?")
print("True - możesz skorzystać")
print('False - nie możesz skorzystać')

wzrost_cm = int(input("Podaj swój wzrost w cm: "))
gorna_granica = 215
dolna_granica = 150
werdykt = dolna_granica < wzrost_cm <= gorna_granica
print(werdykt)


# NOT - negacja - odpowiednik polskiego słówka "nie"
# print(not 50 == 50.05)

# AND - odpowiednik polskiego słówka "i"
# sprawdza czy wszystkie porównywane wartości są prawdą
# print(not (4 != 4.0 and 2 <= 0))
#     not (False) => True

# OR - odpowiednik polskiego słówka "lub"
# sprawdza czy przynajmniej jedna wartość, którą porówujemy jest prawdą
# print(20 < 25 or 24 == 0)
#     True or False => True


"""
1. Program zapyta użytkownika o 3 liczby
2. Przypisze je do zmiennych a, b, c
3. Sprawdzi czy a jest najwieksza liczba z 3 wymienionych
4. Sprawdzi czy b jest najwieksza liczba z 3 wymienionych
5. Sprawdzi czy c jest najwieksza liczba z 3 wymienionych
"""

3, 5, 6
Czy 3 jest najwieksza liczba?
False
Czy 5 jest najwieksza liczba?
False
Czy 6 jest najwieksza liczba?
True
