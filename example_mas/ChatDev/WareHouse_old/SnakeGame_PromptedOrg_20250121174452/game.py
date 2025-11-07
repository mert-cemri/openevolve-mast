'''
Game class manages the game loop, user input, and game state updates.
'''
import pygame
from snake import Snake
from food import Food
from board import Board
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 400))  # Initialize pygame window
        pygame.display.set_caption('Snake Game')
        self.board = Board(20, 20, self.screen)
        self.snake = Snake(self.board)
        self.food = Food(self.board, self.snake)
        self.food.spawn()
        self.running = True
        self.clock = pygame.time.Clock()
    def run(self):
        while self.running:
            self.handle_input()
            self.update()
            self.render()
            self.clock.tick(10)  # Control the game speed
    def handle_input(self):
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
        if self.snake.head == self.food.position:
            self.snake.grow()
            self.food.spawn()
    def render(self):
        self.board.draw(self.snake, self.food)
        pygame.display.flip()  # Update the display