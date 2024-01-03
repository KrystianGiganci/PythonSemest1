# Import modulu pygame, dzieki ktoremu tworzymy aplikacje okienkowa
import pygame

# Inicjalizacja modułu
pygame.init()
# Utworzenie okna o określonych wymiarach
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Nadanie nazwy oknu
pygame.display.set_caption('Pierwsza Gra')

# Utworzenie zegara, który nadzoruje stałe wartości fps
clock = pygame.time.Clock()


def load_image(img_path: str, position):
    image = pygame.image.load(img_path)
    surface = image.convert()

    transparent_color = (0, 0, 0)
    surface.set_colorkey(transparent_color)

    # Pozycja wyświetlania obiektu zapisana jest w rect
    rect = surface.get_rect(center=position)

    return [image, surface, rect]


def print_image(img_list) -> None:
    # [image, surface, rect]
    image, surface, rect = img_list
    screen_surface.blit(surface, rect)
    pass


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
player = load_image('player.png', player_pos)

# Zmienna określająca, czy należy zamknąć okno
game_status = True
# Kod wykonywany póki aplikacja jest uruchomiona
while game_status:

    # Odczytanie zdarzeń zarejestrowanych przez komputer
    events = pygame.event.get()

    for event in events:
        # Naciśnięto X - zamykanie aplikacji
        if event.type == pygame.QUIT:
            game_status = False
        pass  # for event

    # Wyświetl gracza
    print_image(player)

    # Odświeżenie wyświetlanego okna
    pygame.display.update()

    clock.tick(60)
    pass

print("Zamykanie aplikacji")
# Zamknięcie aplikacji
pygame.quit()
# Zamknięcie skryptu
quit()
