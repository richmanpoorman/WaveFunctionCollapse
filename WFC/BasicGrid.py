from __future__ import annotations

from typing import Tuple, List

from Tile import Tile

from Grid import Grid
from BasicCell import BasicCell
import numpy as np 
import pygame as py
import heapq
from random import randint

class BasicGrid(Grid):
    
    def __init__(self, dimensions : Tuple[int, int], tileSet : List[Tile]):
        self.initializeGrid(dimensions, tileSet)
        self.__allTiles = tileSet

        firstPosition = (randint(0, dimensions[0] - 1), randint(0, dimensions[1] - 1))
        firstEntropy = self.__grid[firstPosition].getEntropy()
        self.__entropyQueue = [(firstEntropy, firstPosition)]
        self.__alreadySeen = set()


    def initializeGrid(self, dimensions : Tuple[int, int], tileSet : List[Tile]) -> Grid:
        """Creates the grid of the given size"""
        self.__grid = np.array([[BasicCell(tileSet) for i in range(dimensions[0])] for j in range(dimensions[1])])
        
        return self

    def buildGrid(self) -> bool:
        """Builds the grid of tiles (using Wave Function Collapse), and returns whether it passed or not"""

        isMaking = True
        while isMaking:
            isGoing, hasFailed = self.buildGridStep()
            isMaking = isGoing
            if hasFailed:
                return False
        
        return True

    def buildGridStep(self) -> Tuple[bool, bool]:
        """Builds one step of the algorithm, returning if it is (still going, failed)"""
        nextPosition = self.__getLowestEntropy()
        if (nextPosition == (-1, -1)):
            return (False, False)
        self.__grid[nextPosition].setTile()
        self.__alreadySeen.add(nextPosition)
        if (not self.reduceOptions(nextPosition)):
            return (False, True)
        
        return (True, False)
        

    def reduceOptions(self, position : Tuple[int, int]) -> bool:
        """Reduces a given cell, and propogates, and returns whether it passed or not"""
        dfs = [position]
        w, h = self.__grid.shape
        
        while (dfs):
            x, y = dfs[-1]
            dfs.pop()

            cell = self.__grid[x, y]

            # TODO:: For the heap entropy
            self.__pushEntropyHeap((cell.getEntropy(), (x, y)))

            if (not cell.getPossibleTiles()):
                return False
            
            # Reduce above
            if (x > 0 and self.__grid[x - 1, y].checkTiles(cell.getAdjacentPossible(BasicCell.UP))):
                dfs.append((x - 1, y))
            
            # Reduce below
            if (x < w - 1 and self.__grid[x + 1, y].checkTiles(cell.getAdjacentPossible(BasicCell.DOWN))):
                dfs.append((x + 1, y))

            # Reduce to the left    
            if (y > 0 and self.__grid[x, y - 1].checkTiles(cell.getAdjacentPossible(BasicCell.LEFT))):
                dfs.append((x, y - 1))

            # Reduce to the right 
            if (y < h - 1 and self.__grid[x, y + 1].checkTiles(cell.getAdjacentPossible(BasicCell.RIGHT))):
                dfs.append((x, y + 1))
        
        return True
    
    def getGridImage(self) -> np.ndarray:
        """Returns the tile images, if the tiles are selected (will have 'None' in place of undecided tiles)"""
        imageFunction = lambda cell: cell.getTile().getImage() if cell.getTile() else None
        vectorizedImageFunction = np.vectorize(imageFunction)
        imageGrid = vectorizedImageFunction(self.__grid)
        return imageGrid
        
    
    def __getLowestEntropy(self) -> Tuple[int, int]:
        """Returns the position of the lowest entropy on the grid"""
        return self.__priorityQueueEntropy()

    def __priorityQueueEntropy(self) -> Tuple[int, int]:
        while (self.__entropyQueue):
            entropy, position = self.__entropyQueue[0]
            self.__popEntropyHeap()

            if (position in self.__alreadySeen):
                continue 

            return position

        return (-1, -1)

    def __bruteForceEntropy(self) -> Tuple[int, int]:
        w, h = self.__grid.shape
        val = -1
        pos = (-1, -1)
        for i in range(w):
            for j in range(h):
                if self.__grid[i, j].getTile() != None:
                    continue
                entropy = self.__grid[i, j].getEntropy()
                if val != -1 and val >= entropy:
                    continue
                val = entropy
                pos = (i, j)
        return pos
    
    def __pushEntropyHeap(self, entropy : Tuple[int, Tuple[int, int]]):
        heapq.heappush(self.__entropyQueue, entropy)

    def __popEntropyHeap(self):
        heapq.heappop(self.__entropyQueue)

    
