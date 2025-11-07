# Sudoku Solver and Creator User Manual

Welcome to the Sudoku Solver and Creator application! This software allows you to create, solve, and play Sudoku puzzles using a 9x9 grid. Each row, column, and 3x3 subgrid must contain the digits 1 through 9 exactly once. This manual will guide you through the installation, main functions, and usage of the application.

## Quick Install

This application is built using Python and does not require any external dependencies. Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Installation Steps

1. **Clone the Repository:**
   - Open your terminal or command prompt.
   - Clone the repository using the following command:
     ```bash
     git clone <repository-url>
     ```
   - Navigate to the cloned directory:
     ```bash
     cd <repository-directory>
     ```

2. **Run the Application:**
   - Execute the main script to start the Sudoku game:
     ```bash
     python main.py
     ```

## Main Functions of the Software

The Sudoku Solver and Creator application consists of several key components:

1. **SudokuBoard Class:**
   - Represents the Sudoku board.
   - Provides methods to manipulate, validate, and generate the board.
   - Includes functions to check valid moves, place and remove numbers, and generate puzzles.

2. **SudokuSolver Class:**
   - Provides a method to solve a Sudoku puzzle using backtracking.
   - Ensures that the puzzle adheres to Sudoku rules.

3. **SudokuGame Class:**
   - Manages the game logic and allows player interaction.
   - Facilitates input of values, checks for completion, and provides feedback on moves.

4. **Main Module:**
   - Runs the Sudoku application.
   - Allows users to interact with the game through a command-line interface.

## How to Use/Play

1. **Starting the Game:**
   - Run the `main.py` script to start the game.
   - You will be greeted with a welcome message and instructions on how to enter your moves.

2. **Playing the Game:**
   - Enter your moves in the format: `row col num` (e.g., `0 0 5`).
   - The application will check if the move is valid and provide feedback.
   - Type `exit` to quit the game at any time.

3. **Completing the Puzzle:**
   - The game will notify you when the Sudoku puzzle is complete.
   - Celebrate your success and try another puzzle if you wish!

## Conclusion

Thank you for using the Sudoku Solver and Creator application. We hope you enjoy solving and creating Sudoku puzzles. If you encounter any issues or have suggestions for improvement, please feel free to reach out to our support team. Happy puzzling!