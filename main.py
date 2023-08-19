import pygame
from sys import exit
from random import randint, choice
from player import Player
from enemy import Enemy

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

# Snail
snailSurface = pygame.image.load('graphics/snail1.png').convert_alpha()

# Fly
flySurface = pygame.image.load('graphics/fly1.png').convert_alpha()

# Player

# Groups

enemyGroup = pygame.sprite.Group()

# Create group
player = pygame.sprite.GroupSingle()
# add instance of player to group
player.add(Player())

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

# Music
backgroundMusic = pygame.mixer.Sound('audio/music.wav')
backgroundMusic.set_volume(0.7)
# Loop sound forever
backgroundMusic.play(loops = -1)

# Clock
clock = pygame.time.Clock()

# Timer
# Custom user event
enemyTimer = pygame.USEREVENT + 1
eventRate = 1500
pygame.time.set_timer(enemyTimer, eventRate)

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

def CollisionSprite():
    if pygame.sprite.spritecollide(player.sprite, enemyGroup, False):
        enemyGroup.empty() # Remove all enemies from group (game is over)
        return False
    else:
        return True


def QuitGame():
    pygame.quit()
    exit()

def main():

    # Game varaible setup
    playerAlive = False
    playerGravity = 0
    startTime = int(pygame.time.get_ticks() / timeFactor)
    score = 0
    enemyRectList = []

    # Begin main game loop
    while True:
        
        # Get event from queue (inputs)
        for event in pygame.event.get():
        # Begin event loop

            # on window close
            if event.type == pygame.QUIT:
                QuitGame()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    QuitGame()
                if event.key == pygame.K_SPACE and not playerAlive:
                    # Restart game and reset variables
                    playerAlive = True
                    startTime = int(pygame.time.get_ticks() / timeFactor)
                    score = 0

            # Spawn enemy into group
            if event.type == enemyTimer and playerAlive:
                enemyType = choice(['fly', 'snail', 'snail'])
                enemyGroup.add(Enemy(enemyType))

            # End event loop
                
        if playerAlive:

            # Logical updates
            playerAlive = CollisionSprite()

            # Graphical updates

            # Blit surfaces
            # Environment
            screen.blit(skySurface, centerCoord)
            screen.blit(groundSurface, (0, 300))

            # Entities

            enemyGroup.draw(screen)
            enemyGroup.update()

            # update player sprite group
            player.update()
            player.draw(screen)

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
