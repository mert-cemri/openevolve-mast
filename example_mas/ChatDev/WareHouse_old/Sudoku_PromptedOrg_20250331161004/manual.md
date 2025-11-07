# Sudoku Game User Manual

Welcome to the Sudoku Game! This user manual will guide you through the installation, setup, and gameplay of the classic Sudoku puzzle game developed in Python.

## Introduction

The Sudoku Game is a classic puzzle game that uses a 9x9 grid. The objective is to fill the grid so that each row, column, and 3x3 subgrid contains the digits 1 through 9 exactly once. This program allows players to input values for specific cells, check for mistakes, and confirm when the puzzle is completed.

## Quick Install

### Prerequisites

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory:**

   Change into the project directory:

   ```bash
   cd <project-directory>
   ```

   Replace `<project-directory>` with the name of the directory where the repository was cloned.

3. **Install Dependencies:**

   There are no external dependencies required for this project. However, ensure your Python environment is set up correctly.

## How to Play

1. **Run the Game:**

   Start the game by running the `main.py` file:

   ```bash
   python main.py
   ```

2. **Game Instructions:**

   - The game will display the Sudoku board with numbers and empty cells represented by dots (`.`).
   - You will be prompted to enter your move in the format: `row column number`.
   - Enter the row, column, and number separated by spaces. For example, to place the number 5 in the first row and first column, type: `1 1 5`.
   - The input numbers should be between 1 and 9.

3. **Game Rules:**

   - Each row, column, and 3x3 subgrid must contain the numbers 1 through 9 exactly once.
   - If you make an invalid move, the game will notify you, and you can try again.
   - Continue entering numbers until the puzzle is complete.

4. **Winning the Game:**

   - Once the board is completely and correctly filled, the game will congratulate you on completing the Sudoku puzzle.

## Troubleshooting

- **Invalid Input Format:** Ensure you enter exactly three numbers separated by spaces.
- **Invalid Move:** If the number cannot be placed in the specified cell, try a different number or cell.
- **Python Errors:** Ensure your Python environment is correctly set up and that you are running the game in the correct directory.

## Conclusion

Enjoy playing the classic Sudoku puzzle game! If you have any questions or encounter issues, please reach out to our support team for assistance. Happy puzzling!