# Checkers Game User Manual

Welcome to the Checkers Game application! This user manual will guide you through the installation process, introduce you to the main features of the game, and provide instructions on how to play.

## Introduction

The Checkers Game is a classic board game implemented using Python and the Pygame library. It features an 8x8 board where two players alternate turns, applying standard capture and kinging rules. The game provides a graphical interface for an engaging user experience.

## Quick Install

To get started with the Checkers Game, you need to install the necessary environment dependencies. Follow the steps below:

1. **Install Python**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Pygame**: The game requires the Pygame library. You can install it using pip:

   ```bash
   pip install pygame>=2.0.0
   ```

3. **Download the Game Code**: Clone or download the game code from the repository.

## Main Features

- **Graphical User Interface**: The game features a visually appealing GUI built with Pygame, allowing players to interact with the board using mouse clicks.

- **Turn Management**: The game alternates turns between two players, ensuring fair play.

- **Capture and Kinging Rules**: Standard checkers rules are implemented, including capturing opponent pieces and kinging when a piece reaches the opposite end of the board.

- **Win Conditions**: The game automatically detects win conditions, declaring a winner when one player has no remaining pieces.

## How to Play

1. **Start the Game**: Run the `main.py` file to start the game. You can do this by navigating to the directory containing the game files and executing the following command:

   ```bash
   python main.py
   ```

2. **Game Interface**: Once the game starts, you will see an 8x8 board displayed on the screen. The pieces are placed in their initial positions, with black pieces at the top and white pieces at the bottom.

3. **Making a Move**: To make a move, click on a piece you want to move. The piece must belong to the player whose turn it is (black or white). After selecting a piece, click on the destination square to complete the move.

4. **Capture Moves**: If a capture move is available, you must perform it. The game enforces capture rules, so you cannot make a regular move if a capture is possible.

5. **Kinging**: When a piece reaches the opposite end of the board, it becomes a king. Kings can move both forward and backward diagonally.

6. **Winning the Game**: The game ends when one player has no remaining pieces. The player with pieces left on the board is declared the winner.

## Troubleshooting

- **Pygame Installation Issues**: If you encounter issues installing Pygame, ensure you have the correct version of Python and pip installed. Refer to the [Pygame documentation](https://www.pygame.org/wiki/GettingStarted) for additional help.

- **Game Crashes**: If the game crashes or behaves unexpectedly, check the console for error messages. Ensure all game files are present and correctly named.

## Conclusion

Enjoy playing the Checkers Game! We hope this manual helps you get started and enhances your gaming experience. If you have any questions or feedback, feel free to reach out to our support team.

Happy gaming!