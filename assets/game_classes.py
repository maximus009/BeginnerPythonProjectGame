import pygame, sys, math, os
from pygame.locals import *


'''-------Colors----------------
This can be used for text and drawn objects not from images
I was thinking these color definitions would be useful for
when we make menus and what not.'''
white = (255, 255, 255)
grey = (128, 128, 128)
black = ( 0, 0, 0)
#RGB
red = (255, 0, 0)
green = ( 0, 255, 0)
blue = ( 0, 0, 255)

yellow = ( 255, 255, 0)
cyan = ( 0, 255, 255)
purple = ( 255, 0 , 255)


class Player(object): #create the class of the player
    def __init__(self):
        pass

    def jump(self, image, imgPos):
        self.imgPos = imgPos
        velocity = 0
        gravity = 10

        if self.imgPos[1] < 0:
            pass
        else:
            velocity = 100
            #while self.imgPos[1] != 0:
                #self.imgPos[1] -= (velocity / 10)
                #velocity -= gravity
            #self.imgPos[0] -= 1
        return True
     
    def return_sprite(self, sprites):
        self.sprites = sprites
        #PyMain.allsprites.add(self) #Adds sprite to pygame.sprite.Group()
        return pygame.image.load(sprites)
     
    def position_sprite(self, posx, posy):
        self.pos = [posx, posy]
        return self.pos
     
class Sprites(object):
    def __init__(self):
        pass
     
    def return_sprite(self, sprites):
        self.sprites = sprites
        return pygame.image.load(sprites)
     
    def position_sprite(self, posx, posy):
        self.pos = [posx, posy]
        return self.pos

def print_screen(self):
        self.screen.blit(self.background2, (self.backPos2[0],self.backPos2[1]))
        self.screen.blit(self.background3, (self.backPos3[0],self.backPos3[1]))
        self.screen.blit(self.background4, (self.backPos4[0],self.backPos4[1]))
        self.screen.blit(self.background, (self.backPos[0],self.backPos[1]))
        self.screen.blit(self.img, (self.imgPos[0],self.imgPos[1]))
