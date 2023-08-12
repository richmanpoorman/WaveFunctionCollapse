from __future__ import annotations

from typing import List
import pygame.surface as Surface

from Tile import Tile

class BasicTile(Tile):
    UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
    id = 0
    def __init__(self, image : Surface, weight : float = 1):
        self.initializeTile(image, weight)
        self.__id = BasicTile.id
        BasicTile.id += 1

    def initializeTile(self, image : Surface, weight : float) -> Tile:
        """Initializes the variables for a tile"""
        self.__topAdjacent    : List[Tile] = []
        self.__bottomAdjacent : List[Tile] = []
        self.__leftAdjacent   : List[Tile] = []
        self.__rightAdjacent  : List[Tile] = []
        self.__image : Surface = image.convert()
        self.__weight : float = weight
        
        return self

    def setAdjacent(self, direction : int, newTileList : List[Tile]) -> None:
        """Sets the given direction with what can go next to it"""
        if (direction == BasicTile.UP):
            self.__topAdjacent = newTileList
        elif (direction == BasicTile.RIGHT):
            self.__rightAdjacent = newTileList
        elif (direction == BasicTile.DOWN):
            self.__bottomAdjacent = newTileList
        elif (direction == BasicTile.LEFT):
            self.__leftAdjacent = newTileList
        else:
            raise KeyError("Direction is not defined")

    def getAdjacent(self, direction : int) -> List[Tile]:
        """Get the tile from the given direction"""
        if (direction == BasicTile.UP):
            return self.__getTopAdjacent()
        elif (direction == BasicTile.RIGHT):
            return self.__getLeftAdjacent()
        elif (direction == BasicTile.DOWN):
            return self.__getBottomAdjacent()
        elif (direction == BasicTile.LEFT):
            return self.__getRightAdjacent()
        else:
            raise KeyError("Direction is not defined")
            
    
    def getImage(self) -> Surface:
        """Get the sprite of the tile"""
        return self.__image
    
    def getSurface(self) -> Surface:
        """Get the sprite of the tile"""
        return self.__image

    def getWeight(self) -> float:
        """Gets the weight of the tile"""
        return self.__weight
    
    def getID(self) -> int:
        """Returns the tile identification number"""
        return self.__id
    
    def __eq__(self, other : Tile) -> bool:
        """Checks if two tiles are the same"""
        return other != None and self.getID() == other.getID()
    
    def __ne__(self, other : Tile) -> bool:
        """Checks if two tiles are different"""
        return not self.__eq__(other)
    
    def __hash__(self):
        """Gets the hash code for the Tile"""
        return int.__hash__(self.__id)
    
    
    def __getTopAdjacent(self) -> List[Tile]:
        """Get the tiles adjacemt above"""
        return self.__topAdjacent

    def __getBottomAdjacent(self) -> List[Tile]:
        """Get the tiles adjacemt below"""
        return self.__bottomAdjacent

    def __getLeftAdjacent(self) -> List[Tile]:
        """Get the tiles adjacemt to the left"""
        return self.__leftAdjacent

    def __getRightAdjacent(self) -> List[Tile]:
        """Get the tiles adjacemt to the right"""
        return self.__rightAdjacent
