"""
Napisz program, który poprosi użytkownika o podanie 10 liczb, ale tak żeby się nie powtarzały.
Jeśli któraś się powtórzy należy powiadomić go o tym i poprosić o nową liczbę.
"""

liczby = []

while True:
    a = int(input("Podaj liczbę: "))

    if a in liczby:   # Sprawdzenie czy się powtarza
        print("Wprowadzono już taką liczbę!")
        pass
    else:             # Dodanie nowej unikalnej liczby
        liczby.append(a)
        if len(liczby) == 10:
            break
        pass

print(liczby)
