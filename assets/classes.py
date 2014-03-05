import pygame, math, time
from const import *

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
        
class OpeningScene:
	def __init__(self):
		self.static_width = 150
		if GO_TO_TITLE:
			self.next = TitleScene()
			self.mode = None
			self.flags = ''
			self.fade = 0
			self.mode_counter = 0
		else:
			self.mode = 'open'
			self.ch3 = [
				' XXX  X  X   XXX ',
				'XX XX X  X  X   X',
				'X     X  X      X',
				'X     XXXX    XX ',
				'X     X  X      X',
				'XX XX X  X  X   X',
				' XXX  X  X   XXX '
				]
			self.logo = [
				'TTTTT TTTTT  TTT  T     T       N   N NNNN    NNNN  NNNN  NNNNN  NNN  NNNNN N   N NNNNN  NNN ',
				'  T   T     T   T TT   TT       NN  N N   N   N   N N   N N     N   N N     NN  N   N   N   N',
				'  T   T     T   T T T T T       N N N N   N   N   N N   N N     N     N     N N N   N   N    ',
				'  T   TTT   TTTTT T  T  T       N  NN NNNN    NNNN  NNNN  NNN    NNN  NNN   N  NN   N    NNN ',
				'  T   T     T   T T     T       N   N N       N     N N   N         N N     N   N   N       N',
				'  T   T     T   T T     T       N   N N       N     N  N  N     N   N N     N   N   N   N   N',
				'  T   TTTTT T   T T     T       N   N N       N     N   N NNNNN  NNN  NNNNN N   N   N    NNN ',
			]
			self.next = self
			self.flags = 'W'
			static = pygame.Surface((self.static_width, self.static_width))
			self.scrolly = pygame.Surface((WIDTH, 5))
			self.dark = pygame.Surface((WIDTH, HEIGHT)).convert()
			self.dark.fill((0, 0, 0))
			
			dr = pygame.draw.rect
			pr = pygame.Rect
			e = 0
			y = 0
			self.fade = 0
			colors = [BLACK, WHITE] * (self.static_width * self.static_width // 2)
			random.shuffle(colors)
			i = 0
			while y < self.static_width:
				x = 0
				while x < self.static_width:
					dr(static, colors[i], pr(x, y, 2, 2))
					i += 1
					x += 1
				y += 1
			self.static = static
			self.mode_counter = 0
		
	def processInput(self, events, pressedKeys):
		for event in events:
			
			if self.mode == 'open':
				if event.down and event.action in ('start', 'A', 'B'):
					self.mode = 'starting'
					self.mode_counter = 0
			
	def update(self):
		self.fade += 1
		self.mode_counter += 1
		if self.mode == 'starting' and self.mode_counter > 20:
			self.next = TitleScene()
		if self.mode == 'open':
			if self.mode_counter > 200:
				self.mode = 'starting'
				self.mode_counter = 0
	
	def render(self, screen, renderCounter):
		if self.mode == 'starting':
			if self.mode_counter < 10:
				screen.fill((255, 80, 255))
			else:
				screen.fill((200, 200, 200))
		elif self.mode == 'open':
			left = -random.random() * self.static_width
			top = -random.random() * self.static_width
			y = top
			while y < HEIGHT:
				x = left
				while x < WIDTH:
					screen.blit(self.static, (x, y))
					x += self.static_width
				y += self.static_width
			
			self.scrolly.blit(screen, (0, 0))
			
			for i in range(5):
				y = (renderCounter * 2 + 10 * i + 300) % HEIGHT
				screen.blit(self.scrolly, (0, y))
				
			width = len(self.ch3[0])
			height = len(self.ch3)
			
			y = 0
			while y < height:
				x = 0
				while x < width:
					if self.ch3[y][x] != ' ':
						pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(20 + x * 8, 20 + y * 8, 8, 8))
					x += 1
				y += 1
			
			width = len(self.logo[0])
			height = len(self.logo)
			y = 0
			while y < height:
				x = 0
				while x < width:
					if self.logo[y][x] != ' ':
						pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(20 + x * 8, 250 + y * 8, 8, 8))
					x += 1
				y += 1
			opacity = int(self.fade * 1.5)
			if opacity > 255:
				opacity = 255
			
			v = 255 - opacity
			self.dark.set_alpha(v)
			if (v > 0):
				screen.blit(self.dark, (0, 0))

class Player(BaseClass):

    health = 100.00

    PlayersList = pygame.sprite.Group() #Group of character sprites
    def __init__(self, x, y, width, height, image_path):
        
        #Calls BaseClass so images can be loaded, etc..
        BaseClass.__init__(self, x, y, width, height, image_path)
        Player.PlayersList.add(self)

        #Velocities of movement
        self.velx, self.vely = 0, 0

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

class TitleScene: #This is not integrated yet-I'm working on it though and it will be ready at release
	def __init__(self):
		self.next = self
		self.flags = ''
		self.flash_counter = 0
		self.options = [
			('start', 'Start Game'),
			('password', "Enter Password"),
			('joystick', "Configure Game Pad")]
		self.index = 0
			
	def processInput(self, events, pressedKeys):
		for event in events:
			if self.flash_counter < 0:
				if event.down:
					if event.action in ['start', 'A', 'B']:
						self.flash_counter = 30
						playNoise('menu_select')
					elif event.action == 'up':
						if self.index > 0:
							self.index -= 1
							playNoise('menu_move')
					elif event.action == 'down':
						if self.index < 2:
							self.index += 1
					
	
	def update(self):
		self.flash_counter -= 1
		if self.flash_counter == 1:
			action = self.options[self.index][0]
			if action == 'start':
				self.next = IntroScene()
			elif action == 'password':
				self.next = PasswordScene()
			elif action == 'joystick':
				self.next = JoystickMenuScene()
			else:
				pass 
	
	def render(self, screen, renderCounter):
		
		JUKEBOX.ensureSong('title')
		
		screen.fill((0, 0, 0))
		pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(10, 10, 50, 50))
		
		img = renderText((255, 255, 255), "Hello, World!")
		screen.blit(img, (100, 100))
		
		screen.fill((0, 0, 0))
		screen.blit(getImage('slides/title.png'), (0, 0))
		
		showText = True #(renderCounter // 10) % 3 != 0
		if self.flash_counter > 0:
			showText = renderCounter % 4 < 2
		
		index = 0
		y = 136
		left = 64
		
		drawBox(screen, left - 32, y - 16, 24, 9)
		
		for option in self.options:
			
			if index == self.index:
				screen.blit(getText((255, 255, 255), ">"), (left - 16, y))
			
			if index != self.index or showText:
				screen.blit(getText((255, 255, 255), option[1]), (left, y))
			
			index += 1
			y += 16
		
		y += 32
		active_js = getText((128, 128, 128), "Active joystick: ")
		screen.blit(active_js, (8, y))
		x = 8 + active_js.get_width()
		if active_joystick == None:
			js_name = getText((255, 0, 0), "None")
		else:
			js_name = getText((255, 255, 255), active_joystick)
		screen.blit(js_name, (x, y))
