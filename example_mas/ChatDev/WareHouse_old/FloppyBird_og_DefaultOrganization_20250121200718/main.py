'''
Main game loop and initialization.
'''
import pygame
from bird import Bird
from pipe import Pipe
from score import Score
# Initialize Pygame
pygame.init()
# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 60
PIPE_GAP = 150  # Add this line to define PIPE_GAP
# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird Clone')
# Game class
class Game:
    def __init__(self):
        self.bird = Bird()
        self.pipes = [Pipe(PIPE_GAP)]
        self.score = Score()
        self.clock = pygame.time.Clock()
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
        try:
            self.bird.update()
            for pipe in self.pipes:
                pipe.update()
                if pipe.off_screen():
                    self.pipes.remove(pipe)
                    # Decrease gap size as score increases, with a minimum gap size limit
                    new_gap_size = max(100, PIPE_GAP - self.score.value * 5)
                    self.pipes.append(Pipe(new_gap_size))
                    self.score.increment()
                if pipe.collides_with(self.bird):
                    self.running = False
        except Exception as e:
            print(e)
            self.running = False
    def draw(self):
        screen.fill((135, 206, 235))  # Sky blue background
        self.bird.draw(screen)
        for pipe in self.pipes:
            pipe.draw(screen)
        self.score.draw(screen)
        pygame.display.flip()
if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()