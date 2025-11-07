# Sudoku Solver/Creator Application

Welcome to the Sudoku Solver/Creator Application! This software allows you to create, solve, and play classic Sudoku puzzles using a 9x9 grid. Each row, column, and 3x3 subgrid must contain the digits 1 through 9 exactly once. The application provides functionalities to input values, check for mistakes, and confirm when the puzzle is completed.

## Main Features

- **Sudoku Puzzle Creation**: Generate a new Sudoku puzzle with varying levels of difficulty.
- **Sudoku Puzzle Solving**: Automatically solve any given Sudoku puzzle.
- **Interactive Gameplay**: Input values into the Sudoku grid, check for mistakes, and receive feedback on puzzle completion.

## Quick Install

To get started with the Sudoku Solver/Creator Application, you need to have Python installed on your system. Follow these steps to set up the environment and run the application:

1. **Clone the Repository**: Download the source code from the repository.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Ensure you have Python installed (version 3.6 or higher is recommended). Install any required dependencies using pip.

   ```bash
   pip install -r requirements.txt
   ```

   Note: If there is no `requirements.txt` file, it means there are no additional dependencies beyond standard Python libraries.

3. **Run the Application**: Execute the main module to start the application.

   ```bash
   python main.py
   ```

## How to Use/Play

1. **Starting the Game**: Upon running the application, you will be greeted with a welcome message and the initial Sudoku board will be displayed.

2. **Inputting Values**: You can input values into the Sudoku grid by specifying the row, column, and the number you wish to place. The input format is as follows:

   - Enter row (0-8): [Row number]
   - Enter column (0-8): [Column number]
   - Enter number (1-9): [Number to place]

3. **Checking for Mistakes**: The application will automatically check for mistakes after each input. If there are any mistakes, their positions will be displayed.

4. **Completing the Puzzle**: Continue to fill in the grid until it is complete. The application will notify you if the puzzle is completed correctly or if there are any remaining mistakes.

5. **Solving the Puzzle**: If you wish to solve the puzzle automatically, you can modify the code to call the `solve()` method from the `SudokuSolver` class.

## Documentation

For more detailed information on the classes and methods used in this application, please refer to the source code files:

- `sudoku_board.py`: Defines the `SudokuBoard` class to represent the Sudoku board.
- `sudoku_solver.py`: Defines the `SudokuSolver` class to solve the Sudoku puzzle.
- `sudoku_game.py`: Defines the `SudokuGame` class to manage the game flow.
- `sudoku_creator.py`: Defines the `SudokuCreator` class to generate a new Sudoku puzzle.

Feel free to explore and modify the code to enhance the functionality or adapt it to your needs. Enjoy solving and creating Sudoku puzzles!