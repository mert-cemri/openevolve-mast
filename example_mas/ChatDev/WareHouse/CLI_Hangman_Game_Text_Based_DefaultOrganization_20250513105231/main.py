'''
Main application file for the CLI Hangman game.
'''
from game_logic import HangmanGame
def main():
    game = HangmanGame()
    print("Welcome to Hangman!")
    while not game.is_won() and not game.is_lost():
        print("\nCurrent word: " + game.get_display_word())
        print("Incorrect guesses: " + ", ".join(game.incorrect_guesses))
        guess = input("Enter a letter to guess: ").strip().lower()
        if len(guess) == 1 and guess.isalpha():
            game.guess_letter(guess)
        else:
            print("Please enter a valid single letter.")
        if game.is_won():
            print("\nCongratulations! You've won!")
            print("The word was: " + game.word)
        elif game.is_lost():
            print("\nGame Over! The word was: " + game.word)
if __name__ == "__main__":
    main()