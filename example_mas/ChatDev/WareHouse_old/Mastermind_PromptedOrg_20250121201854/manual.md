# Mastermind Game

Welcome to the Mastermind Game, a classic code-breaking game where the computer selects a hidden sequence of digits, and the player attempts to guess it within a set number of tries. After each guess, feedback is provided regarding the correct digits in the correct position and the correct digits in the wrong position.

## Quick Install

The Mastermind Game is implemented in Python and does not require any external dependencies. Ensure you have Python 3.x installed on your system.

## Installation

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

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

3. **Run the Game:**

   Execute the following command to start the game:

   ```bash
   python main.py
   ```

## How to Play

1. **Start the Game:**

   Run the `main.py` script to start the game. You will be greeted with a welcome message.

2. **Game Objective:**

   The objective of the game is to guess the hidden sequence of digits selected by the computer. You have a limited number of attempts to crack the code.

3. **Making a Guess:**

   - Enter your guess when prompted. The guess should be a sequence of digits with the same length as the hidden code.
   - Type 'exit' to quit the game at any time.

4. **Feedback:**

   After each guess, you will receive feedback in the form of:
   - **Correct Position:** Number of digits that are correct and in the correct position.
   - **Correct Color:** Number of digits that are correct but in the wrong position.

5. **Winning the Game:**

   If you guess the correct sequence within the allowed attempts, you win the game and receive a congratulatory message.

6. **Game Over:**

   If you fail to guess the correct sequence within the allowed attempts, the game ends, and the correct code is revealed.

## Example

```
Welcome to Mastermind!
Type 'exit' to quit the game at any time.
Enter your guess (4 digits): 1234
Feedback: 1 correct position(s), 2 correct color(s)
Enter your guess (4 digits): 5678
Feedback: 0 correct position(s), 1 correct color(s)
Enter your guess (4 digits): 4321
Congratulations! You've cracked the code!
```

Enjoy playing the Mastermind Game and challenge yourself to crack the code!