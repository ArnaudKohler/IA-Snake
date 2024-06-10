import pygame

# Classe Snake
class Snake:
    def __init__(self, GRID_SIZE, CELL_SIZE, grid_offsets):
        self.positions = [(5, 5)]
        self.direction = pygame.Vector2(0, 0) # Direction initiale Right
        #self.grow = False
        self.GRID_SIZE = GRID_SIZE
        self.CELL_SIZE = CELL_SIZE
        self.offset_x, self.offset_y = grid_offsets

    """ def update(self):
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
            self.reset() """

    def reset(self):
        self.positions = [(5, 5)]
        self.direction = pygame.Vector2(0, 0)


    def draw(self, surface):
        for position in self.positions:
            rect = pygame.Rect(self.offset_x + position[0] * self.CELL_SIZE, self.offset_y + position[1] * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE)
            pygame.draw.rect(surface, (0, 255, 0), rect)

    def get_direction(self):
        if(self.direction == pygame.Vector2(0,-1)):
            return 'Up'
        elif(self.direction == pygame.Vector2(0,1)):
            return 'Down'
        elif(self.direction == pygame.Vector2(-1,0)):
            return 'Left'
        else:
            return 'Right'
        
    def get_relative_food_position(self, food):
        head_position = self.positions[0]
        distance_x = food.position[0] - head_position[0]
        distance_y = food.position[1] - head_position[1]
        
        if(distance_x == 0 and distance_y < 0):
            return "Up"
        elif(distance_x == 0 and distance_y > 0):
            return "Down"
        elif(distance_x < 0 and distance_y == 0):
            return "Left"
        elif(distance_x > 0 and distance_y == 0):
            return "Right"
        elif distance_x <= 0 and distance_y <= 0:
            return "Top-Left"
        elif distance_x >= 0 and distance_y <= 0:
            return "Top-Right"
        elif distance_x <= 0 and distance_y >= 0:
            return "Bottom-Left"
        else:
            return "Bottom-Right"
        
    
    def has_obstacles_up(self,grid, head_position, max_range):
        for i in range(max_range):
            head_position = (head_position[0], head_position[1] - 1)
            if head_position in self.positions or head_position[1] < 0:
                return True
        return False

    def has_obstacles_right(self,grid, head_position, max_range):
        for i in range(max_range):
            head_position = (head_position[0] + 1, head_position[1] )
            if head_position in self.positions or head_position[0] >= grid.size:
                return True
        return False
    
    def has_obstacles_down(self,grid, head_position, max_range):
        for i in range(max_range):
            head_position = (head_position[0], head_position[1] + 1)
            if head_position in self.positions or head_position[1] >= grid.size:
                return True
        return False
    
    def has_obstacles_left(self,grid, head_position, max_range):
        for i in range(max_range):
            head_position = (head_position[0] - 1, head_position[1])
            if head_position in self.positions or head_position[0] < 0:
                return True
        return False

    def perform_action(self,action):
        if action == "Up":
            if self.direction != pygame.Vector2(0, 1):
                self.direction = pygame.Vector2(0, -1)
        elif action == "Down":
            if self.direction != pygame.Vector2(0, -1):
                self.direction = pygame.Vector2(0, 1)
        elif action == "Left":
            if self.direction != pygame.Vector2(1, 0):
                self.direction = pygame.Vector2(-1, 0)
        elif action == "Right":
            if self.direction != pygame.Vector2(-1, 0):
                self.direction = pygame.Vector2(1, 0)

    def has_obstacles_ahead(self, grid,direction,max_range):
        head_x = self.positions[0][0]
        head_y = self.positions[0][1]
        match(direction):
            case "Left":
                for i in range (max_range):
                    if((head_x -(i+1),head_y) in self.positions or (head_x -(i+1)) < 0):
                        return i+1
            case "Right":
                for i in range (max_range):
                    if((head_x +(i+1),head_y) in self.positions or (head_x +(i+1)) > grid.size):
                        return i+1
            case "Down":
                for i in range (max_range):
                    if((head_x,head_y +(i+1)) in self.positions or (head_y -(i+1)) > grid.size):
                        return i+1
            case "Up":
                for i in range (max_range):
                    if((head_x,head_y -(i+1)) in self.positions or (head_y +(i+1)) < 0):
                        return i
        return "No obstacles"