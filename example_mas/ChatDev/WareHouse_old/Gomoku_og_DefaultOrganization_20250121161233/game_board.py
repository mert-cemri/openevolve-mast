'''
Manages the state of the Gomoku game board.
'''
class GameBoard:
    def __init__(self, size=15):
        self.size = size
        self.board = [[None for _ in range(size)] for _ in range(size)]
    def place_stone(self, x, y, player):
        if self.board[x][y] is None:
            self.board[x][y] = player
            return True
        return False
    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for x in range(self.size):
            for y in range(self.size):
                if self.board[x][y] and self._check_direction(x, y):
                    return self.board[x][y]
        return None
    def _check_direction(self, x, y):
        # Check all directions from (x, y) for exactly 5 in a row
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        player = self.board[x][y]
        for dx, dy in directions:
            count = 1
            for step in range(1, 5):
                nx, ny = x + step * dx, y + step * dy
                if 0 <= nx < self.size and 0 <= ny < self.size and self.board[nx][ny] == player:
                    count += 1
                else:
                    break
            if count == 5:
                # Check if there are more stones in the same direction
                if not (0 <= x + 5 * dx < self.size and 0 <= y + 5 * dy < self.size and self.board[x + 5 * dx][y + 5 * dy] == player):
                    return True
        return False
    def check_draw(self):
        for row in self.board:
            if None in row:
                return False
        return True