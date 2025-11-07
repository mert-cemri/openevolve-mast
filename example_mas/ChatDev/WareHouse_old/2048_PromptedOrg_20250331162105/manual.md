# 2048 Game User Manual

Welcome to the 2048 Game! This manual will guide you through the installation process, introduce the main functions of the software, and explain how to play the game.

## Introduction

The 2048 Game is a single-player sliding tile puzzle game. The objective is to combine tiles with the same number to create a tile with the number 2048. The game is played on a 4x4 grid, and players can move tiles in four directions: up, down, left, and right. After each move, a new tile appears in a random empty cell. The game ends when no moves are possible. The current score and the highest tile reached are displayed throughout the game.

## Quick Install

### Prerequisites

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Installation Steps

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory:**

   Change your directory to the project folder:

   ```bash
   cd <project-directory>
   ```

   Replace `<project-directory>` with the name of the cloned repository folder.

3. **Install Dependencies:**

   Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

   If a `requirements.txt` file is not provided, ensure you have the `random` module available, which is included in Python's standard library.

## How to Play

1. **Start the Game:**

   Run the `main.py` script to start the game:

   ```bash
   python main.py
   ```

2. **Game Controls:**

   Use the following keys to move the tiles:

   - `w`: Move tiles up
   - `a`: Move tiles left
   - `s`: Move tiles down
   - `d`: Move tiles right

   Enter the corresponding key and press `Enter` to make a move.

3. **Objective:**

   Combine tiles with the same number to create a tile with the number 2048. The game continues until no moves are possible.

4. **Game Over:**

   The game ends when no moves are possible. Your final score and the highest tile reached will be displayed.

5. **Display:**

   The current grid, score, and highest tile are displayed after each move.

## Main Functions

- **Game Initialization:**

  The game initializes with a 4x4 grid and two random tiles.

- **Tile Movement:**

  Tiles can be moved in four directions: up, down, left, and right. Tiles with the same number merge into one, doubling the value.

- **Random Tile Generation:**

  After each move, a new tile appears in a random empty cell.

- **Score Tracking:**

  The current score is updated with each merge, and the highest tile reached is tracked.

- **Game Over Check:**

  The game checks if any moves are possible. If not, the game ends.

Enjoy playing the 2048 Game and aim for the highest score! If you have any questions or need further assistance, please feel free to reach out.