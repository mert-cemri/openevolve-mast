# Connect Four Game User Manual

Welcome to the Connect Four Game! This manual will guide you through the installation, setup, and gameplay of the Connect Four application developed in Python.

## Introduction

Connect Four is a classic two-player connection game in which players take turns dropping colored discs into a seven-column, six-row grid. The objective is to be the first to form a horizontal, vertical, or diagonal line of four discs.

## Features

- **Two-Player Mode:** Play against another player in a turn-based format.
- **Interactive Gameplay:** Players choose columns to drop their discs, and the board updates in real-time.
- **Win and Draw Detection:** The game automatically detects when a player wins or when the game ends in a draw.

## Installation

### Prerequisites

- Python 3.x installed on your system.
- No external dependencies are required for this game.

### Quick Install

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory:**

   Change into the project directory:

   ```bash
   cd connect-four
   ```

3. **Run the Game:**

   Execute the main script to start the game:

   ```bash
   python main.py
   ```

## How to Play

1. **Start the Game:**

   Run the `main.py` script to start the game. You will be greeted with a welcome message.

2. **Player Setup:**

   The game is designed for two players. Player 1 will use the disc symbol "X" and Player 2 will use the disc symbol "O".

3. **Taking Turns:**

   Players take turns to choose a column (0-6) to drop their disc. Enter the column number when prompted.

4. **Winning the Game:**

   The first player to connect four of their discs in a row (horizontally, vertically, or diagonally) wins the game. The game will announce the winner and display the final board.

5. **Draw Condition:**

   If the board is completely filled and no player has connected four discs, the game ends in a draw.

6. **Restarting the Game:**

   To play again, simply rerun the `main.py` script.

## Troubleshooting

- **Invalid Input:** If you enter an invalid column number or a column that is already full, you will be prompted to try again.
- **Empty Input:** If you provide an empty input, the game will ask you to enter a valid column number.

## Conclusion

Enjoy playing Connect Four with your friends! If you encounter any issues or have suggestions for improvements, please feel free to reach out to our support team.

Thank you for choosing our Connect Four game!