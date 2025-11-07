'''
Main entry point for the 2048 game. Handles user input, game loop, and rendering.
'''
from game2048 import Game2048
def print_grid(grid, score, highest_tile):
    print("\nScore:", score, "\tHighest Tile:", highest_tile)
    print("-" * 25)
    for row in grid:
        print("|", end="")
        for num in row:
            if num == 0:
                print("    .", end="|")
            else:
                print(f"{num:5}", end="|")
        print("\n" + "-" * 25)
def main():
    game = Game2048()
    print("Welcome to 2048! Use W/A/S/D keys to move tiles. Press Q to quit.")
    print_grid(game.grid, game.get_score(), game.get_highest_tile())
    while not game.is_game_over():
        move = input("Move (W/A/S/D): ").lower()
        if move == 'q':
            print("Game exited.")
            break
        direction = None
        if move == 'w':
            direction = 'up'
        elif move == 'a':
            direction = 'left'
        elif move == 's':
            direction = 'down'
        elif move == 'd':
            direction = 'right'
        else:
            print("Invalid input. Please use W/A/S/D keys.")
            continue
        if game.move(direction):
            print_grid(game.grid, game.get_score(), game.get_highest_tile())
        else:
            print("Move not possible. Try a different direction.")
    if game.is_game_over():
        print("Game Over! Final Score:", game.get_score(), "Highest Tile:", game.get_highest_tile())
if __name__ == "__main__":
    main()