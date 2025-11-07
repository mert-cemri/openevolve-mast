'''
Handles rendering the game state to the screen.
'''
class Renderer:
    def __init__(self, stdscr):
        self.stdscr = stdscr
    def render(self, board, tetromino):
        # Create a copy of the board grid to overlay the tetromino
        display_grid = [row[:] for row in board.grid]
        # Overlay the tetromino on the display grid
        for x, y in tetromino.get_blocks():
            if 0 <= y < board.height:
                display_grid[y][x] = 1
        # Render the grid
        self.stdscr.clear()
        for row in display_grid:
            self.stdscr.addstr(''.join(['#' if cell else '.' for cell in row]) + '\n')
        self.stdscr.addstr('-' * board.width + '\n')
        self.stdscr.refresh()