import pygame
import sys
from pygame.locals import *


class Grid:
    def __init__(self, window_width, window_height, grid_size, grid_color, grid_line_width):
        self.window_width = window_width
        self.window_height = window_height
        self.grid_size = grid_size
        self.grid_color = grid_color
        self.grid_line_width = grid_line_width

        self.num_horizontal_cells = self.window_width // self.grid_size
        self.num_vertical_cells = self.window_height // self.grid_size

    def draw(self, surface):
        for x in range(0, self.window_width, self.grid_size):
            pygame.draw.line(surface, self.grid_color, (x, 0), (x, self.window_height), self.grid_line_width)
        for y in range(0, self.window_height, self.grid_size):
            pygame.draw.line(surface, self.grid_color, (0, y), (self.window_width, y), self.grid_line_width)

    def get_center_coordinates(self, row, col):
        x = col * self.grid_size + self.grid_size // 2
        y = row * self.grid_size + self.grid_size // 2
        return x, y