import pygame, sys, math, os
from pygame.locals import *
sys.path.append(os.getcwd()+'/assets') #add our module to the path python searches
import game_classes #import our class module
from game_classes import * #import all classes and functions
if not pygame.font: print('ERROR: fonts are disabled for this session')
if not pygame.mixer: print('ERROR: sounds are disabled for this session')
     
class PyMain(pygame.sprite.Sprite):
           
    def __init__(self, width=640,height=480): #main variable storage
        pygame.init()
        pygame.sprite.Sprite.__init__(self) #Initializes the Sprite class from pygame
        self.width = width
        self.height = height
        pygame.display.set_caption('CSPSP Clone in Python')
        self.screen = pygame.display.set_mode((self.width, self.height))
        icon = pygame.image.load("assets/icon.bmp").convert_alpha()        
        pygame.display.set_icon(icon)
        sprite1 = Player()
        back1 = Sprites()
        back2 = Sprites()
        back3 = Sprites()
        back4 = Sprites()
        self.img = sprite1.return_sprite('assets/player.bmp')
        self.imgRect = self.img.get_rect() #Gets dimensions of player sprite
        self.background = back1.return_sprite("assets/background.bmp")
        self.background2 = back2.return_sprite("assets/background2.bmp")
        self.background3 = back3.return_sprite("assets/background3.bmp")
        self.background4 = back4.return_sprite("assets/background4.bmp")
        self.imgPos = sprite1.position_sprite(0,314)
        self.backPos = [0,0]
        self.backPos2 = [0,0]
        self.backPos3 = [0,0]
        self.backPos4 = [0,0]
        self.fps = 60
        self.clock = pygame.time.Clock()
           
    def MainLoop(self): #main loop
        sprite1 = Player()
        print_screen(self)
        self.backPos2[0] = 640

        while True:
            keyboard=pygame.key.get_pressed()
            
            if self.backPos[0] < 0:
                self.backPos2[1] = self.backPos[1]
                self.backPos2[0] = 640 + self.backPos[0]
                
            if self.backPos[0] < 0:
                self.backPos3[1] = self.backPos[1]
                self.backPos3[0] = 1280 + self.backPos[0]

            if self.backPos[0] < 0:
                self.backPos4[1] = self.backPos[1]
                self.backPos4[0] = 1920 + self.backPos[0]


            #Keyboard Commands
            if (keyboard[K_RIGHT] or keyboard[K_d]) and (self.backPos[0] > -1920):
                self.backPos[0] -= 5

            if (keyboard[K_LEFT] or keyboard[K_a]) and (self.backPos[0] < 0):
                self.backPos[0] += 5

            if (keyboard[K_UP] or keyboard[K_w]) and (self.backPos[1] < 0):
                self.backPos[1] -= 5

            if (keyboard[K_DOWN] or keyboard[K_s]) and (self.backPos[1] > 0):
                self.backPos[1] += 5

            if keyboard[K_SPACE]:
                sprite1.jump(self,self.imgPos)

            if keyboard[K_ESCAPE]:
                pygame.quit() #closes pygame
                sys.exit() #closes actual program

            print_screen(self)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() #closes pygame
                    sys.exit() #closes actual program

            pygame.display.update()

            self.clock.tick(self.fps)
         
#classes stored in /assets/game_classes.py
         
if __name__ == "__main__": #if this is the script that was executed then run the main loop
    MainWindow = PyMain()
    MainWindow.MainLoop()
