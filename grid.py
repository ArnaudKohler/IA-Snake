import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

class Grid:
    def __init__(self, size, cell_size):
        self.size = size
        self.cell_size = cell_size
        self.width = size * cell_size
        self.height = size * cell_size
        self.offset_x = (SCREEN_WIDTH - self.width) // 2
        self.offset_y = (SCREEN_HEIGHT - self.height) // 2

    def draw(self, surface): 
        for x in range(self.size):
            for y in range(self.size):
                rect = pygame.Rect(
                    self.offset_x + x * self.cell_size, 
                    self.offset_y + y * self.cell_size, 
                    self.cell_size, 
                    self.cell_size
                )
                pygame.draw.rect(surface, (40, 40, 40), rect, 11) # Peut changer la couleur des cellules et la largeur

    def get_offsets(self):
        return self.offset_x, self.offset_y
