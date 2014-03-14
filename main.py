import pygame, sys, math, os.path
from pygame.locals import *
sys.path.append(os.getcwd()+'/assets') #add our module to the path python searches

from classes import * #import our class module
from process import * #Handles user input and our output.
from const import * #All constants are held in here.
from version_game import * #import version file updater

if not pygame.font: print('ERROR: fonts are disabled for this session')
if not pygame.mixer: print('ERROR: sounds are disabled for this session')


pygame.mixer.pre_init(44100, -16, 2, 2048) #Initialize sound mixer
pygame.init()
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), 0, 32)

try:
    death_sound = pygame.mixer.Sound('assets/audio/youlose.wav')  #load sound
except:
    raise "Error loading audio file."

pygame.display.set_caption('CSPSP Clone in Python')
icon = pygame.image.load("assets/images/icon.bmp").convert_alpha()        
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
FPS = 60
total_frames = 0
playing = False
update_check = False
dead = False

background = background_class(0,0,640,480,"assets/images/background.bmp")
player = Player(0,SCREENHEIGHT - 128,128,128,"assets/images/playerRight.bmp")
#pause = PauseScene(background)
MenuImage = BaseClass(0, 0, 640, 480, "assets/images/menu.bmp")
Button = BaseClass(280, 240, 80, 20, "assets/images/button.bmp")
Spike = BaseClass(300, 400, 80, 80, "assets/images/spike.bmp")
RetryButton = BaseClass(280,240,80,20,"assets/images/tryAgainButton.bmp")
ExitButton = BaseClass(280,270,80,20,"assets/images/exitButton.bmp")
knockbacked = 0

#-------------Main Program Loop-----------------
while True:
    if playing:

        dead = False

        total_frames += 1 #Putting this at the beginning so other functions can use this.

        if knockbacked > 0:
            knockbacked -= 1
            knock_back = True
        else:
            knock_back = False
        
        if knock_back == False:
            keystrokes(player, playing, update_version) #Handles Key Commands and Quitting

        #Handles Player Movement, including jumping.
        player.motion(SCREENWIDTH, SCREENHEIGHT,background,Spike)
        #DRAW
        background.drawbackground(screen)
        Player.PlayersList.draw(screen) #Draws all sprites from the Player class.
        #DRAWS SPIKE and checks for collision with player
        knockbacked = spike(Spike,screen,clock,FPS,player,pygame,SCREENWIDTH,SCREENHEIGHT,knockbacked,background)
        #HEALTH DRAW
        if player.health > 25:
            drawText(400, 444, "Health: " + str(int(player.health)), WHITE, "monospace", 36, screen)
        elif player.health == 0.00:
            dead = True
        else:
            drawText(400, 444, "Health: " + str(int(player.health)), RED, "monospace", 36, screen)

        #Check if dead
        if dead:
            death_sound.play(0)
            playing = False
        pygame.display.flip()
        clock.tick(FPS)
    else:
        if not dead:
            playing = mainMenu(BaseClass, screen, clock, FPS, MenuImage, Button, ExitButton,update_check)
            update_check = True
            keystrokes(player, playing, update_version)
        else:
            #Open up a menu with a retry option.
            playing = inGameMenu(BaseClass, screen, clock, FPS, MenuImage, RetryButton, ExitButton, player, SCREENHEIGHT)
            keystrokes(player, playing, update_version)
