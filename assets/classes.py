import pygame

class BaseClass(pygame.sprite.Sprite):
    #List of ALL sprites. Used for collision detection and drawing.
    allsprites = pygame.sprite.Group()

    def __init__(self, x, y, width, height, image_path):

        pygame.sprite.Sprite.__init__(self) #initialize sprite class from pygame
        BaseClass.allsprites.add(self)

        self.image = pygame.image.load(image_path)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.width = width
        self.height = height

class Player(BaseClass):

    PlayersList = pygame.sprite.Group() #Group of character sprites
    def __init__(self, x, y, width, height, image_path):
        
        #Calls BaseClass so images can be loaded, etc..
        BaseClass.__init__(self, x, y, width, height, image_path)
        Player.PlayersList.add(self)
        self.velx = 0
        self.vely = 0

    def motion(self):

        self.rect.x += self.velx
        self.rect.y += self.vely
