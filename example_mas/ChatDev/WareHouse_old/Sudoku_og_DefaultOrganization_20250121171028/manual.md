# Sudoku Solver/Creator User Manual

Welcome to the Sudoku Solver/Creator application! This software allows you to create and solve classic 9x9 Sudoku puzzles. The application provides a user-friendly interface where you can input values, check for mistakes, and confirm when the puzzle is completed.

## Main Functions

1. **Sudoku Grid Creation**: 
   - The application initializes a 9x9 grid where you can input numbers from 1 to 9.
   
2. **Input Validation**:
   - The application checks the validity of the numbers you input, ensuring they are between 1 and 9.
   
3. **Puzzle Solving**:
   - The application uses a backtracking algorithm to solve the Sudoku puzzle, filling in the grid with a valid solution if one exists.
   
4. **Mistake Checking**:
   - The application checks the current state of the grid for mistakes, ensuring that each row, column, and 3x3 subgrid contains the digits 1 through 9 exactly once.
   
5. **Completion Confirmation**:
   - The application confirms when the puzzle is correctly completed.

## Installation

### Environment Setup

This application does not require any external dependencies beyond Python and the Tkinter library, which is included with most Python installations.

1. **Ensure Python is Installed**:
   - Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Verify Tkinter Installation**:
   - Tkinter is usually included with Python. You can verify its installation by running the following command in your Python environment:
     ```python
     import tkinter
     ```

3. **Download the Application Files**:
   - Download the provided Python files (`sudoku_grid.py`, `sudoku_solver.py`, `sudoku_gui.py`, `main.py`) to a directory on your computer.

## How to Use

1. **Launch the Application**:
   - Navigate to the directory where you saved the application files and run the following command in your terminal or command prompt:
     ```bash
     python main.py
     ```

2. **Input Values**:
   - Click on any cell in the grid and enter a number between 1 and 9. The application will validate your input and alert you if it is invalid.

3. **Solve the Puzzle**:
   - Once you have entered your desired numbers, click the "Solve" button. The application will attempt to solve the puzzle and fill in the remaining cells.

4. **Check Your Solution**:
   - If you have manually completed the puzzle, the application will automatically check your solution for correctness.

5. **Receive Feedback**:
   - The application will notify you if the puzzle is solved correctly or if there are any mistakes.

Enjoy solving and creating Sudoku puzzles with our application! If you encounter any issues or have questions, please feel free to reach out for support.