```markdown
# Gomoku Game

Welcome to the Gomoku Game! This is a classic board game where two players take turns placing stones on a 15x15 grid, aiming to be the first to align five stones in a row, either horizontally, vertically, or diagonally.

## Main Functions

- **Game Board Management**: The game board is a 15x15 grid where players place their stones. The board keeps track of the state of the game and checks for a winner or a draw.

- **Game Logic**: Manages the flow of the game, including switching turns between players and resetting the game.

- **Graphical User Interface (GUI)**: Provides a visual representation of the game board and handles user interactions, such as placing stones and displaying the winner or a draw.

## Installation

### Prerequisites

- Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Quick Install

1. Clone the repository or download the source code.

2. Navigate to the directory containing the source code.

3. Install any required dependencies. This game does not require any external dependencies, so you can skip this step.

## How to Play

1. **Start the Game**: Run the `main.py` file to launch the game.

   ```bash
   python main.py
   ```

2. **Game Interface**: A window will open displaying the Gomoku board.

3. **Placing Stones**: Click on the intersections of the grid to place your stone. The game starts with the "Black" player.

4. **Switching Turns**: After placing a stone, the turn automatically switches to the other player.

5. **Winning the Game**: The first player to align five stones in a row wins the game. The game will display a message indicating the winner.

6. **Draw**: If the board is filled without any player aligning five stones, the game ends in a draw.

7. **Restarting the Game**: Close the window and restart the `main.py` file to play again.

## Additional Information

- The game is implemented using Python's Tkinter library for the GUI, which is included in the standard Python distribution.

- The game logic is encapsulated in separate modules for easy maintenance and potential future enhancements.

Enjoy playing Gomoku and may the best strategist win!
```