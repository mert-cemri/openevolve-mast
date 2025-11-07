'''
This file contains the UserInterface class, which handles interactions with the user, such as displaying the game state and receiving user input.
'''
class UserInterface:
    def display_welcome_message(self):
        print("Welcome to the Puzzle Game! Group the words into their correct categories.")
    def get_user_guess(self):
        while True:
            guess = input("Enter four words separated by spaces: ").split()
            if len(guess) == 4:
                return guess
            else:
                print("Invalid input. Please enter exactly four words.")
    def display_correct_guess_message(self):
        print("Correct! You've found a valid group.")
    def display_incorrect_guess_message(self):
        print("Incorrect. Try again.")
    def display_end_message(self, solved):
        if solved:
            print("Congratulations! You've solved the puzzle.")
        else:
            print("Game over. Better luck next time!")