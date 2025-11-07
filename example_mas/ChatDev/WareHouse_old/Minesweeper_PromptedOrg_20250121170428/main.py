'''
This file contains the implementation of the Minesweeper game, including the Minesweeper class and the main game loop.
'''
import random
class Minesweeper:
    def __init__(self, size=9, mines=10):
        '''
        Initializes the Minesweeper game board with the specified size and number of mines.
        '''
        self.size = size
        self.mines = mines
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.mine_positions = set()
        self.uncovered = set()
        self.place_mines()
        self.calculate_adjacent_mines()
    def place_mines(self):
        '''
        Randomly places the specified number of mines on the board.
        '''
        while len(self.mine_positions) < self.mines:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            self.mine_positions.add((row, col))
    def calculate_adjacent_mines(self):
        '''
        Calculates the number of adjacent mines for each cell on the board.
        '''
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for row in range(self.size):
            for col in range(self.size):
                if (row, col) not in self.mine_positions:
                    count = 0
                    for dr, dc in directions:
                        r, c = row + dr, col + dc
                        if 0 <= r < self.size and 0 <= c < self.size and (r, c) in self.mine_positions:
                            count += 1
                    self.board[row][col] = str(count) if count > 0 else ' '
    def uncover_cell(self, row, col):
        '''
        Uncovers the cell at the specified row and column. If a mine is uncovered, the player loses.
        Recursively uncovers adjacent cells if the uncovered cell has no adjacent mines.
        '''
        if (row, col) in self.uncovered:
            return False
        self.uncovered.add((row, col))
        if (row, col) in self.mine_positions:
            return True
        if self.board[row][col] == ' ':
            directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < self.size and 0 <= c < self.size:
                    self.uncover_cell(r, c)
        return False
    def display_board(self, reveal_mines=False):
        '''
        Displays the current state of the board with updated markings after each move.
        If reveal_mines is True, all mines are displayed.
        '''
        print("  " + " ".join(str(i) for i in range(self.size)))
        for i, row in enumerate(self.board):
            print(f"{i} " + " ".join(
                ('M' if (i, j) in self.mine_positions else row[j]) if reveal_mines or (i, j) in self.uncovered else '.' 
                for j in range(self.size)
            ))
    def is_valid_move(self, row, col):
        '''
        Checks if the move specified by the player is valid.
        '''
        return 0 <= row < self.size and 0 <= col < self.size and (row, col) not in self.uncovered
def main():
    '''
    Main function to handle the game loop.
    '''
    game = Minesweeper()
    game_over = False
    while not game_over:
        game.display_board()
        user_input = input("Enter row and column to uncover (e.g., 0 1): ")
        try:
            row, col = map(int, user_input.split())
            if game.is_valid_move(row, col):
                if game.uncover_cell(row, col):
                    print("Game Over! You hit a mine.")
                    game.display_board(reveal_mines=True)
                    game_over = True
                else:
                    if len(game.uncovered) == game.size * game.size - game.mines:
                        print("Congratulations! You've won the game.")
                        game.display_board(reveal_mines=True)
                        game_over = True
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter exactly two numbers separated by a space.")
if __name__ == "__main__":
    main()