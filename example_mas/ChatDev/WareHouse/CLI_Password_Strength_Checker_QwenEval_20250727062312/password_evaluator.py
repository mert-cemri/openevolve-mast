'''
This module contains the PasswordEvaluator class,
which evaluates the strength of a given password.
'''
import re
class PasswordEvaluator:
    def __init__(self):
        self.min_length = 8
        self.common_patterns = ['123', 'abc', 'password', 'qwerty', 'letmein', '123456', '12345678', 'password1', 'admin', 'welcome']
    def evaluate(self, password):
        '''
        Evaluates the strength of a given password based on several criteria.
        Returns a score between 0 and 5.
        '''
        score = 0
        if self.is_length_sufficient(password):
            score += 1
        if self.has_uppercase(password):
            score += 1
        if self.has_lowercase(password):
            score += 1
        if self.has_numbers(password):
            score += 1
        if self.has_special_characters(password):
            score += 1
        if self.has_no_common_patterns(password):
            score += 1
        return score
    def is_length_sufficient(self, password):
        '''
        Checks if the password meets the minimum length requirement.
        Returns True if the password is long enough, False otherwise.
        '''
        return len(password) >= self.min_length
    def has_uppercase(self, password):
        '''
        Checks if the password contains at least one uppercase letter.
        Returns True if it does, False otherwise.
        '''
        return any(char.isupper() for char in password)
    def has_lowercase(self, password):
        '''
        Checks if the password contains at least one lowercase letter.
        Returns True if it does, False otherwise.
        '''
        return any(char.islower() for char in password)
    def has_numbers(self, password):
        '''
        Checks if the password contains at least one digit.
        Returns True if it does, False otherwise.
        '''
        return any(char.isdigit() for char in password)
    def has_special_characters(self, password):
        '''
        Checks if the password contains at least one special character.
        Returns True if it does, False otherwise.
        '''
        return any(not char.isalnum() for char in password)
    def has_no_common_patterns(self, password):
        '''
        Checks if the password does not contain common patterns or sequences.
        Returns True if it does not, False otherwise.
        '''
        return not any(pattern in password.lower() for pattern in self.common_patterns)