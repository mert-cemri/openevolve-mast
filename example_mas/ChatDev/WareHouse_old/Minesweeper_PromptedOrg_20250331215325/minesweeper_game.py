'''
Defines the MinesweeperGame class with game logic and board management.
'''
import random
class MinesweeperGame:
    LEVELS = {
        'beginner': (9, 9, 10),
        'intermediate': (16, 16, 40),
        'expert': (16, 30, 99)
    }
    def __init__(self, level):
        self.rows, self.cols, self.mines = self.LEVELS[level]
        self.board = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
        self.visible = [['#' for _ in range(self.cols)] for _ in range(self.rows)]
        self.flags = set()
        self.generate_board()
    def generate_board(self):
        mine_positions = set()
        while len(mine_positions) < self.mines:
            mine_positions.add((random.randint(0, self.rows - 1), random.randint(0, self.cols - 1)))
        for r, c in mine_positions:
            self.board[r][c] = '*'
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == '*':
                    continue
                count = sum(
                    (nr, nc) in mine_positions
                    for nr in range(r - 1, r + 2)
                    for nc in range(c - 1, c + 2)
                    if 0 <= nr < self.rows and 0 <= nc < self.cols and (nr, nc) != (r, c)
                )
                self.board[r][c] = str(count) if count > 0 else ' '
    def reveal_cell(self, row, col):
        if (row, col) in self.flags or self.visible[row][col] != '#':
            return True  # Ignore already revealed or flagged cells
        if self.board[row][col] == '*':
            self.visible[row][col] = '*'
            return False
        self._reveal_recursive(row, col)
        return True
    def _reveal_recursive(self, row, col):
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            return
        if self.visible[row][col] != '#' or (row, col) in self.flags:
            return
        self.visible[row][col] = self.board[row][col]
        if self.board[row][col] == ' ':
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr != 0 or dc != 0:
                        self._reveal_recursive(row + dr, col + dc)
    def flag_cell(self, row, col):
        if self.visible[row][col] != '#':
            return
        if (row, col) in self.flags:
            self.flags.remove((row, col))
            self.visible[row][col] = '#'
        else:
            self.flags.add((row, col))
            self.visible[row][col] = 'F'
    def check_win(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.visible[r][c] == '#' and self.board[r][c] != '*':
                    return False
        return True
    def display_board(self):
        print("\nCurrent Board:")
        print("    " + " ".join(f"{c:2}" for c in range(self.cols)))
        print("   +" + "--" * self.cols + "+")
        for idx, row in enumerate(self.visible):
            print(f"{idx:2} | " + " ".join(f"{cell:2}" for cell in row) + " |")
        print("   +" + "--" * self.cols + "+\n")