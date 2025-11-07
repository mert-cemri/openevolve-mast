# Tic-Tac-Toe Game User Manual

Welcome to the Tic-Tac-Toe Game! This user-friendly application allows two players to take turns playing the classic game of Tic-Tac-Toe. The game is developed in Python and runs in a command-line interface.

## Main Functions

The Tic-Tac-Toe Game provides the following main functions:

- **Game Initialization**: Sets up the game board and determines the starting player.
- **Player Turns**: Allows two players to take turns making moves on the board.
- **Winner Determination**: Checks for a winner or a draw after each move.
- **Board Display**: Shows the current state of the board after each move.
- **Player Switching**: Alternates between players after each valid move.

## Installation

### Prerequisites

To run the Tic-Tac-Toe Game, you need to have Python installed on your system. You can download Python from the official website: [python.org](https://www.python.org/).

### Quick Install

1. **Clone the Repository**: Download the game files to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Game Directory**: Change to the directory where the game files are located.

   ```bash
   cd <directory-name>
   ```

3. **Install Dependencies**: The game does not require any external dependencies, so you can skip this step.

## How to Play

1. **Start the Game**: Run the `main.py` file to start the game.

   ```bash
   python main.py
   ```

2. **Game Instructions**: Once the game starts, you will see the initial empty board and a welcome message.

3. **Player Moves**: Players take turns entering their moves. When prompted, enter a position number (1-9) corresponding to the desired cell on the board:

   ```
   1 | 2 | 3
   ---------
   4 | 5 | 6
   ---------
   7 | 8 | 9
   ```

4. **Game Progression**: After each move, the board is updated and displayed. The game checks for a winner or a draw.

5. **Winning the Game**: The first player to align three of their symbols (X or O) horizontally, vertically, or diagonally wins the game. If all cells are filled without a winner, the game ends in a draw.

6. **Restarting the Game**: To play again, simply run the `main.py` file once more.

## Troubleshooting

- **Invalid Input**: If you enter an invalid position or a non-numeric input, the game will prompt you to try again.
- **Position Taken**: If you choose a position that is already occupied, you will be asked to select a different position.

Enjoy playing Tic-Tac-Toe! If you encounter any issues or have questions, please contact our support team for assistance.