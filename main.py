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
centerCoord = (0, 0)
skySurface = pygame.image.load('graphics/Sky.png')
groundSurface = pygame.image.load('graphics/ground.png')

# Entities
snailSurface = pygame.image.load('graphics/snail1.png')

# Text
scoreFont = pygame.font.Font('font/Pixeltype.ttf', 50)
fontSurface = scoreFont.render('Sample text', True, 'Black')

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

        # Blit surfaces
        screen.blit(skySurface, centerCoord)
        screen.blit(groundSurface, (0, 300))
        screen.blit(fontSurface, (300, 50))
        screen.blit(snailSurface, (600, 250))

        # Update display surface
        pygame.display.update()

        # Tick speed
        clock.tick(60)

    # End main game loop.

main()

