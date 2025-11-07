# Chess Game User Manual

Welcome to the Chess Game, a terminal-based application that allows two players to play a game of chess directly from the Linux Terminal. This user manual will guide you through the installation process, introduce the main functions of the software, and provide instructions on how to play the game.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Main Functions](#main-functions)
4. [How to Play](#how-to-play)
5. [Game Features](#game-features)

## Introduction

The Chess Game is a Python-based application designed to be played in the Linux Terminal. It supports standard chess rules, including castling, en passant, and pawn promotion. The game enforces check and checkmate rules, providing a complete chess experience without the need for a graphical user interface.

## Installation

### Prerequisites

- Python 3.x installed on your system.
- A Linux Terminal to run the application.

### Installation Steps

1. **Clone the Repository:**

   Open your terminal and clone the repository using the following command:

   ```bash
   git clone <repository-url>
   ```

   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory:**

   ```bash
   cd <repository-directory>
   ```

   Replace `<repository-directory>` with the name of the cloned repository.

3. **Install Dependencies:**

   The project does not require any external dependencies. However, ensure that Python 3.x is installed on your system.

## Main Functions

- **Initialize Board:** Sets up the chessboard with all pieces in their starting positions.
- **Display Board:** Prints the current state of the chessboard to the terminal.
- **Process Move:** Validates and executes player moves.
- **Check Game Status:** Determines if the game is in check, checkmate, or stalemate.

## How to Play

1. **Start the Game:**

   Run the main script to start the game:

   ```bash
   python main.py
   ```

2. **Gameplay:**

   - The game alternates turns between the two players, starting with White.
   - Players enter their moves using standard algebraic notation (e.g., `e2e4` for moving a pawn from e2 to e4).
   - The game will display the board after each move and indicate whose turn it is.

3. **Winning the Game:**

   - The game continues until one player achieves checkmate, or a stalemate occurs, resulting in a draw.

## Game Features

- **Castling:** Allows the king and rook to move simultaneously under specific conditions.
- **En Passant:** A special pawn capture that can occur immediately after a pawn makes a two-square move from its starting position.
- **Pawn Promotion:** When a pawn reaches the opposite end of the board, it can be promoted to a queen, rook, bishop, or knight.
- **Check