# Number Guessing Game CLI

Welcome to the Number Guessing Game CLI! This application is a simple yet engaging way to test your guessing skills against a randomly generated number. The game is designed to be user-friendly and runs directly from the command line interface (CLI).

## 🤔 What is this?

The Number Guessing Game CLI is a Python-based application that challenges users to guess a randomly generated number within a specified range. The game provides feedback on whether the guess is too high or too low, guiding the user towards the correct answer. Users can play multiple rounds until they decide to quit.

## 📦 Installation

To install the Number Guessing Game CLI, you need to have Python installed on your system. The application does not require any additional dependencies beyond the standard Python library.

### Step-by-Step Installation

1. **Ensure Python is Installed:**
   - Download and install Python from the [official website](https://www.python.org/downloads/).
   - Verify the installation by running `python --version` in your command line interface.

2. **Clone the Repository:**
   - Open your command line interface and navigate to the directory where you want to store the game.
   - Clone the repository using the following command:
     ```bash
     git clone https://github.com/ChatDev/number-guessing-game.git
     ```
   - Navigate into the cloned directory:
     ```bash
     cd number-guessing-game
     ```

3. **Run the Game:**
   - Execute the game by running the following command:
     ```bash
     python main.py
     ```

## 🎲 How to Play

The Number Guessing Game CLI is straightforward to play. Follow these steps to start guessing:

1. **Launch the Game:**
   - Run the game using the command `python main.py`.
   - You will see a welcome message and instructions on how to play.

2. **Guess the Number:**
   - The game will generate a random number within a specified range (default is 1 to 100).
   - You will be prompted to enter your guess.
   - The game will provide feedback on whether your guess is too high, too low, or correct.

3. **Play Multiple Rounds:**
   - After each round, you will be asked if you want to play again.
   - Enter `yes` to continue playing or `no` to quit the game.

## 🛠️ Customization

The Number Guessing Game CLI allows for customization of the game parameters, such as the range of numbers and the maximum number of attempts. You can modify these settings by editing the `NumberGuessingGame` class in the `game.py` file.

### Example Customization

To change the range of numbers to 1 to 50 and the maximum number of attempts to 7, modify the `NumberGuessingGame` class as follows:

```python
class NumberGuessingGame:
    def __init__(self, lower_bound=1, upper_bound=50, max_attempts=7):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.secret_number = generate_random_number(lower_bound, upper_bound)
        self.attempts = 0
        self.max_attempts = max_attempts
```

## 📖 Documentation

For more detailed information on the game mechanics, code structure, and customization options, please refer to the following resources:

- **Code Structure:**
  - `main.py`: Main entry point for the game.
  - `game.py`: Contains the game logic and mechanics.
  - `utils.py`: Utility functions for generating random numbers and obtaining user input.

- **Customization:**
  - Modify the `NumberGuessingGame` class in `game.py` to change game parameters.
  - Edit the `get_user_guess` and `generate_random_number` functions in `utils.py` for advanced customization.

## 🙋‍♂️ Support

If you encounter any issues or have suggestions for improvement, please feel free to reach out to our support team. You can also contribute to the project by submitting pull requests or reporting issues on the [GitHub repository](https://github.com/ChatDev/number-guessing-game).

Enjoy playing the Number Guessing Game CLI and happy coding!

---

This manual provides a comprehensive overview of the Number Guessing Game CLI, including installation instructions, gameplay instructions, customization options, and documentation resources.