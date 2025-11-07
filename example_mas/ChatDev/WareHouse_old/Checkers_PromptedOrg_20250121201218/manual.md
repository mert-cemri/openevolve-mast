# Checkers Game User Manual

Welcome to the Checkers Game! This manual will guide you through the installation, setup, and usage of the Checkers game application developed in Python. 

## Introduction

The Checkers Game is a classic board game implemented in Python. It features:
- An 8x8 board.
- Two players: Black ('B') and White ('W').
- Standard capture and kinging rules.
- Move input in standard notation (e.g., 'A3-B4').

## Installation

### Prerequisites

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Environment Setup

1. **Clone the Repository:**
   Clone the repository containing the Checkers game code to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies:**
   The Checkers game does not have any external dependencies beyond Python itself. Ensure your Python environment is set up correctly.

## How to Play

1. **Run the Game:**
   Navigate to the directory where the `main.py` file is located and run the following command in your terminal or command prompt:

   ```bash
   python main.py
   ```

2. **Game Instructions:**
   - The game will start with the Black player ('B').
   - Players alternate turns.
   - On your turn, you will be prompted to enter your move in the format `from-to` (e.g., 'A3-B4').
   - The game will display the board after each move.

3. **Game Rules:**
   - Pieces move diagonally forward.
   - Capture opponent pieces by jumping over them.
   - A piece becomes a king when it reaches the opponent's back row.
   - Kings can move both forward and backward diagonally.
   - The game ends when a player has no pieces left or no valid moves.

4. **Winning the Game:**
   - The player who captures all opponent pieces or blocks all opponent moves wins the game.

## Troubleshooting

- **Invalid Move:** If you enter an invalid move, the game will prompt you to try again.
- **Game Over:** The game will automatically detect when a player has no valid moves or pieces left.

## Additional Information

For any questions or further assistance, please contact our support team or refer to the documentation provided in the code comments.

Enjoy playing Checkers!