from __future__ import annotations

from typing import Tuple, List

from Tile import Tile

from Grid import Grid
from BasicCell import BasicCell
import numpy as np 
import pygame as py

class BasicGrid(Grid):
    
    def __init__(self, dimensions : Tuple[int, int], tileSet : List[Tile]):
        self.initializeGrid(dimensions, tileSet)
        self.__allTiles = tileSet

    def initializeGrid(self, dimensions : Tuple[int, int], tileSet : List[Tile]) -> Grid:
        """Creates the grid of the given size"""
        self.__grid = np.array([[BasicCell(tileSet) for i in range(dimensions[0])] for j in range(dimensions[1])])
        return self

    def buildGrid(self) -> bool:
        """Builds the grid of tiles (using Wave Function Collapse), and returns whether it fails or not"""

        nextPosition = self.__getLowestEntropy()
        while (nextPosition != (-1, -1)): # Keep going until no more spots left
            self.__grid[nextPosition].setTile()
            if (not self.collapse(nextPosition)):
                return False 
            nextPosition = self.__getLowestEntropy()
        
        return True

    def reduceOptions(self, position : Tuple[int, int]) -> bool:
        """Reduces a given cell, and propogates, and returns whether it fails or not"""
        
        x, y = position
        w, h = self.__grid.shape
        cell = self.__grid[x, y]
        
        if (cell.getTile() != None):
            return True
        
        if (not cell.getPossibleTiles):
            return False

        # Reduce above
        if (x > 0 and self.__grid[x - 1, y].checkTiles(cell.getTopPossible())):
            if (not self.reduceOptions((x - 1, y))):
                return False 
        
        # Reduce below
        if (x < w - 1 and self.__grid[x + 1, y].checkTiles(cell.getBottomPossible())):
            if (not self.reduceOptions((x + 1, y))):
                return False 

        # Reduce to the left    
        if (y > 0 and self.__grid[x, y - 1].checkTiles(cell.getLeftPossible())):
            if (not self.reduceOptions((x, y - 1))):
                return False 

        # Reduce to the right 
        if (y < h - 1 and self.__grid[x, y + 1].checkTiles(cell.getRightPossible())):
            if (not self.reduceOptions((x, y + 1))):
                return False 
        
        return True
    
    def getGridImage(self) -> np.ndarray:
        """Returns the tile images, if the tiles are selected (will have 'None' in place of undecided tiles)"""
        imageFunction = lambda cell: cell.getTile().getImage() if cell.getTile() else None
        imageGrid = imageFunction(self.__grid)
        return imageGrid
        
    
    def __getLowestEntropy(self) -> Tuple[int, int]:
        """Returns the position of the lowest entropy on the grid"""
        w, h = self.__grid.shape
        val = -1
        pos = (-1, -1)
        for i in range(w):
            for j in range(h):
                if self.getTile() != None:
                    continue
                entropy = self.__grid[i, j].getEntropy()
                if val != -1 and val >= entropy:
                    continue
                val = entropy
                pos = (i, j)
        return pos



    
