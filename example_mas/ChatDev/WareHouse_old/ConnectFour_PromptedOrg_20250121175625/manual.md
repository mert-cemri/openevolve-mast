# Connect Four Game User Manual

Welcome to the Connect Four Game! This manual will guide you through the installation, setup, and gameplay of the Connect Four game implemented in Python.

## Introduction

Connect Four is a classic two-player connection game in which the players first choose a color and then take turns dropping colored discs into a seven-column, six-row vertically suspended grid. The pieces fall straight down, occupying the lowest available space within the column. The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of four of one's own discs.

## Main Functions

- **Two-Player Mode:** The game supports two players, each taking turns to drop their discs into the grid.
- **Win Detection:** The game automatically detects when a player has won by forming a line of four discs.
- **Draw Detection:** The game detects when the board is full and declares a draw if no player has won.
- **Interactive Gameplay:** Players choose columns by typing a number, and the board updates after each move.

## Installation

### Prerequisites

- Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Quick Install

1. **Clone the Repository:**
   Clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```
   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory:**
   ```bash
   cd connect-four-game
   ```

3. **Install Dependencies:**
   This project does not require any external dependencies. However, ensure your Python environment is set up correctly.

## How to Play

1. **Run the Game:**
   Navigate to the project directory and run the following command to start the game:
   ```bash
   python main.py
   ```

2. **Gameplay Instructions:**
   - The game will prompt Player 1 to choose a column (0-6) to drop their disc.
   - Player 2 will then be prompted to choose a column.
   - The board will display after each move, showing the current state of the game.
   - The game will continue until a player wins or the board is full, resulting in a draw.

3. **Winning the Game:**
   - A player wins by forming a horizontal, vertical, or diagonal line of four of their discs.
   - The game will announce the winner and end the session.

4. **Draw:**
   - If the board is full and no player has formed a line of four discs, the game will declare a draw.

## Additional Information

- **Invalid Moves:** If a player attempts to place a disc in a full column or enters an invalid input, they will be prompted to try again.
- **Restarting the Game:** To play another round, simply run the `main.py` file again.

Enjoy playing Connect Four and may the best strategist win!