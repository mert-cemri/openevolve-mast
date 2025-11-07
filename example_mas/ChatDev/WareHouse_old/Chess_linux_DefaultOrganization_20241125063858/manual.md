# Chess Game User Manual

Welcome to the Chess Game application, a simple yet engaging terminal-based chess game designed for two players. This manual will guide you through the installation, setup, and usage of the game.

## Overview

The Chess Game application allows two players to play chess in a Linux terminal environment. The game supports standard chess rules and uses algebraic notation for moves. The game will display the chessboard in the terminal and prompt players to enter their moves.

## Features

- **Two-Player Mode:** Play chess against another player in a turn-based format.
- **Algebraic Notation Input:** Enter moves using standard chess notation (e.g., `Ke8`).
- **Check and Checkmate Detection:** The game detects check and checkmate conditions.
- **Terminal-Based Interface:** Play the game entirely within the Linux terminal without the need for a graphical interface.

## Installation

### Prerequisites

- **Python 3.x**: Ensure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/).

### Installation Steps

1. **Clone the Repository:**
   Open your terminal and clone the repository using the following command:
   ```bash
   git clone <repository-url>
   ```
   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory:**
   ```bash
   cd <repository-directory>
   ```
   Replace `<repository-directory>` with the name of the directory where the repository was cloned.

3. **Install Dependencies:**
   The project does not require any external dependencies, as indicated in the `requirements.txt` file. However, ensure your Python environment is set up correctly.

## Usage

1. **Run the Game:**
   Execute the following command in your terminal to start the game:
   ```bash
   python main.py
   ```

2. **Playing the Game:**
   - The game will display the chessboard and prompt the current player to enter their move.
   - Enter your move using algebraic notation (e.g., `e2e4` to move a pawn from e2 to e4).
   - The game will validate the move and update the board accordingly.
   - If a player is in check or checkmate, the game will notify the players.

3. **Switching Turns:**
   - After a valid move, the game automatically switches to the other player.
   - Continue entering moves until a checkmate condition is met or the game is manually terminated.

4. **Ending the Game:**
   - The game ends when a player is checkmated.
   - You can also terminate the game manually by closing the terminal or using keyboard interrupts (e.g., `Ctrl+C`).

## Troubleshooting

- **Invalid Move:** If you enter an invalid move, the game will prompt you to try again.
- **Game Crashes:** Ensure your Python environment is correctly set up and that you have followed the installation steps accurately.

## Support

For further assistance or to report issues, please contact our support team or visit our [GitHub repository](<repository-url>) for more information.

Enjoy your game of chess!