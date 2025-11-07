manual.md

```md
# Minesweeper Game

A classic Minesweeper game implemented in Python, offering an engaging and intuitive gaming experience. Challenge yourself with three difficulty levels, flag suspected mines, and clear the board without detonating any mines!

---

## 🚀 Features

- **Three Difficulty Levels:**
  - **Beginner:** 9x9 grid with 10 mines
  - **Intermediate:** 16x16 grid with 40 mines
  - **Expert:** 16x30 grid with 99 mines

- **Interactive Gameplay:**
  - Reveal cells to uncover numbers indicating adjacent mines.
  - Flagging mechanism to mark suspected mines.
  - Recursive reveal of empty cells for smoother gameplay.

- **Clear Visual Representation:**
  - Distinct visuals for flagged cells (`F`).
  - Easy-to-read board layout.

---

## ⚙️ Installation

### Prerequisites

- Python 3.x installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Dependencies

This project does not require any external Python packages. However, ensure your Python environment is correctly configured.

To confirm Python installation, open your terminal or command prompt and type:

```bash
python --version
```

---

## 🎮 How to Play

### Step 1: Download the Game

Clone or download the repository containing the Minesweeper game files.

### Step 2: Run the Game

Navigate to the directory containing the game files and execute the following command in your terminal:

```bash
python main.py
```

Alternatively, you can use the provided shell script:

```bash
chmod +x run_game.sh
./run_game.sh
```

---

## 🕹️ Gameplay Instructions

### Selecting Difficulty Level

Upon launching the game, you will be prompted to select a difficulty level:

- Enter `beginner`, `intermediate`, or `expert` to choose your preferred difficulty.

### Game Controls

- **Reveal a Cell:** Enter `r [row] [col]`
  - Example: `r 3 4` reveals the cell at row 3, column 4.

- **Flag/Unflag a Cell:** Enter `f [row] [col]`
  - Example: `f 2 5` flags or unflags the cell at row 2, column 5.

### Objective

- Uncover all cells without mines to win the game.
- If you uncover a mine (`*`), the game ends, and you lose.
- Use numbers displayed on revealed cells to deduce mine locations.
- Flag suspected mines to avoid accidental clicks.

---

## 📖 Understanding the Board

- **`#`**: Unrevealed cell
- **`F`**: Flagged cell (suspected mine)
- **`*`**: Mine (revealed upon losing)
- **Numbers (1-8)**: Indicate how many mines are adjacent to the cell
- **Blank (` `)**: No adjacent mines; reveals surrounding cells automatically

---

## ✅ Winning the Game

You win the game by successfully revealing all non-mine cells. Upon winning, the entire board will be revealed, displaying all mine locations clearly.

---

## 📚 Additional Information

For further details, please refer to the included `readme.md` file or contact the development team for support.

Enjoy playing Minesweeper and challenge yourself to master all difficulty levels!

--- 

Happy gaming! 🎉
```