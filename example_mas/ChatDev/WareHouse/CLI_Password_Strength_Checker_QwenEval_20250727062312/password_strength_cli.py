'''
This module contains the PasswordStrengthCLI class,
which provides a command-line interface for the Password Strength Checker tool.
'''
import sys
from password_evaluator import PasswordEvaluator
class PasswordStrengthCLI:
    def __init__(self):
        self.evaluator = PasswordEvaluator()
    def run(self):
        '''
        Main method to run the CLI tool.
        Prompts the user to enter a password and displays the strength score.
        '''
        password = self.get_password()
        self.evaluate_password(password)
    def get_password(self):
        '''
        Prompts the user to enter a password.
        Returns the entered password as a string.
        '''
        return input("Enter a password to evaluate: ")
    def evaluate_password(self, password):
        '''
        Evaluates the password and displays the strength score.
        '''
        score = self.evaluator.evaluate(password)
        self.display_strength(score)
    def display_strength(self, score):
        '''
        Displays the password strength score to the user.
        '''
        feedback = self.get_feedback(score)
        print(f"Password strength score: {score}/5")
        print(feedback)
    def get_feedback(self, score):
        '''
        Provides feedback based on the password strength score.
        '''
        if score == 5:
            return "Your password is very strong! It meets all the criteria."
        elif score == 4:
            return "Your password is strong. Consider adding a special character or a number."
        elif score == 3:
            return "Your password is moderate. Consider adding more complexity."
        elif score == 2:
            return "Your password is weak. Please make it stronger by adding uppercase letters, numbers, and special characters."
        else:
            return "Your password is very weak. Please make it stronger by adding uppercase letters, numbers, and special characters."