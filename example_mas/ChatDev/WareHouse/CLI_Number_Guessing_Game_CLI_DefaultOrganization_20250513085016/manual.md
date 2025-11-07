```markdown
# CLI Number Guessing Game

Welcome to the CLI Number Guessing Game! This is a simple command-line interface game where you try to guess a randomly generated number. The game will provide hints to help you guess the correct number.

## Main Functions

- **Random Number Generation**: The game generates a random number between 1 and 100 at the start of each game session.
- **User Interaction**: You will be prompted to guess the number. After each guess, the game will provide feedback:
  - "Higher!" if your guess is too low.
  - "Lower!" if your guess is too high.
  - "Congratulations! You've guessed it!" when you guess the correct number.
- **Error Handling**: If you enter an invalid input (non-integer), the game will prompt you to enter a valid number.

## Installation

To play the CLI Number Guessing Game, you need to have Python installed on your system. The game requires Python version 3.6 or higher.

### Step 1: Install Python

If you haven't already, download and install Python from the [official website](https://www.python.org/downloads/).

### Step 2: Set Up the Environment

1. **Clone the Repository**: Download or clone the game files to your local machine.

2. **Navigate to the Game Directory**: Open your terminal or command prompt and navigate to the directory where the game files are located.

3. **Install Dependencies**: Although this game does not require any external libraries beyond Python's standard library, it's good practice to ensure your environment is set up correctly. You can create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. **Install Required Python Version**: Ensure you have the correct Python version by checking your current version:

   ```bash
   python --version
   ```

   If necessary, update your Python version to 3.6 or higher.

## How to Play

1. **Start the Game**: Run the game by executing the `main.py` file in your terminal:

   ```bash
   python main.py
   ```

2. **Make a Guess**: Follow the on-screen instructions to enter your guess.

3. **Receive Feedback**: The game will inform you if your guess is too high, too low, or correct.

4. **Continue Guessing**: Keep guessing until you find the correct number.

5. **Win the Game**: Once you guess the correct number, the game will congratulate you, and you can choose to play again by restarting the game.

Enjoy the challenge and have fun guessing!

```