'''
Game class manages the game loop, events, and rendering.
'''
import pygame
from snake import Snake
from food import Food
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((600, 400))
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        # Ensure food does not spawn on the snake's initial position
        while self.food.position in self.snake.body:
            self.food.spawn(self.snake.body)
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
                self.snake.change_direction(event.key)
    def update(self):
        self.snake.move()
        if self.snake.check_collision():
            self.running = False
        if self.snake.body[0] == self.food.position:  # Corrected line
            self.snake.grow()
            self.food.spawn(self.snake.body)  # Pass the snake's body to check for overlap
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        pygame.display.flip()