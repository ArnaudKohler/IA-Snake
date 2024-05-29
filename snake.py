import pygame

# Classe Snake
class Snake:
    def __init__(self, GRID_SIZE, CELL_SIZE, grid_offsets):
        self.positions = [(5, 5)]
        self.direction = pygame.Vector2(0, 0) # Direction initiale Right
        self.grow = False
        self.GRID_SIZE = GRID_SIZE
        self.CELL_SIZE = CELL_SIZE
        self.offset_x, self.offset_y = grid_offsets

    def update(self):
        head_x, head_y = self.positions[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)
        
        if self.grow:
            self.positions.insert(0, new_head)
            self.grow = False
        else: #Movement
            self.positions.pop() #Remove the last cell of the snake
            self.positions.insert(0, new_head) #Add the new position of the head 
        
        if new_head in self.positions[1:]: #If the position of the head is already in the positions of the body of the snake = dead & reset
            self.reset()
        
        if not 0 <= new_head[0] < self.GRID_SIZE or not 0 <= new_head[1] < self.GRID_SIZE: #If get out of the grid, reset
            self.reset()

    def reset(self):
        self.positions = [(5, 5)]
        self.direction = pygame.Vector2(0, 0)


    def grow_snake(self):
        self.grow = True

    def draw(self, surface):
        for position in self.positions:
            rect = pygame.Rect(self.offset_x + position[0] * self.CELL_SIZE, self.offset_y + position[1] * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE)
            pygame.draw.rect(surface, (0, 255, 0), rect)