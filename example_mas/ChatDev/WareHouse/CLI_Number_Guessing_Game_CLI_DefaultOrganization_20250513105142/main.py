'''
This module contains the main application logic for a number guessing game using a Command Line Interface (CLI).
'''
import random
def start_game():
    '''
    Start a new game by generating a random number and prompting the user to guess.
    '''
    random_number = random.randint(1, 100)
    print("Guess the number between 1 and 100")
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if guess < random_number:
                print("Higher!")
            elif guess > random_number:
                print("Lower!")
            else:
                print("Correct! You guessed it!")
                break
        except ValueError:
            print("Please enter a valid number.")
def main():
    '''
    The entry point of the application to start the CLI game.
    '''
    start_game()
if __name__ == "__main__":
    main()