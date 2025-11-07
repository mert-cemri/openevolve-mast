'''
Board class to represent the 8x8 grid and manage disc placement and flipping.
'''
class Board:
    def __init__(self):
        '''
        Initialize the board with the starting position.
        '''
        self.grid = [[' ' for _ in range(8)] for _ in range(8)]
        self.grid[3][3], self.grid[4][4] = 'W', 'W'
        self.grid[3][4], self.grid[4][3] = 'B', 'B'
    def display(self):
        '''
        Display the current state of the board.
        '''
        print("  0 1 2 3 4 5 6 7")
        for i, row in enumerate(self.grid):
            print(f"{i} " + " ".join(row))
    def is_full(self):
        '''
        Check if the board is full.
        '''
        return all(cell != ' ' for row in self.grid for cell in row)
    def has_valid_moves(self, color):
        '''
        Check if there are any valid moves for the given color.
        '''
        for x in range(8):
            for y in range(8):
                if self.is_valid_move((x, y), color):
                    return True
        return False
    def is_valid_move(self, position, color):
        '''
        Check if a move is valid for the given color.
        '''
        x, y = position
        if self.grid[x][y] != ' ':
            return False
        opponent_color = 'B' if color == 'W' else 'W'
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8 and self.grid[nx][ny] == opponent_color:
                while 0 <= nx < 8 and 0 <= ny < 8:
                    nx += dx
                    ny += dy
                    if not (0 <= nx < 8 and 0 <= ny < 8):
                        break
                    if self.grid[nx][ny] == ' ':
                        break
                    if self.grid[nx][ny] == color:
                        return True
        return False
    def place_disc(self, position, color):
        '''
        Place a disc on the board and flip opponent discs.
        '''
        x, y = position
        self.grid[x][y] = color
        self.flip_discs(position, color)
    def flip_discs(self, position, color):
        '''
        Flip opponent discs after a valid move.
        '''
        x, y = position
        opponent_color = 'B' if color == 'W' else 'W'
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            discs_to_flip = []
            while 0 <= nx < 8 and 0 <= ny < 8 and self.grid[nx][ny] == opponent_color:
                discs_to_flip.append((nx, ny))
                nx += dx
                ny += dy
            if 0 <= nx < 8 and 0 <= ny < 8 and self.grid[nx][ny] == color:
                for fx, fy in discs_to_flip:
                    self.grid[fx][fy] = color
    def get_scores(self):
        '''
        Get the current scores for both players.
        '''
        black_score = sum(row.count('B') for row in self.grid)
        white_score = sum(row.count('W') for row in self.grid)
        return black_score, white_score