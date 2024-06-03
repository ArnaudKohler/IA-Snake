import pygame
import random

# Classe Food
class Food:
    def __init__(self, GRID_SIZE, CELL_SIZE, snake, grid_offsets):
        self.grid_size = GRID_SIZE
        self.cell_size = CELL_SIZE
        self.position = random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1)
        self.offset_x, self.offset_y = grid_offsets
        self.new_food(snake)
        

    def new_food(self, snake):
        while(self.position in snake.positions): #Check that food doesn't spawn on a snake tile
            self.position = (random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1))

    def draw(self, surface):
        rect = pygame.Rect(self.offset_x + self.position[0] * self.cell_size, self.offset_y + self.position[1] * self.cell_size, self.cell_size, self.cell_size)
        pygame.draw.rect(surface, (255, 0, 0), rect)