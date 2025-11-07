'''
Graphical User Interface for the 2048 game using Pygame.
'''
import pygame
from game import Game
class GUI:
    def __init__(self, game):
        self.game = game
        self.width = 600
        self.height = 600
        self.tile_size = self.width // self.game.size
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.SysFont("Arial", 24)
    def draw_grid(self):
        for i in range(self.game.size):
            for j in range(self.game.size):
                tile = self.game.grid[i][j]
                x, y = j * self.tile_size, i * self.tile_size
                if tile:
                    pygame.draw.rect(self.screen, (255, 255, 255), (x, y, self.tile_size, self.tile_size))
                    text = self.font.render(str(tile.value), True, (0, 0, 0))
                    self.screen.blit(text, (x + self.tile_size // 3, y + self.tile_size // 3))
                else:
                    pygame.draw.rect(self.screen, (200, 200, 200), (x, y, self.tile_size, self.tile_size))
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.game.move('up')
                elif event.key == pygame.K_DOWN:
                    self.game.move('down')
                elif event.key == pygame.K_LEFT:
                    self.game.move('left')
                elif event.key == pygame.K_RIGHT:
                    self.game.move('right')
    def update_display(self):
        self.screen.fill((0, 0, 0))
        self.draw_grid()
        pygame.display.flip()