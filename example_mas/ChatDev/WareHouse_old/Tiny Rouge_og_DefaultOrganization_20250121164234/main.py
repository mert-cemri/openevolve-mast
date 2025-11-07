'''
Main entry point for the roguelike game. Initializes and runs the game loop.
'''
import pygame
from player import Player
from level import Level
from utils import load_image
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Tower of the Sorcerer")
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.player = Player(self.level.start_position)
        self.running = True
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.player.move('up', self.level)
                elif event.key == pygame.K_s:
                    self.player.move('down', self.level)
                elif event.key == pygame.K_a:
                    self.player.move('left', self.level)
                elif event.key == pygame.K_d:
                    self.player.move('right', self.level)
    def update(self):
        # Update game logic here
        pass
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.level.draw(self.screen)
        self.player.draw(self.screen)
        pygame.display.flip()
if __name__ == "__main__":
    game = Game()
    game.run()