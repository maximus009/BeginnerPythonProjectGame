import pygame
from const import *

class Tile(pygame.Rect):
	tileDict = {}
	tileCount = 0

	subClasses = set()

	def __init__(self, x ,y):
		pass