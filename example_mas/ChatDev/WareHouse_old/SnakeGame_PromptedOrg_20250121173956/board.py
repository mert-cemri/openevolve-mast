'''
Represents the game board, including methods to render the board and check for collisions.
'''
class Board:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
    def render(self, stdscr, snake, food):
        stdscr.clear()
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) in snake.body:
                    stdscr.addstr(y, x, 'S')
                elif (x, y) == food.position:
                    stdscr.addstr(y, x, 'F')
                else:
                    stdscr.addstr(y, x, ' ')
        stdscr.refresh()
    def is_within_bounds(self, position):
        x, y = position
        return 0 <= x < self.width and 0 <= y < self.height