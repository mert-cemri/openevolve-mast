# Chess Game User Manual

Welcome to the Chess Game application! This user manual will guide you through the installation, setup, and usage of the chess game designed to be played in the Linux Terminal.

## Introduction

This Chess Game allows two players to take turns and play a complete game of chess using formal chess notation. The game is designed to run in the Linux Terminal, providing a simple and straightforward interface without the need for a graphical user interface.

## Features

- **Two-Player Mode:** Play against another player in a turn-based format.
- **Terminal-Based Interface:** Play the game directly from the Linux Terminal.
- **Formal Chess Notation:** Enter moves using standard chess notation (e.g., `e2e4`).
- **Real-Time Board Display:** View the chessboard after each move to track the game's progress.

## Installation

### Prerequisites

- **Python 3.x**: Ensure that Python 3.x is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Installation Steps

1. **Clone the Repository:**
   Open your terminal and run the following command to clone the repository:
   ```bash
   git clone <repository-url>
   ```
   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory:**
   ```bash
   cd <repository-directory>
   ```
   Replace `<repository-directory>` with the name of the directory created by the clone command.

3. **Install Dependencies:**
   There are no external dependencies required for this project. However, ensure that your Python environment is set up correctly.

## Usage

### Running the Game

1. **Start the Game:**
   In the terminal, run the following command to start the chess game:
   ```bash
   python main.py
   ```

2. **Playing the Game:**
   - The game will prompt each player to enter their move in formal chess notation (e.g., `e2e4`).
   - After each move, the updated chessboard will be displayed in the terminal.
   - Players take turns until the game concludes with a checkmate, stalemate, or draw.

3. **Game Controls:**
   - **Enter Move:** Type your move in the format `start_positionend_position` (e.g., `e2e4`) and press Enter.
   - **Invalid Moves:** If an invalid move is entered, the game will prompt you to try again.

### Ending the Game

The game will automatically end when a checkmate, stalemate, or draw condition is detected. Players can also manually terminate the game by pressing `Ctrl+C` in the terminal.

## Troubleshooting

- **Invalid Move Error:** Ensure that your move is entered in the correct format and that it follows the rules of chess.
- **Python Errors:** Verify that Python 3.x is installed and properly configured on your system.

## Support

For any issues or questions, please contact our support team at support@chatdev.com.

Enjoy your game of chess!