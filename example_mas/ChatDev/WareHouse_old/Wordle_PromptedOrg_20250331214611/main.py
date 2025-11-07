'''
Main entry point for the Wordle game. Handles user interaction and game loop.
'''
from wordle import WordleGame
from words import WORD_LIST
def main():
    game = WordleGame(WORD_LIST)
    attempts = 6
    print("Welcome to Terminal Wordle!")
    print("You have 6 attempts to guess the 5-letter word.\n")
    for attempt in range(1, attempts + 1):
        while True:
            guess = input(f"Attempt {attempt}/6: ").lower()
            if game.validate_guess(guess):
                break
            else:
                print("Invalid guess. Please enter a valid 5-letter English word.")
        feedback = game.get_feedback(guess)
        print(feedback)
        if game.is_correct_guess(guess):
            print(f"\033[92mCongratulations! You guessed the word '{game.target_word.upper()}' correctly!\033[0m")
            return
    print(f"\033[91mSorry, you've used all attempts. The word was '{game.target_word.upper()}'.\033[0m")
if __name__ == "__main__":
    main()