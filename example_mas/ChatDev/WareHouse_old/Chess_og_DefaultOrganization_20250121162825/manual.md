# Chess Game User Manual

Welcome to the Chess Game application! This manual provides detailed instructions on how to install, set up, and play the chess game from your Linux Terminal. This game allows two players to take turns and determine the winner using standard chess rules.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [How to Play](#how-to-play)
4. [Game Features](#game-features)
5. [Troubleshooting](#troubleshooting)

## Introduction

The Chess Game is a terminal-based application developed in Python. It allows two players to engage in a classic game of chess, taking turns to move pieces using formal chess notation. The game checks for valid moves, detects checkmate, and declares the winner.

## Installation

### Prerequisites

- Python 3.x installed on your Linux system.
- A terminal application to run the game.

### Quick Install

1. **Clone the Repository**

   Open your terminal and clone the repository using the following command:

   ```bash
   git clone <repository-url>
   ```

   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory**

   Change to the directory where the project is located:

   ```bash
   cd <project-directory>
   ```

   Replace `<project-directory>` with the name of the directory you cloned.

3. **Install Dependencies**

   This project does not require any external dependencies. You can proceed to run the game.

## How to Play

1. **Start the Game**

   Run the following command in your terminal to start the game:

   ```bash
   python main.py
   ```

2. **Game Interface**

   - The chessboard will be displayed in the terminal.
   - Players will be prompted to enter their moves in standard chess notation (e.g., `e2 e4`).

3. **Making Moves**

   - Enter your move when prompted. For example, to move a pawn from e2 to e4, type `e2 e4` and press Enter.
   - The game will validate the move and update the board accordingly.

4. **Winning the Game**

   - The game will automatically detect checkmate and declare the winner.
   - If a player is in checkmate, the game will end, and the winner will be announced.

## Game Features

- **Terminal-Based Interface**: Play chess directly from your Linux terminal.
- **Standard Chess Notation**: Enter moves using standard chess notation.
- **Move Validation**: The game checks for valid moves and ensures adherence to chess rules.
- **Checkmate Detection**: Automatically detects checkmate and declares the winner.

## Troubleshooting

- **Invalid Move**: If you enter an invalid move, the game will prompt you to try again.
- **Input Errors**: Ensure you enter moves in the correct format (e.g., `e2 e4`). If you encounter issues, check your input for typos.
- **Game Exit**: To exit the game, you can close the terminal or press `Ctrl + C`.

For further assistance, please refer to the source code documentation or contact support.

Enjoy your game of chess!