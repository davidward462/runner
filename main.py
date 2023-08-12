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

# Variables
groundHeight = 300
startTime = 0
timeFactor = 100

# Surfaces
centerCoord = (0, 0)
skySurface = pygame.image.load('graphics/Sky.png').convert_alpha()
groundSurface = pygame.image.load('graphics/ground.png').convert_alpha()

# Entities
snailSurface = pygame.image.load('graphics/snail1.png').convert_alpha()
snailRect = snailSurface.get_rect(midbottom = (600, groundHeight))

# Player
playerSurface = pygame.image.load('graphics/player_walk_1.png').convert_alpha()

# Draw rectangle around surface
playerRect = playerSurface.get_rect(midbottom = (80, groundHeight)) 

# Colors
textColor = '#404040'
boxColor = '#c0e8ec'

# Text
scoreFont = pygame.font.Font('font/Pixeltype.ttf', 50)
testSurface = scoreFont.render('Sample text', True, textColor)
testRect = testSurface.get_rect(center = (400, 50))


# Clock
clock = pygame.time.Clock()

def DisplayScore(startTime):
    currentTime = int(pygame.time.get_ticks() / timeFactor) - startTime
    scoreSurface = scoreFont.render(f"Score: {currentTime}", False, textColor)
    scoreRect = scoreSurface.get_rect(center = (400, 50))
    screen.blit(scoreSurface, scoreRect)
    return currentTime

def DisplayHighscore(score):
    highscoreSurface = scoreFont.render(f"Highscore: {score}", False, textColor)
    highscoreRect = highscoreSurface.get_rect(center = (400, 100))
    screen.blit(highscoreSurface, highscoreRect)


def main():

    playerAlive = True
    playerGravity = 0
    startTime = int(pygame.time.get_ticks() / timeFactor)
    score = 0

    # Begin main game loop
    while True:
        
        # Get event from queue (inputs)
        for event in pygame.event.get():

            # on window close
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and playerRect.bottom >= groundHeight:
                    playerGravity = -22
                if event.key == pygame.K_SPACE and not playerAlive:
                    # Restart game
                    snailRect.x = 800
                    main()
                
        if playerAlive:
            # Logical updates
            if snailRect.right <= 0:
                snailRect.left = 800
            snailRect.x = snailRect.x - 4

            playerGravity += 1
            playerRect.y += playerGravity

            if playerRect.bottom >= groundHeight: 
                playerRect.bottom = groundHeight

            # Collisions

            # Check if snail rectangle collides with player rectangle.
            # colliderect() returns 0 or 1.
            # Reversing the rectangles in terms of arguments would also work.
            if snailRect.colliderect(playerRect):
                playerAlive = False

            # Graphical updates

            # Blit surfaces
            # Environment
            screen.blit(skySurface, centerCoord)
            screen.blit(groundSurface, (0, 300))

            # Entities
            screen.blit(snailSurface, snailRect)
            screen.blit(playerSurface, playerRect)
            score = DisplayScore(startTime)
        else:
            # If player is dead
            screen.fill((94, 129, 162))
            DisplayHighscore(score)

        # Update display surface
        pygame.display.update()

        # Tick speed
        clock.tick(60)

    # End main game loop.

main()
