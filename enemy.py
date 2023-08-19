import pygame
from random import randint

# class inherets from pygame sprite class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemyType):

        # Initialize parent sprite class
        super().__init__()

        if enemyType == 'fly':
            fly1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
            fly2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
            self.frames = [fly1, fly2]
            yPos = 210
        else:
            # If enemy is a snail
            snail1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
            snail2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail1, snail2]
            yPos = 300

        self.animationIndex = 0

        self.image = self.frames[self.animationIndex]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), yPos))






