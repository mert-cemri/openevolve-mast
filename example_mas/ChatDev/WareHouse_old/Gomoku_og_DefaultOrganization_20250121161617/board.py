'''
Board class to manage the game board state and rendering.
'''
import pygame
class Board:
    def __init__(self):
        self.size = 15
        self.grid = [['' for _ in range(self.size)] for _ in range(self.size)]
    def reset(self):
        self.grid = [['' for _ in range(self.size)] for _ in range(self.size)]
    def draw_board(self, screen):
        for x in range(self.size):
            for y in range(self.size):
                rect = pygame.Rect(x * 40, y * 40, 40, 40)
                pygame.draw.rect(screen, (0, 0, 0), rect, 1)
                if self.grid[y][x]:
                    font = pygame.font.Font(None, 36)
                    text = font.render(self.grid[y][x], True, (0, 0, 0))
                    screen.blit(text, (x * 40 + 10, y * 40 + 5))
    def update_board(self, x, y, player):
        if self.grid[y][x] == '':
            self.grid[y][x] = player
            return True
        return False
    def is_full(self):
        for row in self.grid:
            if '' in row:
                return False
        return True
    def check_winner(self):
        # Check horizontal, vertical, and diagonal lines for a winner
        for y in range(self.size):
            for x in range(self.size):
                if self.grid[y][x] and self.check_line(x, y):
                    return self.grid[y][x]
        # Check for draw
        if self.is_full():
            return "Draw"
        return None
    def check_line(self, x, y):
        # Check lines in all directions
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dx, dy in directions:
            if self.check_direction(x, y, dx, dy):
                return True
        return False
    def check_direction(self, x, y, dx, dy):
        # Check a single direction for exactly 5 in a row
        count = 0
        player = self.grid[y][x]
        for i in range(5):
            nx, ny = x + i * dx, y + i * dy
            if 0 <= nx < self.size and 0 <= ny < self.size and self.grid[ny][nx] == player:
                count += 1
            else:
                break
        # Ensure there are exactly 5 in a row and no more
        if count == 5:
            # Check the next position in the same direction
            nx, ny = x + 5 * dx, y + 5 * dy
            if 0 <= nx < self.size and 0 <= ny < self.size and self.grid[ny][nx] == player:
                return False
            # Check the previous position in the opposite direction
            nx, ny = x - dx, y - dy
            if 0 <= nx < self.size and 0 <= ny < self.size and self.grid[ny][nx] == player:
                return False
            return True
        return False