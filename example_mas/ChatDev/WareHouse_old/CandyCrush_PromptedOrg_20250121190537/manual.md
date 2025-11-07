# Match-3 Puzzle Game User Manual

Welcome to the Match-3 Puzzle Game, a delightful and engaging game reminiscent of Candy Crush. This game allows you to swap adjacent candies to form matches of three or more, clear them from the board, and score points. The board updates dynamically after each valid move, providing endless fun and challenge.

## Main Functions

- **Swap Candies**: Swap adjacent candies to form matches of three or more.
- **Clear Matches**: Matches are automatically cleared from the board.
- **Score Tracking**: Earn points for each match you create.
- **Dynamic Board Update**: New candies fall into place after matches are cleared, and the board refills automatically.

## Installation

This game is developed in Python and does not require any external dependencies. Follow the steps below to set up and play the game:

### Prerequisites

- Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Quick Install

1. **Clone the Repository**: Download the game files to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Game**: Execute the main script to start the game.
   ```bash
   python main.py
   ```

## How to Play

1. **Start the Game**: Run the `main.py` script to launch the game. You will be greeted with a welcome message.

2. **View the Board**: The game board will be displayed with candies represented by their initial letters (e.g., 'r' for red, 'g' for green).

3. **Make a Move**: Enter the coordinates of the first candy you want to swap, followed by the coordinates of the adjacent candy. For example:
   ```
   Enter the coordinates of the first candy (x y): 2 3
   Enter the coordinates of the second candy (x y): 2 4
   ```

4. **Valid Moves**: Only swaps between adjacent candies are allowed. If a move is invalid, you will be prompted to try again.

5. **Score Points**: Matches of three or more candies will be cleared, and you will earn points. The score is displayed after each move.

6. **Continue Playing**: Keep making moves to score as high as possible. The board will update automatically after each valid move.

7. **Exit the Game**: Enter 'q' when prompted for coordinates to quit the game.

## Additional Information

- **Scoring System**: You earn 10 points for each candy in a match. Longer matches yield more points.
- **Game Loop**: The game continues until you decide to quit by entering 'q'.

Enjoy playing the Match-3 Puzzle Game and challenge yourself to achieve the highest score possible! If you have any questions or need further assistance, please feel free to reach out. Happy gaming!