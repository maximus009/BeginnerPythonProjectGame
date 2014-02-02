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
        self.background = pygame.image.load('background.bmp').convert()
     
    def MainLoop(self):
        player = Sprite(64,64)
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    pygame.display.update()
     
class Human(object): #create the class of humans
    def __init__(self, health, speed, weapon):
         self.health = health
         self.speed = speed
         self.weapon = weapon
     
class Sprite(pygame.sprite.Sprite):
    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('player.bmp').convert()
        self.rect = self.image.get_rect() 
        self.rect.topleft = [0, 0] 
        PyMain.screen.blit(self.image, self.rect)
     
if __name__ == "__main__":
    MainWindow = PyMain()
    MainWindow.MainLoop()
