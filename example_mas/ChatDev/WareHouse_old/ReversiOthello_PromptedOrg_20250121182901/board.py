'''
Board module to manage the Reversi game board.
'''
class Board:
    def __init__(self):
        # Initialize an 8x8 board with starting positions
        self.grid = [[' ' for _ in range(8)] for _ in range(8)]
        self.grid[3][3] = 'W'
        self.grid[3][4] = 'B'
        self.grid[4][3] = 'B'
        self.grid[4][4] = 'W'
    def display(self):
        # Display the board
        print("  0 1 2 3 4 5 6 7")
        for i, row in enumerate(self.grid):
            print(f"{i} " + " ".join(row))
    def place_disc(self, row, col, color):
        # Place a disc on the board
        self.grid[row][col] = color
    def get_valid_moves(self, color):
        # Get all valid moves for the current player
        valid_moves = []
        for row in range(8):
            for col in range(8):
                if self.grid[row][col] == ' ' and self.is_valid_move(row, col, color):
                    valid_moves.append((row, col))
        return valid_moves
    def is_valid_move(self, row, col, color):
        # Check if a move is valid
        if self.grid[row][col] != ' ':
            return False
        opponent_color = 'B' if color == 'W' else 'W'
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            has_opponent_disc = False
            while 0 <= r < 8 and 0 <= c < 8:
                if self.grid[r][c] == opponent_color:
                    has_opponent_disc = True
                elif self.grid[r][c] == color:
                    if has_opponent_disc:
                        return True
                    break
                else:
                    break
                r += dr
                c += dc
        return False
    def flip_discs(self, row, col, color):
        # Flip the opponent's discs after a valid move
        opponent_color = 'B' if color == 'W' else 'W'
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            discs_to_flip = []
            while 0 <= r < 8 and 0 <= c < 8 and self.grid[r][c] == opponent_color:
                discs_to_flip.append((r, c))
                r += dr
                c += dc
            if 0 <= r < 8 and 0 <= c < 8 and self.grid[r][c] == color:
                for rr, cc in discs_to_flip:
                    self.grid[rr][cc] = color