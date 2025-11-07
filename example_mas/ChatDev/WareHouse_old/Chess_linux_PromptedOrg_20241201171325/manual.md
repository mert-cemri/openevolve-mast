# Chess Game User Manual

Welcome to the Chess Game application, a terminal-based chess game designed for two players. This manual will guide you through the installation process, introduce the main features of the software, and provide instructions on how to play the game.

## Overview

This Chess Game allows two players to take turns playing chess using formal chess notation. The game is designed to run in a Linux Terminal, providing a simple and straightforward interface without the need for a graphical user interface (GUI).

## Features

- **Two-Player Mode**: Play chess with another player, taking turns to make moves.
- **Chess Notation Input**: Enter moves using standard chess notation (e.g., `e2e4`).
- **Move Validation**: The game checks for valid moves according to chess rules.
- **Turn-Based Play**: Automatically switches turns between players.
- **Winner Determination**: The game checks for checkmate conditions to determine the winner.

## Installation

### Prerequisites

- **Python**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Quick Install

1. **Clone the Repository**: Download the source code from the repository.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: There are no external dependencies required for this project. The game is built using standard Python libraries.

   ```bash
   # No additional installation steps required
   ```

## How to Play

1. **Start the Game**: Run the `main.py` file to start the game.

   ```bash
   python main.py
   ```

2. **Game Interface**: The chessboard will be displayed in the terminal. Each player will be prompted to enter their move.

3. **Enter Moves**: Use standard chess notation to enter your moves. For example, to move a piece from e2 to e4, type `e2e4`.

4. **Turn-Based Play**: After each valid move, the turn will switch to the other player. The game will continue until a checkmate is detected.

5. **Invalid Moves**: If an invalid move is entered, you will be prompted to try again.

6. **Winning the Game**: The game will announce the winner when a checkmate is achieved.

## Documentation

For further details on the implementation and to explore the code, please refer to the source files included in the repository:

- `main.py`: Main entry point for the game.
- `chessboard.py`: Manages the chessboard and piece movements.
- `piece.py`: Defines the behavior of each chess piece.
- `game.py`: Controls the game flow and turn management.
- `utils.py`: Contains utility functions for move parsing and checkmate detection.

Enjoy your game of chess! If you encounter any issues or have questions, please refer to the source code for further insights into the game's mechanics.