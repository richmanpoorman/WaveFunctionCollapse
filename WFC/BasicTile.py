from __future__ import annotations

from typing import List
import pygame.surface as Surface

from Tile import Tile

class BasicTile(Tile):
    id = 0
    def __init__(self, image : Surface, weight : float = 1):
        self.initializeTile(self, image, weight)
        self.__id = id
        id += 1

    def initializeTile(self, image : Surface, weight : float) -> Tile:
        """Initializes the variables for a tile"""
        self.__topAdjacent    : List[Tile] = []
        self.__bottomAdjacent : List[Tile] = []
        self.__leftAdjacent   : List[Tile] = []
        self.__rightAdjacent  : List[Tile] = []
        self.__sprite : Surface = image.convert()
        self.__weight : float = weight
        
        return self

    def getTopAdjacent(self) -> List[Tile]:
        """Get the tiles adjacemt above"""
        return self.__topAdjacent

    def getBottomAdjacent(self) -> List[Tile]:
        """Get the tiles adjacemt below"""
        return self.__bottomAdjacent

    def getLeftAdjacent(self) -> List[Tile]:
        """Get the tiles adjacemt to the left"""
        return self.__leftAdjacent

    def getRightAdjacent(self) -> List[Tile]:
        """Get the tiles adjacemt to the right"""
        return self.__rightAdjacent

    def getSurface(self) -> Surface:
        """Get the sprite of the tile"""
        return self.__sprite

    def getWeight(self) -> float:
        """Gets the weight of the tile"""
        return self.__weight
    
    def getID(self) -> int:
        """Returns the tile identification number"""
        return self.__id
    
    def __eq__(self, other : Tile) -> bool:
        """Checks if two tiles are the same"""
        return self.getID() == other.getID()
    
    def __ne__(self, other : Tile) -> bool:
        """Checks if two tiles are different"""
        return not self.__eq__(other)
    
    def __hash__(self):
        """Gets the hash code for the Tile"""
        return int.__hash__(self.__id)