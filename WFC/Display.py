from __future__ import annotations

from typing import Tuple

import numpy as np
import pygame as py
import pygame.surface as Surface
py.init()


class Display:
    SCREEN_DIMENSIONS = (400, 400)
    SCREEN_CLEAR_COLOR = (255, 255, 255)

    def __init__(self, gridSize : Tuple[int, int], screenSize : Tuple[int, int] = SCREEN_DIMENSIONS):
        py.display.set_caption("WFC")
        self.screen = py.display.set_mode(screenSize)
        
        self.__gridSize = gridSize
        self.__screenSize = screenSize
        self.__cellSize = (screenSize[0] / gridSize[0], screenSize[1] / gridSize[1])
    
    def drawImage(self, image : Surface, position : Tuple[int, int]) -> None:
        absolutePosition = (position[0] * self.__cellSize[0], position[1] * self.__cellSize[1])
        scaledImage = py.transform.scale(image, self.__cellSize)
        self.screen.blit(scaledImage, absolutePosition)

    def drawGrid(self, imageGrid : np.ndarray):
        self.screen.fill(Display.SCREEN_CLEAR_COLOR)
        w, h = imageGrid.shape
        for r in range(w):
            for c in range(h):
                if (not imageGrid[r][c]):
                    continue
                self.drawImage(imageGrid[r][c], (c, r))
        

    def run(self):
        active : bool = True 
        
        while (active):
            for event in py.event.get():
                if event.type == py.QUIT:
                    active = False 
            py.display.update()
        # py.display.update()
            
        
        py.quit()
