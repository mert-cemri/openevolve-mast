'''
Main game file to run the Flappy Bird clone.
'''
import pygame
from bird import Bird
from pipe import Pipe
from score import Score
from constants import *
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.bird = Bird()
        self.pipes = []
        self.score = Score()
        self.running = True
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird.flap()
    def update(self):
        self.bird.update(self)
        for pipe in self.pipes:
            pipe.update()
            if pipe.is_off_screen():
                self.pipes.remove(pipe)
            if pipe.collides_with(self.bird):
                self.running = False
            if pipe.passed_by(self.bird):
                self.score.increment()
        if len(self.pipes) == 0 or self.pipes[-1].x < SCREEN_WIDTH - PIPE_SPACING:
            self.pipes.append(Pipe())
    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.bird.draw(self.screen)
        for pipe in self.pipes:
            pipe.draw(self.screen)
        self.score.draw(self.screen)
        pygame.display.flip()
    def game_over(self):
        self.running = False
if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()