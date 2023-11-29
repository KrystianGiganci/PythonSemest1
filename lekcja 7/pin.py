PIN = "1234"
ROK_URODZENIA = '2000'
HASLO = 'QWERTY'

while True:
    input_pin = input("Podaj PIN: ")
    if input_pin != PIN:
        print("Odmowa dostępu :c")
        continue
    input_rok_urodzenia = input("Podaj rok urodzenia: ")
    if input_rok_urodzenia != ROK_URODZENIA:
        print("Odmowa dostępu :c")
        continue
    input_haslo = input("Wprowadź hasło: ")
    if input_haslo != HASLO:
        print("Odmowa dostępu!")
        continue

    print("Zalogowano poprawnie!")
    break

print("Masz na swoim koncie 10 złotych.")