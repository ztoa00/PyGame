import pygame


pygame.init()


SIZE = WIDTH, HEIGHT = 500, 500
RECT_X, RECT_Y = 0, 0
RECT_WIDTH, RECT_HEIGHT = 50, 100

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("RECT")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.rect(screen, (0, 0, 255),(RECT_X, RECT_Y,  RECT_WIDTH, RECT_HEIGHT))
    pygame.display.update()
