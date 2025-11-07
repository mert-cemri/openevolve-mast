# Tetris Game User Manual

Welcome to the Tetris Game user manual. This document will guide you through the installation, setup, and usage of the Tetris game developed in Python. 

## Introduction

The Tetris game is a classic puzzle game where tetrominoes fall from the top of the screen, and the player can move or rotate them before they land. Completed lines are cleared, and the player's score increases accordingly. The game ends when no more pieces can be placed on the board.

## Main Functions

- **Tetromino Movement**: Players can move tetrominoes left, right, or down, and rotate them to fit them into the board.
- **Line Clearing**: Completed lines are automatically cleared from the board, and the player's score increases.
- **Scoring System**: Players earn points for each line cleared.
- **Game Over Condition**: The game ends when no more tetrominoes can be placed on the board.

## Installation

To run the Tetris game, you need to have Python installed on your system. Follow these steps to set up the environment and run the game:

### Step 1: Install Python

Ensure that Python is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Step 2: Install Required Dependencies

The Tetris game requires the `curses` library, which is used for handling keyboard inputs and rendering the game interface. This library is included with Python on Unix-based systems (Linux, macOS). For Windows, you may need to install a compatible version, such as `windows-curses`.

To install `windows-curses` on Windows, run the following command:

```bash
pip install windows-curses
```

### Step 3: Download the Game Code

Download the game code files (`main.py`, `game.py`, `board.py`, `tetromino.py`) from the provided source or repository.

## How to Play

1. **Run the Game**: Open a terminal or command prompt, navigate to the directory containing the game files, and run the following command:

   ```bash
   python main.py
   ```

2. **Game Controls**:
   - **Left Arrow Key**: Move the current tetromino left.
   - **Right Arrow Key**: Move the current tetromino right.
   - **Up Arrow Key**: Rotate the current tetromino.
   - **Down Arrow Key**: Move the current tetromino down faster.

3. **Objective**: Arrange the falling tetrominoes to complete horizontal lines. Each completed line will disappear, and you will earn points.

4. **Game Over**: The game ends when the tetrominoes stack up to the top of the board and no more pieces can be placed.

5. **Scoring**: Your score is displayed at the bottom of the game screen. Try to achieve the highest score possible by clearing multiple lines.

Enjoy playing Tetris and challenge yourself to beat your high score!