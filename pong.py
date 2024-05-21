import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Ball dimensions
BALL_WIDTH = 10
BALL_HEIGHT = 10

# Paddle dimensions
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100

# Speed
BALL_SPEED = 5
PADDLE_SPEED = 10

# Font
FONT = pygame.font.Font(None, 36)

# Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

# Ball
ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_WIDTH // 2, SCREEN_HEIGHT // 2 - BALL_HEIGHT // 2, BALL_WIDTH, BALL_HEIGHT)
ball_dx = BALL_SPEED * random.choice([-1, 1])
ball_dy = BALL_SPEED * random.choice([-1, 1])

# Paddles
left_paddle = pygame.Rect(10, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(SCREEN_WIDTH - 20, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Scores
left_score = 0
right_score = 0

# Game loop
running = True
clock = pygame.time.Clock()

def reset_ball():
    global ball_dx, ball_dy
    ball.x = SCREEN_WIDTH // 2 - BALL_WIDTH // 2
    ball.y = SCREEN_HEIGHT // 2 - BALL_HEIGHT // 2
    ball_dx = BALL_SPEED * random.choice([-1, 1])
    ball_dy = BALL_SPEED * random.choice([-1, 1])

def draw_scores():
    left_text = FONT.render(str(left_score), True, WHITE)
    right_text = FONT.render(str(right_score), True, WHITE)
    screen.blit(left_text, (SCREEN_WIDTH // 4, 20))
    screen.blit(right_text, (3 * SCREEN_WIDTH // 4, 20))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle.bottom < SCREEN_HEIGHT:
        left_paddle.y += PADDLE_SPEED
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle.bottom < SCREEN_HEIGHT:
        right_paddle.y += PADDLE_SPEED

    ball.x += ball_dx
    ball.y += ball_dy

    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_dy = -ball_dy

    if ball.left <= 0:
        right_score += 1
        reset_ball()
    if ball.right >= SCREEN_WIDTH:
        left_score += 1
        reset_ball()

    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_dx = -ball_dx

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))
    draw_scores()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()