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


def set_position_image(img_list, position):
    image, surface, rect = img_list
    rect = surface.get_rect(center=position)
    return [image, surface, rect]


def calculate_player_movement(pressed_keys):
    speed = 10
    delta_y = 0
    delta_x = 0

    if pressed_keys[pygame.K_w]:
        delta_y -= speed
    if pressed_keys[pygame.K_s]:
        delta_y += speed
    if pressed_keys[pygame.K_a]:
        delta_x -= speed
    if pressed_keys[pygame.K_d]:
        delta_x += speed
    return [delta_x, delta_y]


def limit_position():
    # TODO
    pass


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
player = load_image('player.png', player_pos)
background_color = [10, 122, 207]


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

    # TODO - reakcja na klawisze

    # Uzupełnienie tła (zakrycie wcześniejszej ikonki gracza)
    screen_surface.fill(background_color)
    # Wyświetl gracza
    print_image(player)

    pressed_keys = pygame.key.get_pressed()
    # Obliczenie zmiany współrzędnych gracza
    delta_x, delta_y = calculate_player_movement(pressed_keys)

    # Zmiana wartości współrzędnych gracza
    player_pos[0] += delta_x
    player_pos[1] += delta_y

    # Zmieniamy położenie obrazu (ikonki gracza)
    player = set_position_image(player, player_pos)

    # Odświeżenie wyświetlanego okna
    pygame.display.update()

    clock.tick(60)
    pass

print("Zamykanie aplikacji")
# Zamknięcie aplikacji
pygame.quit()
# Zamknięcie skryptu
quit()
