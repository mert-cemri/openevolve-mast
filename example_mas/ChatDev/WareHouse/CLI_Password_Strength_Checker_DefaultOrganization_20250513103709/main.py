'''
This is the main file that initializes the CLI application for checking password strength.
'''
import sys
from password_strength_checker import PasswordStrengthChecker
def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <password>")
        sys.exit(1)
    password = sys.argv[1]
    checker = PasswordStrengthChecker()
    strength = checker.evaluate_password_strength(password)
    print(f"Password Strength: {strength}")
if __name__ == "__main__":
    main()