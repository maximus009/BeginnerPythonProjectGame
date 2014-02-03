import pygame, sys, math, os
from pygame.locals import *
sys.path.append(os.getcwd()+'/assets') #add our module to the path python searches
import game_classes #inport our class module
from game_classes import * #import all classes and functions
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
        back1 = sprite_class()
        self.image = sprite1.return_sprite('assets/player.bmp')
        self.background = back1.return_sprite("assets/background.bmp")
        self.imgPos = sprite1.position_sprite(255,145)
        self.backPos = [0,0]
        self.fps = 30
        self.fpsTime = pygame.time.Clock()
           
         
    def MainLoop(self):
        self.screen.blit(self.background, (self.backPos[0],self.backPos[1]))
        self.screen.blit(self.image, (self.imgPos[0],self.imgPos[1]))

        while True:
            keyboard=pygame.key.get_pressed()

            if self.imgPos[0] >= 640 :
                self.screen.blit(self.background, (self.backPos[0],self.backPos[1]))
            if keyboard[K_RIGHT] or keyboard[K_d]:
                self.backPos[0] += 5
                self.screen.blit(self.background, (self.backPos[0],self.backPos[1]))
                self.screen.blit(self.image, (self.imgPos[0],self.imgPos[1]))

            if keyboard[K_LEFT] or keyboard[K_a]:
                self.backPos[0] -= 5
                self.screen.blit(self.background, (self.backPos[0],self.backPos[1]))
                self.screen.blit(self.image, (self.imgPos[0],self.imgPos[1]))

            if keyboard[K_UP] or keyboard[K_w]:
                self.backPos[1] -= 5
                self.screen.blit(self.background, (self.backPos[0],self.backPos[1]))
                self.screen.blit(self.image, (self.imgPos[0],self.imgPos[1]))

            if keyboard[K_DOWN] or keyboard[K_s]:
                self.backPos[1] += 5
                self.screen.blit(self.background, (self.backPos[0],self.backPos[1]))
                self.screen.blit(self.image, (self.imgPos[0],self.imgPos[1]))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.update()
            self.fpsTime.tick(self.fps)
         
#classes stored in /assets/game_classes.py
         
if __name__ == "__main__":
    MainWindow = PyMain()
    MainWindow.MainLoop()
