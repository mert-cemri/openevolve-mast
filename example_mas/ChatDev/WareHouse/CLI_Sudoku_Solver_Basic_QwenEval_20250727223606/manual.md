# Sudoku Solver CLI User Manual

## Introduction

Welcome to the Sudoku Solver CLI! This application is designed to solve 9x9 Sudoku puzzles using a backtracking algorithm. You can input a partially filled Sudoku grid either from a file or directly via the command line, and the application will output the solved grid.

## Main Functions

### Input Handling

- **File Input:** You can provide a text file containing the Sudoku grid. Each row of the grid should be on a new line, with numbers separated by spaces. Use `0` to represent empty cells.
- **Direct Input:** You can enter the Sudoku grid row by row directly in the command line. Again, use `0` to represent empty cells.

### Sudoku Solver

- The core functionality of the application is the `SudokuSolver` class, which implements a backtracking algorithm to solve the puzzle. The algorithm tries to fill the grid by placing numbers 1-9 in empty cells and backtracks when it encounters a conflict.

### Output Handling

- Once the puzzle is solved, the `OutputHandler` class prints the solved grid to the console.

## Installation

### Prerequisites

- Python 3.6 or higher must be installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installing the Application

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-repo/sudoku-solver-cli.git
   cd sudoku-solver-cli
   ```

2. **Install Dependencies:**

   This application does not require any external dependencies. You can verify this by checking the `requirements.txt` file, which should be empty.

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

1. **Using File Input:**

   - Create a text file containing your Sudoku grid. For example, `sudoku.txt`:

     ```
     5 3 0 0 7 0 0 0 0
     6 0 0 1 9 5 0 0 0
     0 9 8 0 0 0 0 6 0
     8 0 0 0 6 0 0 0 3
     4 0 0 8 0 3 0 0 1
     7 0 0 0 2 0 0 0 6
     0 6 0 0 0 0 2 8 0
     0 0 0 4 1 9 0 0 5
     0 0 0 0 8 0 0 7 9
     ```

   - Run the application with the file as an argument:

     ```bash
     python main.py sudoku.txt
     ```

2. **Using Direct Input:**

   - Run the application with the keyword `direct`:

     ```bash
     python main.py direct
     ```

   - Follow the prompts to enter each row of the Sudoku grid:

     ```
     Enter the Sudoku grid row by row, using 0 for empty cells. Separate numbers with spaces.
     Row 1: 5 3 0 0 7 0 0 0 0
     Row 2: 6 0 0 1 9 5 0 0 0
     Row 3: 0 9 8 0 0 0 0 6 0
     Row 4: 8 0 0 0 6 0 0 0 3
     Row 5: 4 0 0 8 0 3 0 0 1
     Row 6: 7 0 0 0 2 0 0 0 6
     Row 7: 0 6 0 0 0 0 2 8 0
     Row 8: 0 0 0 4 1 9 0 0 5
     Row 9: 0 0 0 0 8 0 0 7 9
     ```

### Example Output

After running the application with a valid input, you should see the solved Sudoku grid printed to the console:

```
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```

## Troubleshooting

- **Invalid Input:** If you provide an invalid input (e.g., incorrect number of numbers in a row, non-integer values), the application will print an error message and prompt you to enter the row again.
- **No Solution:** If the provided Sudoku grid has no solution, the application will print "No solution exists."

## Conclusion

Thank you for using the Sudoku Solver CLI! We hope you find it useful for solving your Sudoku puzzles. If you encounter any issues or have suggestions for improvement, please feel free to reach out to us.

---

This manual should cover everything a user needs to know to install, use, and troubleshoot the Sudoku Solver CLI application.