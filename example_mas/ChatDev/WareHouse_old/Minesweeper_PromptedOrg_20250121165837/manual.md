# Minesweeper Game User Manual

Welcome to the Minesweeper Game, a classic puzzle game where your goal is to uncover all cells that do not contain mines. This manual will guide you through the installation, setup, and gameplay of the Minesweeper Game.

## Introduction

The Minesweeper Game is a single-player puzzle game implemented in Python. The game consists of a 9x9 grid with 10 hidden mines. The player uncovers cells by specifying the row and column. Numbers on uncovered cells indicate how many mines are adjacent. If a mine is uncovered, the player loses. The game displays the board with updated markings after each move.

## Main Functions

- **Initialize Game**: Set up a 9x9 grid with 10 hidden mines randomly placed.
- **Uncover Cell**: Uncover a cell by specifying its row and column. If the cell contains a mine, the game ends.
- **Display Board**: Show the current state of the board with uncovered cells and hidden cells marked.
- **Check Win**: Determine if the player has won by uncovering all non-mine cells.

## Installation

### Prerequisites

- Python 3.x installed on your system.
- Basic understanding of running Python scripts from the command line.

### Quick Install

1. **Clone the Repository**: Download the game code from the repository or copy the provided code into your local directory.

2. **Navigate to the Game Directory**: Open your terminal or command prompt and navigate to the directory containing the game files.

3. **Run the Game**: Execute the following command to start the game:
   ```bash
   python main.py
   ```

## How to Play

1. **Start the Game**: Run the `main.py` script to start the game. The initial board will be displayed with all cells covered.

2. **Uncover Cells**: Enter the row and column numbers to uncover a cell. For example, to uncover the cell at row 0, column 1, input:
   ```
   0 1
   ```

3. **Game Feedback**: After each move, the board will update to show uncovered cells. If you uncover a mine, the game will end with a "Mine hit! Game over." message.

4. **Winning the Game**: Uncover all cells that do not contain mines to win the game. A congratulatory message will be displayed upon winning.

5. **Restarting the Game**: To play again, simply rerun the `main.py` script.

## Troubleshooting

- **Invalid Input**: Ensure that you enter valid row and column numbers within the range of 0 to 8.
- **Game Over**: If you hit a mine, the game will end. Restart the game to try again.

## Conclusion

Enjoy playing the classic Minesweeper Game! Challenge yourself to uncover all non-mine cells and achieve victory. If you encounter any issues or have questions, feel free to reach out for support.

Happy gaming!