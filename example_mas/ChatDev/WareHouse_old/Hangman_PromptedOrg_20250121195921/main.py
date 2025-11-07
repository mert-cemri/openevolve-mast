'''
This is the main module to run the Hangman game. It handles user interaction and game loop.
'''
from hangman import HangmanGame
from utils import load_words
def main():
    '''
    Run the Hangman game loop, handle user input, and display results.
    '''
    word_list = load_words()
    game = HangmanGame(word_list)
    print("Welcome to Hangman!")
    while not game.is_game_over():
        game.display_current_state()
        guess = input("Guess a letter: ").lower()
        while not (len(guess) == 1 and guess.isalpha()):
            print("Please enter a single alphabetic character.")
            guess = input("Guess a letter: ").lower()
        if guess in game.correct_guesses or guess in game.incorrect_guesses:
            print("You've already guessed that letter. Try again.")
        else:
            game.guess_letter(guess)
    if game.is_word_guessed():
        print(f"Congratulations! You've guessed the word: {game.word_to_guess}")
    else:
        print(f"Game over! The word was: {game.word_to_guess}")
if __name__ == "__main__":
    main()