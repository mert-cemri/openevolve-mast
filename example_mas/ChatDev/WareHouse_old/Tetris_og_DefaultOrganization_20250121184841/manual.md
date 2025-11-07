# Tetris Game User Manual

Welcome to the Tetris Game developed by ChatDev. This manual will guide you through the installation process, introduce the main features of the game, and provide instructions on how to play.

## Introduction

Tetris is a classic puzzle game where tetrominoes fall from the top of the screen, and the player can move or rotate them before they land. The objective is to complete horizontal lines, which are then cleared, increasing the player's score. The game ends when no more pieces can be placed on the board.

## Main Features

- **Interactive Gameplay**: Move and rotate tetrominoes to fit them into the board.
- **Scoring System**: Earn points by clearing lines.
- **Game Over Condition**: The game ends when the board is full and no more tetrominoes can be placed.
- **Real-time Updates**: The board updates after each move or drop of a tetromino.

## Installation

To play the Tetris game, you need to have Python and the Pygame library installed on your system. Follow the steps below to set up your environment:

### Step 1: Install Python

Ensure that Python is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Step 2: Install Pygame

Pygame is a set of Python modules designed for writing video games. It provides functionalities like creating windows, drawing shapes, and handling user input.

To install Pygame, open your terminal or command prompt and run the following command:

```bash
pip install pygame>=2.0.0
```

### Step 3: Download the Game Files

Download the game files from the repository or the provided source. Ensure you have the following files:

- `main.py`
- `game.py`
- `board.py`
- `tetromino.py`
- `constants.py`
- `requirements.txt`

## How to Play

1. **Start the Game**: Run the `main.py` file to start the game. You can do this by navigating to the directory containing the game files in your terminal or command prompt and executing:

   ```bash
   python main.py
   ```

2. **Game Controls**:
   - **Left Arrow Key**: Move the tetromino left.
   - **Right Arrow Key**: Move the tetromino right.
   - **Down Arrow Key**: Move the tetromino down faster.
   - **Up Arrow Key**: Rotate the tetromino.

3. **Objective**: Arrange the falling tetrominoes to complete horizontal lines. Each completed line will disappear, and your score will increase.

4. **Game Over**: The game ends when the tetrominoes stack up to the top of the board, and no more pieces can be placed.

5. **Exit the Game**: To exit the game, close the game window or press the close button.

## Troubleshooting

- **Pygame Installation Issues**: Ensure that you have a compatible version of Python and Pygame installed. Check the Pygame documentation for more details on compatibility.
- **Game Not Starting**: Verify that all game files are in the same directory and that you are running the `main.py` file.

## Support

For further assistance or to report any issues, please contact our support team at support@chatdev.com.

Enjoy playing Tetris and challenge yourself to achieve the highest score!