import pygame
import random
from sys import exit
pygame.init

width, height = 600, 600
Window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# snake's head
snake_x, snake_y = 0, 0
head = pygame.Rect((20, 520, 20, 20))

# snake's position
x, y = 0, 0

# level_chose=pygame.surface()
level = 2

# load food in random positions
food_x, food_y = random.randint(0, 600), random.randint(0, 600)
food = pygame.Rect((food_x, food_y, 10, 10))


up, down, left, right = 'up', 'down', 'left', 'right'
head_facing = right

while True:
    # level = input(print("enter level: 1/2/3"))
    Window.fill((0, 0, 0))

    # for constant movement
    if (head_facing == right):
        head.move_ip(x + level, y)
    elif (head_facing == up):
        head.move_ip(x, y - level)
    elif (head_facing == left):
        head.move_ip(x - level, y)
    elif (head_facing == down):
        head.move_ip(x, y + level)

    # to keep the snake within the window
    if (x, y > width, height):
        x, y = 0, 0

    # control snake's head
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        head_facing = left
    if key[pygame.K_d] == True:
        head_facing = right
    elif key[pygame.K_w] == True:
        head_facing = up
    elif key[pygame.K_s] == True:
        head_facing = down

    # when snake eats food
    if (head.colliderect(food) == True):
        food_x = random.randint(0, 600)
        food_y = random.randint(0, 600)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.draw.rect(Window, (255, 0, 0), head)
    pygame.draw.rect(Window, (255, 255, 255), food)

    pygame.display.update()
    clock.tick(60)
