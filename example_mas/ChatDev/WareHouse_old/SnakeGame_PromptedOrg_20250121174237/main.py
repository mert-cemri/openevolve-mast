'''
Main module to run the Snake game.
'''
import pygame
import sys
from snake import Snake
from food import Food
from board import Board
class Game:
    def __init__(self, width=600, height=400, block_size=20):
        pygame.init()
        self.width = width
        self.height = height
        self.block_size = block_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.snake = Snake(self.block_size)
        self.food = Food(self.width, self.height, self.block_size)
        self.board = Board(self.screen, self.snake, self.food, self.width, self.height, self.block_size)
    def run(self):
        while True:
            self.handle_events()
            self.snake.move()
            if self.snake.check_collision(self.width, self.height):
                print("Game Over")
                pygame.quit()
                sys.exit()
            if self.snake.eat_food(self.food.position):
                self.snake.grow()
                self.food.spawn(self.snake.body)
            self.board.draw()
            self.clock.tick(10)
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction('UP')
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction('DOWN')
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction('LEFT')
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction('RIGHT')
if __name__ == "__main__":
    game = Game()
    game.run()