'''
Handles rendering of the game grid and tiles using Pygame.
'''
import pygame
class Renderer:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        self.tile_size = 80
        self.margin = 5
    def draw(self):
        self.screen.fill((187, 173, 160))
        self.draw_grid()
        self.draw_tiles()
        self.draw_score()
        if self.game.game_over:
            self.draw_game_over()
    def draw_grid(self):
        for r in range(self.game.grid_size):
            for c in range(self.game.grid_size):
                pygame.draw.rect(self.screen, (205, 193, 180), 
                                 (c * (self.tile_size + self.margin), r * (self.tile_size + self.margin), 
                                  self.tile_size, self.tile_size))
    def draw_tiles(self):
        for r in range(self.game.grid_size):
            for c in range(self.game.grid_size):
                value = self.game.grid[r][c]
                if value > 0:
                    pygame.draw.rect(self.screen, (238, 228, 218), 
                                     (c * (self.tile_size + self.margin), r * (self.tile_size + self.margin), 
                                      self.tile_size, self.tile_size))
                    font = pygame.font.Font(None, 36)
                    text = font.render(str(value), True, (119, 110, 101))
                    text_rect = text.get_rect(center=(c * (self.tile_size + self.margin) + self.tile_size / 2, 
                                                      r * (self.tile_size + self.margin) + self.tile_size / 2))
                    self.screen.blit(text, text_rect)
    def draw_score(self):
        font = pygame.font.Font(None, 36)
        text = font.render(f'Score: {self.game.score}', True, (119, 110, 101))
        self.screen.blit(text, (10, 10))
    def draw_game_over(self):
        font = pygame.font.Font(None, 72)
        text = font.render('Game Over', True, (255, 0, 0))
        text_rect = text.get_rect(center=(self.screen.get_width() / 2, self.screen.get_height() / 2))
        self.screen.blit(text, text_rect)