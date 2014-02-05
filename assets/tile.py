import pygame
from const import *

class Tile(pygame.Rect):
	tileDict = {} #Dictionary that holds the tile grid.
	tileCount = 0

	subClasses = set()

	def __init__(self, x ,y):

		if x % TW == 0 and y % TH == 0: #Checks to see if tile is on grid.
			super(Tile, self).__init__(x, y, TW, TH) #Construct rectangle for tile. Super acceses pygame.Rect
			Tile.tileDict.update({tile.tileCount:self}) #Add tile to tileDict in Tile
			Tile.tileCount += 1

			#Gets self's class (type of tile)
			subClass = self.__class__
			#Keep all subclasses in one place
			Tile.subClasses.add(subClass)
			#Creating a dictionary of subclasses will allow us to manipulate individual subclasses
			subClass.titleDict.update({subClass.titleCount:self})
			subClass.titleCount += 1

		else:
			print ("Tile failed to manifest onto the grid.")
			raise ValueError #Will give an error if tile is not on the grid.