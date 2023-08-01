import pygame
from sys import exit

# Initialize pygame subsystems
pygame.init()

# Set up window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

# Display surface
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Runner')

# Surfaces
width = 100
height = 200
test_surface = pygame.Surface((width, height))
test_surface.fill('blue')

# Clock
clock = pygame.time.Clock()

def main():

    # Begin main game loop
    while True:

        # Get event from queue (inputs)
        for event in pygame.event.get():

            # on window close
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Logical updates

        # Graphical updates

        screen.blit(test_surface, (300, 20))

        # Update display surface
        pygame.display.update()

        # Tick speed
        clock.tick(60)

    # End main game loop.

main()

