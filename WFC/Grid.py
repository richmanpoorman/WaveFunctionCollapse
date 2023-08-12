from __future__ import annotations

from typing import Tuple, List 

from Tile import Tile
import numpy as np

class Grid:
    def initializeGrid(self, dimensions : Tuple[int, int], tileSet : List[Tile]) -> Grid:
        """Creates the grid of the given size"""
        pass

    def buildGrid(self) -> bool:
        """Builds the grid of tiles (using Wave Function Collapse), and returns whether it passed or not"""
        pass 
    
    def buildGridStep(self) -> Tuple[bool, bool]:
        """Builds one step of the algorithm, returning if it is (still going, failed)"""
        pass

    def reduceOptions(self, position : Tuple[int, int]) -> bool:
        """Reduced the possibilities a given cell, and propogates, and returns whether it passed or not"""
        pass

    def getGridImage(self) -> np.ndarray:
        """Returns the tile images, if the tiles are selected (will have 'None' in place of undecided tiles)"""
        pass

    
