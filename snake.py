import pygame
import random

pygame.init()

# Screen
WIDTH, HEIGHT = 1530, 795
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

# Colors
DARK_GREEN = (1, 54, 1)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Snake
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

# Snake's Speed
snake_speed = 20

# Food
food_pos = [random.randrange(1, (WIDTH // 10)) * 10,
            random.randrange(1, (HEIGHT // 10)) * 10]
food_spawn = True

clock = pygame.time.Clock()
direction = "RIGHT"
change_to = direction

# Score
score = 0

# Game Over
game_over = False

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"

    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    # Moving the snake
    if direction == "UP":
        snake_pos[1] -= 10
    if direction == "DOWN":
        snake_pos[1] += 10
    if direction == "LEFT":
        snake_pos[0] -= 10
    if direction == "RIGHT":
        snake_pos[0] += 10

    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH // 10)) * 10,
                    random.randrange(1, (HEIGHT // 10)) * 10]
    food_spawn = True

    win.fill(DARK_GREEN)
    for pos in snake_body:
        pygame.draw.rect(win, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(win, RED, pygame.Rect(
        food_pos[0], food_pos[1], 10, 10))

    if snake_pos[0] < 0 or snake_pos[0] > WIDTH-10:
        game_over = True
    if snake_pos[1] < 0 or snake_pos[1] > HEIGHT-10:
        game_over = True
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over = True

    pygame.display.update()
    clock.tick(snake_speed)

pygame.quit()
quit()
