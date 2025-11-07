# Chess Game User Manual

Welcome to the Chess Game application! This manual will guide you through the installation process, introduce the main functions of the software, and provide instructions on how to play the game.

## Overview

This Chess Game is a terminal-based application that allows two players to play a game of chess. The game is designed to be simple and accessible, with no need for a graphical user interface. Players can enter their moves using standard chess notation, and the game will display the board state after each move.

## Installation

### Requirements

This project does not require any external dependencies, making it easy to set up and run. You only need to have Python installed on your system.

### Quick Install

1. **Clone the Repository:**

   First, clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory:**

   Change into the project directory:

   ```bash
   cd <project-directory>
   ```

   Replace `<project-directory>` with the name of the directory where the project is located.

3. **Run the Game:**

   Execute the main script to start the game:

   ```bash
   python main.py
   ```

## How to Play

### Starting the Game

- Once you run the `main.py` script, the game will start, and the initial chessboard will be displayed in the terminal.

### Taking Turns

- The game alternates turns between two players: White and Black.
- The current player will be prompted to enter their move using standard chess notation (e.g., `e2e4`).

### Entering Moves

- Moves should be entered in the format of starting position followed by the ending position (e.g., `e2e4` means moving the piece from e2 to e4).
- The game will validate the move and update the board accordingly.

### Game End Conditions

- The game will automatically detect checkmate and stalemate conditions:
  - **Checkmate:** The game will announce the winner when a checkmate is detected.
  - **Stalemate:** The game will declare a draw if a stalemate occurs.

### Exiting the Game

- You can exit the game at any time by closing the terminal or using keyboard interrupts (e.g., `Ctrl+C`).

## Additional Information

- The game currently includes basic move validation and board state management. Future updates may include more detailed rule enforcement and additional features.
- If you encounter any issues or have suggestions for improvement, please feel free to contribute to the project or contact the development team.

Enjoy your game of chess!