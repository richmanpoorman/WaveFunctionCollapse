from Display import Display
from BasicGrid import BasicGrid 

import pygame as py
import numpy as np
py.init()

display : Display = Display(gridSize = (2, 2), screenSize = (400, 400))

testTile = py.image.load("WFC\\TileSets\\TileSet1-RedAndBlue\\1.PNG")
# display.drawImage(testTile, (0, 0))
testGrid = np.array([[None, None], [testTile, testTile]])
display.drawGrid(testGrid)
# py.display.update()
display.run()
