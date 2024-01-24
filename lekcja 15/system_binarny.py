"""
Napisz funkcję, która otrzyma jeden argument w postaci liczby dzięsiętnej.
Funkcja ma zwrócić tę samą liczbę, lecz w postaci binarnej.
"""
print(bin(3))

'''
Sprawdzic czy liczba jest pierwsza
'''
def czy_jest_pierwsza(a):
    if a <= 1:
        return False
    else:
        for i in range(2, a):
            if a % i == 0:
                return False
        return True

czy_jest_pierwsza(1065847)


"""
Napisz funkcję, która sprawdzi czy string podany jako argument jest palindromem.
Palindrom - słowo/zdanie/ciąg znaków, które czytane od początki i od końca brzmi tak samo.
"""
# tekst = "przykladowy tekst"
# 6-ty element -> tekst[5]
# 10-ty element -> tekst[9]
# i-ty element -> tekst[i-1]

# 6-ty element od konca -> tekst[-6]
# 10-ty elemetn od konca -> tekst[-10]
# i-ty element od konca -> tekst[-i]

def czy_jest_palindromem(text):
    if text == text[::-1]:
        print(f"{text} jest palindromem")
    else:
        print(f"{text} nie jest palindromem")


czy_jest_palindromem("kajak")

"""
Anagramy to słowa, które składają się z tej samej ilości oraz z dokładnie tych samych
liter.
Przykład:
bark – krab, adam – dama.

Napisz funkcję która przyjmnie jako argument dwa słowa i sprawdzi czy są one anagramami.
"""

def czy_jest_anagramem(slowo1, slowo2):
    #TODO

czy_jest_anagramem("test", "estt")