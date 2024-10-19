import pygame
import random

# Initialize pygame
pygame.init()

# Define screen dimensions
screen_width = 600
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

# Set title
pygame.display.set_caption("Falling Objects Catcher")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# Define the basket and falling object dimensions
basket_width = 100
basket_height = 20
object_width = 20
object_height = 20

# Basket class
class Basket:
    def __init__(self):
        self.x = screen_width / 2 - basket_width / 2
        self.y = screen_height - basket_height - 10
        self.speed = 10

    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        if direction == "right" and self.x < screen_width - basket_width:
            self.x += self.speed

    def draw(self):
        pygame.draw.rect(screen, blue, [self.x, self.y, basket_width, basket_height])

# Falling Object class
class FallingObject:
    def __init__(self):
        self.x = random.randint(0, screen_width - object_width)
        self.y = -object_height
        self.speed = random.randint(3, 6)

    def fall(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.rect(screen, red, [self.x, self.y, object_width, object_height])

# Game loop
def game_loop():
    basket = Basket()
    objects = [FallingObject()]
    score = 0
    missed = 0
    max_missed = 5

    running = True
    while running:
        screen.fill(white)
        basket.draw()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get key presses to move the basket
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            basket.move("left")
        if keys[pygame.K_RIGHT]:
            basket.move("right")

        # Manage falling objects
        for obj in objects:
            obj.fall()
            obj.draw()

            # Check if the object is caught by the basket
            if obj.y + object_height >= basket.y and basket.x < obj.x < basket.x + basket_width:
                score += 1
                objects.remove(obj)
                objects.append(FallingObject())

            # Check if the object goes past the basket (missed)
            elif obj.y > screen_height:
                missed += 1
                objects.remove(obj)
                objects.append(FallingObject())

        # Display score and missed objects
        font = pygame.font.SysFont(None, 35)
        score_text = font.render(f"Score: {score}", True, black)
        screen.blit(score_text, (10, 10))

        missed_text = font.render(f"Missed: {missed}", True, black)
        screen.blit(missed_text, (10, 40))

        # Game over condition
        if missed >= max_missed:
            game_over_text = font.render("Game Over!", True, red)
            screen.blit(game_over_text, (screen_width / 2 - 70, screen_height / 2))
            pygame.display.update()
            pygame.time.wait(2000)
            running = False

        pygame.display.update()
        pygame.time.Clock().tick(30)

    pygame.quit()

# Start the game
game_loop()
