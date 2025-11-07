'''
Gomoku game logic implementation.
'''
class GomokuGame:
    def __init__(self):
        self.size = 15  # Standard Gomoku board size
        self.board = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.current_player = 'Black'
    def reset_game(self):
        self.board = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.current_player = 'Black'
    def make_move(self, x, y):
        if not (0 <= x < self.size and 0 <= y < self.size):
            return "Invalid move!"
        if self.board[x][y] is None:
            self.board[x][y] = self.current_player
            if self.check_winner(x, y):
                return f"{self.current_player} wins!"
            self.current_player = 'White' if self.current_player == 'Black' else 'Black'
            return None
        else:
            return "Invalid move!"
    def check_winner(self, x, y):
        # Check all directions for a win
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dx, dy in directions:
            count = 1
            for step in range(1, 5):
                nx, ny = x + step * dx, y + step * dy
                if 0 <= nx < self.size and 0 <= ny < self.size and self.board[nx][ny] == self.current_player:
                    count += 1
                else:
                    break
            for step in range(1, 5):
                nx, ny = x - step * dx, y - step * dy
                if 0 <= nx < self.size and 0 <= ny < self.size and self.board[nx][ny] == self.current_player:
                    count += 1
                else:
                    break
            if count >= 5:
                return True
        return False