# Checkers Game User Manual

Welcome to the Checkers Game! This manual will guide you through the installation, setup, and usage of the Checkers game application developed in Python. This game allows two players to play Checkers on an 8x8 board, following standard rules including capturing and kinging.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Game Rules](#game-rules)
- [Troubleshooting](#troubleshooting)

## Introduction

The Checkers Game is a Python-based application that simulates a classic game of Checkers (Draughts). It features:
- An 8x8 board
- Two players: Black and White
- Standard capture and kinging rules
- Move input in standard notation (e.g., A3-B4)

## Installation

### Prerequisites

To run the Checkers Game, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Quick Install

1. **Clone the Repository:**
   Clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```
   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory:**
   ```bash
   cd <project-directory>
   ```
   Replace `<project-directory>` with the path to the cloned repository.

3. **Install Dependencies:**
   The Checkers Game does not require any external dependencies. However, ensure your Python environment is set up correctly.

## How to Play

1. **Run the Game:**
   Execute the main module to start the game:
   ```bash
   python main.py
   ```

2. **Game Interface:**
   - The game will display the board and prompt players to enter their moves.
   - Moves should be entered in the format `A3-B4`, where `A3` is the starting position and `B4` is the ending position.

3. **Turn Alternation:**
   - The game alternates turns between the two players, starting with Black.

4. **Capture Moves:**
   - If a player can capture an opponent's piece, they must do so.
   - Multiple captures in a single turn are allowed if possible.

5. **Winning the Game:**
   - The game ends when one player has no pieces left or cannot make a valid move.

## Game Rules

- **Board Setup:**
  - The board is an 8x8 grid with pieces placed on the dark squares.
  - Black pieces start on rows 0 to 2, and White pieces start on rows 5 to 7.

- **Movement:**
  - Regular pieces move diagonally forward.
  - Kings can move diagonally both forward and backward.

- **Capturing:**
  - A piece captures an opponent's piece by jumping over it to an empty square.
  - Captures are mandatory when available.

- **Kinging:**
  - A piece becomes a king when it reaches the opponent's back row.

## Troubleshooting

- **Invalid Move Format:**
  - Ensure moves are entered in the correct format (e.g., A3-B4).

- **Move Errors:**
  - If an error occurs during a move, check the move validity and try again.

- **Game Crashes:**
  - If the game crashes, restart the application and ensure all files are intact.

For further assistance, please contact our support team.

Enjoy playing Checkers!