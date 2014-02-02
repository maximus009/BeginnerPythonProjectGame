import pygame, sys, math, os
from pygame.locals import *
if not pygame.font: print('ERROR: fonts are disabled for this session')
if not pygame.mixer: print('ERROR: sounds are disabled for this session')
     
class PyMain:
           
    def __init__(self, width=640,height=480):
        pygame.init()
        self.width = width
        self.height = height
        pygame.display.set_caption('CSPSP Clone in Python')
        self.screen = pygame.display.set_mode((self.width, self.height))
        sprite1 = sprite_class()
        self.image = sprite1.return_sprite('player.bmp')
        self.background=pygame.image.load("background.bmp")
        self.imgPos = [0,0]
        self.fps = 30
        self.fpsTime = pygame.time.Clock()
           
         
    def MainLoop(self):
        while True:
     
            if self.imgPos[0] < 320:
                self.imgPos[0] += 1
                self.screen.blit(self.background, (0,0))
                self.screen.blit(self.image, (self.imgPos[0],10))
     
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.update()
            self.fpsTime.tick(self.fps)
         
class Human(object): #create the class of humans
    def __init__(self, health, speed, weapon):
        self.health = health
        self.speed = speed
        self.weapon = weapon
     
class sprite_class(object):
    def __init__(self):
        pass
     
    def return_sprite(self, sprites):
        self.sprites = sprites
        return pygame.image.load(sprites)
     
    def position_sprite(self, posx, posy):
        self.pos = [posx, posy]
        return pos
           
         
if __name__ == "__main__":
    MainWindow = PyMain()
    MainWindow.MainLoop()