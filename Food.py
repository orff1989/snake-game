import random

import pygame

from Grid import Grid


class Food:
    def __init__(self, new_grid: Grid):
        self.position = (0, 0)
        self.grid = new_grid
        self.color = (223, 163, 49)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, self.grid.GRID_WIDTH - 1) * self.grid.GRIDSIZE,
                         random.randint(0, self.grid.GRID_HEIGHT - 1) * self.grid.GRIDSIZE)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (self.grid.GRIDSIZE, self.grid.GRIDSIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)
