manual.md

```
# Tic-Tac-Toe Game

A simple, user-friendly Tic-Tac-Toe game implemented in Python, allowing two players to compete against each other on a standard 3x3 grid. Players alternate placing their marks (X or O) on the board, and the game automatically determines the winner or declares a draw if the board is full.

---

## 🚀 Features

- **User-Friendly Interface:** Clear and intuitive command-line interface for easy gameplay.
- **Two-Player Mode:** Players alternate turns, placing X or O on the board.
- **Automatic Winner Detection:** The game automatically checks for a winner after each move.
- **Draw Detection:** If the board is full and no player has won, the game declares a draw.
- **Input Validation:** Ensures players enter valid moves within the 3x3 grid.

---

## 📋 Requirements

This game is built using Python and does not require any external dependencies.

**Python Version:** Python 3.x

---

## ⚙️ Installation and Setup

### Step 1: Clone or Download the Repository

Clone the repository using git:

```bash
git clone <repository-url>
cd <repository-directory>
```

Alternatively, download and extract the ZIP file containing the source code.

### Step 2: Set Up Python Environment

Ensure Python is installed on your system. You can verify your Python installation by running:

```bash
python --version
```

### Step 3: Install Dependencies

No external dependencies are required for this project. However, it's recommended to use a virtual environment to manage your Python projects.

To create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
```

Activate the virtual environment:

- On Windows:

```bash
venv\Scripts\activate
```

- On macOS/Linux:

```bash
source venv/bin/activate
```

---

## 🎮 How to Play

### Running the Game

Execute the provided shell script (`run.sh`) or directly run the Python script (`main.py`):

- Using the shell script (Linux/macOS):

```bash
chmod +x run.sh
./run.sh
```

- Directly using Python:

```bash
python main.py
```

### Gameplay Instructions

1. **Starting the Game:**
   - Upon running the game, you'll see a welcome message and an empty 3x3 Tic-Tac-Toe board.

2. **Taking Turns:**
   - Player X starts first, followed by Player O.
   - When prompted, enter the row and column numbers (both between 1 and 3) to place your mark.
   - Example input:
     ```
     Enter row (1-3): 2
     Enter column (1-3): 3
     ```

3. **Winning the Game:**
   - The game automatically checks for a winner after each move.
   - If a player successfully places three of their marks in a horizontal, vertical, or diagonal line, the game announces the winner and ends.

4. **Draw Condition:**
   - If all cells are filled and no player has three marks in a row, the game declares a draw.

---

## 📂 Project Structure

```
tic-tac-toe/
├── board.py          # Manages the game board state and operations.
├── game.py           # Contains the game logic and player management.
├── main.py           # Main executable file to start the game.
├── run.sh            # Shell script to run the game.
└── requirements.txt  # Lists external dependencies (none required).
```

---

## 🛠️ Troubleshooting

- **Invalid Input:** Ensure you enter integers between 1 and 3 for both row and column inputs.
- **Occupied Cell:** If you select a cell that's already occupied, the game will prompt you to choose another cell.

---

## 📞 Support

For any issues, questions, or suggestions, please contact our support team or open an issue in the project's repository.

Enjoy playing Tic-Tac-Toe! 🎉
```