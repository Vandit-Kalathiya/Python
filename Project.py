import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 900, 700
PADDLE_WIDTH, PADDLE_HEIGHT = 180, 20
BALL_RADIUS = 20
BG = (0, 0, 0)
BALL_COLOR = (0, 234, 255)
c = 0

# Creating the game console  using dimensions
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball.!")

# Creating the paddle
paddle = pygame.Rect((WIDTH - PADDLE_WIDTH) // 2, HEIGHT - PADDLE_HEIGHT - 5, PADDLE_WIDTH, PADDLE_HEIGHT)

# Creating a list to store the falling balls
balls = []

t = -1
# Clock to control the frame rate
clock = pygame.time.Clock()
# Function to create a new ball
def create_ball():
    x = random.randint(BALL_RADIUS, WIDTH - BALL_RADIUS)
    y = -BALL_RADIUS - random.random() * 100 - random.random() * 100
    speed = 2  # random.uniform(2, 5)
    t = y
    return pygame.Rect(x, y, BALL_RADIUS, BALL_RADIUS), speed
    
    # Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(c)
            pygame.quit()
            sys.exit()

    # Moving the paddle with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-15, 0)
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.move_ip(15, 0)

    # Creating a new ball at random intervals
    if random.random() < 0.008:
        balls.append(create_ball())

    # Moving the balls
    for ball, speed in balls:
        ball.move_ip(0, speed)

    # print(balls)

    # Checking for collisions with the paddle
    for ball, _ in balls:
        if ball.colliderect(paddle):
            c += 1
            balls.remove((ball, _))

    # Removing balls that go off the screen
    balls = [(ball, speed) for ball, speed in balls if ball.centery < HEIGHT]

    # Clearing the screen
    screen.fill(BG)

    # Drawing the paddle
    pygame.draw.rect(screen, BALL_COLOR, paddle)

    # Drawing the balls
    for ball, _ in balls:
        pygame.draw.circle(screen, BALL_COLOR, ball.center, BALL_RADIUS)

    # Updating the display
    pygame.display.flip()

    # Seting the frame rate
    clock.tick(60)




