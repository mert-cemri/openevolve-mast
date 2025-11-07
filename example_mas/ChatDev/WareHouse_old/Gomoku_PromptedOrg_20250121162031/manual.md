# Gomoku Game User Manual

Welcome to the Gomoku Game! This manual will guide you through the installation, setup, and gameplay of the Gomoku application developed in Python. 

## Introduction

Gomoku, also known as Five in a Row, is a traditional board game played on a 15x15 grid. The objective is to be the first player to form an unbroken chain of five stones horizontally, vertically, or diagonally.

## Main Functions

- **Game Initialization**: The game initializes with two players, each assigned a unique stone ('X' or 'O').
- **Board Management**: A 15x15 board is created where players can place their stones.
- **Gameplay**: Players take turns to place their stones on the board. The game checks for a winner or a draw after each move.
- **Winner Detection**: The game checks for five consecutive stones in any direction to declare a winner.
- **Draw Detection**: The game checks if the board is full without any winner to declare a draw.

## Installation

### Prerequisites

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Environment Setup

1. **Clone the Repository**: Clone the repository containing the Gomoku game code to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Change your directory to the project folder.

   ```bash
   cd <project-directory>
   ```

3. **Install Dependencies**: Install any required dependencies using pip. If there are any specific dependencies, they will be listed in a `requirements.txt` file.

   ```bash
   pip install -r requirements.txt
   ```

   Note: The current version of the game does not have external dependencies beyond standard Python libraries.

## How to Play

1. **Run the Game**: Execute the main script to start the game.

   ```bash
   python main.py
   ```

2. **Game Instructions**: 
   - The game will welcome you to Gomoku.
   - Players will take turns to place their stones on the board.
   - Enter the row and column numbers when prompted to place your stone.
   - The board will be displayed after each move, showing the current state of the game.

3. **Winning the Game**: 
   - The first player to align five stones in a row, column, or diagonal wins the game.
   - The game will announce the winner and end.

4. **Draw Condition**: 
   - If the board is filled without any player achieving five in a row, the game will declare a draw.

5. **Invalid Moves**: 
   - If a player attempts to place a stone in an occupied cell or outside the board, the game will prompt for a valid move.

## Conclusion

Enjoy playing Gomoku! This game provides a simple yet challenging experience for players of all ages. If you encounter any issues or have suggestions for improvement, please contact our support team.

Thank you for choosing our Gomoku game!