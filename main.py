import pygame
import sys
from snake import Snake
from food import Food
from grid import Grid

# Initialisation de Pygame
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
GRID_SIZE = 15 #Number of cells
CELL_SIZE = 30 #Sife of celles in pixel

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #Size of the app in pixels
pygame.display.set_caption("Snake Game")

font = pygame.font.Font(None, 36) #File path & size

def main():
    clock = pygame.time.Clock()
    grid = Grid(GRID_SIZE, CELL_SIZE) #Size of the grid & size of the cell
    grid_offsets = grid.get_offsets()
    snake = Snake(GRID_SIZE, CELL_SIZE, grid_offsets)
    food = Food(GRID_SIZE, CELL_SIZE, snake, grid_offsets)


    while True:
        updated = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN: ##Check the pressed key and move the snake if direction accordingly, check if not the opposite direction
                if event.key == pygame.K_UP:
                    if snake.direction != pygame.Vector2(0, 1):
                        snake.direction = pygame.Vector2(0, -1)
                elif event.key == pygame.K_DOWN:
                    if snake.direction != pygame.Vector2(0, -1):
                        snake.direction = pygame.Vector2(0, 1)
                elif event.key == pygame.K_LEFT:
                    if snake.direction != pygame.Vector2(1, 0):
                        snake.direction = pygame.Vector2(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    if snake.direction != pygame.Vector2(-1, 0):
                        snake.direction = pygame.Vector2(1, 0)
                snake.update()
                updated = True
        if(not updated):
            snake.update()
        

        if snake.positions[0] == food.position:
            snake.grow_snake()
            food.new_food(snake)

        screen.fill((0, 0, 0)) #background color of the grid
        grid.draw(screen)
        snake.draw(screen)
        food.draw(screen)

        score_text = font.render(f"Score: {len(snake.positions) - 1}", True, (255, 255, 255)) #text, antialias, color
        screen.blit(score_text, (SCREEN_WIDTH / 2 - 50, 20)) #Position x & y
        pygame.display.update()
        clock.tick(8) #Speed of the game

if __name__ == "__main__":
    main()
