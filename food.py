import pygame
import random

# Classe Food
class Food:
    def __init__(self, GRID_SIZE, CELL_SIZE):
        self.position = (0, 0)
        self.grid_size = GRID_SIZE
        self.cell_size = CELL_SIZE
        self.new_food()
        

    def new_food(self):
        self.position = (random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1))

    def draw(self, surface):
        rect = pygame.Rect(self.position[0] * self.cell_size, self.position[1] * self.cell_size, self.cell_size, self.cell_size)
        pygame.draw.rect(surface, (255, 0, 0), rect)