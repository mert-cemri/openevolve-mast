'''
This file contains the Game class which represents the Gomoku game logic.
'''
class Game:
    def __init__(self):
        self.board_size = 15
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 'X'
    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        return False
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    def check_winner(self, row, col):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            r, c = row, col
            while count < 5:
                r += dr
                c += dc
                if r < 0 or r >= self.board_size or c < 0 or c >= self.board_size or self.board[r][c] != self.current_player:
                    break
                count += 1
            r, c = row, col
            while count < 5:
                r -= dr
                c -= dc
                if r < 0 or r >= self.board_size or c < 0 or c >= self.board_size or self.board[r][c] != self.current_player:
                    break
                count += 1
            if count >= 5:
                return True
        return False
    def is_board_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True
    def reset(self):
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 'X'