import time


liczba = int(input("Wprowadź liczbę: "))

while liczba > 0:
    print(liczba)
    liczba -= 1
    time.sleep(1)
    pass

print("BOOOOOOM!!!")