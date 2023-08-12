from __future__ import annotations

from Tile import Tile 
from Cell import Cell 

from typing import List

from random import choices, uniform
import numpy as np

class BasicCell(Cell):
    UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3

    ENTROPY_NOISE = 1

    def __init__(self, tileSet : List[Tile]):
        """Initilaizes the Cell"""
        self.initializeCell(tileSet)
        self.__entropy = self.__updateEntropy()
        self.__adjacentPossible = [[], [], [], []]
        # self.__updateAdjacentPossible()
        
    def initializeCell(self, tileSet : List[Tile]) -> Cell:
        """Sets up the necessary parts for the self"""
        self.__tileSet = tileSet
        self.__tile    = None
        
        return self

    def getTile(self) -> Tile:
        """Gets the tile if it has been chosen, or 'none' if it has not been chosen yet"""
        return self.__tile

    def getPossibleTiles(self) -> List[Tile]:
        """Gets all possible tiles that the self could be, along with their weighting"""
        return self.__tileSet

    def setTile(self) -> Tile:
        """Sets the current tile to the given 'tile'"""
        self.__tile = choices(self.__tileSet, weights = [tile.getWeight() for tile in self.__tileSet])[0]
        return self.__tile
    
    def getEntropy(self) -> float:
        """Gets the entropy of the self"""
        return self.__entropy
    
    def __updateEntropy(self) -> float:
        totalWeight = self.__getTotalWeightSum()
        probabilities = [tile.getWeight() / totalWeight for tile in self.__tileSet]
        self.__entropy = -sum([prob * np.log2(prob) for prob in probabilities]) # Shannon entropy
        self.__entropy += uniform(-BasicCell.ENTROPY_NOISE, BasicCell.ENTROPY_NOISE)
        return self.__entropy


    def checkTiles(self, availibleTiles : List[Tile]) -> bool:
        """Checks if there are tiles that need to be removed, and removes them, returning if it removed any"""
        # If we have already selected a tile, not need to reduce
        if (self.getTile()):
            return False
        
        # Filter based on the other list
        newList = list(set(self.__tileSet) & set(availibleTiles))
        if len(newList) != len(self.__tileSet):
            self.__tileSet = newList
            # Only change entropy when your tiles actually change
            self.__updateEntropy()
            # self.__updateAdjacentPossible()
            return True
        return False 
    
    def getAdjacentPossible(self, direction : int) -> List[Tile]:
        """Gets all possible tiles that can go next to the current cell"""
        if (self.getTile() != None):
            return self.getTile().getAdjacent(direction)
        return list(set( sum([possibleTile.getAdjacent(direction) for possibleTile in self.getPossibleTiles()], [])))
        # return self.__adjacentPossible[direction]

    def __updateAdjacentPossible(self) -> None:
        """Updates all possible adjacent tiles"""
        for i in range(4):
            self.__adjacentPossible[i] = list(set( sum([possibleTile.getAdjacent(i) for possibleTile in self.getPossibleTiles()], [])))

    def __getTotalWeightSum(self):
        """Returns the total weighting of the remaining tileset"""
        return sum([tile.getWeight() for tile in self.__tileSet])