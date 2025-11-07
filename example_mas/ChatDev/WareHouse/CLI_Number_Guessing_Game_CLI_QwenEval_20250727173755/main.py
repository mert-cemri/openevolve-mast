'''
Main entry point for the Number Guessing Game CLI application.
This script initializes and runs the game, allowing the user to play multiple rounds.
'''
from game import NumberGuessingGame
def main():
    print("Welcome to the Number Guessing Game CLI!")
    while True:
        game = NumberGuessingGame()
        game.play_game()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break
if __name__ == "__main__":
    main()