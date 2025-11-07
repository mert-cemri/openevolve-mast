# Match-3 Puzzle Game User Manual

Welcome to the Match-3 Puzzle Game, a fun and engaging game reminiscent of Candy Crush. This game allows users to swap adjacent candies to form matches of three or more, clear matches, and track their scores. The board updates after each valid move, providing an exciting and dynamic gaming experience.

## Main Functions

- **Game Initialization**: Start the game with a customizable board size (default is 8x8).
- **Candy Swapping**: Swap adjacent candies to create matches of three or more.
- **Match Clearing**: Automatically clear matched candies and update the board.
- **Score Tracking**: Keep track of your score as you clear matches.
- **Board Updating**: New candies drop down and fill the board after matches are cleared.

## Installation

To run the Match-3 Puzzle Game, you need to have Python installed on your system. Follow these steps to set up the environment and run the game:

1. **Install Python**: Ensure that Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the game repository from the source where the code is hosted.

3. **Install Dependencies**: Navigate to the directory containing the game files and install any required dependencies. This game primarily uses Python's standard library, so no additional packages are required.

## How to Play

1. **Start the Game**: Run the `main.py` file to start the game. You can do this by opening a terminal, navigating to the game directory, and executing the command:
   ```bash
   python main.py
   ```

2. **View the Board**: The game will display an 8x8 board filled with randomly colored candies. Each candy is represented by a letter (R, G, B, Y, P) corresponding to its color (Red, Green, Blue, Yellow, Purple).

3. **Make a Move**: Enter the positions of two adjacent candies you want to swap in the format `row1 col1 row2 col2`. For example, to swap the candy at row 0, column 0 with the candy at row 0, column 1, enter:
   ```
   0 0 0 1
   ```

4. **Check for Matches**: If the swap results in a match of three or more candies of the same color, the matched candies will be cleared, and new candies will drop down to fill the board.

5. **Track Your Score**: After each successful move, your score will be updated and displayed.

6. **Quit the Game**: To exit the game, enter `q` when prompted for a move.

## Additional Information

- **Invalid Moves**: If you attempt to swap non-adjacent candies or make a move that does not result in a match, the game will notify you of the invalid move, and you can try again.

- **Continuous Play**: The game continues indefinitely, allowing you to make as many moves as you like. Challenge yourself to achieve the highest score possible!

Enjoy playing the Match-3 Puzzle Game and have fun clearing those candies! If you encounter any issues or have questions, feel free to reach out for support.