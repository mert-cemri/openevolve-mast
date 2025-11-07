```markdown
# Minesweeper Game

Welcome to the classic Minesweeper game! This application allows you to enjoy the timeless puzzle game where you uncover cells on a grid, avoiding hidden mines, and using numbers to deduce the locations of the mines.

## Main Functions

- **Grid Setup**: The game features a 9x9 grid with 10 hidden mines randomly placed.
- **Cell Uncovering**: Players can uncover cells by clicking on them. If a mine is uncovered, the game is over.
- **Adjacent Mines Indicator**: Numbers on uncovered cells indicate how many mines are adjacent to that cell.
- **Win Condition**: Uncover all non-mine cells to win the game.
- **Graphical User Interface**: The game is presented with a simple GUI using Tkinter, allowing for easy interaction.

## Installation

### Environment Setup

This project does not require any external dependencies beyond Python's standard library. Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Running the Game

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Project Directory**: Open a terminal or command prompt and navigate to the directory where the project files are located.

3. **Run the Game**: Execute the following command to start the game:
   ```bash
   python main.py
   ```

## How to Play

1. **Start the Game**: Launch the game by running `main.py`. A window will open displaying the Minesweeper grid.

2. **Uncover Cells**: Click on any cell to uncover it. If the cell contains a mine, the game will end, and a message will inform you that you hit a mine.

3. **Use Numbers to Deduce**: Numbers on uncovered cells indicate the number of mines in the adjacent cells. Use these clues to avoid mines.

4. **Win the Game**: Successfully uncover all cells that do not contain mines to win the game. A congratulatory message will appear upon winning.

5. **Game Over**: If you uncover a mine, the game will end, and you will be notified with a "Game Over" message.

## Troubleshooting

- **Tkinter Errors**: If you encounter errors related to Tkinter, ensure you are running the game in an environment that supports GUI applications. Tkinter is included with standard Python installations, but some environments may not support GUI operations.

- **Display Issues**: Ensure your system supports graphical displays. This game requires a display to render the GUI.

Enjoy playing Minesweeper and challenge yourself to clear the board without hitting a mine!
```