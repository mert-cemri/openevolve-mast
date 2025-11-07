# Tic-Tac-Toe Game User Manual

Welcome to the Tic-Tac-Toe Game! This user-friendly application allows two players to take turns playing the classic game of Tic-Tac-Toe. Below, you'll find instructions on how to install the necessary environment dependencies, an introduction to the main functions of the software, and a guide on how to play the game.

## Quick Install

To get started with the Tic-Tac-Toe game, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/).

### Step 1: Install Python

Ensure that Python is installed on your system. You can verify this by running the following command in your terminal or command prompt:

```bash
python --version
```

If Python is not installed, download and install it from the official [Python website](https://www.python.org/downloads/).

### Step 2: Install Tkinter

Tkinter is a standard GUI toolkit in Python. It is usually included with Python, but if not, you can install it using the following command:

For Windows:

```bash
pip install tk
```

For macOS/Linux, Tkinter is typically included with Python, but if you encounter issues, you may need to install it via your package manager.

## Main Functions of the Software

The Tic-Tac-Toe game consists of three main components:

1. **Game Logic (`game.py`)**: Manages the game state, including the board, current player, and winner determination. It handles player moves and checks for win conditions or draws.

2. **Graphical User Interface (`gui.py`)**: Provides a user-friendly interface using Tkinter. It displays the game board, handles button clicks, and updates the game status.

3. **Main Application (`main.py`)**: Initializes and runs the Tic-Tac-Toe game by creating the game and GUI instances.

## How to Play

1. **Start the Game**: Run the `main.py` script to start the Tic-Tac-Toe game. You can do this by navigating to the directory containing the script and executing the following command:

   ```bash
   python main.py
   ```

2. **Game Interface**: The game window will open, displaying a 3x3 grid of buttons. The status label at the bottom indicates which player's turn it is.

3. **Make a Move**: Players take turns clicking on the buttons to place their mark ('X' or 'O') on the board. The game automatically switches turns between Player X and Player O.

4. **Determine the Winner**: The game checks for a winner after each move. If a player wins, a message will be displayed, and the game will disable further moves.

5. **Draw Condition**: If all spaces are filled and there is no winner, the game will declare a draw.

6. **Restart the Game**: To play again, you will need to close the current game window and restart the script.

Enjoy playing Tic-Tac-Toe with your friends! If you encounter any issues or have questions, please feel free to reach out for support.