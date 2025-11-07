# Minesweeper Game User Manual

Welcome to the Minesweeper Game! This classic game challenges you to uncover all the cells on a 9x9 grid without hitting any of the 10 hidden mines. Use your logic and deduction skills to navigate the board and win the game.

## Main Functions

The Minesweeper game includes the following main functions:

- **Initialize Game Board**: The game initializes a 9x9 grid with 10 hidden mines placed randomly.
- **Uncover Cells**: Players can uncover cells by specifying the row and column. If a mine is uncovered, the player loses.
- **Display Board**: The game displays the current state of the board after each move, showing uncovered cells and marking mines if the game is over.
- **Win/Lose Conditions**: The game ends when all non-mine cells are uncovered (win) or a mine is uncovered (lose).

## Installation

### Environment Setup

This Minesweeper game is implemented in Python and does not require any external dependencies. Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Quick Install

1. **Clone the Repository**: Download the Minesweeper game code to your local machine.
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Change your working directory to the location of the downloaded code.
   ```bash
   cd <project-directory>
   ```

3. **Run the Game**: Execute the `main.py` file to start playing the game.
   ```bash
   python main.py
   ```

## How to Play

1. **Start the Game**: Run the `main.py` file to start the game. The game will display an empty 9x9 grid with hidden mines.

2. **Make a Move**: Enter the row and column numbers to uncover a cell. For example, to uncover the cell at row 0, column 1, input:
   ```
   0 1
   ```

3. **Game Feedback**: After each move, the game will display the updated board. Numbers indicate how many mines are adjacent to the uncovered cell. If you uncover a mine, the game will display all mines and end with a "Game Over" message.

4. **Winning the Game**: Uncover all non-mine cells to win. The game will congratulate you and reveal all mines.

5. **Invalid Moves**: If you attempt to uncover an already uncovered cell or input invalid coordinates, the game will prompt you to try again.

## Additional Information

- **No External Dependencies**: This project does not require any additional Python packages beyond the standard library.
- **Replayability**: You can play the game multiple times by re-running the `main.py` file.

Enjoy playing Minesweeper and test your strategic thinking and problem-solving skills! If you have any questions or need further assistance, feel free to reach out to our support team.