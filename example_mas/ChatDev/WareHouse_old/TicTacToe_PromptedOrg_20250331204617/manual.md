manual.md

```
# Tic-Tac-Toe Game

A simple, user-friendly Tic-Tac-Toe game developed in Python, allowing two players to compete against each other on a standard 3x3 grid. Players alternate placing their marks (X or O), and the game automatically determines the winner or a draw.

---

## 🚀 Features

- **User-Friendly Interface:** Clear and intuitive command-line interface.
- **Two-Player Mode:** Players alternate turns to place their marks.
- **Automatic Winner Detection:** Instantly detects and announces the winner.
- **Draw Detection:** Recognizes when the board is full without a winner.
- **Input Validation:** Ensures valid moves and prevents overwriting existing moves.

---

## 📋 Requirements

This project does not require any external dependencies. Python 3.x is the only requirement.

Ensure Python is installed by running:

```bash
python --version
```

If Python is not installed, download it from [python.org](https://www.python.org/downloads/).

---

## ⚙️ Installation

1. **Clone the Repository**

```bash
git clone <repository-url>
cd <repository-directory>
```

2. **Verify Python Installation**

Make sure Python is installed and accessible from your command line.

```bash
python --version
```

3. **Dependencies**

No external dependencies are required. The game is ready to run immediately after cloning.

---

## 🎮 How to Play

1. **Start the Game**

Navigate to the project directory and run the following command:

```bash
python main.py
```

2. **Gameplay Instructions**

- The game starts with Player X.
- Players alternate turns, entering their moves by specifying the row and column numbers (both ranging from 1 to 3).
- Rows and columns are numbered as follows:

```
Row: 1 | Column: 1 | Column: 2 | Column: 3
Row: 2 | Column: 1 | Column: 2 | Column: 3
Row: 3 | Column: 1 | Column: 2 | Column: 3
```

- Example move input:

```
Enter row (1-3): 2
Enter column (1-3): 3
```

- The game will display the updated board after each move.

3. **Winning the Game**

- The game automatically checks for a winner after each move.
- A player wins by placing three of their marks (X or O) in a horizontal, vertical, or diagonal row.
- If a player wins, the game announces the winner and ends.

4. **Draw Condition**

- If all positions on the board are filled without any player achieving three marks in a row, the game announces a draw.

---

## 📖 Project Structure

```
tic-tac-toe/
├── main.py
├── tic_tac_toe.py
└── requirements.txt
```

- `main.py`: Entry point of the game, handles user interaction.
- `tic_tac_toe.py`: Contains the game logic and board management.
- `requirements.txt`: Lists external dependencies (none required for this project).

---

## 🛠️ Customization and Extension

Feel free to extend and customize the game:

- **Graphical Interface:** Integrate GUI libraries like Tkinter or PyGame for a graphical experience.
- **AI Opponent:** Implement an AI opponent for single-player mode.
- **Score Tracking:** Add functionality to track and display player scores across multiple rounds.

---

## 📞 Support

For any questions, issues, or suggestions, please contact the development team or open an issue in the project's repository.

Enjoy playing Tic-Tac-Toe! 🎉
```