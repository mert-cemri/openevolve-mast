# Reversi (Othello) Game User Manual

Welcome to the Reversi (Othello) game! This manual will guide you through the installation, setup, and gameplay of the Reversi game developed in Python. 

## Introduction

Reversi, also known as Othello, is a classic board game for two players. The game is played on an 8x8 grid, where players take turns placing discs on the board. The objective is to have the majority of discs of your color on the board at the end of the game. Discs are flipped to the player's color when they are outflanked by the opponent's discs.

## Main Functions

- **Game Initialization**: The game starts with an initial setup of four discs in the center of the board.
- **Player Turns**: Players alternate turns, placing a disc of their color on the board.
- **Valid Moves**: A move is valid if it outflanks one or more of the opponent's discs.
- **Disc Flipping**: Discs are flipped to the player's color when they are outflanked.
- **Game End**: The game ends when the board is full or no valid moves remain for either player.
- **Winner Announcement**: The player with the most discs of their color on the board at the end of the game is declared the winner.

## Installation

### Environment Setup

To run the Reversi game, you need to have Python installed on your system. The game does not require any external dependencies, so you can get started right away.

1. **Install Python**: If you don't have Python installed, download and install it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the game repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Project Directory**: Change into the project directory:
   ```bash
   cd <project-directory>
   ```

### Running the Game

To start the game, run the `main.py` file using Python:

```bash
python main.py
```

## How to Play

1. **Start the Game**: Run the game using the command above. The initial board will be displayed with the starting position of the discs.

2. **Player Turns**: Players take turns to place their discs on the board. The game will prompt the current player to enter their move in the format `row col`.

3. **Valid Moves**: Enter a valid move that outflanks the opponent's discs. If no valid moves are available, the game will skip the player's turn.

4. **Game End**: The game ends when the board is full or no valid moves remain for either player. The final board state will be displayed, and the winner will be announced.

5. **Scoring**: The player with the most discs of their color on the board at the end of the game wins. If both players have the same number of discs, the game is a tie.

## Troubleshooting

- **Invalid Move**: If you enter an invalid move, the game will prompt you to try again. Ensure that your move is within the board boundaries and outflanks the opponent's discs.

- **No Valid Moves**: If no valid moves are available for a player, the game will automatically skip their turn.

## Conclusion

Enjoy playing Reversi! This game is a great way to challenge your strategic thinking and have fun with a friend. If you encounter any issues or have suggestions for improvement, feel free to reach out to the development team. Happy gaming!