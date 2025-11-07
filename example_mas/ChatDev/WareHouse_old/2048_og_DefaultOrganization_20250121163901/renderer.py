'''
Renderer for drawing the grid and tiles on the screen.
'''
import pygame
class Renderer:
    def __init__(self, screen, grid):
        self.screen = screen
        self.grid = grid
        self.tile_size = min(self.screen.get_width() // self.grid.size, self.screen.get_height() // self.grid.size)  # Ensure it fits both dimensions
    def draw_grid(self):
        for x in range(0, self.screen.get_width(), self.tile_size):
            pygame.draw.line(self.screen, (204, 192, 179), (x, 0), (x, self.screen.get_height()))
        for y in range(0, self.screen.get_height(), self.tile_size):
            pygame.draw.line(self.screen, (204, 192, 179), (0, y), (self.screen.get_width(), y))
    def draw_tiles(self):
        for row in self.grid.grid:
            for tile in row:
                if tile:
                    self.draw_tile(tile)
    def draw_tile(self, tile):
        x, y = tile.position
        rect = pygame.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
        pygame.draw.rect(self.screen, (238, 228, 218), rect)
        font = pygame.font.Font(None, 36)
        text = font.render(str(tile.value), True, (119, 110, 101))
        text_rect = text.get_rect(center=rect.center)
        self.screen.blit(text, text_rect)