'''
Main game file. Initializes the game and runs the main loop.
'''
import pygame
from bird import Bird
from pipe import Pipe
from score import Score
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 600))
        pygame.display.set_caption('Flappy Bird Clone')
        self.clock = pygame.time.Clock()
        self.bird = Bird()
        self.pipes = [Pipe()]
        self.score = Score()
        self.running = True
        self.pipe_timer = 0  # Add a timer for pipe generation
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird.flap()
    def update(self):
        if self.bird.update():  # Check if the bird hit the ground
            self.running = False
        self.pipe_timer += 1
        if self.pipe_timer >= 90:  # Adjust the interval as needed
            self.pipes.append(Pipe())
            self.pipe_timer = 0
        for pipe in self.pipes:
            pipe.update()
            if pipe.collides_with(self.bird):
                self.running = False
            if pipe.off_screen():
                self.pipes.remove(pipe)
            if pipe.x + pipe.width < self.bird.rect.x and not pipe.passed:
                pipe.passed = True
                self.score.increment()
    def render(self):
        self.screen.fill((135, 206, 235))  # Sky blue background
        self.bird.draw(self.screen)
        for pipe in self.pipes:
            pipe.draw(self.screen)
        self.score.draw(self.screen)
        pygame.display.flip()
if __name__ == '__main__':
    Game().run()