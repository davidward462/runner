import pygame

# class inherets from pygame sprite class
class Player(pygame.sprite.Sprite):
    def __init__(self):

        # Initialize parent sprite class
        super().__init__()

        # class variables
        playerWalk1 = pygame.image.load('graphics/player_walk_1.png').convert_alpha()
        playerWalk2 = pygame.image.load('graphics/player_walk_2.png').convert_alpha()

        # instance variables
        self.playerWalk = [playerWalk1, playerWalk2]
        self.playerIndex = 0
        self.playerJump = pygame.image.load('graphics/jump.png').convert_alpha()

        self.image = self.playerWalk[self.playerIndex]
        self.rect = self.image.get_rect(midbottom = (80,300))
        self.gravity = 0

        self.jumpSound = pygame.mixer.Sound('audio/jump.mp3')
        self.jumpSound.set_volume(0.5)

    def PlayerInput(self):
        # get all key inputs
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jumpSound.play()

    def ApplyGravity(self):
        self.gravity +=1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
            
    def AnimationState(self):
        if self.rect.bottom < 300:
            self.image = self.playerJump
        else:
            self.playerIndex += 0.1
            if self.playerIndex >= len(self.playerWalk):
                self.playerIndex = 0
            self.image = self.playerWalk[int(self.playerIndex)]

    def update(self):
        self.PlayerInput()
        self.ApplyGravity()
        self.AnimationState()





