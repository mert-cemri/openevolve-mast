'''
Game logic for Reversi. Manages the board state, current player, and game rules.
'''
class Game:
    def __init__(self):
        self.board = [[None] * 8 for _ in range(8)]
        self.current_player = 'B'
        self.initialize_board()
    def initialize_board(self):
        self.board[3][3] = 'W'
        self.board[3][4] = 'B'
        self.board[4][3] = 'B'
        self.board[4][4] = 'W'
    def make_move(self, row, col):
        if not self.is_valid_move(row, col):
            return False
        self.board[row][col] = self.current_player
        self.flip_discs(row, col)
        return True
    def is_valid_move(self, row, col):
        if self.board[row][col] is not None:
            return False
        # Check all directions for valid flips
        return any(self.check_direction(row, col, dr, dc) for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)])
    def check_direction(self, row, col, dr, dc):
        r, c = row + dr, col + dc
        if not (0 <= r < 8 and 0 <= c < 8) or self.board[r][c] != self.opponent():
            return False
        r += dr
        c += dc
        while 0 <= r < 8 and 0 <= c < 8:
            if self.board[r][c] is None:
                return False
            if self.board[r][c] == self.current_player:
                return True
            r += dr
            c += dc
        return False
    def flip_discs(self, row, col):
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]:
            if self.check_direction(row, col, dr, dc):
                r, c = row + dr, col + dc
                while self.board[r][c] == self.opponent():
                    self.board[r][c] = self.current_player
                    r += dr
                    c += dc
    def opponent(self):
        return 'W' if self.current_player == 'B' else 'B'
    def switch_player(self):
        self.current_player = self.opponent()
    def is_game_over(self):
        # Check if the board is full
        is_full = all(all(cell is not None for cell in row) for row in self.board)
        # Check if either player has a valid move
        original_player = self.current_player
        has_moves_current = any(self.is_valid_move(r, c) for r in range(8) for c in range(8))
        self.switch_player()
        has_moves_opponent = any(self.is_valid_move(r, c) for r in range(8) for c in range(8))
        # Restore the original player
        self.current_player = original_player
        # Game is over if the board is full or neither player has a valid move
        return is_full or not (has_moves_current or has_moves_opponent)
    def get_winner(self):
        b_count = sum(row.count('B') for row in self.board)
        w_count = sum(row.count('W') for row in self.board)
        if b_count > w_count:
            return 'Black'
        elif w_count > b_count:
            return 'White'
        else:
            return 'Draw'