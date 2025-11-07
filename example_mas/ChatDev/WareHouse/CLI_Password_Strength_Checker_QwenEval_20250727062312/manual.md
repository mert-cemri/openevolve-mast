# Password Strength Checker Tool

## Introduction

The Password Strength Checker Tool is a command-line interface (CLI) application designed to evaluate the strength of a given password. It checks various criteria such as length, use of uppercase and lowercase letters, numbers, and special characters, providing a strength score or rating.

## Quick Install

To install the Password Strength Checker Tool, you need to have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Install the required dependencies by running the following command:

```bash
pip install -r requirements.txt
```

*Note: Currently, the `requirements.txt` file is empty, as there are no third-party dependencies. However, it's a good practice to maintain this file for future growth.*

## Main Functions

### CLI Tool

The CLI tool allows you to evaluate the strength of a password directly from the command line.

#### Usage

To run the CLI tool, use the following command:

```bash
python main.py --password <your_password>
```

Replace `<your_password>` with the password you want to evaluate.

*Example:*

```bash
python main.py --password MySecureP@ssw0rd!
```

If you run the tool without the `--password` argument, it will prompt you to enter a password:

```bash
python main.py
```

### GUI Tool

The GUI tool provides a graphical user interface for evaluating password strength.

#### Usage

To run the GUI tool, use the following command:

```bash
python main.py --gui
```

A window will appear, allowing you to enter a password and check its strength.

## How to Use/Play

### CLI Tool

1. Open your terminal or command prompt.
2. Navigate to the project directory.
3. Run the CLI tool with the `--password` argument followed by the password you want to evaluate, or run it without arguments to be prompted for a password.
4. The tool will display the password strength score and provide feedback.

### GUI Tool

1. Open your terminal or command prompt.
2. Navigate to the project directory.
3. Run the GUI tool using the `--gui` argument.
4. A window will appear, allowing you to enter a password.
5. Click the "Check Strength" button to evaluate the password.
6. The tool will display the password strength score and provide feedback.

## Feedback and Scoring

The tool evaluates the password based on the following criteria:

- Length (minimum 8 characters)
- Use of uppercase letters
- Use of lowercase letters
- Use of numbers
- Use of special characters
- Absence of common patterns (e.g., "123", "abc", "password")

The password strength score ranges from 0 to 5, with 5 being the strongest. The tool provides feedback based on the score:

- **5:** Your password is very strong! It meets all the criteria.
- **4:** Your password is strong. Consider adding a special character or a number.
- **3:** Your password is moderate. Consider adding more complexity.
- **2:** Your password is weak. Please make it stronger by adding uppercase letters, numbers, and special characters.
- **1 or 0:** Your password is very weak. Please make it stronger by adding uppercase letters, numbers, and special characters.

## Conclusion

The Password Strength Checker Tool is a simple yet powerful application for evaluating password strength. Whether you prefer using the command line or a graphical interface, this tool provides valuable feedback to help you create strong, secure passwords.

If you encounter any issues or have suggestions for improvement, please feel free to contact us. Happy coding!

---

This manual should provide a comprehensive guide for users to understand and use the Password Strength Checker Tool effectively.