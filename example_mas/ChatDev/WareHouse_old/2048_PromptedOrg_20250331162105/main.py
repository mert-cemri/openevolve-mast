'''
This script initializes the game and handles user input for the 2048 game.
'''
from game import Game
def main():
    game = Game()
    game.display_grid()
    while not game.is_game_over():
        move = input("Enter move (w/a/s/d for up/left/down/right): ").strip().lower()
        if move in ['w', 'a', 's', 'd']:
            direction = {'w': 'up', 'a': 'left', 's': 'down', 'd': 'right'}[move]
            game.move(direction)
            game.display_grid()
        else:
            print("Invalid move. Please enter w, a, s, or d.")
    print("Game Over!")
    print(f"Final Score: {game.get_score()}, Highest Tile: {game.get_highest_tile()}")
if __name__ == "__main__":
    main()