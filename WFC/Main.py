from typing import List


from Grid import Grid
from Tile import Tile 
from Display import Display
from BasicGrid import BasicGrid 
from BasicTileFactory import BasicTileFactory
from BasicImageSorter import BasicImageSorter

import pygame as py
py.init()

GRID_SIZE = (100, 100)
SCREEN_SIZE = (800, 800)


display : Display = Display(gridSize = GRID_SIZE, screenSize = SCREEN_SIZE) 

# tileSet : List[Tile] = BasicTileFactory() \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\1.PNG" , "r", "rb", "b", "br") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\2.PNG" , "b", "bb", "b", "bb") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\3.PNG" , "r", "rr", "r", "rr") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\4.PNG" , "b", "b", "br", "rb") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\5.PNG" , "r", "r", "rb", "br") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\6.PNG" , "b", "b", "bb", "bb") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\7.PNG" , "r", "r", "rr", "rr") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\8.PNG" , "r", "rr", "rr", "rr") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\9.PNG" , "b", "br", "rr", "rb") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\10.PNG", "r", "rb", "br", "rr") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\11.PNG", "b", "bb", "br", "rb") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\12.PNG", "r", "rr", "rb", "br") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\13.PNG", "b", "br", "rb", "bb") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\14.PNG", "r", "rb", "bb", "br") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\15.PNG", "b", "bb", "bb", "bb") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\16.PNG", "bb", "bb", "bb", "bb") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\17.PNG", "br", "rb", "br", "rb") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\18.PNG", "rr", "rb", "bb", "br") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\19.PNG", "rr", "rb", "br", "rr") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\20.PNG", "bb", "br", "rb", "bb") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\21.PNG", "rr", "rr", "rr", "rr") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\22.PNG", "r", "r", "r", "rr") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\23.PNG", "b", "b", "b", "bb") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\24.PNG", "bb", "bb", "bb", "bb") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\25.PNG", "rr", "rr", "rr", "rr") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\26.PNG", "rb", "br", "rr", "rr") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\27.PNG", "br", "rb", "bb", "bb") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\28.PNG", "br", "rb", "br", "rb") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\29.PNG", "rb", "br", "rb", "br") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\30.PNG", "b", "b", "b", "b") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\31.PNG", "r", "r", "r", "r") \
#     .getTileSet()


# editedTileSet : List[Tile] = BasicTileFactory() \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\1.PNG" , "r", "rb", "b", "br") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\4.PNG" , "b", "b", "br", "rb") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\5.PNG" , "r", "r", "rb", "br") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\17.PNG", "br", "rb", "br", "rb") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\28.PNG", "br", "rb", "br", "rb") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\29.PNG", "rb", "br", "rb", "br") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\30.PNG", "b", "b", "b", "b") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\31.PNG", "r", "r", "r", "r") \
#     .getTileSet()

# testTileSet : List[Tile] = BasicTileFactory() \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\30.PNG", "b", "b", "b", "b") \
#     .addRotatedTile("WFC\\TileSets\\TileSet1-RedAndBlue\\31.PNG", "r", "r", "r", "r") \
#     .getTileSet()

# rgbTileSet : List[Tile] = BasicImageSorter("WFC\\TileSets\\RGB\\") \
#     .makeTiles(0) \
#     .getTileSet()

rgbTileSet2 : List[Tile] = BasicImageSorter("WFC\\TileSets\\RGB\\") \
    .makeTiles(0) \
    .addCustomRotatedTile("WFC\\TileSets\\RGB\\1.PNG", weight = 1000) \
    .addCustomRotatedTile("WFC\\TileSets\\RGB\\2.PNG", weight = 1000) \
    .getTileSet()

# for tile in rgbTileSet:
#     print("ID:", tile.getID(), ":", 
#           "UP:"   , [x.getID() for x in tile.getAdjacent(0)], 
#           "RIGHT:", [x.getID() for x in tile.getAdjacent(1)], 
#           "DOWN:" , [x.getID() for x in tile.getAdjacent(2)], 
#           "LEFT:" , [x.getID() for x in tile.getAdjacent(3)]
#         )

testBasicGrid : Grid = BasicGrid(GRID_SIZE, rgbTileSet2)
print("Building")
display.runStep(testBasicGrid)