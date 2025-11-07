# Password Strength Checker CLI Tool

Welcome to the Password Strength Checker CLI Tool! This tool is designed to help you evaluate the strength of a given password based on several criteria, including length, use of uppercase and lowercase letters, numbers, and special characters. This user manual will guide you through the installation and usage of the tool.

## Quick Install

This tool is built using Python and does not require any external dependencies. Ensure you have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

## Installation

1. **Clone the Repository:**

   First, clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory:**

   Change your directory to the project folder:

   ```bash
   cd <project-directory>
   ```

   Replace `<project-directory>` with the name of the cloned directory.

3. **Install Python (if not already installed):**

   Ensure Python is installed on your system. You can check if Python is installed by running:

   ```bash
   python --version
   ```

   If Python is not installed, download and install it from the [official website](https://www.python.org/downloads/).

## Usage

### Command Line Interface (CLI)

1. **Run the CLI Tool:**

   To check the strength of a password using the CLI tool, run the following command:

   ```bash
   python main.py <password>
   ```

   Replace `<password>` with the password you want to evaluate.

2. **Output:**

   The tool will output the strength of the password as one of the following ratings: "Very Weak", "Weak", "Moderate", "Strong", or "Very Strong".

### Graphical User Interface (GUI)

1. **Run the GUI Tool:**

   If you prefer a graphical interface, you can use the GUI version of the tool. Run the following command:

   ```bash
   python password_strength_gui.py
   ```

2. **Using the GUI:**

   - Enter your password in the provided input field.
   - Click on the "Check Strength" button.
   - The strength of the password will be displayed below the button.

## Main Functions

- **Password Evaluation:** The tool evaluates passwords based on length, presence of lowercase and uppercase letters, numbers, and special characters.
- **Strength Rating:** Provides a clear rating of the password strength, helping users to improve their password security.

## Documentation

For more detailed information about the tool's implementation, refer to the source code files:

- `main.py`: Initializes the CLI application.
- `password_strength_checker.py`: Contains the logic for evaluating password strength.
- `password_strength_gui.py`: Provides a Tkinter-based GUI for password strength checking.

## Support

If you encounter any issues or have questions, please contact our support team or refer to the source code for further insights.

Thank you for using the Password Strength Checker CLI Tool!