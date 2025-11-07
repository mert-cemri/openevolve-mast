'''
This file contains the UserInterface class which handles user input and output.
'''
class UserInterface:
    def get_user_input(self):
        guess = input("Enter your guess (four words separated by spaces): ")
        return guess.split()
    def display_message(self, message):
        print(message)