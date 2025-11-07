'''
Main entry point for the Password Strength Checker tool.
This script can be run as a CLI tool or a GUI tool.
'''
import sys
from password_evaluator import PasswordEvaluator
from password_strength_cli import PasswordStrengthCLI
from password_strength_gui import PasswordStrengthGUI
def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--gui':
        # Run as GUI tool
        gui_tool = PasswordStrengthGUI()
        gui_tool.run()
    elif len(sys.argv) > 1 and sys.argv[1] == '--password':
        # Run as CLI tool with password argument
        password = sys.argv[2]
        cli_tool = PasswordStrengthCLI()
        cli_tool.evaluate_password(password)
    else:
        # Run as CLI tool by default
        cli_tool = PasswordStrengthCLI()
        cli_tool.run()
if __name__ == "__main__":
    main()