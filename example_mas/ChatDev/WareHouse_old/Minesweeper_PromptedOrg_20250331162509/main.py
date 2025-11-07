'''
This is the main file for the Minesweeper game. It initializes the game, handles user input, and updates the game state.
'''
from game import Game
def main():
    print("Welcome to Minesweeper!")
    valid_difficulties = ["beginner", "intermediate", "expert"]
    difficulty = input("Choose difficulty (beginner, intermediate, expert): ").strip().lower()
    while difficulty not in valid_difficulties:
        print("Invalid difficulty. Please choose from 'beginner', 'intermediate', or 'expert'.")
        difficulty = input("Choose difficulty (beginner, intermediate, expert): ").strip().lower()
    game = Game(difficulty)
    while not game.is_over():
        game.display_board()
        action = input("Enter action (uncover x y / flag x y): ").strip().lower()
        parts = action.split()
        if len(parts) != 3:
            print("Invalid input. Please enter a valid action.")
            continue
        command = parts[0]
        try:
            x, y = int(parts[1]), int(parts[2])
        except ValueError:
            print("Invalid coordinates. Please enter integer values for x and y.")
            continue
        if command == "uncover":
            game.uncover_cell(x, y)
        elif command == "flag":
            game.flag_cell(x, y)
        else:
            print("Invalid command. Use 'uncover' or 'flag'.")
    if game.is_won():
        print("Congratulations! You've won the game!")
    else:
        print("Game over! You hit a mine.")
    game.display_board()
if __name__ == "__main__":
    main()