# Chess Game User Manual

Welcome to the Chess Game User Manual. This document will guide you through the installation, setup, and usage of our terminal-based chess game application.

## Overview

This chess game allows two players to play against each other in a terminal environment. The game is implemented in Python and supports standard chess rules. Players take turns entering moves using formal chess notation, and the game determines the winner based on checkmate or stalemate conditions.

## Features

- **Terminal-Based Gameplay**: Play chess directly from your Linux terminal without the need for a graphical user interface.
- **Standard Chess Rules**: The game follows standard chess rules, including piece movement, check, checkmate, and stalemate.
- **Interactive Play**: Players input moves using standard chess notation (e.g., `e2 e4`), and the game updates the board accordingly.
- **Turn-Based System**: The game alternates turns between two players, starting with white.

## Installation

### Prerequisites

- **Python 3.x**: Ensure that Python 3.x is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Quick Install

1. **Clone the Repository**: Clone the repository containing the chess game code to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Change into the directory where the code is located.

   ```bash
   cd <repository-directory>
   ```

3. **Install Dependencies**: There are no external dependencies required for this project, as indicated in the `requirements.txt` file.

   ```bash
   pip install -r requirements.txt
   ```

## How to Play

1. **Start the Game**: Run the `main.py` file to start the chess game.

   ```bash
   python main.py
   ```

2. **Game Interface**: The game will display the chessboard in the terminal. Each piece is represented by its initial letter (e.g., `P` for Pawn, `R` for Rook).

3. **Enter Moves**: Players take turns entering their moves in standard chess notation. For example, to move a pawn from e2 to e4, type:

   ```plaintext
   e2 e4
   ```

4. **Game Progression**: The game will update the board after each valid move. If a move is invalid, the game will prompt you to try again.

5. **Winning the Game**: The game ends when one player achieves checkmate or when a stalemate is reached. The game will announce the winner or declare a stalemate.

## Troubleshooting

- **Invalid Moves**: If you receive an "Invalid move" message, ensure that your move follows the rules of chess and that you are using the correct notation.
- **Game Not Starting**: Ensure that Python is correctly installed and that you are in the correct directory when running the game.

## Conclusion

Thank you for using our terminal-based chess game. We hope you enjoy playing and improving your chess skills. If you have any questions or feedback, please feel free to reach out to our support team. Happy playing!