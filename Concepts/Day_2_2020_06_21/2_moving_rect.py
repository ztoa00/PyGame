import pygame


pygame.init()


SIZE = WIDTH, HEIGHT = 1200, 600
RECT_X, RECT_Y = 0, 0
RECT_WIDTH, RECT_HEIGHT = 20, 20
VELOCITY = 1

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("RECT")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    """
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        RECT_X -= VELOCITY
    if key[pygame.K_RIGHT]:
        RECT_X += VELOCITY
    if key[pygame.K_UP]:
        RECT_Y -= VELOCITY
    if key[pygame.K_DOWN]:
        RECT_Y += VELOCITY
    """

    # Before Update new Position or coordinate check if rect is within screen or outside of screen

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and RECT_X - RECT_WIDTH > 0:
        RECT_X -= VELOCITY
    if key[pygame.K_RIGHT] and RECT_X + RECT_WIDTH < WIDTH:
        RECT_X += VELOCITY
    if key[pygame.K_UP] and RECT_Y - RECT_HEIGHT > 0:
        RECT_Y -= VELOCITY
    if key[pygame.K_DOWN] and RECT_Y + RECT_HEIGHT < HEIGHT:
        RECT_Y += VELOCITY

    # To Delete a Previous Rect

    screen.fill((0, 0, 0))

    # To Draw a new Rect

    pygame.draw.rect(screen, (0, 0, 255), (RECT_X, RECT_Y,  RECT_WIDTH, RECT_HEIGHT))
    pygame.display.update()
