'''
Main game loop and initialization.
'''
import pygame
from player import Player
from map import Map
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Tower of the Sorcerer")
        self.clock = pygame.time.Clock()
        self.map = Map()
        self.player = Player(self.map.start_position)
        self.running = True
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    self.handle_key(event.key)
            self.update()
            self.draw()
            self.clock.tick(60)
    def handle_key(self, key):
        if key == pygame.K_w:
            self.player.move(0, -1, self.map)
        elif key == pygame.K_s:
            self.player.move(0, 1, self.map)
        elif key == pygame.K_a:
            self.player.move(-1, 0, self.map)
        elif key == pygame.K_d:
            self.player.move(1, 0, self.map)
    def update(self):
        self.player.interact(self.map)
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.map.draw(self.screen)
        self.player.draw(self.screen)
        pygame.display.flip()
if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()