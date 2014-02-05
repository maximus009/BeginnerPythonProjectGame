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

	@staticmethod
	def preInit():
		pass

	@staticmethod
	def getTile(tileNumber):
		#tileNumber is the key in tileDict
		return Tile.tileDict.get(tileNumber)

	@staticmethod
	def shiftTiles(*args):
		#Will shift tiles about our character like we had before.
		pass


	def __str__(self):
		#Added this class for debugging purposes. Will print class name of tile and its coords.
		#I may remove this later.
		return ("{0} X: {1}, Y: {2}".format(self.__class__.__name__, self.x, self.y))

class EmptyTile(Tile):
	#Empty tiles are walkable tiles. No obstacles, in other words.
	tileDict = {} #Dictionary that holds the tile grid.
	tileCount = 0

	def __init__(self, x, y):
		#Calls the superclass so these tiles will be added to the list of all tiles.
		super(EmptyTile, self).__init__(x, y)

	@staticmethod
	def getTile(tileNumber):
		#getTile method specifically for empty tiles.
		return EmptyTile.tileDict.get(tileNumber)

	@staticmethod
	def drawTiles(screen):

		for tileNumber in xrange(EmptyTile.tileCount):
			emmptyTile = EmptyTile.getTile(tileNumber)
			#Draws the tile we just made!
			#Replace BLACK with image later.
			pygame.draw.rect(screen, BLACK, emmptyTile)

class BorderTile(Tile):
	pass