from __future__ import annotations
from typing import List, Tuple
from pathlib import Path
from PIL import Image
import numpy as np

from BasicTileFactory import BasicTileFactory
from Tile import Tile
from random import uniform


class BasicImageSorter:
    BASE_WEIGHT = 100
    def __init__(self, imageFolderPath : str):
        self.path = imageFolderPath 
        self.__tileFactory = BasicTileFactory()
        self.__currASCII = 0
        self.__colorMap = dict()

    def makeTiles(self, noise : float = 0) -> BasicImageSorter:
        

        folder = Path(self.path).glob('*.PNG')
        
        for image in folder:
            with Image.open(image, 'r') as im:
                data = np.asarray(im)
                w, h, _ = data.shape
                midW, midH = w // 2, h // 2
                
                right  = self.__assignCode(tuple(data[0, 0])  , tuple(data[midW, 0]) , tuple(data[-1, 0]) )
                bottom = self.__assignCode(tuple(data[-1, 0]) , tuple(data[-1, midH]), tuple(data[-1, -1]))
                left   = self.__assignCode(tuple(data[-1, -1]), tuple(data[midW, -1]), tuple(data[0, -1]) )
                top    = self.__assignCode(tuple(data[0, -1]) , tuple(data[0, midH]) , tuple(data[0, 0])  )
                # print(image, "Top:", top, "Right:", right, "Bottom:", bottom, "Left:", left)
                weight = BasicImageSorter.BASE_WEIGHT + uniform(-noise, noise)
                self.__tileFactory.addRotatedTile(image, top, left, bottom, right, weight)
        
        return self
    
    def addCustomRotatedTile(self, path : str, weight = BASE_WEIGHT) -> BasicImageSorter:
        with Image.open(path, 'r') as image:
            data = np.asarray(image)
            w, h, _ = data.shape
            midW, midH = w // 2, h // 2
            
            right  = self.__assignCode(tuple(data[0, 0])  , tuple(data[midW, 0]) , tuple(data[-1, 0]) )
            bottom = self.__assignCode(tuple(data[-1, 0]) , tuple(data[-1, midH]), tuple(data[-1, -1]))
            left   = self.__assignCode(tuple(data[-1, -1]), tuple(data[midW, -1]), tuple(data[0, -1]) )
            top    = self.__assignCode(tuple(data[0, -1]) , tuple(data[0, midH]) , tuple(data[0, 0])  )

            self.__tileFactory.addRotatedTile(path, top, left, bottom, right, weight)
            
        return self


    def getTileSet(self):
        return self.__tileFactory.getTileSet()
        

    def __assignCode(self, left : Tuple[int, int, int, int], mid : Tuple[int, int, int, int], right : Tuple[int, int, int, int]) -> str:
        if (left not in self.__colorMap):
            self.__currASCII += 1
            self.__colorMap[left] = chr(self.__currASCII)

        if (mid not in self.__colorMap):
            self.__currASCII += 1
            self.__colorMap[mid] = chr(self.__currASCII)

        if (right not in self.__colorMap):
            self.__currASCII += 1
            self.__colorMap[right] = chr(self.__currASCII)

        return self.__colorMap[left] + self.__colorMap[mid] + self.__colorMap[right]

