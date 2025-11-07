'''
Main module to run the Gomoku game.
'''
from board import Board
from player import Player
from utils import get_input
class Game:
    def __init__(self, board_size=15):
        self.board = Board(board_size)
        self.players = [Player("Player 1", "X"), Player("Player 2", "O")]
        self.current_player_index = 0
    def play(self):
        while True:
            self.board.display()
            current_player = self.players[self.current_player_index]
            print(f"{current_player.name}'s turn ({current_player.stone}):")
            row, col = current_player.make_move(self.board)
            if self.board.place_stone(row, col, current_player.stone):
                if self.check_winner(row, col, current_player.stone):
                    self.board.display()
                    print(f"{current_player.name} wins!")
                    break
                self.current_player_index = 1 - self.current_player_index
            else:
                print("Invalid move. Try again.")
    def check_winner(self, row, col, stone):
        # Check horizontal, vertical, and two diagonal directions
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            for i in range(1, 5):
                r, c = row + dr * i, col + dc * i
                if self.board.is_within_bounds(r, c) and self.board.grid[r][c] == stone:
                    count += 1
                else:
                    break
            for i in range(1, 5):
                r, c = row - dr * i, col - dc * i
                if self.board.is_within_bounds(r, c) and self.board.grid[r][c] == stone:
                    count += 1
                else:
                    break
            if count >= 5:
                return True
        return False
if __name__ == "__main__":
    game = Game()
    game.play()