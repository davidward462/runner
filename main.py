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
skySurface = pygame.image.load('graphics/Sky.png').convert_alpha()
groundSurface = pygame.image.load('graphics/ground.png').convert_alpha()

# Entities
snailSurface = pygame.image.load('graphics/snail1.png').convert_alpha()
snailRect = snailSurface.get_rect(midbottom = (600, 300))

# Player
playerSurface = pygame.image.load('graphics/player_walk_1.png').convert_alpha()

# Draw rectangle around surface
playerRect = playerSurface.get_rect(midbottom = (80, 300)) 

# Colors
textColor = '#404040'
boxColor = '#c0e8ec'

# Text
scoreFont = pygame.font.Font('font/Pixeltype.ttf', 50)
scoreSurface = scoreFont.render('Sample text', True, textColor)
scoreRect = scoreSurface.get_rect(center = (400, 50))

# Variables
playerGravity = 0

# Clock
clock = pygame.time.Clock()

# Begin main game loop
while True:
    
    # Get event from queue (inputs)
    for event in pygame.event.get():

        # on window close
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                playerGravity = -20
            
    # Logical updates
    if snailRect.right <= 0:
        snailRect.left = 800
    snailRect.x = snailRect.x - 2

    playerGravity += 1
    playerRect.y += playerGravity

    # Collisions

    # Check if player rectangle collides with snail rectangle.
    # colliderect() returns 0 or 1.
    # Reversing the rectangles in terms of arguments would also work.
    playerRect.colliderect(snailRect)

    # Graphical updates

    # Blit surfaces
    # Environment
    screen.blit(skySurface, centerCoord)
    screen.blit(groundSurface, (0, 300))

    # Score text
    pygame.draw.rect(screen, boxColor, scoreRect) 
    pygame.draw.rect(screen, boxColor, scoreRect, 10) 
    screen.blit(scoreSurface, scoreRect)
    
    # Entities
    screen.blit(snailSurface, snailRect)
    screen.blit(playerSurface, playerRect)

    # Update display surface
    pygame.display.update()

    # Tick speed
    clock.tick(60)

# End main game loop.


