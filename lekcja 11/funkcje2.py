# def komunikat(imie: str, wiek: int, wzrost: float) -> str:
#     return f"Osoba o imieniu {imie} ma {wiek} lat oraz {wzrost} m wzrostu"


# tekst = komunikat("Tomek", 22, 1.85)
# print(tekst)

"""
Przygotuj funkcję, która jako argument otrzymuje string oraz listę stringów, a zwraca
napis, gdzie pomiędzy elementy z listy dokładana jest zawartość pierwszego argumentu.
Przykład:
znak: "SPACJA", slowa: ["ala", 'ma', 'kota']    ->   nowy_teskt: alaSPACJAmaSPACJAkota
"""


def lacz_slowa(znak: str, lista):
    # tekst = lista[0]+znak
    tekst = ''
    for i in range(len(lista)-1):
        tekst += lista[i]+znak
    ######### ala?ma?kota?oraz?psa?a?takze?ma?

    tekst += lista[-1]  # tekst = tekst + lista[-1]
            # jaszczurke
    ####### ala?ma?kota?oraz?psa?a?takze?ma?jaszczurke
    return tekst

                    #    0      1     2      3        4     5     6       7      8
print(lacz_slowa("?", ["ala", 'ma', 'kota', 'oraz', 'psa', 'a', 'takze', 'ma','rozowa', 'jaszczurke']))
