"""
Stwórz grę, w której użytkownik ma za zadanie
odgadnąć liczbę, o której pomyślał komputer.
"""

import random  # import modułu, który pozwala na losowanie wartości

# Ustalamy zakres, z którego możemy wylosować liczbę
MINIMUM = 0
MAXIMUM = 100

# Wylosowanie wartości i zapisanie jej do zmiennej
wylosowana_liczba = random.randint(MINIMUM, MAXIMUM)

...
