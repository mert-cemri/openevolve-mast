```markdown
# Minesweeper Game

Welcome to the classic Minesweeper game! This application allows you to play Minesweeper on a 9x9 grid with 10 hidden mines. The objective is to uncover all cells that do not contain mines. If you uncover a mine, you lose the game.

## Main Functions

- **Grid Setup**: The game initializes a 9x9 grid with 10 randomly placed mines.
- **Cell Uncovering**: Players can uncover cells by clicking on them. Numbers indicate how many mines are adjacent to the uncovered cell.
- **Game Over**: If a mine is uncovered, the game ends, and all mines are revealed.
- **Graphical User Interface (GUI)**: The game features a user-friendly GUI for easy interaction.

## Installation

### Environment Setup

Before running the Minesweeper game, ensure you have Python installed on your system. The minimum required version is Python 3.6.

1. **Clone the Repository**: Download the code to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Install the necessary dependencies using pip.
   ```bash
   pip install -r requirements.txt
   ```

### Running the Game

1. **Navigate to the Project Directory**: Ensure you are in the directory containing the `main.py` file.

2. **Start the Game**: Run the following command to start the Minesweeper game.
   ```bash
   python main.py
   ```

## How to Play

1. **Launch the Game**: After running `main.py`, a window will open displaying the Minesweeper grid.

2. **Uncover Cells**: Click on any cell to uncover it. If the cell contains a number, it indicates how many mines are adjacent to that cell.

3. **Avoid Mines**: The goal is to uncover all cells that do not contain mines. If you click on a mine, the game will end, and a message will inform you of the loss.

4. **Game Over**: If you uncover a mine, all mines will be revealed, and the game will display a "Game Over" message.

5. **Restart**: To play again, simply close the window and rerun the `main.py` script.

## Troubleshooting

- **GUI Errors**: If you encounter errors related to the GUI, ensure that your system supports Tkinter and that a display environment is available.

- **Python Version**: Ensure you are using Python 3.6 or higher.

Enjoy playing Minesweeper and challenge yourself to clear the board without hitting a mine!
```
