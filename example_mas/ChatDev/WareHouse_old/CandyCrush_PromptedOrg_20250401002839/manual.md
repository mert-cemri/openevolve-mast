manual.md

```
# Candy Crush Match-3 Puzzle Game

Welcome to the Candy Crush Match-3 Puzzle Game! This Python-based game provides a fun and engaging experience reminiscent of the popular Candy Crush game. Swap adjacent candies to form matches of three or more, clear candies, score points, and enjoy exciting chain reactions!

## 🎮 Game Features

- **Interactive Gameplay:** Swap adjacent candies to create matches of three or more.
- **Chain Reactions:** Matches trigger candies above to fall, potentially creating additional matches.
- **Scoring System:** Earn points for every candy cleared.
- **Move-Based Constraints:** Challenge yourself by completing the game within a limited number of moves.
- **Dynamic Board:** The board updates after each valid move, introducing new candies.

## 🚀 Installation

### Prerequisites

- Python 3.6 or higher installed on your system.

### Dependencies

This game does not require any external dependencies. However, ensure you have Python installed.

You can verify your Python installation by running:

```bash
python --version
```

### Downloading the Game

Clone or download the game files (`game.py` and `main.py`) to your local machine.

```bash
git clone <repository-url>
cd <repository-directory>
```

## 🎲 How to Play

### Starting the Game

Navigate to the directory containing the game files and run the following command:

```bash
python main.py
```

### Gameplay Instructions

1. **View the Board:**  
   The game board will display candies represented by colored emojis:
   - 🔴 (Red)
   - 🟢 (Green)
   - 🔵 (Blue)
   - 🟡 (Yellow)
   - 🟣 (Purple)

2. **Making a Move:**  
   Enter positions of two adjacent candies you wish to swap. Positions are entered as row and column numbers separated by a space.

   Example:
   ```
   Enter first candy position (row col): 3 4
   Enter second candy position (row col): 3 5
   ```

   **Note:** Rows and columns are zero-indexed (0 to 7 for an 8x8 board).

3. **Validating Moves:**  
   - Moves must swap adjacent candies horizontally or vertically.
   - A valid move must result in at least one match of three or more candies.
   - Invalid swaps will revert automatically, prompting you to try again.

4. **Scoring:**  
   - Each candy cleared earns you 10 points.
   - Chain reactions can significantly boost your score.

5. **Move Constraints:**  
   - You have a maximum of 30 moves to achieve the highest possible score.
   - The game ends when you reach the maximum number of moves or when no more valid moves are available.

### Ending the Game

The game concludes under two conditions:
- You've used all available moves.
- No more valid moves are possible on the board.

Your final score will be displayed at the end of the game.

## 📌 Tips and Tricks

- Plan your moves carefully to maximize chain reactions.
- Prioritize moves that clear larger groups of candies for higher scores.
- Keep an eye on the number of moves remaining.

## 🛠 Troubleshooting

- **Invalid Input:** Ensure you enter positions correctly as two integers separated by a space.
- **Positions Out of Bounds:** Rows and columns must be within the board dimensions (0-7 for an 8x8 board).

## 📞 Support

If you encounter any issues or have suggestions, please contact our support team or open an issue in our repository.

Enjoy playing and have fun crushing candies! 🍬🍭
```