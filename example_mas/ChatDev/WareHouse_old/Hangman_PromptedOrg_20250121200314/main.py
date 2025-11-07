'''
This is the main file for the Hangman game. It initializes the game and handles user interaction.
'''
import random
from hangman_game import HangmanGame
def main():
    word_list = ["python", "hangman", "challenge", "programming", "developer"]
    max_attempts = 6
    game = HangmanGame(word_list, max_attempts)
    print("Welcome to Hangman!")
    while not game.is_game_over():
        print("\nCurrent word:", game.display_word())
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue
        result = game.guess_letter(guess)
        if result is None:
            print("You've already guessed that letter.")
            continue  # Skip decrementing attempts if the letter was already guessed
        elif result:
            print("Good guess!")
        else:
            print("Incorrect guess.")
        print(f"Attempts remaining: {game.max_attempts - game.incorrect_guesses}")
    if game.is_word_guessed():
        print(f"Congratulations! You've guessed the word: {game.selected_word}")
    else:
        print(f"Game over! The word was: {game.selected_word}")
if __name__ == "__main__":
    main()