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
cyan = ( 0 2555, 255)
purple = ( 255, 0 , 255)


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
        return self.pos

