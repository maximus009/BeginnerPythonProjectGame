import pygame, sys, math, os.path
from pygame.locals import *
sys.path.append(os.getcwd()+'/assets') #add our module to the path python searches

from classes import * #import our class module
from process import * #Handles user input and our output.
from const import * #All constants are held in here.
from tile import *

if not pygame.font: print('ERROR: fonts are disabled for this session')
if not pygame.mixer: print('ERROR: sounds are disabled for this session')

pygame.init()

screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), 0, 32)

pygame.display.set_caption('CSPSP Clone in Python')
icon = pygame.image.load("assets/images/icon.bmp").convert_alpha()        
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
FPS = 60
total_frames = 0
playing = False

#Draws tiles to the screen at the beginning
Tile.preInit()


background = pygame.image.load("assets/images/background.bmp")
player = Player(0,SCREENHEIGHT - 166,131,166,"assets/images/player.bmp")
MenuImage = BaseClass(0, 0, 640, 480, "assets/images/menu.bmp")
Button = BaseClass(280, 240, 80, 20, "assets/images/button.bmp")


#-------------Main Program Loop-----------------
while True:
    if playing == True:
        total_frames += 1 #Putting this at the beginning so other functions can use this.
        keystrokes(player) #Handles Key Commands and Quitting

        #Handles Player Movement, including jumping.
        player.motion(SCREENWIDTH, SCREENHEIGHT)


        #DRAW
        BorderTile.drawTiles(screen) #Draws border tiles
        EmptyTile.drawTiles(screen) #Draws walkable tiles
        Player.PlayersList.draw(screen) #Draws all sprites from the Player class.
        pygame.display.flip()

        clock.tick(FPS)
    else:
        playing = menu(BaseClass, screen, clock, FPS, MenuImage, Button)
        keystrokes(player)
