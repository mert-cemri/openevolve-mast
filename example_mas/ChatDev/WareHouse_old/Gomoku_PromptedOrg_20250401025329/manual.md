manual.md

```
# Gomoku Game

A simple and intuitive Gomoku game implemented in Python, allowing two players to compete on a standard 15x15 board. Players alternate placing black and white stones, aiming to form an unbroken row of five stones horizontally, vertically, or diagonally.

---

## 🚀 Features

- **Standard 15x15 Gomoku Board:** Play on a traditional Gomoku board.
- **Two-Player Gameplay:** Alternate turns between Black and White players.
- **Win Detection:** Automatically detects and announces the winner.
- **User-Friendly Interface:** Simple command-line interface for easy gameplay.
- **No External Dependencies:** Lightweight and easy to set up.

---

## 📦 Installation

### Prerequisites

- Python 3.x installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Clone the Repository

Clone or download the project files to your local machine.

```bash
git clone <repository_url>
cd <repository_directory>
```

### Install Dependencies

This project does not require any external dependencies. However, it's recommended to create a virtual environment for better project management.

```bash
# Create a virtual environment (optional but recommended)
python -m venv gomoku_env

# Activate the virtual environment
# On Windows:
gomoku_env\Scripts\activate
# On macOS/Linux:
source gomoku_env/bin/activate
```

---

## 🎮 How to Play

### Starting the Game

Navigate to the project directory and run the following command to start the game:

```bash
python main.py
```

### Gameplay Instructions

- The game starts with Player Black ('B') making the first move.
- Players alternate turns, placing their stones by specifying the row and column numbers separated by a space (e.g., `7 7`).
- The board coordinates range from `0` to `14` for both rows and columns.

Example move input:

```
Enter your move (row col): 7 7
```

### Rules

- Players must place their stones on empty cells.
- A player wins by forming an unbroken row of five stones horizontally, vertically, or diagonally.
- The game ends immediately when a player achieves five in a row or when the board is completely filled, resulting in a draw.

---

## 🖥️ Interface Overview

- **Board Display:** The board is displayed in the terminal, with '.' representing empty cells, 'B' for Black stones, and 'W' for White stones.
- **Move Validation:** The game automatically validates moves and prompts the player again if an invalid move is attempted.
- **Win Announcement:** The game clearly announces the winner or a draw at the end of the game.

---

## 📂 Project Structure

```
gomoku_project/
├── gomoku.py        # Contains the Gomoku game logic
├── main.py          # Entry point to run the Gomoku game
└── requirements.txt # Lists external dependencies (none required)
```

---

## 🙋‍♂️ Support & Feedback

For any issues, suggestions, or feedback, please contact our support team or open an issue in the project's repository.

Enjoy playing Gomoku! 🎉
```