from __future__ import annotations

from typing import Tuple, Dict, List

from Tile import Tile
from BasicTile import BasicTile
import pygame as py

class BasicTileFactory:
    def __init__(self):
        self.tileCodes      : Dict[Tile, Tuple[str, str, str, str]] = dict()
        self.topTileDict    : Dict[str, List[Tile]] = dict()
        self.leftTileDict   : Dict[str, List[Tile]] = dict()
        self.bottomTileDict : Dict[str, List[Tile]] = dict()
        self.rightTileDict  : Dict[str, List[Tile]] = dict()

    def addTile(self, imagePath : str, topCode : str, leftCode : str, bottomCode : str, rightCode : str, weight : float = 1) -> BasicTileFactory:
        image = py.image.load(imagePath)
        self.__makeTile(image, topCode, leftCode, bottomCode, rightCode, weight)

        return self

    def addRotatedTile(self, imagePath : str, topCode : str, leftCode : str, bottomCode : str, rightCode : str, weight : float = 1) -> BasicTileFactory:
        image = py.image.load(imagePath)

        for i in range(4):
            self.__makeTile(image, topCode, leftCode, bottomCode, rightCode, weight)

            image = py.transform.rotate(image, 90)
            temp = topCode 
            topCode = leftCode 
            leftCode = bottomCode 
            bottomCode = rightCode 
            rightCode = temp

        return self
    
    def getTileSet(self) -> List[Tile]:
        
        self.tileList : Tile = list()
        for tile in self.tileCodes:
            top, left, bottom, right = self.tileCodes[tile]
            # The tile connects to the same code, but the other tile must have it on the opposite matching
            tile.setAdjacent(BasicTile.UP, self.bottomTileDict[top[::-1]])
            tile.setAdjacent(BasicTile.DOWN, self.topTileDict[bottom[::-1]])
            tile.setAdjacent(BasicTile.LEFT, self.rightTileDict[left[::-1]])
            tile.setAdjacent(BasicTile.RIGHT, self.leftTileDict[right[::-1]])

            self.tileList.append(tile)
        return self.tileList
    
    def __makeTile(self, image : py.surface, topCode : str, leftCode : str, bottomCode : str, rightCode : str, weight : float = 1) -> Tile:
        tile : Tile = BasicTile(image, weight)
        self.__dictAdd(self.topTileDict   , topCode   , tile)
        self.__dictAdd(self.leftTileDict  , leftCode  , tile)
        self.__dictAdd(self.bottomTileDict, bottomCode, tile)
        self.__dictAdd(self.rightTileDict , rightCode , tile)

        self.tileCodes[tile] = (topCode, leftCode, bottomCode, rightCode)

        return tile

    def __dictAdd(self, dictionary : Dict[str, List[Tile]], code : str, tile : Tile) -> None:
        if code not in dictionary:
            dictionary[code] = list()
        dictionary[code].append(tile)
            
        

        

