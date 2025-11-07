'''
This file contains the Game class.
'''
class Game:
    def __init__(self):
        self.board = [[0] * 10 for _ in range(10)]
        self.current_player = 1
        self.board_canvas = None
    def make_move(self, row, col):
        if self.board[row][col] == 0:
            self.board[row][col] = self.current_player
            self.current_player = 3 - self.current_player
    def draw_board(self, canvas):
        self.board_canvas = canvas
        for row in range(10):
            for col in range(10):
                x1 = col * 40
                y1 = row * 40
                x2 = x1 + 40
                y2 = y1 + 40
                if self.board[row][col] == 1:
                    self.board_canvas.create_oval(x1, y1, x2, y2, fill="black")
                elif self.board[row][col] == 2:
                    self.board_canvas.create_oval(x1, y1, x2, y2, fill="white")