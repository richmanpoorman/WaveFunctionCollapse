from __future__ import annotations

from Tile import Tile 
from Cell import Cell 

from typing import List

from random import uniform
from math import log2

class BasicCell(Cell):
    def __init__(self, tileSet : List[Tile]):
        """Initilaizes the Cell"""
        self.initializeCell(tileSet)

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
        
        # Goes through each tile, and checks if it 'passes' the check, by being below the added threshold
        # Can think of as being on one bar, and checking where seed lands
        # |---|--X-----|------| <- this would mean to use tile 2
        seed = uniform(0, self.__getTotalWeightSum())
        tileThreshold = 0
        for tile in self.__tileSet:
            tileThreshold += tile.getWeight()
            if seed < tileThreshold:
                self.__tile = tile
                return self.__tile
        self.__tile = self.__tileSet[-1] # Just in case seed is equal to the total sum
        return self.__tile
    
    def getEntropy(self) -> float:
        """Gets the entropy of the self"""
        totalWeight = self.__getTotalWeightSum()
        probabilities = [tile.getWeight() / totalWeight for tile in self.__tileSet]
        return -sum([prob * log2(prob) for prob in probabilities]) # Shannon entropy

    def checkTiles(self, availibleTiles : List[Tile]) -> bool:
        """Checks if there are tiles that need to be removed, and removes them, returning if it removed any"""
        
        # Filter based on the other list
        newList = [tile for tile in self.__tileSet if tile in availibleTiles]
        if len(newList) != len(self.__tileSet):
            self.__tileSet = newList
            return True
        return False 
    
    def getTopPossible(self) -> List[Tile]:
        """Gets all possible tiles for the top"""
        
        if (self.getTile() != None):
            return self.getTile().getTopAdjacency()
        
        return list(set(sum([tile.getTopAdjacency() for tile in self.possibleTiles()])))
    
    def getBottomPossible(self) -> List[Tile]:
        """Gets all possible tiles for the bottom"""
        if (self.getTile() != None):
            return self.getTile().getBottomAdjacency()
        
        return list(set(sum([tile.getBottomAdjacency() for tile in self.possibleTiles()])))
    
    def getLeftPossible(self) -> List[Tile]:
        """Gets all possible tiles for the left"""
        if (self.getTile() != None):
            return self.getTile().getLeftAdjacency()
        
        return list(set(sum([tile.getLeftAdjacency() for tile in self.possibleTiles()])))
    
    def getRightPossible(self) -> List[Tile]:
        """Gets all possible tiles for the right"""
        if (self.getTile() != None):
            return self.getTile().getRightAdjacency()
        
        return list(set(sum([tile.getRightAdjacency() for tile in self.possibleTiles()])))


    def __getTotalWeightSum(self):
        """Returns the total weighting of the remaining tileset"""
        return sum([tile.getWeight() for tile in self.__tileSet])