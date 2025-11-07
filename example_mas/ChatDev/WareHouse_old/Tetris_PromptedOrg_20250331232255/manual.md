manual.md

```
# Tetris Game

A classic Tetris game implemented in Python using Pygame. Enjoy the timeless puzzle game where you strategically rotate and position falling Tetrominoes to clear lines and score points. The game progressively increases in speed, challenging your reflexes and strategic thinking.

---

## 🚀 Features

- **Classic Gameplay:** Enjoy the traditional Tetris experience with all seven standard Tetromino shapes (I, J, L, O, S, T, Z).
- **Intuitive Controls:** Move, rotate, and drop Tetrominoes easily using keyboard controls.
- **Dynamic Difficulty:** Game speed increases progressively as you score higher, providing a challenging experience.
- **Scoring System:** Clear multiple lines simultaneously to earn bonus points.
- **Visual Feedback:** Clear and colorful graphics enhance the gaming experience.

---

## 📦 Installation

### Prerequisites

Ensure you have Python (version 3.6 or higher) installed. You can download Python from [python.org](https://www.python.org/downloads/).

### Install Dependencies

Install the required Python package using pip:

```bash
pip install -r requirements.txt
```

Alternatively, you can manually install the dependency:

```bash
pip install pygame>=2.0.0
```

---

## 🎮 How to Play

### Launching the Game

Navigate to the directory containing the game files and run the following command:

```bash
python main.py
```

### Controls

- **Left Arrow (←)**: Move Tetromino left
- **Right Arrow (→)**: Move Tetromino right
- **Down Arrow (↓)**: Soft drop (move Tetromino down faster)
- **Up Arrow (↑)**: Rotate Tetromino clockwise
- **Spacebar**: Hard drop (instantly drop Tetromino to the bottom)

### Gameplay Instructions

- Tetrominoes fall from the top of the screen. Your goal is to rotate and position them to create complete horizontal lines.
- Completed lines are cleared from the board, and you earn points accordingly.
- The game speed gradually increases as your score increases, making the game progressively more challenging.
- The game ends when new Tetrominoes cannot enter the board due to existing blocks.

---

## 🖥️ Game Interface

- **Game Board:** The main area where Tetrominoes fall and stack.
- **Score:** Your current score is calculated based on the number of lines cleared.
- **Tetrominoes:** Each shape has a unique color for easy identification.

---

## 🛠️ Project Structure

```
TetrisGame/
├── main.py          # Entry point of the game
├── game.py          # Contains the game logic and board management
├── tetromino.py     # Defines Tetromino shapes and rotations
└── requirements.txt # Lists required Python packages
```

---

## 📌 Tips and Tricks

- Plan ahead and leave space for upcoming Tetrominoes.
- Clearing multiple lines simultaneously (especially four lines, known as a "Tetris") yields significantly higher scores.
- Use the hard drop (spacebar) strategically to quickly position Tetrominoes and gain extra points.

---

## 📝 License

This project is open-source and available for personal and educational use. Feel free to modify and enhance the game according to your preferences.

Enjoy playing Tetris! 🎉
```