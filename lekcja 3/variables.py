# imie = input('Jak masz na imię?')
# print(imie)

a = 10
b = 7
c = -5
suma = a + b
roznica = a - b
a = a + 3
a += 3
# print(-c)
print(a*b)          # mnożenie
print(a/b)          # dzielenie - zawsze liczba typu float
print(10/1)
print(a % b)        # modulo (reszta z dzielenia)
print(26 % 5)
print(a // b)       # dzielenie całkowitoliczbowe
print(3 ** 2)       # potęgowanie


napis1 = 'Ala '
napis2 = 'ma '
napis3 = 'kota.'
print(napis1+napis2+napis3) # dodawanie napisów
print(3 * "Jurek")
tekst = ' tekst'
nowy = 'nowy'
nowy += tekst
print(nowy)

d = 10
e = 10
d = d + 2
e += 2
print(f'd = {d}')
print(f'e = {e}')

d = d - 2
e -= 2
print(f'd = {d}')
print(f'e = {e}')

# operacje na typie zmiennej bool (True/False)
                                  # 1     0
print(True + True)              # 2
print(False + False)            # 0
print(3*True)                   # 3
print(True + False)             # 1

tekst = ' tekst'
nowy = 'nowy'
nowy += tekst
print(nowy)


print(round(5.42))                         # zaokrąglenie liczby np. 5.42; wynik to 5
print(max(5, 10, 28, -20, 17, 1, 4))       # znalezienie największej wartości z liczb wymienionych po przecinku
print(min(5, 10, 28, -20, 17, 1, 4))       # znalenienie najmniejszej wartości
print(abs(-30))                            # wartość bezwzględna z liczby

print(len("Mamy dzisiaj środę."))
print(len([3, 5, 190, -2, 2.54]))


print('51 dzielone przez 5 daje wynik 10 i 1 reszty')


# ZADANIE DOMOWE
# Kalkulator średniej oceny z przedmiotów. Program ma pytać użytkownika o
# oceny z różnych przedmiotów (podawane jako liczby całkowite) sumować je, a na końcu ma wyświetlić
# średnią z tych ocen.