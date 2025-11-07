```markdown
# Reversi (Othello) Game

Welcome to the Reversi (Othello) Game! This application allows two players to enjoy the classic board game of Reversi, where strategic placement of discs can turn the tide of the game. This user manual will guide you through the installation, setup, and gameplay.

## Quick Install

To get started with the Reversi game, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Setup

1. **Clone the Repository:**
   First, clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies:**
   The game requires no external Python packages beyond the standard library. However, ensure your Python environment is set up correctly.

3. **Run the Game:**
   Execute the main script to start the game:
   ```bash
   python main.py
   ```

## 🤔 What is this?

Reversi, also known as Othello, is a strategy board game for two players. The game is played on an 8x8 grid, and players take turns placing discs on the board. The objective is to have the majority of discs turned to display your color when the last playable empty square is filled.

## 📖 How to Play

1. **Game Start:**
   - The game starts with an initial setup of four discs in the center of the board: two black and two white, arranged diagonally.

2. **Player Turns:**
   - Players alternate turns, starting with the player controlling the black discs.
   - On your turn, place a disc of your color on the board. The disc must be placed so that it brackets one or more of the opponent's discs between another disc of your color.

3. **Flipping Discs:**
   - When a disc is placed, all opponent discs that are bracketed in a straight line (horizontally, vertically, or diagonally) are flipped to your color.

4. **Valid Moves:**
   - A move is valid if it results in at least one opponent disc being flipped.
   - If a player has no valid moves, they must pass their turn.

5. **Game End:**
   - The game ends when the board is full or neither player can make a valid move.
   - The player with the most discs of their color on the board wins.

## 🎮 Game Controls

- **Input Moves:**
  - During your turn, input your move in the format `row col`, where `row` and `col` are the zero-indexed coordinates of the board.
  - Example: To place a disc in the top-left corner, enter `0 0`.

- **Invalid Moves:**
  - If an invalid move is entered, the game will prompt you to try again.

## 🏆 Winning the Game

- The player with the most discs of their color on the board at the end of the game is declared the winner.
- In the event of a tie, the game will announce it as such.

Enjoy playing Reversi and may the best strategist win!
```