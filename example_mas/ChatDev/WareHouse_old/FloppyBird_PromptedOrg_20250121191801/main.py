'''
Main module to run the Flappy Bird clone game.
'''
import pygame
from bird import Bird
from pipe import Pipe
from score import Score
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Flappy Bird Clone')
        self.clock = pygame.time.Clock()
        self.bird = Bird()
        self.pipes = [Pipe()]
        self.score = Score()
        self.running = True
        self.pipe_timer = 0  # New variable to track time since last pipe
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird.flap()
    def update(self):
        self.bird.update()
        if self.bird.y >= SCREEN_HEIGHT:  # Check if the bird hits the ground
            self.running = False
        for pipe in self.pipes:
            pipe.update()
            if pipe.is_colliding(self.bird):
                self.running = False
            if not pipe.passed and pipe.x < self.bird.x:
                self.score.increase()
                pipe.passed = True
        # Update pipe timer and generate new pipe if necessary
        self.pipe_timer += 1
        if self.pipe_timer > 100:  # Adjust the threshold as needed
            self.pipes.append(Pipe())
            self.pipe_timer = 0
    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.bird.draw(self.screen)
        for pipe in self.pipes:
            pipe.draw(self.screen)
        self.score.draw(self.screen)
        pygame.display.flip()
if __name__ == '__main__':
    Game().run()