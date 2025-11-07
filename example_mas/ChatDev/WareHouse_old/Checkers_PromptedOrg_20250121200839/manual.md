# Checkers Game User Manual

Welcome to the Checkers Game! This manual will guide you through the installation, setup, and gameplay of our Checkers application. Enjoy playing this classic board game with friends or family!

## Introduction

The Checkers Game is a digital version of the classic board game, designed to be played by two players. It features an 8x8 board, alternating turns between two players, and includes standard capture and kinging rules. Players input their moves using standard notation (e.g., A3-B4), and the game updates the board state accordingly.

## Quick Install

### Prerequisites

Ensure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Installation

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory:**

   Change your directory to the project folder:

   ```bash
   cd <project-directory>
   ```

   Replace `<project-directory>` with the name of the cloned repository.

3. **Install Dependencies:**

   The Checkers Game does not require any external Python packages. However, ensure your Python environment is set up correctly.

   If you are using a virtual environment, activate it:

   ```bash
   # On Windows
   .\venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

   If you haven't created a virtual environment, you can do so with:

   ```bash
   python -m venv venv
   ```

## How to Play

1. **Start the Game:**

   Run the main script to start the game:

   ```bash
   python main.py
   ```

2. **Game Rules:**

   - The game is played on an 8x8 board.
   - Players alternate turns, starting with the White player.
   - Pieces move diagonally and can capture opponent pieces by jumping over them.
   - When a piece reaches the opposite end of the board, it becomes a "King" and can move both forwards and backwards.
   - Players must make a capturing move if available.

3. **Input Moves:**

   - Enter your move in the format `A3-B4`, where `A3` is the starting position and `B4` is the ending position.
   - The game will prompt you for your move and validate it according to the rules.

4. **Winning the Game:**

   - The game ends when one player has no remaining pieces or no valid moves left.
   - The player with remaining pieces or valid moves is declared the winner.

## Troubleshooting

- **Invalid Move:**

  If you enter an invalid move, the game will prompt you to try again. Ensure your move follows the game rules.

- **Capturing Moves:**

  If a capturing move is available, you must make it. The game will notify you of possible capturing moves.

## Conclusion

We hope you enjoy playing the Checkers Game! If you have any questions or encounter issues, please reach out to our support team. Happy gaming!