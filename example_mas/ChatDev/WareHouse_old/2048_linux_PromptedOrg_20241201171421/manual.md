# 2048 Game User Manual

Welcome to the 2048 Game! This manual will guide you through the installation and usage of the game, which is designed to be played directly from the Linux Terminal. The game is implemented in Python and does not require any external dependencies.

## Game Overview

2048 is a single-player sliding tile puzzle game. The objective is to slide numbered tiles on a 4x4 grid to combine them and create a tile with the number 2048. The game continues even after reaching the 2048 tile, allowing players to achieve higher scores.

## Features

- **Simple Gameplay**: Use the keyboard to slide tiles in four directions: up, down, left, and right.
- **Score Tracking**: Keep track of your score as you combine tiles.
- **Game Over Detection**: The game will notify you when there are no more valid moves.

## Installation

### Prerequisites

- **Python**: Ensure that Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation Steps

1. **Clone the Repository**: Download the game files to your local machine. You can do this by cloning the repository or downloading the files directly.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Game Directory**: Change your directory to where the game files are located.

   ```bash
   cd <repository-directory>
   ```

3. **Install Python (if not already installed)**: Follow the instructions on the Python website to install Python on your system.

4. **Verify Installation**: Ensure that Python is correctly installed by running:

   ```bash
   python --version
   ```

## How to Play

1. **Start the Game**: Run the game using the following command in your terminal:

   ```bash
   python main.py
   ```

2. **Game Controls**: Use the following keys to move the tiles:

   - `w`: Move tiles up
   - `a`: Move tiles left
   - `s`: Move tiles down
   - `d`: Move tiles right

3. **Objective**: Combine tiles with the same number to create a tile with the number 2048. Continue playing to achieve higher scores.

4. **Game Over**: The game ends when there are no more valid moves. The final grid and score will be displayed.

5. **Restart**: To play again, simply run the game command again.

## Troubleshooting

- **Invalid Input**: If you enter an invalid key, the game will prompt you to enter a valid move (`w`, `a`, `s`, or `d`).
- **Python Errors**: Ensure that you have Python installed and that you are running the game from the correct directory.

## Conclusion

Enjoy playing the 2048 game in your terminal! This simple yet challenging game is perfect for quick breaks and testing your strategic thinking. If you have any questions or encounter issues, please reach out to our support team. Happy gaming!