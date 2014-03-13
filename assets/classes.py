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
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.width, self.height = width, height

class PauseScene:
	def __init__(self, bg):
		self.bg = bg
		self.next = self
		self.flags = ''
		self.counter = 0
	
	def processInput(self, events, pressed):
		for event in events:
			if event.down and event.action == 'start':
				if 'M' in self.bg.flags:
					#playNoise('pause_sound')
					pygame.mixer.music.unpause()
				self.next = self.bg
				self.bg.next = self.bg
	
	def update(self):
		if 'M' in self.bg.flags:
			if self.counter == 0:
				pygame.mixer.music.pause()
				playNoise('pause_sound')
		
		self.counter += 1
	
	def render(self, screen, rc):
		screen.fill(BLACK)
		img = getText(WHITE, "PAUSE")
		x = 128 - img.get_width() // 2
		y = 112 - img.get_height() // 2
		screen.blit(img, (x, y))
        
class Player(BaseClass):

    health = 100.00

    PlayersList = pygame.sprite.Group() #Group of character sprites
    def __init__(self, x, y, width, height, image_path):
        
        #Calls BaseClass so images can be loaded, etc..
        BaseClass.__init__(self, x, y, width, height, image_path)
        Player.PlayersList.add(self)

        #Velocities of movement
        self.velx, self.vely = 0, 0

    def motion(self, SCREENWIDTH, SCREENHEIGHT,background):

        #Predicts where image is going to be placed next to prevent going
        #Off of the screen a smidge.
        predicted_location_x = self.rect.x + self.velx
        predicted_location_y = self.rect.y + self.vely

        #Horizontal Constraints
        if predicted_location_x < 0:
            self.velx = 0

        elif predicted_location_x + self.width > SCREENWIDTH:
            background.x -= self.velx
            self.velx = 0

        self.rect.x += self.velx

        #Vertical Constraints
        if predicted_location_y < 0:
            self.vely = 0

        elif predicted_location_y + self.height > SCREENHEIGHT:
            self.vely = 0


        self.rect.y += self.vely

        def reset(self, SCREENHEIGHT):
            self.health = 100.00
            self.rect.x = 0
            self.rect.y = SCREENHEIGHT - 128
            self.image = pygame.image.load("assets/images/playerRight.bmp")

class background_class():

    def __init__(self, x, y, width, height, image_path):
        self.x = x
        self.y = y

        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.width, self.height = width, height

    def drawbackground(self,screen):
        screen.blit(self.image, (self.x,self.y))
        if (self.x < 0) and (self.x <640):
            screen.blit(self.image, (self.x+640,self.y))