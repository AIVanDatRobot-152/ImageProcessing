import pygame
import random
import time

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Snake and food setup
snake_pos = []  # Snake's body will be initialized after start
def reset_snake():
    global snake_pos, snake_dir, change_to, food_pos, food_spawn, score
    snake_pos = [[100, 50], [90, 50], [80, 50]]  # Initial snake body
    snake_dir = "RIGHT"
    change_to = snake_dir
    food_pos = [random.randrange(1, (WIDTH//CELL_SIZE)) * CELL_SIZE,
                random.randrange(1, (HEIGHT//CELL_SIZE)) * CELL_SIZE]
    food_spawn = True
    score = 0
reset_snake()

# Score
score = 0

def display_start_screen():
    font = pygame.font.SysFont('times new roman', 50)
    start_surface = font.render('Press SPACE to Start', True, WHITE)
    start_rect = start_surface.get_rect()
    start_rect.center = (WIDTH / 2, HEIGHT / 2)
    screen.fill(BLACK)
    screen.blit(start_surface, start_rect)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False

# Game over function
def game_over():
    font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = font.render('Your Score: ' + str(score), True, RED)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (WIDTH/2, HEIGHT/4)
    screen.fill(BLACK)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    reset_snake()
    display_start_screen()

# Display start screen
display_start_screen()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not snake_dir == "DOWN":
                change_to = "UP"
            elif event.key == pygame.K_DOWN and not snake_dir == "UP":
                change_to = "DOWN"
            elif event.key == pygame.K_LEFT and not snake_dir == "RIGHT":
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT and not snake_dir == "LEFT":
                change_to = "RIGHT"

    # Change direction based on input
    snake_dir = change_to

    # Move the snake
    if snake_dir == "UP":
        snake_pos[0][1] -= CELL_SIZE
    if snake_dir == "DOWN":
        snake_pos[0][1] += CELL_SIZE
    if snake_dir == "LEFT":
        snake_pos[0][0] -= CELL_SIZE
    if snake_dir == "RIGHT":
        snake_pos[0][0] += CELL_SIZE

    # Snake body growing mechanism
    # If food and snake collide
    if snake_pos[0] == food_pos:
        score += 10
        food_spawn = False
    else:
        snake_pos.pop()

    # Spawn food
    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH//CELL_SIZE)) * CELL_SIZE,
                    random.randrange(1, (HEIGHT//CELL_SIZE)) * CELL_SIZE]
    food_spawn = True

    # Add new head to snake
    snake_pos.insert(0, list(snake_pos[0]))

    # Game over conditions
    if (snake_pos[0][0] < 0 or snake_pos[0][0] >= WIDTH or
        snake_pos[0][1] < 0 or snake_pos[0][1] >= HEIGHT):
        game_over()

    # Check if the snake bites itself
    for block in snake_pos[1:]:
        if snake_pos[0] == block:
            game_over()

    # Refresh screen
    screen.fill(BLACK)

    # Draw snake
    for pos in snake_pos:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], CELL_SIZE, CELL_SIZE))

    # Draw food
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))

    # Display score
    font = pygame.font.SysFont('times new roman', 20)
    score_surface = font.render('Score: ' + str(score), True, WHITE)
    screen.blit(score_surface, (10, 10))

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    clock.tick(15)
