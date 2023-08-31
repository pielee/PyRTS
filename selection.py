import sys
import pygame
from pygame.locals import *


class Selection:
    def __init__(self):
        self.dragging = False
        self.start_pos = None
        self.selection_box = None
        self.selected_units_list = []  # Store the selected units here

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                self.dragging = True
                self.start_pos = event.pos
                self.selected_units_list = []  # Clear the previous selection

            elif event.type == MOUSEBUTTONUP:
                self.dragging = False
                self.start_pos = None

    def draw(self, surface):
        if self.dragging and self.start_pos:
            end_pos = pygame.mouse.get_pos()
            x = min(self.start_pos[0], end_pos[0])
            y = min(self.start_pos[1], end_pos[1])
            width = abs(end_pos[0] - self.start_pos[0])
            height = abs(end_pos[1] - self.start_pos[1])
            self.selection_box = pygame.draw.rect(surface, (255, 255, 255), (x, y, width, height), 1)

    def update_selected_units(self, units):
        if self.dragging:
            self.selected_units_list = [unit for unit in units if self.selection_box.colliderect(unit.get_rect())]

    def get_selected_units(self):
        return self.selected_units_list
        

            


