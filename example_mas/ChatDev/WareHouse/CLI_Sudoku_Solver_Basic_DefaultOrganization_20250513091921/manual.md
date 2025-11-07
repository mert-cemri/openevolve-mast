# Sudoku Solver CLI Application

Welcome to the Sudoku Solver CLI Application! This application allows you to solve any partially filled 9x9 Sudoku grid using a backtracking algorithm. This user manual will guide you through the main functions of the software, how to install it, and how to use it.

## Main Functions

The Sudoku Solver CLI Application provides the following main functions:

- **Input a Sudoku Grid**: Enter a partially filled 9x9 Sudoku grid directly into the command line interface. Use '0' to represent empty cells.
- **Solve the Sudoku**: The application uses a backtracking algorithm to solve the Sudoku puzzle.
- **Output the Solved Grid**: Once solved, the application will print the completed Sudoku grid to the console.

## Installation

### Prerequisites

- **Python 3.x**: Ensure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Quick Install

1. **Clone the Repository**: First, clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```
   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory**: Change your directory to the project folder:
   ```bash
   cd <project-directory>
   ```
   Replace `<project-directory>` with the name of the cloned directory.

3. **Install Dependencies**: There are no external dependencies required for this project. However, ensure your Python environment is set up correctly.

## How to Use

1. **Run the Application**: Execute the main script to start the application:
   ```bash
   python main.py
   ```

2. **Input the Sudoku Grid**: When prompted, enter the Sudoku grid row by row. Use spaces to separate numbers and '0' for empty cells. Each row should contain exactly 9 numbers.

   Example input:
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

3. **View the Solved Sudoku**: After entering the grid, the application will process the input and display the solved Sudoku grid. If no solution exists, it will notify you accordingly.

## Troubleshooting

- **Invalid Input**: Ensure each row contains exactly 9 numbers. Use '0' for empty cells.
- **No Solution Exists**: If the application states that no solution exists, verify the input grid for any inconsistencies or errors.

## Support

For further assistance, please contact our support team or visit our documentation page.

Thank you for using the Sudoku Solver CLI Application! Enjoy solving your puzzles.