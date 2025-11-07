# Match-3 Puzzle Game User Manual

Welcome to the Match-3 Puzzle Game, a fun and engaging game reminiscent of Candy Crush. This game allows you to swap adjacent candies to form matches of three or more, clear them from the board, and score points. The board updates after each valid move, providing endless entertainment.

## Main Functions

- **Board Representation**: The game board is an 8x8 grid filled with candies of different colors.
- **Candy Swapping**: Users can swap adjacent candies to form matches.
- **Match Detection**: The game detects matches of three or more candies of the same type.
- **Clearing Matches**: Matched candies are cleared from the board, and new candies appear.
- **Scoring**: Points are awarded for each match made.
- **Board Update**: The board updates after each valid move, with candies dropping to fill empty spaces and new candies appearing.

## Installation

### Environment Dependencies

To run the Match-3 Puzzle Game, you need to have Python installed on your system. You can download and install Python from the official website: [python.org](https://www.python.org/).

### Quick Install

1. **Clone the Repository**: Clone the game repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```
   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Game Directory**: Change your directory to the game folder:
   ```bash
   cd match-3-puzzle-game
   ```

3. **Install Required Packages**: Install any required packages using pip. If there are any specific dependencies, they will be listed in a `requirements.txt` file. Use the following command to install them:
   ```bash
   pip install -r requirements.txt
   ```

## How to Play

1. **Start the Game**: Run the main script to start the game:
   ```bash
   python main.py
   ```

2. **View the Board**: The current state of the board will be displayed in the console. Each candy is represented by the first letter of its color (e.g., 'R' for red, 'G' for green).

3. **Make a Move**: Enter the coordinates of the first candy you want to swap, followed by the coordinates of the second candy. The format is:
   ```
   Enter the coordinates of the first candy to swap (row col): x1 y1
   Enter the coordinates of the second candy to swap (row col): x2 y2
   ```

4. **Valid Moves**: Ensure that the candies you choose to swap are adjacent. The game will validate your move and update the board if it's valid.

5. **Scoring**: Matches will be cleared, new candies will appear, and your score will be updated accordingly.

6. **Exit the Game**: To exit the game, enter `-1 -1 -1 -1` when prompted for coordinates.

Enjoy playing the Match-3 Puzzle Game and challenge yourself to achieve the highest score possible!