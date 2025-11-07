# Minesweeper Game User Manual

Welcome to the Minesweeper Game! This classic game challenges you to uncover all non-mine cells on a 9x9 grid without hitting any of the 10 hidden mines. This manual will guide you through the installation process, introduce the main functions of the software, and provide instructions on how to play the game.

## Quick Install

To run the Minesweeper game, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Step-by-Step Installation

1. **Clone the Repository:**
   - Open your terminal or command prompt.
   - Clone the repository using the following command:
     ```
     git clone <repository-url>
     ```
   - Navigate to the cloned directory:
     ```
     cd <repository-directory>
     ```

2. **Install Dependencies:**
   - The Minesweeper game does not require any external Python packages beyond the standard library. Ensure your Python environment is set up correctly.

3. **Run the Game:**
   - Execute the following command to start the game:
     ```
     python main.py
     ```

## Main Functions of the Software

The Minesweeper game consists of several key components:

- **MinesweeperGame Class:** Manages the game logic and board state, including placing mines, calculating adjacent mines, uncovering cells, and checking win conditions.

- **Cell Class:** Represents each cell on the Minesweeper board, storing information about whether it contains a mine, if it is uncovered, and the number of adjacent mines.

- **Game Flow:** The game initializes a 9x9 grid with 10 hidden mines. Players uncover cells by specifying row and column numbers. The game displays the board with updated markings after each move.

## How to Play

1. **Start the Game:**
   - Run the game using the command `python main.py`.
   - You will be greeted with a welcome message and instructions on how to play.

2. **Uncover Cells:**
   - Enter the row and column numbers to uncover a cell (e.g., `0 0` for the top-left corner).
   - If you uncover a mine, the game is over, and you lose.
   - If you uncover a non-mine cell, the number of adjacent mines will be displayed.

3. **Winning the Game:**
   - Uncover all non-mine cells to win the game.
   - If you win, a congratulatory message will be displayed.

4. **Quit the Game:**
   - Type `q` at any time to quit the game.

## Additional Information

- **Game Board Display:**
  - The board is displayed with row and column indices for easy reference.
  - Uncovered cells show the number of adjacent mines or a `*` if it's a mine.
  - Covered cells are represented by a `.`.

- **Input Validation:**
  - The game checks for valid input and prompts you to enter correct values if necessary.

Enjoy playing Minesweeper and challenge yourself to uncover all the safe cells without hitting a mine! If you have any questions or need further assistance, please contact our support team.