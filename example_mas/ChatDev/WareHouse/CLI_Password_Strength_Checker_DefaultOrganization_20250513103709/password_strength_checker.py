'''
This module contains the PasswordStrengthChecker class, which evaluates the strength of a given password.
'''
import re
class PasswordStrengthChecker:
    def evaluate_password_strength(self, password: str) -> str:
        length_criteria = len(password) >= 8
        lowercase_criteria = re.search(r'[a-z]', password) is not None
        uppercase_criteria = re.search(r'[A-Z]', password) is not None
        number_criteria = re.search(r'[0-9]', password) is not None
        special_criteria = re.search(r'[\W_]', password) is not None
        score = sum([length_criteria, lowercase_criteria, uppercase_criteria, number_criteria, special_criteria])
        if score == 5:
            return "Very Strong"
        elif score == 4:
            return "Strong"
        elif score == 3:
            return "Moderate"
        elif score == 2:
            return "Weak"
        else:
            return "Very Weak"