# Connect Four Game User Manual

Welcome to the Connect Four Game! This manual will guide you through the installation, setup, and usage of the Connect Four game application developed using Python and Tkinter.

## Introduction

Connect Four is a classic two-player connection game in which the players first choose a color and then take turns dropping colored discs into a seven-column, six-row grid. The pieces fall straight down, occupying the lowest available space within the column. The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of four of one's own discs.

## Main Functions

- **Game Initialization**: Start a new game with a clean board and set the first player.
- **Player Interaction**: Players alternate turns by selecting a column to drop their disc.
- **Win Detection**: Automatically checks for a win condition after each move.
- **Draw Detection**: Detects if the board is full without any player winning, resulting in a draw.
- **Graphical User Interface**: Provides an intuitive interface for players to interact with the game.
- **Restart Game**: Option to restart the game after a win or draw.

## Installation

### Environment Setup

This application does not require any external dependencies beyond the standard Python library. Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Running the Game

1. **Clone the Repository**: Download the game files to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Game**: Execute the main script to start the game.
   ```bash
   python main.py
   ```

## How to Play

1. **Start the Game**: Launch the game by running the `main.py` script. A window will open displaying the Connect Four board.

2. **Select a Column**: Players take turns clicking on the buttons at the top of each column to drop their disc. The first player uses red discs ('R'), and the second player uses yellow discs ('Y').

3. **Winning the Game**: The game automatically checks for a win after each move. A player wins by forming a line of four discs horizontally, vertically, or diagonally.

4. **Draw Condition**: If the board is filled without any player winning, the game declares a draw.

5. **Restarting the Game**: After a win or draw, a "Restart Game" button will appear. Click it to reset the board and start a new game.

## Additional Information

- **User Interface**: The game uses Tkinter for the graphical interface, providing a simple and interactive experience.
- **Game Logic**: The game logic is encapsulated in the `ConnectFourGame` class, handling moves, win checks, and game resets.

Enjoy playing Connect Four! If you encounter any issues or have suggestions for improvements, please feel free to reach out to our support team.