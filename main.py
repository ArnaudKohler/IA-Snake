import pickle
import pygame
import sys
from snake import Snake
from food import Food
from grid import Grid
from agent import Agent
import matplotlib.pyplot as plt
# Initialisation de Pygame
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
GRID_SIZE = 15 #Number of cells
CELL_SIZE = 30 #Sife of celles in pixel
NUMBER_OF_EPISODES = 200

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #Size of the app in pixels
pygame.display.set_caption("Snake Game")

font = pygame.font.Font(None, 36) #File path & size

def main():
    clock = pygame.time.Clock()
    grid = Grid(GRID_SIZE, CELL_SIZE) #Size of the grid & size of the cell
    grid_offsets = grid.get_offsets()
    snake = Snake(GRID_SIZE, CELL_SIZE, grid_offsets)
    food = Food(GRID_SIZE, CELL_SIZE, snake, grid_offsets)
    agent = Agent(0.1,0.95,1,0.997)
    CLOCK_TIME = 10

    all_rewards = []
    total_rewards = 0

    try:
        agent.load_q_table('q_table.pkl')
        agent.epsilon = 0
        print("Q-table chargée avec succès.")
    except FileNotFoundError:
        print("Aucune Q-table trouvée, création d'une nouvelle Q-table.")

    while (agent.episodes <= NUMBER_OF_EPISODES):
        print(agent.episodes)
        print("actual head", snake.positions[0])
        print("actual food position", food.position)
        current_state = agent.get_state(snake,food,grid)
        print(current_state)
        q_values = agent.get_q_values(current_state)
        action = agent.choose_action(q_values, snake.get_direction())
        #print(action)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.KEYDOWN: ##Check the pressed key and move the snake if direction accordingly, check if not the opposite direction
                if event.key == pygame.K_UP:
                    CLOCK_TIME += 10
                elif event.key == pygame.K_DOWN:
                        CLOCK_TIME -= 10
            """ elif event.type == pygame.KEYDOWN: ##Check the pressed key and move the snake if direction accordingly, check if not the opposite direction
                if event.key == pygame.K_UP:
                    #CLOCK_TIME += 1
                    if snake.direction != pygame.Vector2(0, 1):
                        snake.direction = pygame.Vector2(0, -1)
                elif event.key == pygame.K_DOWN:
                    if snake.direction != pygame.Vector2(0, -1):
                        snake.direction = pygame.Vector2(0, 1)
                        #CLOCK_TIME -= 1
                elif event.key == pygame.K_LEFT:
                    if snake.direction != pygame.Vector2(1, 0):
                        snake.direction = pygame.Vector2(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    if snake.direction != pygame.Vector2(-1, 0):
                        snake.direction = pygame.Vector2(1, 0) """
                
        snake.perform_action(action)
        #snake.update()

        next_state, reward = agent.measure_rewards(snake,food,grid,screen)
        agent.update_q_table(current_state, action, reward, next_state)

        total_rewards += reward
        
        if(reward == -350):
            all_rewards.append(total_rewards)
            total_rewards = 0

        """ if snake.positions[0] == food.position:
            snake.grow_snake()
            food.new_food(snake) """
    

        score_text = font.render(f"Score: {len(snake.positions) - 1}", True, (255, 255, 255)) #text, antialias, color
        screen.blit(score_text, (SCREEN_WIDTH / 2 - 50, 20)) #Position x & y
        pygame.display.update()
        clock.tick(CLOCK_TIME) #Speed of the game
    
    avg_reward = sum(all_rewards) / len(all_rewards)

    print(f"Score moyen: {sum(agent.scores) / len(agent.scores)}")
    print(f"Récompense moyenne: {avg_reward}")

    plt.figure(facecolor='black')
    plt.plot(agent.scores, color='cyan', label='Scores by episodes')
    plt.xlabel('episodes', color='white')
    plt.ylabel('Score', color='white')
    plt.title('Snake agent performance', color='white')
    plt.legend()
    plt.grid(True, which='both', color='gray', linestyle='--', linewidth=0.5)
    plt.gca().spines['bottom'].set_color('white')
    plt.gca().spines['top'].set_color('white') 
    plt.gca().spines['right'].set_color('white')
    plt.gca().spines['left'].set_color('white')
    plt.gca().xaxis.label.set_color('white')
    plt.gca().yaxis.label.set_color('white')
    plt.gca().tick_params(axis='x', colors='white')
    plt.gca().tick_params(axis='y', colors='white')
    plt.gca().title.set_color('white')

    plt.savefig('results.png', facecolor='black')

    agent.save_q_table('q_table.pkl')

if __name__ == "__main__":
    main()
