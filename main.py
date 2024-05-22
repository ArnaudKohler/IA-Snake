import pygame
import sys
from snake import Snake
from food import Food
from grid import Grid

# Initialisation de Pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake Game")

def main():
    clock = pygame.time.Clock()
    grid = Grid(10, 20)
    snake = Snake(grid.size, grid.cell_size)
    food = Food(grid.size, grid.cell_size)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
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

        if snake.positions[0] == food.position:
            snake.grow_snake()
            food.new_food()

        screen.fill((0, 0, 0))
        grid.draw(screen)
        snake.draw(screen)
        food.draw(screen)
        pygame.display.update()
        clock.tick(10)

if __name__ == "__main__":
    main()
