from snake import Snake
from food import Food
from grid import Grid
import math
import numpy as np

class Agent:
    def __init__(self, learning_rate, discount_factor, exploration_rate,exploration_decay):
        self.alpha = learning_rate
        self.gamma = discount_factor
        self.epsilon = exploration_rate
        self.exploration_decay = exploration_decay
        self.q_table = {}
        self.actions = ['Up','Right','Down','Left']

    def get_state(self,snake,food,grid):

        head_direction = snake.get_direction() #Up, right, down, left
        food_direction = snake.get_relative_food_position(food) #Can be Up, Right, Down, Left, Top-left, Top-Right, Bottom-Left, Bottom-Right

        has_obstacles_up = snake.has_obstacles_up(grid,snake.positions[0],1)  #Check wihtin a range if there is a wall or self tail
        has_obstacles_right = snake.has_obstacles_right(grid,snake.positions[0],1)
        has_obstacles_down = snake.has_obstacles_down(grid,snake.positions[0],1)
        has_obstacles_left = snake.has_obstacles_left(grid,snake.positions[0],1)

        state = (head_direction,food_direction,has_obstacles_up,has_obstacles_right,has_obstacles_down,has_obstacles_left)
        
        return state
    
    def choose_action(self,q_values,current_snake_direction):
        random_number = np.random.rand()
        opposite_directions = {
            'Up': 'Down',
            'Down': 'Up',
            'Left': 'Right',
            'Right': 'Left'
        }
        if(random_number < self.epsilon):
            action = self.actions[np.random.randint(0,4)]
            while action == opposite_directions[current_snake_direction]:
                action = self.actions[np.random.randint(0,4)]
        else:
            sorted_actions = sorted(q_values, key=q_values.get, reverse=True)
            for action in sorted_actions:
                if action != opposite_directions[current_snake_direction]:
                    break
        self.epsilon *= self.exploration_decay
        print("En dessous de 0.05 ?", self.epsilon < 0.05)
        return action

    def get_q_values(self,state):
        if(state not in self.q_table):
            self.q_table[state] = {actions: 0 for actions in self.actions}
            print("NEW !", len(self.q_table))
        return self.q_table[state]


    def measure_rewards(self,snake,food, grid):
        head_x, head_y = snake.positions[0]
        dir_x, dir_y = snake.direction
        new_head = (head_x + dir_x, head_y + dir_y)

        if(new_head == food.position):
            reward = 100
            snake.positions.insert(0, new_head)
            food.new_food(snake)
        elif(new_head in snake.positions[1:]):
            reward = -100
            snake.reset()
        elif(not 0 <= new_head[0] < grid.size or not 0 <= new_head[1]):
            snake.reset()
            reward = -10
        else:
            if(self.get_distance(food.position,snake.positions[0]) > self.get_distance(food.position,new_head)):
                reward = 1
            else:
                reward = -1
            snake.positions.pop() #Remove the last cell of the snake
            snake.positions.insert(0, new_head) #Insert a new cell in front of the snake
        return self.get_state(snake,food,grid), reward
    
    def update_q_table(self,current_state, action, reward, next_state):
        next_state_q_values = self.get_q_values(next_state)
        max_next_q_values = max(next_state_q_values.values())
        self.q_table[current_state][action] += self.alpha * (reward + self.gamma * max_next_q_values - self.q_table[current_state][action])
        #print(self.q_table)

    def get_distance(self,food_position,head_position):
        return math.sqrt((food_position[0]-head_position[0])**2 + (food_position[1]-head_position[1])**2)
