'''
This module implements a classic Hangman game. The game selects a random word from a predefined list,
and the user attempts to guess the word by suggesting letters within a limited number of attempts.
'''
import random
class HangmanGame:
    def __init__(self, word_list, max_attempts=6):
        '''
        Initialize the Hangman game with a random word from the word list and set up the initial game state.
        :param word_list: List of words to choose from.
        :param max_attempts: Maximum number of incorrect attempts allowed.
        '''
        self.word_to_guess = random.choice(word_list).lower()
        self.max_attempts = max_attempts
        self.attempts_remaining = max_attempts
        self.correct_guesses = set()
        self.incorrect_guesses = set()
    def guess_letter(self, letter):
        '''
        Process a letter guessed by the user, updating the game state.
        :param letter: The letter guessed by the user.
        :return: A message indicating the result of the guess.
        '''
        letter = letter.lower()
        if letter in self.correct_guesses or letter in self.incorrect_guesses:
            return f"You've already guessed the letter '{letter}'."
        if letter in self.word_to_guess:
            self.correct_guesses.add(letter)
            return f"Good guess! The letter '{letter}' is in the word."
        else:
            self.incorrect_guesses.add(letter)
            self.attempts_remaining -= 1
            return f"Sorry, the letter '{letter}' is not in the word. Attempts remaining: {self.attempts_remaining}"
    def is_game_over(self):
        '''
        Check if the game is over (either won or lost).
        :return: True if the game is over, False otherwise.
        '''
        return self.attempts_remaining <= 0 or self.is_word_guessed()
    def is_word_guessed(self):
        '''
        Check if the entire word has been guessed.
        :return: True if the word is fully guessed, False otherwise.
        '''
        return all(letter in self.correct_guesses for letter in self.word_to_guess)
    def display_current_state(self):
        '''
        Show the current state of the word with placeholders for unguessed letters.
        :return: A string representing the current state of the word.
        '''
        return ' '.join(letter if letter in self.correct_guesses else '_' for letter in self.word_to_guess)
    def display_result(self):
        '''
        Display the final result of the game (win/lose).
        :return: A message indicating whether the player won or lost.
        '''
        if self.is_word_guessed():
            return f"Congratulations! You've guessed the word '{self.word_to_guess}'!"
        else:
            return f"Game over! The word was '{self.word_to_guess}'. Better luck next time!"
def main():
    '''
    Run the Hangman game loop, handling user input and coordinating with the HangmanGame class.
    '''
    word_list = ["python", "hangman", "challenge", "programming", "developer"]
    game = HangmanGame(word_list)
    print("Welcome to Hangman!")
    while not game.is_game_over():
        print("\nCurrent word:", game.display_current_state())
        guess = input("Guess a letter: ").strip()
        if len(guess) == 1 and guess.isalpha():
            print(game.guess_letter(guess))
        else:
            print("Please enter a single alphabetical character.")
    print("\n" + game.display_result())
if __name__ == "__main__":
    main()