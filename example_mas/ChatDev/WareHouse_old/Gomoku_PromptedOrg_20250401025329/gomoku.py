'''
This file contains the GomokuGame class which manages the logic of the Gomoku game.
'''
class GomokuGame:
    def __init__(self, size=15):
        self.size = size
        self.board = [['.' for _ in range(size)] for _ in range(size)]
        self.current_player = 'B'  # B for Black, W for White
    def display_board(self):
        print("  ", end="")
        for i in range(self.size):
            print(f"{i:2}", end="")
        print()
        for idx, row in enumerate(self.board):
            print(f"{idx:2}", end=" ")
            for cell in row:
                print(f"{cell:2}", end="")
            print()
    def is_valid_move(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size and self.board[x][y] == '.'
    def make_move(self, x, y):
        if self.is_valid_move(x, y):
            self.board[x][y] = self.current_player
            print(f"Player {'Black' if self.current_player == 'B' else 'White'} placed a stone at ({x}, {y}).")
            return True
        else:
            print(f"Invalid move at ({x}, {y}). Cell already occupied or out of bounds.")
            return False
    def switch_player(self):
        self.current_player = 'W' if self.current_player == 'B' else 'B'
    def check_win(self, x, y, player):
        """
        Check if the specified player has won the game after placing a stone at (x, y).
        """
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dx, dy in directions:
            count = 1
            # Check forward direction
            i, j = x + dx, y + dy
            while 0 <= i < self.size and 0 <= j < self.size and self.board[i][j] == player:
                count += 1
                i += dx
                j += dy
            # Check backward direction
            i, j = x - dx, y - dy
            while 0 <= i < self.size and 0 <= j < self.size and self.board[i][j] == player:
                count += 1
                i -= dx
                j -= dy
            if count >= 5:
                return True
        return False
    def is_board_full(self):
        """Check if the board is completely filled."""
        for row in self.board:
            if '.' in row:
                return False
        return True