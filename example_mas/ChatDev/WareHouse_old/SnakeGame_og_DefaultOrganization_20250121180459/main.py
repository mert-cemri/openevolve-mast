'''
Main entry point for the Snake game. Initializes the game and starts the game loop.
'''
import pygame
from snake import Snake
from food import Food
from utils import random_position
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 400))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.running = True
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(10)
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction('UP')
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction('DOWN')
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction('LEFT')
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction('RIGHT')
    def update(self):
        self.snake.move()
        if self.snake.check_collision():
            self.running = False
        if self.snake.head_position() == self.food.position:
            self.snake.grow()
            self.food.spawn(self.snake.body)  # Pass the snake's body to avoid overlap
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        pygame.display.flip()
if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()