# Minesweeper Game User Manual

Welcome to the Minesweeper Game! This classic puzzle game challenges you to uncover cells on a grid without detonating hidden mines. With three levels of difficulty, Minesweeper offers a fun and engaging experience for players of all skill levels.

## Main Functions

- **Difficulty Levels**: Choose from three levels of difficulty:
  - Beginner: 9x9 grid with 10 mines
  - Intermediate: 16x16 grid with 40 mines
  - Expert: 24x24 grid with 99 mines

- **Uncovering Cells**: Click on cells to uncover them. If a mine is uncovered, the game is over. Numbers on uncovered cells indicate how many mines are adjacent.

- **Flagging Mechanism**: Flag cells you suspect contain mines. Flagged cells are marked with an "F" and can be toggled on or off.

- **Winning the Game**: Uncover all non-mine cells to win the game.

## Installation

### Environment Setup

To play the Minesweeper game, you need to have Python installed on your system. Follow these steps to set up your environment:

1. **Install Python**: Download and install Python from the [official website](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the Minesweeper game repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Project Directory**: Change your directory to the project folder:
   ```bash
   cd <repository-folder>
   ```

4. **Install Dependencies**: Install any required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```
   Note: Ensure you have a `requirements.txt` file listing any necessary packages. If not, you can skip this step as the game may not require additional packages beyond standard Python libraries.

## How to Play

1. **Start the Game**: Run the main script to start the game:
   ```bash
   python main.py
   ```

2. **Choose Difficulty**: When prompted, choose your desired difficulty level by typing "beginner", "intermediate", or "expert".

3. **Game Commands**:
   - **Uncover a Cell**: Type `uncover x y` to uncover the cell at coordinates (x, y).
   - **Flag a Cell**: Type `flag x y` to flag or unflag the cell at coordinates (x, y).

4. **Game Objective**: Uncover all non-mine cells to win the game. If you uncover a mine, the game is over.

5. **Game End**: The game ends when all non-mine cells are uncovered or a mine is uncovered. The board will display the final state, showing all mines and flagged cells.

Enjoy the challenge of Minesweeper and test your puzzle-solving skills!