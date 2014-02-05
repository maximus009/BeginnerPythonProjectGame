import pygame

class BaseClass(pygame.sprite.Sprite):
    #List of ALL sprites. Used for collision detection and drawing.
    allsprites = pygame.sprite.Group()

    def __init__(self, x, y, width, height, image_path):

        pygame.sprite.Sprite.__init__(self) #initialize sprite class from pygame
        BaseClass.allsprites.add(self) #Adds sprite to allsprites, and images are displayed in main.py

        self.image = pygame.image.load(image_path)

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.width, self.height = width, height


class Player(BaseClass):

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

        #Horizontal Constraints
        if predicted_location_x < 0:
            self.velx = 0

        elif predicted_location_x + self.width > SCREENWIDTH:
            self.velx = 0


        self.rect.x += self.velx

        self.jump(SCREENHEIGHT)

    def jump(self, SCREENHEIGHT):

        #Jump! Jump! Jump!

        max_jump = 150

        if self.jumping:
            self.vely = 10
			
            if self.rect.y < max_jump:
                self.go_down = True

            if self.go_down:
                self.rect.y += self.vely
                if self.velx < 0:
                    self.image = pygame.image.load("assets/images/playerflippedjump.bmp")
                else:
                    self.image = pygame.image.load("assets/images/playerjump.bmp")

                predicted_location = self.rect.y + self.vely

                if predicted_location + self.height > SCREENHEIGHT:
                    self.jumping = False
                    self.go_down = False
                    if self.velx < 0:
                        self.image = pygame.image.load("assets/images/playerflipped.bmp")
                    else:  
                        self.image = pygame.image.load("assets/images/player.bmp")

            else:
                self.rect.y -= self.vely
                if self.velx < 0:
                    self.image = pygame.image.load("assets/images/playerflippedjump.bmp")
                else:
                    self.image = pygame.image.load("assets/images/playerjump.bmp")
