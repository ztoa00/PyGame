import pygame
import random

pygame.init()


DISPLAY_WIDTH = 750
DISPLAY_HEIGHT = 600

CAR_WIDTH = 100
CAR_HEIGHT = 100

THING_WIDTH = 100
THING_HEIGHT = 100
THING_SPEED = 7

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

ROAD_DIVIDER_WIDTH = 10
ROAD_DIVIDER_HEIGHT = 100
ROAD_DIVIDER_SPEED = 7

DIVIDER_INTERVAL = DISPLAY_HEIGHT // ROAD_DIVIDER_HEIGHT
DIVIDER_INTERVAL_WITH_SPACES = DIVIDER_INTERVAL - 1
SPACE = (ROAD_DIVIDER_HEIGHT * 2) // (DIVIDER_INTERVAL_WITH_SPACES - 1)
DIVIDERS_Y = []
count = 0
for i in range(DIVIDER_INTERVAL_WITH_SPACES):
    DIVIDERS_Y.append(count)
    count += ROAD_DIVIDER_HEIGHT + SPACE

PAUSE = False


CAR_IMG = pygame.image.load('racecar.png')
CRASH_SOUND = pygame.mixer.Sound("Crash.wav")


GAME_DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('A bit Racey')
pygame.display.set_icon(CAR_IMG)
clock = pygame.time.Clock()


def road_divider(y):
    div1_pos = (DISPLAY_WIDTH // 3, y, ROAD_DIVIDER_WIDTH, ROAD_DIVIDER_HEIGHT)
    div2_pos = ((DISPLAY_WIDTH // 3) * 2, y, ROAD_DIVIDER_WIDTH, ROAD_DIVIDER_HEIGHT)
    pygame.draw.rect(GAME_DISPLAY, GREEN, div1_pos)
    pygame.draw.rect(GAME_DISPLAY, GREEN, div2_pos)


def car(x, y):
    GAME_DISPLAY.blit(CAR_IMG, (x, y))


def crash(dodged):

    pygame.mixer.Sound.play(CRASH_SOUND)
    pygame.mixer.music.stop()

    message_display(msg='You Crashed', font_position=(DISPLAY_WIDTH/2, (DISPLAY_HEIGHT/2)-25), font_size=50)
    message_display(msg='Dodged : {}'.format(dodged), font_position=(DISPLAY_WIDTH / 2, (DISPLAY_HEIGHT / 2)+25))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        button(msg="Play Again", button_pos=BUTTON1_POS, color=GREEN, hover_color=LIGHT_GREEN, action=game_loop)
        button(msg="Quit", button_pos=BUTTON2_POS, color=RED, hover_color=LIGHT_RED, action=quit_game)

        pygame.display.update()
        clock.tick(15)


def get_thing_x():
    x1 = ((DISPLAY_WIDTH // 3) // 2) - (THING_WIDTH / 2)
    x2 = x1 + (DISPLAY_WIDTH // 3)
    x3 = x2 + (DISPLAY_WIDTH // 3)
    return random.choice([x1, x2, x3])


def things(thing_x, thing_y):
    pygame.draw.rect(GAME_DISPLAY, BLUE, [thing_x, thing_y, THING_WIDTH, THING_HEIGHT])


def things_dodged(count):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("Dodged: "+str(count), True, BLACK)
    GAME_DISPLAY.blit(text, (0, 0))


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
        message_display(msg="A Bit Racey", font_position=(DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2), font_size=80)

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

    pygame.mixer.music.load('Night_Drive.mp3')
    pygame.mixer.music.play(-1)

    global PAUSE

    # car Attributes
    x = (DISPLAY_WIDTH // 2) - (CAR_WIDTH // 2)
    y = DISPLAY_HEIGHT - CAR_HEIGHT
    x_change = 0
    #######################
    y_change = 0
    #######################

    # objects / Things / Obstacles
    thing_x = get_thing_x()
    thing_y = -600

    # Score Attributes
    dodged = 0

    # game loop
    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                ##############################################
                if event.key == pygame.K_UP:
                    y_change = -5
                if event.key == pygame.K_DOWN:
                    y_change = 5
                ##############################################
                if event.key == pygame.K_p:
                    PAUSE = True
                    paused()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                ##############################################
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                ##############################################

        x += x_change
        #######################
        if 0 < y + y_change < DISPLAY_HEIGHT - CAR_HEIGHT:
            y += y_change
        #######################

        GAME_DISPLAY.fill(GREY)

        for i in range(len(DIVIDERS_Y)):
            road_divider(DIVIDERS_Y[i])
            DIVIDERS_Y[i] += ROAD_DIVIDER_SPEED
            if DIVIDERS_Y[i] > DISPLAY_HEIGHT:
                DIVIDERS_Y[i] = 0 - ROAD_DIVIDER_HEIGHT - SPACE

        car(x, y)
        if x > DISPLAY_WIDTH - CAR_WIDTH or x < 0:
            crash(dodged)

        things(thing_x, thing_y)
        thing_y += THING_SPEED
        if thing_y > DISPLAY_HEIGHT:
            thing_y = 0 - THING_HEIGHT
            thing_x = get_thing_x()
            dodged += 1
            # increase speed of thing to increase toughness
            # thing_speed += 1
            # thing_width += (dodged * 1.2)

        if thing_y <= y <= thing_y + THING_HEIGHT:
            if thing_x <= x <= thing_x + THING_WIDTH or thing_x <= x + CAR_WIDTH <= thing_x + THING_WIDTH:
                crash(dodged)
        things_dodged(dodged)

        pygame.display.update()
        clock.tick(60)


# Driver Code

game_intro()
game_loop()
quit_game()
