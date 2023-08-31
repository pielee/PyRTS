import pygame
import sys
import random

from pygame.locals import *

class Unit:
    def __init__(self, grid):
        # Create a Unit at a random grid location
        self.grid_row = random.randint(0, grid.num_vertical_cells - 1)
        self.grid_col = random.randint(0, grid.num_horizontal_cells - 1)
        self.grid = grid
        self.radius = self.grid.grid_size // 2
        self.color = (255, 255, 255)
        self.x, self.y = self.grid.get_center_coordinates(self.grid_row, self.grid_col)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius)
    
    def select(self):
        self.color = (255, 0, 0)

    def deselect(self):
        self.color = (255, 255, 255)

