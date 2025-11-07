'''
PuzzleBoard class manages the puzzle grid, word placement, validation, and highlighting.
'''
class PuzzleBoard:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [['' for _ in range(width)] for _ in range(height)]
    def place_word(self, word, positions):
        for letter, (x, y) in zip(word, positions):
            self.board[y][x] = letter
    def is_valid_word(self, word, path):
        if len(word) != len(path):
            return False
        for letter, (x, y) in zip(word, path):
            if not (0 <= x < self.width and 0 <= y < self.height):
                return False
            if self.board[y][x] != letter:
                return False
        return True
    def display_board(self, highlight_words, found_theme_words):
        for y in range(self.height):
            row = ''
            for x in range(self.width):
                letter = self.board[y][x] if self.board[y][x] else '.'
                highlighted = False
                for word, positions, color in highlight_words:
                    if (x, y) in positions and word in found_theme_words:
                        highlighted = True
                        if color == 'blue':
                            row += f"[{letter}]"
                        elif color == 'yellow':
                            row += f"({letter})"
                        break
                if not highlighted:
                    row += f" {letter} "
            print(row)
    def get_adjacent_positions(self, position):
        x, y = position
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        adjacent = []
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                adjacent.append((nx, ny))
        return adjacent
    def is_spangram_valid(self, positions):
        sides_touched = set()
        for x, y in positions:
            if x == 0:
                sides_touched.add('left')
            if x == self.width - 1:
                sides_touched.add('right')
            if y == 0:
                sides_touched.add('top')
            if y == self.height - 1:
                sides_touched.add('bottom')
        return ('left' in sides_touched and 'right' in sides_touched) or ('top' in sides_touched and 'bottom' in sides_touched)