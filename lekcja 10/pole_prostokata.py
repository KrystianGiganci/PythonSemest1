import math


def prostokat(a, b):
    pole = a * b
    print(f'Pole prostokąta o wymiarach {a}x{b} wynosi {pole}')
    return pole


# print(pole)
imie = input("Wpisz swoje imie: ")
pole = prostokat(a=3, b=5)
print(pole)


def kolo(r, pi=3.14):
    pole = pi * (r**2)
    print(f'Koło o promieniu {r} wynosi {pole}')


prostokat(1, 10)
prostokat(80, 20)

kolo(4, math.pi)
print(math.pi)
kolo(4)
