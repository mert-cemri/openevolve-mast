'''
This file contains the implementation of a number guessing game with a CLI.
The game generates a random number, and the user tries to guess it, receiving hints (higher/lower) until they guess correctly.
'''
import random
def generate_random_number(start, end):
    '''
    Generate a random number between start and end.
    '''
    return random.randint(start, end)
def start_game():
    '''
    Start a new game by generating a random number and resetting the game state.
    '''
    random_number = generate_random_number(1, 100)
    print("Guess the number between 1 and 100")
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if guess < random_number:
                print("Higher!")
            elif guess > random_number:
                print("Lower!")
            else:
                print("Congratulations! You've guessed it!")
                break
        except ValueError:
            print("Please enter a valid number.")
if __name__ == "__main__":
    start_game()