import pygame
from random import randint

# class inherets from pygame sprite class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemyType):

        # Initialize parent sprite class
        super().__init__()

        if enemyType == 'fly':
            fly1 = pygame.image.load('graphics/fly1.png').convert_alpha()
            fly2 = pygame.image.load('graphics/fly2.png').convert_alpha()
            self.frames = [fly1, fly2]
            yPos = 210
        else:
            # If enemy is a snail
            snail1 = pygame.image.load('graphics/snail1.png').convert_alpha()
            snail2 = pygame.image.load('graphics/snail2.png').convert_alpha()
            self.frames = [snail1, snail2]
            yPos = 300

        self.animationIndex = 0

        self.image = self.frames[self.animationIndex]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), yPos))

    def AnimationState(self):
        self.animationIndex += 0.1
        if self.animationIndex >= len(self.frames):
            self.animationIndex = 0
        self.image = self.frames[int(self.animationIndex)]

    def update(self):
        self.AnimationState()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= 100:
            self.kill()


