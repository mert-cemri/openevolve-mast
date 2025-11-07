'''
Main file to run the 2048 game with a 10x10 grid.
'''
from game import Game
def main():
    game = Game()
    game.reset()
    while not game.is_game_over():
        print(game)
        move = input("Enter move (w/a/s/d): ").strip().lower()
        if move in ['w', 'a', 's', 'd']:
            game.move(move)
            if game.is_won():
                print("Congratulations! You've reached 2048!")
                break
        else:
            print("Invalid move. Please enter w, a, s, or d.")
    else:
        print("Game Over!")
if __name__ == "__main__":
    main()