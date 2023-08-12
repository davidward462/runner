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
playerRect = playerSurface.get_rect(midbottom = (100, groundHeight)) 

# Scaled player
playerStand = pygame.image.load('graphics/player_stand.png').convert_alpha()
playerStand = pygame.transform.scale2x(playerStand)
playerStandRect = playerStand.get_rect(center = (400, 220))

# Colors
midGrey = (64, 64, 64)
softBlue = (94, 129, 162)
teal = (111, 196, 169)

# Text

# Fonts
gameFont = pygame.font.Font('font/Pixeltype.ttf', 50)
titleFont = pygame.font.Font('font/Pixeltype.ttf', 75)

# Title
titleSurface = titleFont.render('Runner', True, teal)
titleRect = titleSurface.get_rect(center = (400, 50))

# Game instruction text
instructionSurface = gameFont.render('press SPACE to begin', True, midGrey)
instructionRect = instructionSurface.get_rect(center = (400, 350))


# Clock
clock = pygame.time.Clock()


def DisplayScore(startTime):
    currentTime = int(pygame.time.get_ticks() / timeFactor) - startTime
    scoreSurface = gameFont.render(f"Score: {currentTime}", False, midGrey)
    scoreRect = scoreSurface.get_rect(center = (400, 50))
    screen.blit(scoreSurface, scoreRect)
    return currentTime

def DisplayHighscore(score):
    highscoreSurface = gameFont.render(f"Score: {score}", False, midGrey)
    highscoreRect = highscoreSurface.get_rect(center = (400, 350))
    screen.blit(highscoreSurface, highscoreRect)

def QuitGame():
    pygame.quit()
    exit()


def main():

    # Game varaible setup
    playerAlive = False
    playerGravity = 0
    startTime = int(pygame.time.get_ticks() / timeFactor)
    score = 0

    # Begin main game loop
    while True:
        
        # Get event from queue (inputs)
        for event in pygame.event.get():

            # on window close
            if event.type == pygame.QUIT:
                QuitGame()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    QuitGame()
                if event.key == pygame.K_SPACE and playerRect.bottom >= groundHeight:
                    playerGravity = -22
                if event.key == pygame.K_SPACE and not playerAlive:
                    # Restart game and reset variables
                    snailRect.x = 800
                    playerAlive = True
                    playerGravity = 0
                    startTime = int(pygame.time.get_ticks() / timeFactor)
                    score = 0
                    
                
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
            # Title/end screen
            screen.fill(softBlue)
            screen.blit(playerStand, playerStandRect)
            screen.blit(titleSurface, titleRect)

            if score > 0:
                DisplayHighscore(score)
            else:
                screen.blit(instructionSurface, instructionRect)

        # Update display surface
        pygame.display.update()

        # Tick speed
        clock.tick(60)

    # End main game loop.

main()
