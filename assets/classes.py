import pygame

class BaseClass(pygame.sprite.Sprite):
    #List of ALL sprites. Used for collision detection and drawing.
    allsprites = pygame.sprite.Group()

    def __init__(self, x, y, width, height, image_path):
        self.x = x
        self.y = y
        
        pygame.sprite.Sprite.__init__(self) #initialize sprite class from pygame
        BaseClass.allsprites.add(self) #Adds sprite to allsprites, and images are displayed in main.py

        self.image = pygame.image.load(image_path)

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.width, self.height = width, height
        
class Player(BaseClass):

    health = 100.00

    PlayersList = pygame.sprite.Group() #Group of character sprites
    def __init__(self, x, y, width, height, image_path):
        
        #Calls BaseClass so images can be loaded, etc..
        BaseClass.__init__(self, x, y, width, height, image_path)
        Player.PlayersList.add(self)

        #Velocities of movement
        self.velx, self.vely = 0, 0
        #Will want to add self.standing soon
        self.jumping, self.go_down = False, False

    def motion(self, SCREENWIDTH, SCREENHEIGHT):

        #Predicts where image is going to be placed next to prevent going
        #Off of the screen a smidge.
        predicted_location_x = self.rect.x + self.velx
        predicted_location_y = self.rect.y + self.vely

        #Horizontal Constraints
        if predicted_location_x < 0:
            self.velx = 0

        elif predicted_location_x + self.width > SCREENWIDTH:
            self.velx = 0


        self.rect.x += self.velx

        #Vertical Constraints
        if predicted_location_y < 0:
            self.vely = 0

        elif predicted_location_y + self.height > SCREENWIDTH:
            self.vely = 0


        self.rect.y += self.vely
