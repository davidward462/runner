import pygame

# class inherets from pygame sprite class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemyType):

        # Initialize parent sprite class
        super().__init__()
        self.image = None
        self.rect = None
