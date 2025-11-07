'''
Main entry point for the chess game application.
'''
from chessboard import ChessBoard
from game import Game
def main():
    board = ChessBoard()
    game = Game(board)
    game.play()
if __name__ == "__main__":
    main()