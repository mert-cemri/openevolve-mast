# Connect Four Game User Manual

Welcome to the Connect Four Game! This manual will guide you through the installation, setup, and usage of the Connect Four game application developed using Python and Tkinter.

## Introduction

Connect Four is a two-player connection game in which the players first choose a color and then take turns dropping colored discs into a seven-column, six-row grid. The pieces fall straight down, occupying the lowest available space within the column. The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of four of one's own discs.

## Main Functions

- **Game Logic**: The game logic is implemented to handle player turns, check for a win or draw condition, and manage the game board state.
- **Graphical User Interface (GUI)**: The GUI is built using Tkinter, providing an interactive and user-friendly interface for players to play the game.

## Installation

### Environment Setup

The Connect Four game requires Python to be installed on your system. It uses the Tkinter library, which is included in the standard Python distribution. No additional packages are required.

1. **Install Python**: Ensure that Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Verify Tkinter Installation**: Tkinter is included with Python, but you can verify its installation by running the following command in your Python environment:

   ```bash
   python -m tkinter
   ```

   If a small window appears, Tkinter is installed correctly.

### Running the Game

1. **Clone the Repository**: Download or clone the repository containing the game code to your local machine.

2. **Navigate to the Project Directory**: Open a terminal or command prompt and navigate to the directory where the game files are located.

3. **Run the Game**: Execute the following command to start the game:

   ```bash
   python main.py
   ```

## How to Play

1. **Start the Game**: Launch the game by running `main.py`. A window titled "Connect Four" will appear.

2. **Game Interface**: The interface consists of a grid representing the game board and buttons at the top for each column.

3. **Make a Move**: Players take turns clicking the "Drop" button corresponding to the column where they want to drop their disc. The discs will fall to the lowest available position in the selected column.

4. **Winning the Game**: The game checks for a win condition after each move. A player wins by forming a line of four discs horizontally, vertically, or diagonally.

5. **Draw Condition**: If the board is filled and no player has won, the game ends in a draw.

6. **Game Over**: When a player wins or the game ends in a draw, a message box will display the result. The game can be restarted by closing and reopening the application.

## Support

For any issues or questions regarding the Connect Four game, please contact our support team at support@chatdev.com.

Enjoy playing Connect Four!