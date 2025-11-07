```markdown
# Gomoku Game

Welcome to the Gomoku Game! This application allows you to play the classic board game Gomoku, also known as Five in a Row, against another player. The objective of the game is to be the first player to get an unbroken row of five stones horizontally, vertically, or diagonally on a 15x15 board.

## Quick Install

To run the Gomoku game, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Installation Steps

1. **Clone the Repository:**
   Clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory:**
   Change your directory to the project folder:
   ```bash
   cd <repository-folder>
   ```

3. **Install Dependencies:**
   The Gomoku game does not require any external Python packages, so no additional dependencies need to be installed.

## 🤔 What is this?

Gomoku is a strategy board game traditionally played with black and white stones on a Go board. The game is known for its simple rules but complex strategies. This software provides a digital version of the game where two players can compete against each other.

## 📖 How to Play

1. **Start the Game:**
   Run the `main.py` file to start the game:
   ```bash
   python main.py
   ```

2. **Game Interface:**
   - The game board is displayed in the console.
   - Player 1 uses the stone "X" and Player 2 uses the stone "O".

3. **Making a Move:**
   - Players take turns to place their stones on the board.
   - Enter the row and column numbers separated by a space to place your stone (e.g., `7 7`).

4. **Winning the Game:**
   - The first player to align five stones in a row, column, or diagonal wins the game.
   - The game will announce the winner and display the final board state.

5. **Invalid Moves:**
   - If a player attempts to place a stone on an occupied space or outside the board boundaries, they will be prompted to try again.

## Additional Information

- The game is designed to be played in a terminal or command prompt.
- Ensure that your terminal supports Python execution and that you have the necessary permissions to run scripts.

Enjoy playing Gomoku and may the best strategist win!
```