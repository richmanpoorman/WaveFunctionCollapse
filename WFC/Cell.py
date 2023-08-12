from __future__ import annotations

from Tile import Tile 

from typing import List

class Cell:
    
    def initializeCell(self, tileSet : List[Tile]) -> Cell:
        """Sets up the necessary parts for the cell"""
        pass

    def getTile(self) -> Tile:
        """Gets the tile if it has been chosen, or 'none' if it has not been chosen yet"""
        pass 

    def getPossibleTiles(self) -> List[Tile]:
        """Gets all possible tiles that the cell could be, along with their weighting"""
        pass 

    def setTile(self) -> Tile:
        """Sets the current tile to the given 'tile'"""
        pass

    def getEntropy(self) -> float:
        """Gets the entropy of the tile"""
        pass

    def checkTiles(self, availibleTiles : List[Tile]) -> bool:
        """Checks if there are tiles (not in availible tiles) that need to be removed, and removes them, returning if it removed any"""
        pass

    def getAdjacentPossible(self, direction : int) -> List[Tile]:
        """Gets all possible tiles that can go next to the current cell"""
        pass
    
