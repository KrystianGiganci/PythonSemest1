import time


def pasek_ladowania(gotowe, wszystko=100):
    """
    Znak # oznaczamy wykonaną część
    Znak - oznaczamy niewykonaną część
    """
    wykonane = round(10*gotowe/wszystko)
    niewykonane = 10 - wykonane

    tekst_wykonane = "#" * wykonane
    tekst_niewykonane = '-' * niewykonane
    print(f'\r[{tekst_wykonane}{tekst_niewykonane}]', end=' ')
    pass


for i in range(100):
    pasek_ladowania(gotowe=i, wszystko=50)  # dobrze
    pasek_ladowania(wszystko=50, gotowe=i)  # dobrze
    pasek_ladowania(50, i)                  # źle
    time.sleep(0.1)
    pass
