'''
Main game file to initialize and run the roguelike game.
'''
import pygame
from player import Player
from game_map import GameMap
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Tower of the Sorcerer")
        self.clock = pygame.time.Clock()
        self.map = GameMap()
        self.player = Player(self.map.start_position)
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.player.move('up', self.map)
                    elif event.key == pygame.K_s:
                        self.player.move('down', self.map)
                    elif event.key == pygame.K_a:
                        self.player.move('left', self.map)
                    elif event.key == pygame.K_d:
                        self.player.move('right', self.map)
            self.screen.fill((0, 0, 0))
            self.map.draw(self.screen)
            self.player.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()
if __name__ == "__main__":
    game = Game()
    game.run()