'''
This file contains the GomokuGame class, which manages the Gomoku game logic.
'''
class GomokuGame:
    def __init__(self, size=15):
        self.size = size
        self.board = [['.' for _ in range(size)] for _ in range(size)]
        self.current_player = 'B'  # B for Black, W for White
    def display_board(self):
        print("   " + " ".join(f"{i:2}" for i in range(self.size)))
        for idx, row in enumerate(self.board):
            print(f"{idx:2} " + " ".join(row))
    def place_stone(self, row, col):
        if not (0 <= row < self.size and 0 <= col < self.size):
            print("Move out of bounds. Please enter valid coordinates.")
            return False
        if self.board[row][col] != '.':
            print("Cell already occupied. Please choose another cell.")
            return False
        self.board[row][col] = self.current_player
        return True
    def check_win(self, row, col):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            # Check in one direction
            r, c = row + dr, col + dc
            while 0 <= r < self.size and 0 <= c < self.size and self.board[r][c] == self.current_player:
                count += 1
                r += dr
                c += dc
            # Check in the opposite direction
            r, c = row - dr, col - dc
            while 0 <= r < self.size and 0 <= c < self.size and self.board[r][c] == self.current_player:
                count += 1
                r -= dr
                c -= dc
            if count >= 5:
                return True
        return False
    def is_full(self):
        return all(self.board[row][col] != '.' for row in range(self.size) for col in range(self.size))
    def switch_player(self):
        self.current_player = 'W' if self.current_player == 'B' else 'B'