import pygame
import random
import logging

# Initialize pygame
pygame.init()

# Set up logging
logging.basicConfig(level=logging.INFO)

# Set up the display in fullscreen mode
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.NOFRAME)
width, height = screen.get_size()
pygame.display.set_caption("Screen Saver Animation")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the clock for a decent frame rate
clock = pygame.time.Clock()

# Ball class to represent each ball in the animation
class Ball:
    def __init__(self):
        self.x = random.randint(50, width - 50)
        self.y = random.randint(50, height - 50)
        self.radius = random.randint(20, 50)
        self.color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        self.dx = random.choice([-1, 1]) * random.uniform(2, 4)
        self.dy = random.choice([-1, 1]) * random.uniform(2, 4)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x - self.radius <= 0 or self.x + self.radius >= width:
            self.dx = -self.dx
        if self.y - self.radius <= 0 or self.y + self.radius >= height:
            self.dy = -self.dy
        logging.info(f"Ball position: ({self.x}, {self.y})")

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# Create a list of balls
balls = [Ball() for _ in range(10)]

# Define the main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Fill the screen with black
    screen.fill(BLACK)

    # Move and draw each ball
    for ball in balls:
        ball.move()
        ball.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit pygame
pygame.quit()