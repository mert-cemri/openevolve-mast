'''
Grid management for the 2048 game, including rendering and tile operations.
'''
import pygame
GRID_SIZE = 10
TILE_SIZE = 50
TILE_MARGIN = 5
COLORS = {
    0: (205, 193, 180),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}
class Grid:
    def __init__(self):
        self.tiles = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    def reset(self):
        self.tiles = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    def draw(self, screen):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                value = self.tiles[row][col]
                color = COLORS.get(value, (60, 58, 50))
                pygame.draw.rect(screen, color, 
                                 (col * (TILE_SIZE + TILE_MARGIN) + TILE_MARGIN,
                                  row * (TILE_SIZE + TILE_MARGIN) + TILE_MARGIN,
                                  TILE_SIZE, TILE_SIZE))
                if value != 0:
                    font = pygame.font.Font(None, 36)
                    text = font.render(str(value), True, (0, 0, 0))
                    text_rect = text.get_rect(center=(col * (TILE_SIZE + TILE_MARGIN) + TILE_MARGIN + TILE_SIZE // 2,
                                                      row * (TILE_SIZE + TILE_MARGIN) + TILE_MARGIN + TILE_SIZE // 2))
                    screen.blit(text, text_rect)
    def move(self, direction, game):
        moved = False
        if direction in ['left', 'right']:
            for row in self.tiles:
                if direction == 'left':
                    moved |= self._compress(row, game)
                else:
                    row.reverse()
                    moved |= self._compress(row, game)
                    row.reverse()  # Reverse back after compression
        elif direction in ['up', 'down']:
            for col in range(GRID_SIZE):
                column = [self.tiles[row][col] for row in range(GRID_SIZE)]
                if direction == 'up':
                    moved |= self._compress(column, game)
                else:
                    column.reverse()
                    moved |= self._compress(column, game)
                    column.reverse()  # Reverse back after compression
                for row in range(GRID_SIZE):
                    self.tiles[row][col] = column[row]
        return moved
    def _compress(self, line, game):
        new_line = [i for i in line if i != 0]
        merged = []
        skip = False
        for i in range(len(new_line)):
            if skip:
                skip = False
                continue
            if i + 1 < len(new_line) and new_line[i] == new_line[i + 1]:
                merged_value = new_line[i] * 2
                merged.append(merged_value)
                game.score += merged_value  # Update the score
                skip = True
            else:
                merged.append(new_line[i])
        merged.extend([0] * (GRID_SIZE - len(merged)))
        if merged != line:
            line[:] = merged
            return True
        return False
    def get_empty_cells(self):
        return [(r, c) for r in range(GRID_SIZE) for c in range(GRID_SIZE) if self.tiles[r][c] == 0]
    def set_tile(self, row, col, value):
        self.tiles[row][col] = value
    def can_move(self):
        for row in self.tiles:
            for i in range(GRID_SIZE - 1):
                if row[i] == 0 or row[i] == row[i + 1]:
                    return True
        for col in range(GRID_SIZE):
            for row in range(GRID_SIZE - 1):
                if self.tiles[row][col] == 0 or self.tiles[row][col] == self.tiles[row + 1][col]:
                    return True
        return False