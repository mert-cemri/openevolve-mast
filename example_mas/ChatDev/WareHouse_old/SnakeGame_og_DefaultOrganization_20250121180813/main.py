'''
Main game loop and initialization.
'''
import pygame
from snake import Snake
from food import Food
from utils import draw_grid
# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
GRID_SIZE = 20
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.running = True
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
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
        if self.snake.check_collision(SCREEN_WIDTH, SCREEN_HEIGHT):
            self.running = False
        if self.snake.positions[0] == self.food.position:
            self.snake.grow()
            self.food.randomize_position()
    def render(self):
        self.screen.fill((0, 0, 0))
        draw_grid(self.screen, SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE)
        self.snake.draw(self.screen, GRID_SIZE)
        self.food.draw(self.screen, GRID_SIZE)
        pygame.display.flip()
if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()