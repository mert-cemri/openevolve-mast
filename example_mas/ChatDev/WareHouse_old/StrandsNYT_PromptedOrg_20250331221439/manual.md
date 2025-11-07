manual.md

```
# NYT Strands Puzzle Game

Welcome to the NYT Strands Puzzle Game! This software provides an engaging and interactive word search puzzle experience inspired by the popular NYT Strands puzzle. Players will uncover themed words hidden within a 6x8 grid of letters, with a special challenge word called the "spangram" that connects two opposite sides of the board.

---

## 🚀 Main Features

- **Interactive Word Search:** Discover themed words hidden within a 6x8 grid.
- **Spangram Challenge:** Find the special "spangram" word that touches two opposite sides of the puzzle board.
- **Dynamic Highlighting:** Themed words highlight in blue, and the spangram highlights in yellow for easy identification.
- **Flexible Word Formation:** Words can be formed by connecting adjacent letters in any direction (vertically, horizontally, diagonally) and can change direction mid-word.
- **Hint System:** Earn hints by finding non-theme words. Every 3 non-theme words discovered unlocks a new hint.
- **Puzzle Completion:** Complete the puzzle by finding all theme words and the spangram, filling the entire board.

---

## 📦 Installation

### Prerequisites

- Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation Steps

1. **Clone or Download the Repository**

   Clone the repository using Git:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

   Alternatively, download and extract the ZIP file to your preferred directory.

2. **Set Up the Environment**

   This project does not require any external dependencies. However, it is recommended to use a virtual environment for better management:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Verify Installation**

   Ensure you have the following files in your project directory:
   ```
   puzzle_board.py
   game.py
   main.py
   ```

---

## 🎮 How to Play

### Starting the Game

Run the game by executing the following command in your terminal:

```bash
python main.py
```

You will see the welcome message and the initial puzzle board displayed in your terminal.

### Game Rules

- **Finding Words:** Enter words by specifying the word followed by the positions of each letter in the format `WORD x1,y1 x2,y2 ...`. Positions are zero-indexed, with `(0,0)` representing the top-left corner of the board.

  **Example:**
  ```
  PYTHON 0,0 1,0 2,0 2,1 2,2 3,2
  ```

- **Word Validation:** The game will validate your input. If the word and positions are correct, you will receive confirmation:
  - **Theme Word Found:** Highlights in blue.
  - **Spangram Found:** Highlights in yellow.
  - **Non-theme Word Found:** Every 3 non-theme words found unlocks a hint.

- **Hints:** After unlocking hints, the game will inform you of the number of available hints. Use these hints strategically to complete the puzzle.

- **Puzzle Completion:** The game ends when you successfully find all theme words and the spangram, filling the entire puzzle board.

---

## 🖥️ Interface Guide

- **Puzzle Board Display:**
  - Letters enclosed in `[ ]` indicate theme words you've found (highlighted in blue).
  - Letters enclosed in `( )` indicate the spangram you've found (highlighted in yellow).
  - Unhighlighted letters are displayed plainly.

- **User Input:**
  - Follow the input format strictly to ensure correct validation.
  - Incorrect formats or invalid paths will prompt an error message.

---

## ✅ Example Gameplay

```
Welcome to the NYT Strands Puzzle!

 .  .  .  .  .  .  .  .
 .  .  .  .  .  .  .  .
 .  .  .  .  .  .  .  .
 .  .  .  .  .  .  .  .
 .  .  .  .  .  .  .  .
 .  .  .  .  .  .  .  .

Enter a word and positions (e.g., WORD x1,y1 x2,y2 ...): PYTHON 0,0 1,0 2,0 2,1 2,2 3,2
Theme word found!

[P][Y][T] .  .  .  .  .
 .  . [H] .  .  .  .  .
 .  . [O][N] .  .  .  .
 .  .  .  .  .  .  .  .
 .  .  .  .  .  .  .  .
 .  .  .  .  .  .  .  .

Enter a word and positions (e.g., WORD x1,y1 x2,y2 ...): JAVA 4,0 4,1 4,2 4,3
Theme word found!

[P][Y][T] . (J) .  .  .
 .  . [H] . (A) .  .  .
 .  . [O][N](V) .  .  .
 .  .  .  . (A) .  .  .
 .  .  .  .  .  .  .  .
 .  .  .  .  .  .  .  .

You have completed the puzzle! Congratulations!
```

---

## 📞 Support & Feedback

For any questions, issues, or feedback, please contact our support team or open an issue in the project's repository.

Enjoy playing the NYT Strands Puzzle Game and happy puzzling!

--- 
```