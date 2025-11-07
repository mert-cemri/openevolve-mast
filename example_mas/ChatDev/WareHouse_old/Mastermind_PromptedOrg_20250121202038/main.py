'''
This is the main file for the Mastermind game. It initializes the game and manages the game loop.
'''
import random
from utilities import validate_guess
class Game:
    def __init__(self, code_length=4, max_attempts=10):
        '''
        Initializes the game with a hidden code and sets the number of attempts.
        '''
        self.code_length = code_length
        self.max_attempts = max_attempts
        self.hidden_code = self.generate_code()
        self.attempts = 0
    def generate_code(self):
        '''
        Generates a random sequence of colors as the hidden code.
        '''
        colors = 'RGBYOP'  # Red, Green, Blue, Yellow, Orange, Purple
        return [random.choice(colors) for _ in range(self.code_length)]
    def get_feedback(self, guess):
        '''
        Compares the player's guess to the hidden code and returns feedback.
        '''
        correct_position = sum(a == b for a, b in zip(guess, self.hidden_code))
        correct_color = sum(min(guess.count(x), self.hidden_code.count(x)) for x in set(guess)) - correct_position
        return correct_position, correct_color
    def get_user_input(self):
        '''
        Abstracts the input mechanism to allow for different input methods.
        '''
        return input(f"Attempt {self.attempts + 1}: ").upper()
    def play(self):
        '''
        Manages the game loop, taking user input and providing feedback until the game is won or attempts are exhausted.
        '''
        print("Welcome to Mastermind!")
        print(f"Try to guess the {self.code_length}-color code using the letters R, G, B, Y, O, P.")
        print(f"You have {self.max_attempts} attempts.")
        while self.attempts < self.max_attempts:
            try:
                guess = self.get_user_input()
                if not validate_guess(guess, self.code_length):
                    print(f"Invalid guess. Please enter a {self.code_length}-letter code using R, G, B, Y, O, P.")
                    continue
            except EOFError:
                print("Input error. Please try again.")
                continue
            except Exception as e:
                print(f"An unexpected error occurred: {e}. Please try again.")
                continue
            self.attempts += 1
            correct_position, correct_color = self.get_feedback(guess)
            if correct_position == self.code_length:
                print("Congratulations! You've cracked the code!")
                return
            print(f"Feedback: {correct_position} correct position(s), {correct_color} correct color(s).")
        print(f"Sorry, you've run out of attempts. The code was: {''.join(self.hidden_code)}")
if __name__ == "__main__":
    game = Game()
    game.play()