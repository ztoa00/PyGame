import pygame

pygame.init()


DISPLAY_WIDTH = 750
DISPLAY_HEIGHT = 600


BLACK = (0, 0, 0)
GREY = (100, 100, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
LIGHT_RED = (200, 0, 0)
LIGHT_GREEN = (0, 200, 0)


LOGO = pygame.image.load('src/logo.png')
BG_IMG = pygame.image.load('src/bg.png')
HIT_SOUND = pygame.mixer.Sound("src/hit.wav")

GAME_DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Space_Invaders')
pygame.display.set_icon(LOGO)
clock = pygame.time.Clock()


while True:
    pygame.mixer.music.load('src/Night_Drive.mp3')
    pygame.mixer.music.play(-1)

    GAME_DISPLAY.blit(BG_IMG, (0, 0))
    pygame.display.update()
    while True:
        print(1)

