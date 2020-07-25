import pygame

pygame.init()


DISPLAY_WIDTH = 750
DISPLAY_HEIGHT = 600

JET_WIDTH = 100
JET_HEIGHT = 100

ENEMY_WIDTH = 50
ENEMY_HEIGHT = 50

BULLET_WIDTH = 10
BULLET_HEIGHT = 20

BUTTON_WIDTH = 150
BUTTON_HEIGHT = 50
BUTTON_Y = DISPLAY_HEIGHT - 150
BUTTON1_X = ((DISPLAY_WIDTH // 3) // 2) - (BUTTON_WIDTH / 2)
BUTTON2_X = BUTTON1_X + ((DISPLAY_WIDTH // 3) * 2)
BUTTON1_POS = (BUTTON1_X, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
BUTTON2_POS = (BUTTON2_X, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)

BLACK = (0, 0, 0)
GREY = (100, 100, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
LIGHT_RED = (200, 0, 0)
LIGHT_GREEN = (0, 200, 0)

PAUSE = False


LOGO = pygame.image.load('src/images/logo.png')
BG_IMG = pygame.image.load('src/images/bg.png')
JET_IMG = pygame.image.load('src/images/jet.png')
JET_IMG = pygame.transform.scale(JET_IMG, (JET_WIDTH, JET_HEIGHT))
ENEMY_IMG = pygame.image.load('src/images/enemy.png')
ENEMY_IMG = pygame.transform.scale(ENEMY_IMG, (ENEMY_WIDTH, ENEMY_HEIGHT))
HIT_SOUND = pygame.mixer.Sound("src/audios/hit.wav")
pygame.mixer.music.load('src/audios/bg.mp3')

GAME_DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Space_Invaders')
pygame.display.set_icon(LOGO)
clock = pygame.time.Clock()


def jet(x, y):
    GAME_DISPLAY.blit(JET_IMG, (x, y))


def enemy(x, y):
    GAME_DISPLAY.blit(ENEMY_IMG, (x, y))


def bullet(bullet_x, bullet_y):
    pygame.draw.rect(GAME_DISPLAY, RED, [bullet_x, bullet_y, BULLET_WIDTH, BULLET_HEIGHT])


def score(count):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("Dodged: "+str(count), True, LIGHT_GREEN)
    GAME_DISPLAY.blit(text, (0, 0))


def message_display(msg, font_position, font_name="freesansbold.ttf", font_size=20, font_color=WHITE):

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

        GAME_DISPLAY.blit(BG_IMG, (0, 0))
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

    pygame.mixer.music.play(-1)
    global PAUSE

    # JET Attributes
    x = (DISPLAY_WIDTH // 2) - (JET_WIDTH // 2)
    y = DISPLAY_HEIGHT - JET_HEIGHT
    x_change = 0
    y_change = 0

    # Score Attribute
    score_count = 0

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
                if event.key == pygame.K_UP:
                    y_change = -5
                if event.key == pygame.K_DOWN:
                    y_change = 5
                if event.key == pygame.K_p:
                    PAUSE = True
                    paused()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        if 0 < x+x_change < DISPLAY_WIDTH - JET_WIDTH:
            x += x_change
        if 0 < y + y_change < DISPLAY_HEIGHT - JET_HEIGHT:
            y += y_change

        GAME_DISPLAY.blit(BG_IMG, (0, 0))
        jet(x, y)

        # enemy call
        # enemy(100, 200)

        # bullet
        # bullet(100, 200)

        score(score_count)
        pygame.display.update()
        clock.tick(60)


# Driver Code

game_intro()
game_loop()
quit_game()
