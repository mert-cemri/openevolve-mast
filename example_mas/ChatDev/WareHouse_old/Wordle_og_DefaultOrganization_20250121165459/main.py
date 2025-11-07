'''
This module contains the main entry point for the Wordle game. It initializes the game and starts the game loop.
'''
import random
class WordleGame:
    def __init__(self):
        '''
        Initializes the WordleGame with a daily word and sets the maximum number of attempts.
        '''
        self.daily_word = self.get_daily_word()
        self.max_attempts = 6
        self.attempts = 0
    def get_daily_word(self):
        '''
        Selects a random word from a predefined list of words to be the daily word.
        '''
        word_list = ['apple', 'grape', 'peach', 'berry', 'melon']
        return random.choice(word_list)
    def process_guess(self, guess):
        '''
        Processes the player's guess and provides feedback on each letter's correctness.
        Parameters:
        guess (str): The player's guessed word.
        Returns:
        list: A list of feedback strings ('green', 'yellow', 'grey') for each letter.
        '''
        feedback = ['grey'] * 5
        word_letters = list(self.daily_word)
        # First pass: check for correct letters in correct positions
        for i in range(5):
            if guess[i] == self.daily_word[i]:
                feedback[i] = 'green'
                word_letters[i] = None  # Mark this letter as used
        # Second pass: check for correct letters in wrong positions
        for i in range(5):
            if feedback[i] == 'grey' and guess[i] in word_letters:
                feedback[i] = 'yellow'
                word_letters[word_letters.index(guess[i])] = None  # Mark this letter as used
        return feedback
    def play(self):
        '''
        Starts the game loop, allowing the player to make guesses and receive feedback.
        '''
        print("Welcome to Wordle!")
        print("Guess the 5-letter word. You have 6 attempts.")
        while self.attempts < self.max_attempts:
            guess = input(f"Attempt {self.attempts + 1}: ").strip().lower()
            if len(guess) != 5:
                print("Please enter a 5-letter word.")
                continue
            self.attempts += 1
            feedback = self.process_guess(guess)
            print("Feedback:", feedback)
            if guess == self.daily_word:
                print("Congratulations! You've guessed the word!")
                return
        print(f"Sorry, you've used all attempts. The word was: {self.daily_word}")
def main():
    '''
    The main function to create and start a WordleGame instance.
    '''
    game = WordleGame()
    game.play()
if __name__ == "__main__":
    main()