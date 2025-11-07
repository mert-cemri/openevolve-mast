'''
Evaluates the strength of a given password.
'''
import re
class PasswordStrengthChecker:
    '''
    Evaluates the strength of a given password.
    '''
    def evaluate_password_strength(self, password):
        '''
        Evaluates the password and returns a strength score and rating.
        '''
        score = 0
        # Check for minimum length of 8 characters
        if len(password) >= 8:
            score += 1
        # Check for at least one uppercase letter
        if re.search(r"[A-Z]", password):
            score += 1
        # Check for at least one lowercase letter
        if re.search(r"[a-z]", password):
            score += 1
        # Check for at least one digit
        if re.search(r"[0-9]", password):
            score += 1
        # Check for at least one special character
        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            score += 1
        # Determine the rating based on the score
        if score == 5:
            rating = "Very Strong"
        elif score == 4:
            rating = "Strong"
        elif score == 3:
            rating = "Moderate"
        elif score == 2:
            rating = "Weak"
        else:
            rating = "Very Weak"
        return score, rating