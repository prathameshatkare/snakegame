
import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Title and Icon
pygame.display.set_caption("Shooting Game")
icon = pygame.image.load('spaceship.png')  # You can use any image file for the player
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load('spaceship.png')  # You can replace with your image
player_x = 370
player_y = 480
player_x_change = 0

# Bullet
bullet_img = pygame.image.load('bullet.png')
bullet_x = 0
bullet_y = 480
bullet_y_change = 10
bullet_state = "ready"  # Ready - You can't see the bullet; Fire - The bullet is moving

# Enemy
enemy_img = pygame.image.load('enemy.png')
enemy_x = random.randint(0, 735)
enemy_y = random.randint(50, 150)
enemy_x_change = 4
enemy_y_change = 40

# Background
background = pygame.image.load('background.png')  # You can add a background image


# Function to draw player
def player(x, y):
    screen.blit(player_img, (x, y))


# Function to draw enemy
def enemy(x, y):
    screen.blit(enemy_img, (x, y))


# Function to fire bullet
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))


# Game Loop
running = True
while running:

    # RGB Background color
    screen.fill((0, 0, 128))
    # Drawing the background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keystroke check for moving left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            if event.key == pygame.K_RIGHT:
                player_x_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Updating player's position
    player_x += player_x_change

    # Boundary check for player
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # Enemy movement
    enemy_x += enemy_x_change
    if enemy_x <= 0:
        enemy_x_change = 4
        enemy_y += enemy_y_change
    elif enemy_x >= 736:
        enemy_x_change = -4
        enemy_y += enemy_y_change

    # Bullet movement
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    # Drawing the player and enemy on the screen
    player(player_x, player_y)
    enemy(enemy_x, enemy_y)

    pygame.display.update()
