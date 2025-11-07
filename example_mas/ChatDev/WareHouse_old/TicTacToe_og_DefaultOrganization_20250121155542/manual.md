```markdown
# Tic-Tac-Toe Game

A classic Tic-Tac-Toe game application with a user-friendly interface, allowing two players to take turns and determining the winner.

## Overview

This application provides a simple and intuitive interface for playing Tic-Tac-Toe. It is designed for two players who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.

## Main Features

- **User-Friendly Interface**: The game uses a graphical user interface (GUI) built with Tkinter, making it easy to interact with.
- **Two-Player Mode**: Allows two players to play against each other.
- **Automatic Winner Detection**: The game automatically detects and announces the winner or a draw.
- **Reset Functionality**: After a game ends, the board can be reset to start a new game.

## Installation

### Prerequisites

Ensure you have Python 3.6 or higher installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

### Install Environment Dependencies

1. **Clone the Repository**: Download or clone the repository containing the game code to your local machine.

2. **Navigate to the Project Directory**: Open a terminal or command prompt and navigate to the directory where the game code is located.

3. **Install Required Packages**: Run the following command to install the necessary dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   This will ensure that you have the correct version of Python and any other necessary packages.

## How to Play

1. **Start the Game**: Run the `main.py` file to start the game. You can do this by executing the following command in your terminal or command prompt:

   ```bash
   python main.py
   ```

2. **Game Interface**: A window will open displaying a 3x3 grid. This is the game board.

3. **Take Turns**: Players take turns clicking on the empty squares to place their mark (either 'X' or 'O').

4. **Winning the Game**: The first player to align three of their marks in a row, column, or diagonal wins the game. A message box will appear announcing the winner.

5. **Draw**: If all squares are filled and no player has three marks in a row, the game is a draw. A message box will announce the draw.

6. **Reset the Game**: After a game ends, the board will automatically reset for a new game.

## Troubleshooting

- **GUI Initialization Error**: If you encounter a `tk.TclError`, ensure that your environment supports graphical display. This error typically occurs when running the script in a non-GUI environment.

## Support

For any issues or questions, please contact our support team at support@chatdev.com.

Enjoy playing Tic-Tac-Toe!
```
