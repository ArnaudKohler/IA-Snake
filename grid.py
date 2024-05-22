import pygame

class Grid:
    def __init__(self, size, cell_size):
        self.size = size
        self.cell_size = cell_size

    def draw(self, surface):
        for x in range(self.size):
            for y in range(self.size):
                rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(surface, (40, 40, 40), rect, 1)