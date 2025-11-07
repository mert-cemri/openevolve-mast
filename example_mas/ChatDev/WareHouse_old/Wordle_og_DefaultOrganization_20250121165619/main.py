'''
This script implements a terminal-based Wordle game. The player has six attempts to guess a five-letter word. Feedback is provided for each guess: green for correct letters in the correct position, yellow for correct letters in the wrong position, and grey for incorrect letters.
'''
import random
class WordleGame:
    def __init__(self, word):
        '''
        Initialize the game with a word to guess and set up the number of attempts.
        '''
        self.word = word
        self.attempts = 6
    def check_guess(self, guess):
        '''
        Compare the player's guess to the word and return feedback.
        '''
        feedback = ['grey'] * 5
        word_list = list(self.word)
        guess_list = list(guess)
        # First pass: check for correct letters in the correct position
        for i in range(5):
            if guess_list[i] == word_list[i]:
                feedback[i] = 'green'
                word_list[i] = None  # Remove matched letter
        # Second pass: check for correct letters in the wrong position
        for i in range(5):
            if feedback[i] == 'grey' and guess_list[i] in word_list:
                feedback[i] = 'yellow'
                word_list[word_list.index(guess_list[i])] = None  # Remove matched letter
        return feedback
    def play(self):
        '''
        Main loop to handle user input and game progression.
        '''
        print("Welcome to Wordle!")
        print("You have 6 attempts to guess the 5-letter word.")
        for attempt in range(self.attempts):
            guess = input(f"Attempt {attempt + 1}: ").strip().lower()
            if len(guess) != 5:
                print("Please enter a 5-letter word.")
                continue
            feedback = self.check_guess(guess)
            print("Feedback:", feedback)
            if feedback == ['green'] * 5:
                print("Congratulations! You've guessed the word!")
                return
        print(f"Sorry, you've used all attempts. The word was: {self.word}")
def get_random_word():
    '''
    Select a random 5-letter word from a predefined list.
    '''
    words = ["apple", "grape", "peach", "berry", "melon"]
    return random.choice(words)
def main():
    '''
    Start the game and handle user interaction.
    '''
    word = get_random_word()
    game = WordleGame(word)
    game.play()
if __name__ == "__main__":
    main()