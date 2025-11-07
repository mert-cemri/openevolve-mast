'''
This script initializes and runs the Mastermind game, handling user input and displaying feedback.
'''
from game import Game
def main():
    print("Welcome to Mastermind!")
    print("Type 'exit' to quit the game at any time.")
    game = Game()
    guess = None
    while not game.is_game_over(guess):
        guess = input(f"Enter your guess ({game.code_length} digits): ")
        if guess.lower() == 'exit':
            print("Exiting the game. Goodbye!")
            break
        if len(guess) != game.code_length or not guess.isdigit():
            print(f"Invalid input. Please enter exactly {game.code_length} digits.")
            continue
        correct_position, correct_color = game.make_guess(guess)
        print(f"Feedback: {correct_position} correct position(s), {correct_color} correct color(s)")
        if correct_position == game.code_length:
            print("Congratulations! You've cracked the code!")
            break
    if game.is_game_over():
        print(f"Game over! The correct code was: {''.join(game.hidden_code)}")
if __name__ == "__main__":
    main()