"""
Ogólny schemat tworzenia programu z pętlą while:
1. Przykładowy kod który wykonuje się przed pętlą
2. Pętla while:
    while warunek:
        kod który wykona się tylko gdy warunek jest prawdziwy
3. Kod który wykona się gdy skończy się pętla
"""
'''
a = int(input("Podaj jakąś liczbę: "))      # punkt pierwszy
# prosimy uzytkownika o podanie liczby
while a < 10:                               # punkt drugi
    print(a)      # pętla która wyświetli nam liczbę wpisaną przez użytkownika tylko gdy liczba ta jest mniejsza od 10
    a += 1        # a następnie powiększy tę liczbę o 1 (i jeśli nowa liczba jest mniejsza od 10 to ponownie ją wypisze)
    # to samo co a = a + 1
print("Dotarliśmy do końca programu!")      # punkt trzeci
'''
# Napiszcie program, który 10-krotnie wyświetli w konsoli napis “Cześć Gigancie!”

# i = 0
# while i < 25:
#     print("Cześć Gigancie!")
#     i += 1

import time

while True:
    print("Nie da się mnie zatrzymać!!")
    time.sleep(1)
    break
print("A może jednak się da?")