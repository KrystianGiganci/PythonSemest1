lista_ocen = [4124124,
              45123412241224,
              51231234,
              21312314, 4124124,
              45123412241224,
              51231234, 21312314,
              4124124, 45123412241224, 51231234,
              21312314, 4124124,
              45123412241224, 51231234, 21312314,
              4124124, 45123412241224, 51231234,
              21312314, 4124124, 45123412241224,
              51231234, 21312314, 4124124, 45123412241224, 51231234, 21312314,
              4124124, 45123412241224, 51231234, 21312314, 4124124,
              45123412241224,
              51231234, 21312314
              ]

for a in range(6):
    ocena = int(input("Podaj ocenę: "))  # Przyjęcie oceny od użytkownika
    lista_ocen.append(ocena)  # Dodawanie oceny do listy

print(lista_ocen)  # Wyświetlenie listy ocen
srednia = sum(lista_ocen)/len(lista_ocen)  # Policzenie średniej, czyli zsumowanie elementów listy
                                           # a następnie podzielenie sumy przez długość listy ocen
print(f"Twoja średnia to: {srednia}")
