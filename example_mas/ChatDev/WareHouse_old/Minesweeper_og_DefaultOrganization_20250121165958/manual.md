```markdown
# Minesweeper Game

A classic Minesweeper game implemented in Python using the tkinter library for the graphical user interface (GUI). This game provides a 9x9 grid with 10 hidden mines. The objective is to uncover all cells that do not contain mines.

## Main Functions

- **Grid Setup**: The game initializes a 9x9 grid with 10 randomly placed mines. Each cell can either be a mine or a number indicating how many mines are adjacent to it.
- **Cell Uncovering**: Players can uncover cells by clicking on them. If a mine is uncovered, the game is over. If a number is uncovered, it indicates the count of adjacent mines.
- **Flagging**: Players can right-click to place or remove a flag on a cell to mark it as suspected to contain a mine.
- **Win Condition**: The player wins by uncovering all cells that do not contain mines.
- **Game Over**: If a mine is uncovered, the game ends and all mines are revealed.

## Installation

### Environment Setup

This game does not require any external dependencies beyond Python's standard library. Ensure you have Python installed on your system.

1. **Python Installation**: If you do not have Python installed, download and install it from [python.org](https://www.python.org/downloads/).

### Running the Game

1. **Clone or Download the Repository**: Obtain the source code by cloning the repository or downloading it as a ZIP file and extracting it.

2. **Navigate to the Project Directory**: Open a terminal or command prompt and navigate to the directory containing the `main.py` file.

3. **Run the Game**: Execute the following command to start the game:
   ```bash
   python main.py
   ```

## How to Play

1. **Start the Game**: Launch the game by running the `main.py` script. A window will open displaying a 9x9 grid.

2. **Uncover Cells**: Click on a cell to uncover it. If the cell contains a mine, the game will end. If it contains a number, it will display the number of adjacent mines.

3. **Flag Mines**: Right-click on a cell to place a flag, marking it as a potential mine location. Right-click again to remove the flag.

4. **Winning the Game**: Uncover all non-mine cells to win the game. A message will appear congratulating you on your victory.

5. **Game Over**: If you uncover a mine, the game will reveal all mines and display a "Game Over" message.

Enjoy playing Minesweeper and challenge yourself to clear the board without hitting a mine!
```