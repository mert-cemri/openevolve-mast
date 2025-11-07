'''
Board class to represent the game board and handle board operations.
'''
import pygame
class Board:
    def __init__(self):
        self.grid = [['' for _ in range(8)] for _ in range(8)]
        self.grid[3][3] = 'white'
        self.grid[3][4] = 'black'
        self.grid[4][3] = 'black'
        self.grid[4][4] = 'white'
    def draw_board(self, screen):
        screen.fill((0, 128, 0))
        for x in range(8):
            for y in range(8):
                rect = pygame.Rect(x * 100, y * 100, 100, 100)
                pygame.draw.rect(screen, (0, 0, 0), rect, 1)
                if self.grid[y][x] == 'black':
                    pygame.draw.circle(screen, (0, 0, 0), rect.center, 40)
                elif self.grid[y][x] == 'white':
                    pygame.draw.circle(screen, (255, 255, 255), rect.center, 40)
    def update_board(self, x, y, player):
        self.grid[y][x] = player.color
        self.flip_discs(x, y, player.color)
    def is_valid_move(self, x, y, player):
        if self.grid[y][x] != '':
            return False
        # Check all directions for valid moves
        return any(self.check_direction(x, y, dx, dy, player.color) for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)])
    def check_direction(self, x, y, dx, dy, color):
        x += dx
        y += dy
        if not (0 <= x < 8 and 0 <= y < 8) or self.grid[y][x] != ('white' if color == 'black' else 'black'):
            return False
        x += dx
        y += dy
        while 0 <= x < 8 and 0 <= y < 8:
            if self.grid[y][x] == '':
                return False
            if self.grid[y][x] == color:
                return True
            x += dx
            y += dy
        return False
    def flip_discs(self, x, y, color):
        for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            if self.check_direction(x, y, dx, dy, color):
                nx, ny = x + dx, y + dy
                while 0 <= nx < 8 and 0 <= ny < 8 and self.grid[ny][nx] != color:
                    self.grid[ny][nx] = color
                    nx += dx
                    ny += dy
    def get_valid_moves(self, player):
        return [(x, y) for x in range(8) for y in range(8) if self.is_valid_move(x, y, player)]