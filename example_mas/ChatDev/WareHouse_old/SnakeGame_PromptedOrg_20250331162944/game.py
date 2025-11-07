'''
Game class to manage the game loop and state.
'''
import pygame
from snake import Snake
from food import Food
from board import Board
from score import Score
class Game:
    def __init__(self):
        pygame.init()
        self.board = Board()
        self.snake = Snake(self.board.width, self.board.height)
        self.food = Food(self.board.width, self.board.height)
        self.score = Score()
        self.clock = pygame.time.Clock()
        self.running = True
        self.difficulty = self.select_difficulty()
    def select_difficulty(self):
        print("Select Difficulty Level: 1. Easy 2. Medium 3. Hard")
        choice = input("Enter 1, 2, or 3: ")
        if choice == '1':
            return 5  # Easy
        elif choice == '2':
            return 10  # Medium
        elif choice == '3':
            return 15  # Hard
        else:
            print("Invalid choice, defaulting to Medium.")
            return 10  # Default to Medium
    def run(self):
        while self.running:
            self.handle_input()
            self.update()
            self.render()
            self.clock.tick(self.difficulty)  # Use the selected difficulty level
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.snake.change_direction(event.key)
    def update(self):
        self.snake.move()
        if self.snake.check_collision():
            self.running = False
        if self.snake.head == self.food.position:
            self.snake.grow()
            self.food.spawn(self.snake.body)
            self.score.update()
    def render(self):
        self.board.draw(self.snake, self.food)
        self.score.display()
        pygame.display.flip()