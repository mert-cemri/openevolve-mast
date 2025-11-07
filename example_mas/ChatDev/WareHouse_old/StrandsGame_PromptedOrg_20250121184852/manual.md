# Strands Puzzle Game

Welcome to the Strands Puzzle Game! This is a word-segmentation puzzle where players combine strands of text to form meaningful words or phrases. The game verifies valid strand formations and confirms completion once all strands are correctly merged.

## Main Functions

- **Load Strands**: Load strands from a specified file to start the game.
- **Combine Strands**: Combine selected strands to form valid words or phrases.
- **Check Completion**: Verify if all strands have been correctly merged to complete the puzzle.

## Installation

### Prerequisites

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Quick Install

1. Clone the repository or download the source code.
2. Navigate to the directory containing the source code.
3. Install any necessary dependencies (if applicable). For this game, no additional Python packages are required beyond the standard library.

## How to Play

1. **Prepare the Strands File**: Create a text file named `strands.txt` in the same directory as the source code. This file should contain the strands of text, each on a new line, that players will combine to form words or phrases.

2. **Run the Game**: Execute the `main.py` file to start the game. You can do this by opening a terminal or command prompt, navigating to the directory containing `main.py`, and running the command:
   ```bash
   python main.py
   ```

3. **Game Instructions**:
   - The game will display the current strands available.
   - Enter the strands you wish to combine, separated by commas (e.g., `str1,str2`).
   - The game will inform you if the combination is valid or invalid.
   - Continue combining strands until all strands are correctly merged.

4. **Winning the Game**: Once all strands are correctly combined, the game will congratulate you on completing the puzzle.

## Example

Suppose your `strands.txt` file contains the following strands:
```
he
llo
wo
rld
```

To form the words "hello" and "world", you would enter:
- `he,llo` to form "hello"
- `wo,rld` to form "world"

The game will confirm each valid combination and notify you upon successful completion of the puzzle.

Enjoy playing the Strands Puzzle Game and challenge yourself to find the correct combinations!