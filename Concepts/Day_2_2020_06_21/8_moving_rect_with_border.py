import pygame


pygame.init()


SIZE = WIDTH, HEIGHT = 1200, 600

BORDER_TOP_X = BORDER_TOP_Y = BORDER_LEFT_X = BORDER_LEFT_Y = 0
BORDER_DOWN_X = BORDER_RIGHT_Y = 0
BORDER_DOWN_Y = HEIGHT - 10
BORDER_RIGHT_X = WIDTH - 10
BORDER_TOP_HEIGHT = BORDER_DOWN_HEIGHT = BORDER_LEFT_WIDTH = BORDER_RIGHT_WIDTH = 10
BORDER_TOP_WIDTH = BORDER_DOWN_WIDTH = WIDTH
BORDER_LEFT_HEIGHT = BORDER_RIGHT_HEIGHT = HEIGHT

BORDER = 10

RECT_X, RECT_Y = 10, 10
RECT_WIDTH, RECT_HEIGHT = 20, 20
VELOCITY = 3


screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("RECT")


def clear_screen():
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (BORDER_TOP_X, BORDER_TOP_Y, BORDER_TOP_WIDTH, BORDER_TOP_HEIGHT))
    pygame.draw.rect(screen, (255, 255, 255), (BORDER_DOWN_X, BORDER_DOWN_Y, BORDER_DOWN_WIDTH, BORDER_DOWN_HEIGHT))
    pygame.draw.rect(screen, (255, 255, 255), (BORDER_LEFT_X, BORDER_LEFT_Y, BORDER_LEFT_WIDTH, BORDER_LEFT_HEIGHT))
    pygame.draw.rect(screen, (255, 255, 255), (BORDER_RIGHT_X, BORDER_RIGHT_Y, BORDER_RIGHT_WIDTH, BORDER_RIGHT_HEIGHT))


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and RECT_X - RECT_WIDTH > 0:
        RECT_X -= VELOCITY
    if key[pygame.K_RIGHT] and RECT_X + RECT_WIDTH < WIDTH - BORDER:
        RECT_X += VELOCITY
    if key[pygame.K_UP] and RECT_Y - RECT_HEIGHT > 0:
        RECT_Y -= VELOCITY
    if key[pygame.K_DOWN] and RECT_Y + RECT_HEIGHT < HEIGHT - BORDER:
        RECT_Y += VELOCITY

    # To Delete a Previous Rect

    clear_screen()

    # To Draw a new Rect

    pygame.draw.rect(screen, (0, 0, 255), (RECT_X, RECT_Y,  RECT_WIDTH, RECT_HEIGHT))
    pygame.display.update()
