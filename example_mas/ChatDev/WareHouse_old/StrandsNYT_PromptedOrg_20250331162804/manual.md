# NYT Strands Puzzle Game

Welcome to the NYT Strands Puzzle Game! This is a word search game where players uncover words within a 6x8 grid of letters. The game includes themed words and a special challenge word called the "spangram" that touches two opposite sides of the board. Let's dive into how you can set up and play this exciting game.

## Main Features

- **6x8 Grid**: The game is played on a 6x8 grid filled with letters.
- **Themed Words**: Find words that fall under a specific theme. These words are highlighted in blue.
- **Spangram**: A special challenge word that touches two opposite sides of the grid, highlighted in yellow.
- **Non-Theme Words**: Discover additional words to earn hints. Every 3 non-theme words found unlocks a hint.
- **Dynamic Word Formation**: Words can be formed by connecting adjacent letters in any direction (vertically, horizontally, diagonally) and can change direction mid-word.
- **Completion Goal**: The puzzle is completed by finding all theme words and filling the board.

## Installation

### Prerequisites

- Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Quick Install

1. **Clone the Repository**: Clone the project repository to your local machine.
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Change into the project directory.
   ```bash
   cd <project-directory>
   ```

3. **Install Dependencies**: Although there are no external dependencies required for this project, ensure your environment is set up correctly.
   ```bash
   pip install -r requirements.txt
   ```

## How to Play

1. **Start the Game**: Run the main Python script to start the game.
   ```bash
   python main.py
   ```

2. **Game Interface**: The game will display the 6x8 grid of letters.

3. **Enter Words**: Type in words you find on the grid. Words must be entered in uppercase.

4. **Check Words**: The game will check if the word is valid:
   - If valid, the word will be highlighted on the grid.
   - If invalid, you will be prompted to try again.

5. **Unlock Hints**: For every 3 non-theme words you find, a hint will be unlocked.

6. **Complete the Puzzle**: The game is completed when all theme words and the spangram are found.

7. **Winning the Game**: Once the puzzle is completed, a congratulatory message will be displayed.

## Additional Information

- **Grid Display**: The grid is displayed with letters. Empty spaces are represented by dots ('.').
- **Word Highlighting**: Themed words are highlighted in blue, and the spangram is highlighted in yellow.
- **Dynamic Gameplay**: Words can be formed in any direction and can change direction mid-word, adding a layer of complexity to the puzzle.

Enjoy playing the NYT Strands Puzzle Game and challenge yourself to find all the words! If you have any questions or need further assistance, feel free to reach out. Happy puzzling!