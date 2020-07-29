import pygame


pygame.init()


SIZE = WIDTH, HEIGHT = 1200, 600
RECT_X, RECT_Y = 0, 0
RECT_WIDTH, RECT_HEIGHT = 20, 20
VELOCITY = 3
VELOCITY_Y = VELOCITY


screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("RECT")


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Moving by velocity for each step

    RECT_Y += VELOCITY_Y

    # Forward moving or backward decision

    if RECT_Y <= 0:
        VELOCITY_Y = VELOCITY
    if RECT_Y >= HEIGHT - RECT_HEIGHT:
        VELOCITY_Y = -VELOCITY

    # To Delete a Previous Rect

    screen.fill((0, 0, 0))

    # To Draw a new Rect

    pygame.draw.rect(screen, (0, 0, 255), (RECT_X, RECT_Y,  RECT_WIDTH, RECT_HEIGHT))
    pygame.display.update()
