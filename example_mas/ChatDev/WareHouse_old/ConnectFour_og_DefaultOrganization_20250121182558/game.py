'''
Contains the Game class to manage the game logic for Connect Four.
'''
class Game:
    def __init__(self):
        self.current_player = 1
        self.board = [[0 for _ in range(7)] for _ in range(6)]
        self.winner = None
    def make_move(self, column):
        for row in reversed(range(6)):
            if self.board[row][column] == 0:
                self.board[row][column] = self.current_player
                if self.check_winner(row, column):
                    self.winner = self.current_player
                self.current_player = 3 - self.current_player
                return True
        return False
    def check_winner(self, row, column):
        # Check horizontal, vertical, and diagonal lines for a win
        return (self.check_line(row, column, 1, 0) or
                self.check_line(row, column, 0, 1) or
                self.check_line(row, column, 1, 1) or
                self.check_line(row, column, 1, -1))
    def check_line(self, row, column, delta_row, delta_col):
        count = 0
        player = self.board[row][column]
        for d in range(-3, 4):
            r = row + d * delta_row
            c = column + d * delta_col
            if 0 <= r < 6 and 0 <= c < 7 and self.board[r][c] == player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
        return False
    def is_draw(self):
        return all(self.board[0][col] != 0 for col in range(7))