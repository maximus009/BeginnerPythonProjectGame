import pygame, sys, math, os
from pygame.locals import *
sys.path.append(os.getcwd()+'/assets') #add our module to the path python searches

import classes #import our class module
import process
from classes import * #import our class module
from process import * #Handles user input and our output

if not pygame.font: print('ERROR: fonts are disabled for this session')
if not pygame.mixer: print('ERROR: sounds are disabled for this session')

pygame.init()

SCREENWIDTH, SCREENHEIGHT = 640, 480
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), 0, 32)

pygame.display.set_caption('CSPSP Clone in Python')
icon = pygame.image.load("assets/images/icon.bmp").convert_alpha()        
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
FPS = 60


background = pygame.image.load("assets/images/background.bmp")
PlayerYGround = SCREENHEIGHT - 166 #height from bottom according to image size in this case 166
player = Player(0,PlayerYGround,131,166,"assets/images/player.bmp")

#-------------Main Program Loop-----------------
while True:
    keystrokes(player) #Handles Key Commands and Quitting

    #Handles Player Movement, including jumping.
    player.motion(SCREENWIDTH, SCREENHEIGHT)


    #DRAW
    screen.blit(background, (0,0) )
    BaseClass.allsprites.draw(screen) #Draws ALL sprites to the screen.
    pygame.display.flip()


    clock.tick(FPS)

