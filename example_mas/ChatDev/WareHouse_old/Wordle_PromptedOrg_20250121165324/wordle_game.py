'''
This file contains the WordleGame class, which manages the game logic and feedback.
'''
class WordleGame:
    def __init__(self, daily_word):
        '''
        Initialize the Wordle game with the daily word.
        '''
        self.daily_word = daily_word
    def evaluate_guess(self, guess):
        '''
        Evaluate the player's guess and return feedback.
        '''
        feedback = ['grey'] * 5
        daily_word_count = {}
        guess_count = {}
        # First pass: Check for correct positions (green)
        for i, letter in enumerate(guess):
            if letter == self.daily_word[i]:
                feedback[i] = 'green'
            else:
                # Count letters for second pass
                daily_word_count[self.daily_word[i]] = daily_word_count.get(self.daily_word[i], 0) + 1
                guess_count[letter] = guess_count.get(letter, 0) + 1
        # Second pass: Check for correct letters in wrong positions (yellow)
        for i, letter in enumerate(guess):
            if feedback[i] == 'grey' and letter in daily_word_count and guess_count[letter] > 0:
                feedback[i] = 'yellow'
                guess_count[letter] -= 1
        is_correct = all(color == 'green' for color in feedback)
        return list(zip(feedback, guess)), is_correct
    def display_feedback(self, feedback):
        '''
        Display feedback to the player using colors.
        '''
        for color, letter in feedback:
            if color == 'green':
                print(f"\033[92m{letter}\033[0m", end=' ')
            elif color == 'yellow':
                print(f"\033[93m{letter}\033[0m", end=' ')
            else:
                print(f"\033[90m{letter}\033[0m", end=' ')
        print()