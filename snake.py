import pygame

# Classe Snake
class Snake:
    def __init__(self, GRID_SIZE, CELL_SIZE):
        self.positions = [(5, 5)]
        self.direction = pygame.Vector2(1, 0) # Direction initiale Right
        self.grow = False
        self.GRID_SIZE = GRID_SIZE
        self.CELL_SIZE = CELL_SIZE

    def update(self):
        head_x, head_y = self.positions[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)
        
        if self.grow:
            self.positions.insert(0, new_head)
            self.grow = False
        else:
            self.positions.pop()
            self.positions.insert(0, new_head)
        
        if new_head in self.positions[1:]:
            self.reset()
        
        if not 0 <= new_head[0] < self.GRID_SIZE or not 0 <= new_head[1] < self.GRID_SIZE:
            self.reset()

    def reset(self):
        self.positions = [(5, 5)]
        self.direction = pygame.Vector2(1, 0)


    def grow_snake(self):
        self.grow = True

    def draw(self, surface):
        for position in self.positions:
            rect = pygame.Rect(position[0] * self.CELL_SIZE, position[1] * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE)
            pygame.draw.rect(surface, (0, 255, 0), rect)