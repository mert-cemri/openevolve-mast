'''
Contains the game logic for Connect Four.
'''
class ConnectFourGame:
    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.board = [['' for _ in range(self.columns)] for _ in range(self.rows)]
        self.current_player = 'R'  # R for Red, Y for Yellow
    def drop_disc(self, column):
        for row in reversed(range(self.rows)):
            if self.board[row][column] == '':
                self.board[row][column] = self.current_player
                if self.check_winner(row, column):
                    return f"Player {self.current_player} wins!"
                elif self.is_draw():
                    return "It's a draw!"
                self.current_player = 'Y' if self.current_player == 'R' else 'R'
                return None
        return "Column is full!"
    def check_winner(self, row, column):
        # Check horizontal, vertical, and diagonal lines for a win
        return (self.check_line(row, column, 0, 1) or  # Horizontal
                self.check_line(row, column, 1, 0) or  # Vertical
                self.check_line(row, column, 1, 1) or  # Diagonal /
                self.check_line(row, column, 1, -1))   # Diagonal \
    def check_line(self, row, column, delta_row, delta_col):
        count = 0
        player = self.board[row][column]
        for d in range(-3, 4):
            r = row + d * delta_row
            c = column + d * delta_col
            if 0 <= r < self.rows and 0 <= c < self.columns and self.board[r][c] == player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
        return False
    def is_draw(self):
        return all(self.board[0][col] != '' for col in range(self.columns))