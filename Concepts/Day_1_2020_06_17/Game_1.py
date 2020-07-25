"""


import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 50)
    # circle - shape_to_draw
    # screen - screen_where_to_draw
    # (0, 0, 255) - drawing_color_in_rgb
    # (25, 250) - position_of_draw_in_screen
    # 50 - radius_because_of_circle_shape) if rect then height and width

    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 50)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()



"""














"""

import pygame
pygame.init()


SIZE = HEIGHT, WIDTH = 500, 500
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Game_1")
# this is a our game clock. We use this to track time within the game, and this is mostly used for FPS
clock = pygame.time.Clock()

crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    pygame.display.update()
    clock.tick(60)


""
you'll see that we run a pygame.display.update(). 
It's important to note the difference between display.update() and display.flip(). 
Display.flip will update the entire surface. Basically the entire screen. 
Display.update can just update specific areas of the screen. 
That said, if you do not pass a parameter, then update will update the entire surface as well, 
basically making flip() pointless for our interests. 
There might come times when you want to use flip for very specific tasks, however.
""



"""
