import pygame  # Import modułu
pygame.init()  # Inicjalizacja modułu

# Utworzenie okna o określonych wymiarach
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Nadanie nazwy oknu
pygame.display.set_caption('Pierwsza Gra')


# Zmienna określająca, czy należy zamknąć okno
game_status = True

# Kod wykonywany póki aplikacja jest uruchomiona
while game_status:
    events = pygame.event.get()
    for event in events:
        # Odkomentuj tę linijkę by zobaczyć co jest rejestrowane przez komputer
        # kiedy ruszasz myszką, klikasz klawisz na klawiaturze
        print(event)

    # Sprawdzenie, czy należy zamknąć aplikację
    # Czy kliknięto na X
    if event.type == pygame.QUIT:
        game_status = False
        pass

    pygame.display.update()  # Odświeżenie wyświetlanego okna

pygame.quit()  # Zamknięcie aplikacji
quit()  # Zamknięcie skryptu
