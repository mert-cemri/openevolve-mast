# Reversi (Othello) Game

Welcome to the Reversi (Othello) Game! This is a classic board game where two players take turns placing discs on an 8x8 grid. The objective is to have the majority of discs in your color by the end of the game. This manual will guide you through the installation, setup, and gameplay of the Reversi game.

## Quick Install

To get started with the Reversi game, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/).

### Step 1: Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/reversi-game.git
cd reversi-game
```

### Step 2: Install Dependencies

The Reversi game requires no external Python packages, so you can directly run the game without additional installations. However, ensure that your Python environment is set up correctly.

### Step 3: Run the Game

To start the game, run the following command in your terminal:

```bash
python main.py
```

## 🤔 What is Reversi?

Reversi, also known as Othello, is a strategy board game for two players. The game is played on an 8x8 board with discs that are black on one side and white on the other. Players take turns placing discs on the board with their assigned color facing up. The goal is to have the majority of discs showing your color when the board is full or no valid moves remain.

## 🎮 How to Play

1. **Game Start**: The game starts with four discs placed in the center of the board in a diagonal pattern. Black always moves first.

2. **Placing Discs**: On your turn, place a disc on the board such that it sandwiches one or more of your opponent's discs between the disc you placed and another disc of your color. All of the opponent's discs between your discs are flipped to your color.

3. **Valid Moves**: A move is valid if it results in at least one opponent's disc being flipped. If no valid moves are available, the player must pass their turn.

4. **Game End**: The game ends when the board is full or neither player can make a valid move. The player with the most discs of their color on the board wins.

5. **Winning the Game**: The winner is determined by counting the discs of each color on the board. The player with the majority of discs wins. If both players have the same number of discs, the game is a draw.

## 📖 Documentation

For more information on the rules and strategies of Reversi, you can refer to the following resources:

- [Reversi Rules](https://en.wikipedia.org/wiki/Reversi)
- [Othello Strategy Guide](https://www.worldothello.org/about/about-othello/strategy-guide)

Enjoy playing Reversi and may the best strategist win!