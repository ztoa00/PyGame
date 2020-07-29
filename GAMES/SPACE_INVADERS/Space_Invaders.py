import random
import pygame

pygame.init()


######################################


# GLOBAL VARIABLES


######################################


DISPLAY_WIDTH = 750
DISPLAY_HEIGHT = 600

BUTTON_WIDTH = 150
BUTTON_HEIGHT = 50
BUTTON_Y = DISPLAY_HEIGHT - 150
BUTTON1_X = ((DISPLAY_WIDTH // 3) // 2) - (BUTTON_WIDTH / 2)
BUTTON2_X = BUTTON1_X + ((DISPLAY_WIDTH // 3) * 2)
BUTTON1_POS = (BUTTON1_X, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
BUTTON2_POS = (BUTTON2_X, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIGHT_RED = (200, 0, 0)
LIGHT_GREEN = (0, 200, 0)


PAUSE = False


LOGO = pygame.image.load('src/images/logo.png')
BG_IMG = pygame.image.load('src/images/bg.png')
SHOOT_SOUND = pygame.mixer.Sound("src/audios/shoot.wav")
BULLET_HTI_SOUND = pygame.mixer.Sound("src/audios/bullet_hit.wav")
EXPLOSION_SOUND = pygame.mixer.Sound("src/audios/explosion.wav")
pygame.mixer.music.load('src/audios/bg.mp3')

GAME_DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Space_Invaders')
pygame.display.set_icon(LOGO)
clock = pygame.time.Clock()


######################################


# PLAYER JET


#######################################


class Jet:

    JET_WIDTH = 100
    JET_HEIGHT = 100

    JET_IMG = pygame.image.load('src/images/jet.png')
    JET_IMG = pygame.transform.scale(JET_IMG, (JET_WIDTH, JET_HEIGHT))

    X = (DISPLAY_WIDTH // 2) - (JET_WIDTH // 2)
    Y = DISPLAY_HEIGHT - JET_HEIGHT

    def show(self):
        GAME_DISPLAY.blit(self.JET_IMG, (self.X, self.Y))

    def update(self, new_x, new_y):
        if 0 < self.X + new_x < DISPLAY_WIDTH - self.JET_WIDTH:
            self.X += new_x
        if 0 < self.Y + new_y < DISPLAY_HEIGHT - self.JET_HEIGHT:
            self.Y += new_y
        self.show()

    def check_crashed(self, enemies):
        for enemy in enemies:
            if enemy.Y < self.Y < (enemy.Y + enemy.ENEMY_HEIGHT) or \
                    enemy.Y < (self.Y + self.JET_HEIGHT) < (enemy.Y + enemy.ENEMY_HEIGHT):
                if enemy.X < self.X < (enemy.X + enemy.ENEMY_WIDTH) or \
                        enemy.X < (self.X + self.JET_WIDTH) < (enemy.X + enemy.ENEMY_WIDTH):
                    return True
        return False


######################################


# PLAYER_JET_BULLET


#######################################


class Bullet:

    BULLET_WIDTH = 10
    BULLET_HEIGHT = 20
    BULLET_SPEED = 3
    ACTIVE_STATE = False

    def __init__(self, x, y):
        self.X = x
        self.Y = y
        self.ACTIVE_STATE = True

    def show(self):
        pygame.draw.rect(GAME_DISPLAY, RED, [self.X, self.Y, self.BULLET_WIDTH, self.BULLET_HEIGHT])

    def update(self):
        if self.ACTIVE_STATE:
            if 0 < self.Y < DISPLAY_HEIGHT:
                self.Y -= self.BULLET_SPEED
                self.show()
            else:
                self.ACTIVE_STATE = False

    def check_bullet_hit(self, enemies):
        for enemy in enemies:
            if enemy.Y < self.Y < (enemy.Y + enemy.ENEMY_HEIGHT):
                if enemy.X < self.X < (enemy.X + enemy.ENEMY_WIDTH) or \
                        enemy.X < (self.X + self.BULLET_WIDTH) < (enemy.X + enemy.ENEMY_WIDTH):
                    enemy.ACTIVE_STATE = False
                    self.ACTIVE_STATE = False
                    return True
        return False


######################################


# ENEMY / INVADER


#######################################


class Enemy:

    ENEMY_WIDTH = 50
    ENEMY_HEIGHT = 50
    ENEMY_SPEED = 2
    ENEMY_IMG = pygame.image.load('src/images/enemy.png')
    ENEMY_IMG = pygame.transform.scale(ENEMY_IMG, (ENEMY_WIDTH, ENEMY_HEIGHT))
    ACTIVE_STATE = False
    REACHED_EARTH = False

    def __init__(self):
        self.X = random.randint(0, DISPLAY_WIDTH-self.ENEMY_WIDTH)
        self.Y = - self.ENEMY_HEIGHT
        self.ACTIVE_STATE = True

    def show(self):
        GAME_DISPLAY.blit(self.ENEMY_IMG, (self.X, self.Y))

    def update(self):
        if self.ACTIVE_STATE:
            if self.Y < DISPLAY_HEIGHT:
                self.Y += self.ENEMY_SPEED
                self.show()
            else:
                self.REACHED_EARTH = True
                self.ACTIVE_STATE = False


#####################################


# DISPLAY SCORE AND LIFE ON SCREEN


######################################


def score(score_count, life_count):
    font = pygame.font.SysFont("comicsansms", 25)
    text1 = font.render("Score : "+str(score_count), True, LIGHT_GREEN)
    text2 = font.render("Remaining Life: "+str(life_count), True, LIGHT_RED)
    GAME_DISPLAY.blit(text1, (0, 0))
    GAME_DISPLAY.blit(text2, (0, 20))


#####################################


# DISPLAY MESSAGE ON SCREEN


######################################


def message_display(msg, font_position, font_name="freesansbold.ttf", font_size=20, font_color=WHITE):

    font_style = pygame.font.Font(font_name, font_size)
    text_surf = font_style.render(msg, True, font_color)
    text_rect = text_surf.get_rect()
    text_rect.center = font_position

    GAME_DISPLAY.blit(text_surf, text_rect)


#####################################


# DISPLAY BUTTON ON SCREEN


######################################


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


#####################################


# DISPLAY THE GAME INTRO SCREEN


######################################


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


#####################################


# DISPLAY THE PAUSED SCREEN


######################################


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


#####################################


# RESUMING / UN_PAUSE


######################################


def un_pause():
    global PAUSE
    pygame.mixer.music.unpause()
    PAUSE = False


#####################################


# DISPLAY THE GAME OVER SCREEN


######################################


def game_over(msg, score_count):
    pygame.mixer.Sound.play(EXPLOSION_SOUND)
    pygame.mixer.music.stop()

    message_display(msg=msg, font_position=(DISPLAY_WIDTH / 2, (DISPLAY_HEIGHT / 2) - 25), font_size=50)
    message_display(msg='Score : {}'.format(score_count), font_position=(DISPLAY_WIDTH / 2, (DISPLAY_HEIGHT / 2) + 25))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        button(msg="Play Again", button_pos=BUTTON1_POS, color=GREEN, hover_color=LIGHT_GREEN, action=game_loop)
        button(msg="Quit", button_pos=BUTTON2_POS, color=RED, hover_color=LIGHT_RED, action=quit_game)

        pygame.display.update()
        clock.tick(15)


#####################################


# CLOSING RESOURCES ANG QUIT


######################################


def quit_game():
    pygame.mixer.music.stop()
    pygame.quit()
    quit()


#####################################


# GAME LOOP


######################################


def game_loop():

    pygame.mixer.music.play(-1)
    global PAUSE

    # GAME Attributes
    score_count = 0
    life = 10
    jet = Jet()
    jet.show()
    x_change = 0
    y_change = 0
    bullets_list = []
    enemies_list = []
    for i in range(3):
        enemy = Enemy()
        enemies_list.append(enemy)

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
                if event.key == pygame.K_SPACE:
                    pygame.mixer.Sound.play(SHOOT_SOUND)
                    bullet = Bullet(jet.X + (jet.JET_WIDTH // 2), jet.Y)
                    bullets_list.append(bullet)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        GAME_DISPLAY.blit(BG_IMG, (0, 0))

        jet.update(x_change, y_change)
        if jet.check_crashed(enemies_list):
            game_over('Crashed', score_count)

        for bullet in bullets_list:
            if bullet.check_bullet_hit(enemies_list):
                pygame.mixer.Sound.play(BULLET_HTI_SOUND)
                score_count += 1
            if bullet.ACTIVE_STATE:
                bullet.update()
            else:
                bullets_list.remove(bullet)

        for enemy in enemies_list:
            if enemy.ACTIVE_STATE:
                enemy.update()
            else:
                if enemy.REACHED_EARTH:
                    life -= 1
                enemies_list.remove(enemy)
                new_enemy = Enemy()
                enemies_list.append(new_enemy)

        if life < 0:
            game_over('Game Over !', score_count)

        score(score_count, life)

        pygame.display.update()
        clock.tick(60)


#####################################


# Driver Code


######################################


if __name__ == "__main__":
    game_intro()
    game_loop()
    quit_game()
