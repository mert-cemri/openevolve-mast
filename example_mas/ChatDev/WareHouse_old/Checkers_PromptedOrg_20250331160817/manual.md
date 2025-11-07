# Checkers Game User Manual

Welcome to the Checkers Game application! This manual will guide you through the installation, setup, and usage of the Checkers game developed in Python. This application allows two players to play the classic game of Checkers on an 8x8 board, following standard rules including capturing and kinging.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [How to Play](#how-to-play)
4. [Game Rules](#game-rules)
5. [Troubleshooting](#troubleshooting)

## Introduction

The Checkers Game application is a command-line based game where two players alternate turns to move their pieces across the board. The objective is to capture all of the opponent's pieces or block them so they cannot move.

## Installation

To run the Checkers Game, you need to have Python installed on your system. Follow these steps to set up the game:

1. **Clone the Repository:**
   Clone the repository containing the game code to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory:**
   Change your working directory to the location where the game code is stored.

   ```bash
   cd <repository-directory>
   ```

3. **Install Dependencies:**
   Ensure you have Python installed (version 3.6 or higher is recommended). No additional Python packages are required for this game.

4. **Run the Game:**
   Execute the main script to start the game.

   ```bash
   python main.py
   ```

## How to Play

1. **Starting the Game:**
   - Run the `main.py` script to start the game.
   - The game will display the initial board setup and indicate which player's turn it is.

2. **Making a Move:**
   - Players take turns to move their pieces.
   - Enter your move in the format `x1,y1 to x2,y2`, where `(x1, y1)` is the starting position and `(x2, y2)` is the destination position.
   - Example input: `2,3 to 3,4`

3. **Capturing Pieces:**
   - If a capture is possible, you must make the capture.
   - Additional captures are allowed if available after a move.

4. **Winning the Game:**
   - The game ends when one player captures all the opponent's pieces or blocks them from making any legal moves.
   - The game will announce the winner.

## Game Rules

- **Board Setup:** The game is played on an 8x8 board with pieces placed on dark squares.
- **Movement:** Pieces move diagonally forward. Kings can move diagonally both forward and backward.
- **Capturing:** A piece can capture an opponent's piece by jumping over it to an empty square.
- **Kinging:** A piece becomes a king when it reaches the opponent's back row.

## Troubleshooting

- **Invalid Move:** If you enter an invalid move, the game will prompt you to try again.
- **Input Format:** Ensure your move input follows the correct format `x1,y1 to x2,y2`.
- **Game Not Starting:** Verify that Python is installed and you are in the correct directory.

Enjoy playing the Checkers Game! If you encounter any issues or have questions, please refer to this manual or contact support for assistance.