# Tic-Tac-Toe Game User Manual

Welcome to the Tic-Tac-Toe Game! This user manual will guide you through the installation process, introduce the main features of the game, and provide instructions on how to play.

## Introduction

The Tic-Tac-Toe Game is a classic two-player game implemented in Python using the Tkinter library for a graphical user interface (GUI). Players take turns marking spaces in a 3x3 grid, aiming to be the first to get three of their marks in a row, column, or diagonal.

## Main Features

- **User-Friendly Interface**: The game features a simple and intuitive interface, making it easy for players of all ages to enjoy.
- **Two-Player Mode**: Allows two players to take turns playing on the same device.
- **Winner Determination**: Automatically checks for a winner after each move and displays the result.
- **Game Reset**: Easily restart the game after a win or draw.

## Installation

### Prerequisites

- Python 3.6 or higher must be installed on your system.
- Tkinter library is required for the GUI. It is usually included with Python installations, but you may need to install it separately on some systems.

### Steps to Install

1. **Clone the Repository**: Download or clone the repository containing the game code to your local machine.

2. **Install Python**: Ensure you have Python 3.6 or higher installed. You can download it from [Python's official website](https://www.python.org/downloads/).

3. **Install Dependencies**: Although there are no external Python packages required beyond Tkinter, ensure your environment is set up correctly. You can create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. **Run the Game**: Navigate to the directory where `main.py` is located and execute the following command to start the game:

   ```bash
   python main.py
   ```

## How to Play

1. **Start the Game**: Run the `main.py` script to launch the game window.

2. **Gameplay**:
   - The game board consists of a 3x3 grid.
   - Player X starts the game, followed by Player O.
   - Click on an empty space in the grid to place your mark (X or O).
   - The game automatically switches turns between the two players.

3. **Winning the Game**:
   - A player wins by placing three of their marks in a horizontal, vertical, or diagonal row.
   - The game will display a message announcing the winner.

4. **Draw**:
   - If all spaces are filled without a winner, the game ends in a draw, and a message will be displayed.

5. **Restarting the Game**:
   - After a win or draw, the game can be restarted by clicking "OK" on the message box. The board will reset, and Player X will start the new game.

## Troubleshooting

- **GUI Issues**: If you encounter issues starting the GUI, ensure you are running the game on a system with a graphical display. The game may not work in environments without GUI support, such as some remote servers.

## Conclusion

Enjoy playing the Tic-Tac-Toe Game! If you have any questions or encounter any issues, please feel free to reach out for support. Happy gaming!