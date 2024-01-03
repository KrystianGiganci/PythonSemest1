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
    # Odczytanie zdarzeń zarejestrowanych przez komputer
    events = pygame.event.get()

    pygame.display.update()  # Odświeżenie wyświetlanego okna
    pass

pygame.quit()  # Zamknięcie aplikacji
quit()  # Zamknięcie skryptu
