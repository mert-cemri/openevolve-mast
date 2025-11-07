'''
Main function to run the CLI for password strength checking.
'''
from password_checker import PasswordStrengthChecker
def main():
    '''
    Main function to run the CLI for password strength checking.
    '''
    checker = PasswordStrengthChecker()
    password = input("Enter Password: ")
    score, rating = checker.evaluate_password_strength(password)
    print(f"Strength: {rating} (Score: {score})")
if __name__ == "__main__":
    main()