import pygame
import random

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

BUTTON_WIDTH = 150
BUTTON_HEIGHT = 50
BUTTON_Y = DISPLAY_HEIGHT - 150
BUTTON1_X = ((DISPLAY_WIDTH // 3) // 2) - (BUTTON_WIDTH / 2)
BUTTON2_X = BUTTON1_X + ((DISPLAY_WIDTH // 3) * 2)
BUTTON1_POS = (BUTTON1_X, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
BUTTON2_POS = (BUTTON2_X, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)


PAUSE = False


LOGO = pygame.image.load('src/logo.png')

GAME_DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Space_Invaders')
pygame.display.set_icon(LOGO)
clock = pygame.time.Clock()


def message_display(msg, font_position, font_name="freesansbold.ttf", font_size=20, font_color=BLACK):

    font_style = pygame.font.Font(font_name, font_size)
    text_surf = font_style.render(msg, True, font_color)
    text_rect = text_surf.get_rect()
    text_rect.center = font_position

    GAME_DISPLAY.blit(text_surf, text_rect)


def button(msg, button_pos, color, hover_color, action=None):

    x, y, w, h = button_pos

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(GAME_DISPLAY, hover_color, button_pos)
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(GAME_DISPLAY, color, button_pos)

    message_display(msg=msg, font_position=((x+(w/2)), (y+(h/2))))


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        GAME_DISPLAY.fill(GREY)
        message_display(msg="Space Invaders", font_position=(DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2), font_size=80)

        button(msg="GO!", button_pos=BUTTON1_POS, color=GREEN, hover_color=LIGHT_GREEN, action=game_loop)
        button(msg="Quit", button_pos=BUTTON2_POS, color=RED, hover_color=LIGHT_RED, action=quit_game)

        pygame.display.update()
        clock.tick(15)


def paused():

    global PAUSE

    pygame.mixer.music.pause()
    message_display(msg='PAUSED', font_position=(DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2), font_size=77)

    while PAUSE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        button(msg="Continue", button_pos=BUTTON1_POS, color=GREEN, hover_color=LIGHT_GREEN, action=un_pause)
        button(msg="Quit", button_pos=BUTTON2_POS, color=RED, hover_color=LIGHT_RED, action=quit_game)

        pygame.display.update()
        clock.tick(15)


def un_pause():
    global PAUSE
    pygame.mixer.music.unpause()
    PAUSE = False


def quit_game():
    pygame.mixer.music.stop()
    pygame.quit()
    quit()


def game_loop():
    pass


# Driver Code

game_intro()
game_loop()
quit_game()
