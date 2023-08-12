from __future__ import annotations

from typing import List
import pygame.surface as Surface


class Tile:
    def initializeTile(self, image : Surface, weight : float) -> Tile:
        """Initializes the variables for a tile"""
        pass
    
    def getAdjacent(self, direction : int) -> List[Tile]:
        """Get the tile from the given direction"""
        pass
    
    def setAdjacent(self, direction : int, newTileList : List[Tile]) -> None:
        """Sets the given direction with what can go next to it"""
        pass

    def getImage(self) -> Surface:
        """Get the sprite of the tile"""
        pass

    def getWeight(self) -> float:
        """Gets the weight of the tile"""
        pass
    
    def getID(self) -> int:
        """Returns the tile identification number"""
        pass 

    def __eq__(self, other : Tile) -> bool:
        """Checks if two tiles are the same"""
        pass

    def __ne__(self, other : Tile) -> bool:
        """Checks if two tiles are different"""
        pass

    

