'''
Manages the overall game state and game loop.
'''
from board import Board
from tetromino import Tetromino
from renderer import Renderer
from input_handler import InputHandler
class Game:
    def __init__(self, stdscr):
        self.board = Board()
        self.renderer = Renderer(stdscr)
        self.input_handler = InputHandler(stdscr)
        self.current_tetromino = Tetromino()
        self.score = 0
        self.game_over = False
    def start(self):
        while not self.game_over:
            self.update()
            self.renderer.render(self.board, self.current_tetromino)
    def update(self):
        self.input_handler.process_input(self.current_tetromino, self.board)
        self.current_tetromino.move(0, 1, self.board)  # Move down by default
        if self.board.is_collision(self.current_tetromino):
            self.current_tetromino.move(0, -1, self.board)  # Revert move
            self.board.place_tetromino(self.current_tetromino)
            lines_cleared = self.board.clear_lines()
            self.score += lines_cleared * 100  # Example scoring: 100 points per line
            self.current_tetromino = Tetromino()
            self.game_over = self.check_game_over()
    def check_game_over(self):
        return self.board.is_collision(self.current_tetromino)