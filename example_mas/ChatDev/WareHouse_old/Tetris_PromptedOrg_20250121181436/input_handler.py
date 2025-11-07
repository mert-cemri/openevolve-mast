'''
Handles user input for controlling the tetrominoes.
'''
import curses
class InputHandler:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.stdscr.nodelay(True)  # Non-blocking input
    def process_input(self, tetromino, board):
        ch = self.stdscr.getch()
        if ch == curses.KEY_LEFT:  # Move left
            tetromino.move(-1, 0, board)
        elif ch == curses.KEY_RIGHT:  # Move right
            tetromino.move(1, 0, board)
        elif ch == curses.KEY_UP:  # Rotate
            tetromino.rotate()
            if board.is_collision(tetromino):
                tetromino.rotate()  # Revert rotation if collision
                tetromino.rotate()
                tetromino.rotate()
        elif ch == curses.KEY_DOWN:  # Move down faster
            tetromino.move(0, 1, board)