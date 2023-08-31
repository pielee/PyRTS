import os
import sys

from selection import Selection
from map import Grid
from unit import Unit

import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the window
WINDOWWIDTH = 1280
WINDOWHEIGHT = 720

GRID_COLOR = (100, 100, 100)
GRID_LINE_WIDTH = 1

# Create Grid instance
grid = Grid(WINDOWWIDTH, WINDOWHEIGHT, 20, GRID_COLOR, GRID_LINE_WIDTH)



windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption("Mouse Rectangle Drawer")

# Create MouseRectDrawer instance
selection = Selection()
unit = Unit(grid)

# Create a list of units
units = [Unit(grid) for i in range(5)]

# Game loop
fps = 60
fpsClock = pygame.time.Clock()

while True:
    windowSurface.fill((0, 0, 0))
    
    selection.handle_events()
    selection.draw(windowSurface)
    selection.update_selected_units(units)

    grid.draw(windowSurface)

    unit.draw(windowSurface)

    for unit in units:
        unit.draw(windowSurface)

    selected_units = selection.get_selected_units()

    for unit in selected_units:
        unit.color = (0, 255, 0) 

    # make non selected units normal colour 
    for unit in units:
        if unit not in selected_units:
            unit.deselect()
            unit.draw(windowSurface)

    

    
    pygame.display.flip()
    fpsClock.tick(fps)