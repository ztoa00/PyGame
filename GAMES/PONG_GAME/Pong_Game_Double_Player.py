import pygame

pygame.init()

SIZE = WIDTH, HEIGHT = 1360, 720
BORDER = 10
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
BLUE_COLOR = (0, 0, 255)
RED_COLOR = (255, 0, 0)

HIT_SOUND = pygame.mixer.Sound('h.wav')


# Class for Paddle


class Paddle:

    P_WIDTH = 10
    P_HEIGHT = 100
    VELOCITY = 2

    def __init__(self, name):
        self.name = name
        self.Y = (HEIGHT - self.P_HEIGHT) // 2
        self.VY = self.VELOCITY

        if self.name not in ["LEFT", "RIGHT"]:
            raise ValueError

    def show_paddle(self, paddle_color):

        if self.name == "LEFT":
            pygame.draw.rect(screen, paddle_color, (0, self.Y, self.P_WIDTH, self.P_HEIGHT))

        if self.name == "RIGHT":
            pygame.draw.rect(screen, paddle_color, (WIDTH - self.P_WIDTH, self.Y, self.P_WIDTH, self.P_HEIGHT))

    def update_paddle_up(self):

        # Erase the Paddle in Previous Position
        self.show_paddle(BLACK_COLOR)

        # Updating Paddle Position
        new_y = self.Y - self.VY

        if new_y > BORDER:
            self.Y = new_y

        # Show the Paddle in New Position
        self.show_paddle(RED_COLOR)

    def update_paddle_down(self):
        # Erase the Paddle in Previous Position
        self.show_paddle(BLACK_COLOR)

        # Updating Paddle Position
        new_y = self.Y + self.VY

        if new_y < HEIGHT - BORDER - self.P_HEIGHT:
            self.Y = new_y

        # Show the Paddle in New Position
        self.show_paddle(RED_COLOR)


# class for Ball


class Ball:

    RADIUS = 12
    VELOCITY = 2

    def __init__(self):
        self.X = WIDTH - Paddle.P_WIDTH - self.RADIUS
        self.Y = HEIGHT // 2
        self.VX = - self.VELOCITY
        self.VY = - self.VELOCITY

    def show_ball(self, ball_color):
        pygame.draw.circle(screen, ball_color, (self.X, self.Y), self.RADIUS)

    def update_ball(self):

        # Updating Ball Position
        new_x = self.X + self.VX
        new_y = self.Y + self.VY

        if new_y < BORDER + self.RADIUS or new_y > HEIGHT - BORDER - self.RADIUS:
            HIT_SOUND.play()
            self.VY = - self.VY

        elif new_x > WIDTH - Paddle.P_WIDTH - self.RADIUS and (1 < abs(new_y - right_paddle.Y) < Paddle.P_HEIGHT):
            HIT_SOUND.play()
            self.VX = - self.VX

        elif new_x < Paddle.P_WIDTH + self.RADIUS and (1 < abs(new_y - left_paddle.Y) < Paddle.P_HEIGHT):
            HIT_SOUND.play()
            self.VX = - self.VX

        elif new_x < 0 or new_x > WIDTH:
            pygame.quit()

        else:

            # Erase the Ball in Previous Position
            self.show_ball(BLACK_COLOR)

            self.X = self.X + self.VX
            self.Y = self.Y + self.VY

            # Show the Ball in New Position
            self.show_ball(BLUE_COLOR)


# Driver Code


screen = pygame.display.set_mode(SIZE)

pygame.display.set_caption("PONG_GAME")
pygame.draw.rect(screen, WHITE_COLOR, (0, 0, WIDTH, BORDER))
pygame.draw.rect(screen, WHITE_COLOR, (0, HEIGHT - BORDER, WIDTH, BORDER))

left_paddle = Paddle("LEFT")
left_paddle.show_paddle(RED_COLOR)
right_paddle = Paddle("RIGHT")
right_paddle.show_paddle(RED_COLOR)

ball = Ball()
ball.show_ball(BLUE_COLOR)

# clock = pygame.time.Clock()

run = True
while run:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        run = False

    key = pygame.key.get_pressed()

    if key[pygame.K_UP]:
        right_paddle.update_paddle_up()

    if key[pygame.K_DOWN]:
        right_paddle.update_paddle_down()

    if key[pygame.K_w]:
        left_paddle.update_paddle_up()

    if key[pygame.K_s]:
        left_paddle.update_paddle_down()

    ball.update_ball()
    pygame.display.flip()

    # clock.tick(1000)
