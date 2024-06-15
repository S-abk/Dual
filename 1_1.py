import pygame

# Initialize pygame
pygame.init()

# Set up the display
infoObject = pygame.display.Info()
width, height = infoObject.current_w, infoObject.current_h
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Basic Test")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the clock for a decent frame rate
clock = pygame.time.Clock()

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

    # Draw a white rectangle
    pygame.draw.rect(screen, WHITE, (width // 4, height // 4, width // 2, height // 2))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit pygame
pygame.quit()